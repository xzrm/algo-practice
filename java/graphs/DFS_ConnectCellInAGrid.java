package graphs;

import java.util.Arrays;

public class DFS_ConnectCellInAGrid {

    public static boolean isValidLocation(int[][] grid, int[] loc) {
        return loc[0] >= 0 && loc[0] < grid.length && loc[1] >= 0 && loc[1] < grid[0].length;
    }

    public static int[][] getNeighbors(int[][] grid, int[] loc) {
        int[][] moves = { { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 }, { 1, 1 }, { 1, -1 }, { -1, 1 }, { -1, -1 } };
        return Arrays.stream(moves)
                .map(move -> new int[] { loc[0] + move[0], loc[1] + move[1]
                }).filter(v -> isValidLocation(grid, v)).toArray(int[][]::new);
    }

    public static void main(String[] args) {
        // example for testing:
        String s = "1 0 1 1 0\n" +
                "1 1 0 0 1\n" +
                "0 1 1 1 0\n" +
                "0 0 0 0 1\n" +
                "1 1 1 0 0";

        String[] rows = s.split("\n");
        int[][] grid = new int[rows.length][];

        for (int i = 0; i < rows.length; i++) {
            grid[i] = Arrays.stream(rows[i].split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
        }

        /*
         * maxRegion method in hackerrank interactive window takes arg:
         * List<List<Integer>> gridList
         * so transformation to nested arrays is required, for example:
         * 
         * int[][] grid = new int[gridList.size()][];
         * for(int i=0; i<gridList.size(); i++){
         * grid[i] = gridList.get(i).stream().mapToInt(j -> j).toArray();
         * }
         */

        System.out.println(findMaxRegion(grid));
    }

    public static int countFields(int[][] grid, int[] loc) {
        if (!isValidLocation(grid, loc)) {
            return 0;
        }
        int r = loc[0];
        int c = loc[1];
        if (grid[r][c] == 0)
            return 0;
        grid[r][c] = 0;
        int count = 1;
        int[][] neighbors = getNeighbors(grid, loc);
        for (int[] n : neighbors) {
            count += countFields(grid, n);
        }
        return count;
    }

    public static int findMaxRegion(int[][] grid) {
        int maxCount = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                int[] loc = { i, j };
                maxCount = Math.max(maxCount, countFields(grid, loc));
            }
        }
        return maxCount;
    }
}
