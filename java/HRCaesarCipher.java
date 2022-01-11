
import java.util.List;
import java.util.stream.Collectors;

class HRCaesarCipher {

    public static void main(String[] args) {
//        String s = "middle-Outz";
        String s = "www.abc.xy";
        int rot = 28 % 26;
        List<Character> chars = s.chars().mapToObj(e -> (char) e).collect(Collectors.toList());
        String ciphered = chars.stream().map(c -> {
            if (Character.isAlphabetic(c)) {
                int val;
                if (c > 64 && c <= 90) {
                    if (c + rot > 90) {
                        val = 65 + ((c + rot - 1) % 90);
                        return (char) val;
                    }
                } else if (c > 96 && c <= 122) {
                    if (c + rot > 122) {
                        val = 97 + ((c + rot - 1) % 122);
                        return (char) val;
                    }
                }
                val = c + rot;
                return (char) val;
            } else return c;
        }).map(Object::toString).collect(Collectors.joining());
	return ciphered;
    }
}