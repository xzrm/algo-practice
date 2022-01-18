import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

class HRBetweenTwoSets {

    public static void main(String[] args) {
        String s1 = "2 4";
        String s2 = "16 32 96";

        List<Integer> num1 = Arrays.stream(s1.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        List<Integer> num2 = Arrays.stream(s2.split(" ")).map(Integer::parseInt).collect(Collectors.toList());
        Integer min_val = Collections.min(num2);

        List<Boolean> temp = new ArrayList<>();
        List<Integer> res = new ArrayList<>();


        for (int i = 1; i <= min_val; i++) {
            temp.clear();
            for (Integer j : num1) {
                if (i % j == 0) {
                    temp.add(true);
                } else {
                    temp.add(false);
                }
            }
            if (temp.stream().allMatch(e -> e)) {
                res.add(i);
            }
        }

        int count = 0;
        for (Integer i : res) {
            temp.clear();
            for (Integer j : num2) {
                if (j % i == 0) {
                    temp.add(true);
                } else {
                    temp.add(false);
                }
            }
            if (temp.stream().allMatch(e -> e)) {
                count++;
            }
        }
        System.out.println(count);
    }
}