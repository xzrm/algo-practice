class HRseparateNumbers {

    public static void main(String[] args) {
//        7
//        1234
//        91011
//        99100
//        101103
//        010203
//        13
//        1
//        String s = "99100101";
        String s = "101102";
        if (s.startsWith("0") && s.length() > 1) {
            System.out.println("NO");
            return;
        }
        Boolean isValid = false;
        String substr = "";
        for(int i = 1; i <= s.length() / 2; i++){
            substr = s.substring(0, i);
            String validStr = substr;
            Long num = Long.parseLong(validStr);
            while(validStr.length() < s.length()){
                Long next_num = num + 1;
                validStr += next_num;
                num = next_num;
            }
            if(validStr.equals(s)){
                isValid = true;
                break;
            }
        }
        System.out.println(isValid ? "YES " + substr : "NO");
	return;
    }
}
