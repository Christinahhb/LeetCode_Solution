public class Solution {
    public String longestPalindrome(String s) {
        int len = s.length();
        int ispal = 0;
        String result = "";
        String ans = "";
        for (int i = 0; i< len-1;i++){
            for (int j = len-1; j>i; j-- ){
                //遍历一遍
                result = s.substring(i,j+1);
                ispal = isPalindrome(result);
                if (ispal == 1){

                    if(result.length() >= ans.length() )
                    ans =  (s.substring(i,j+1));
                }  
            }
        } 
        return (ans);       
    }
    public int isPalindrome(String s){
        int len2 = s.length();
        int ans2 = 0;
        int x = len2-1;
        int z = 0;
        while(z < len2/2){
            char a = s.charAt(z);
            char b = s.charAt(x);
            System.out.println(s.substring(z+1,x));
            if ( a == b ){
                //if words len is 3 or 2 "aa" or "aba"
                if (x-z < 3){
                    ans2 = 1;
                    return(ans2);
                }
                else{
                    //System.out.println("len:"+ len2);
                    //System.out.println("j"+ x);
                    
                    ans2 = isPalindrome(s.substring(z+1,x));
                }
                x =x-1;
                z = z+1;   
            }

            else{
                return(ans2);
            }
        }
        return ans2;                    
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        String result = sol.longestPalindrome("awaba");
        System.out.println(result); // 输出: "bab" 或 "aba"
    }
};