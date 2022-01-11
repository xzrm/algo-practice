import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

class HRtwoChars {

    public static boolean isValid(String s) {
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i - 1) == s.charAt(i)) return false;
        }
        return true;
    }

    public static void main(String[] args) {

        String s = "beabeefeab";
        Set<Character> charSet = s.chars().mapToObj(c -> (char) c).collect(Collectors.toSet());

        List<String> pairs = new ArrayList<>();

        for (char c1 : charSet) {
            for (char c2 : charSet) {
                if (c1 != c2) {
                    String c1c2 = "" + c1 + c2;
                    String c2c1 = "" + c2 + c1;
                    if (!pairs.contains(c1c2) && !pairs.contains(c2c1)) {
                        pairs.add(c1c2);
                    }
                }
            }
        }
        List<List<Character>> charPairs = new ArrayList<>();

        for (String ss : pairs) {
            charPairs.add(ss.chars().mapToObj(c -> (char) c).collect(Collectors.toList()));
        }
        System.out.println(charPairs.toString());

        List<String> validStrings = new ArrayList<>();

        for (List<Character> p : charPairs) {
            String newString = s.replace(p.get(0).toString(), "");
            newString = newString.replace(p.get(1).toString(), "");
            System.out.println(newString);
            if (isValid(newString)) {
                validStrings.add(newString);
                System.out.println("is valid: " + newString);
            }
        }

        if (validStrings.size() > 0) {
            int maxVal = validStrings.stream().map(String::length).max(Integer::compareTo).get();
            System.out.println(maxVal);
        }
        System.out.println(0);


    }


}
