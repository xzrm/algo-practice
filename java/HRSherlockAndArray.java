import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class HRSherlockAndArray {
    public static void main(String[] args) {
        String s = "1 2 3 3";
        // String s = "1 0 0 0";
        List<Integer> numbers = Arrays.stream(s.split(" "))
                .map(Integer::parseInt)
                .collect(Collectors.toList());
        System.out.println(balancedSums(numbers));
    }

    public static String balancedSums(List<Integer> numbers) {
        if (numbers.size() == 1) {
            return "YES";
        }
        int tot = numbers.stream().mapToInt(x -> x).sum();
        int sum = 0;

        for (Integer n : numbers) {
            if (sum == tot - n - sum) {
                return "YES";
            }
            sum += n;
        }
        return "NO";
    }
}