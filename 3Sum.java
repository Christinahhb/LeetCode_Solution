import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
class Solution {
    public List<List<Integer>> threeSum(int[] num) {
        Arrays.sort(num);
        int len = num.length;
        List<List<Integer>> answer = new ArrayList<>();
        if (len<3){
            return(answer);
        }
        else{
            for (int i = 0; i< len-2; i++){
 
                if(i> 0 && num[i] == num[i-1])  {
                    continue;
                } 
                int left = i+1;
                int right = len -1;          
                while(left <right ){
                    
 
                    int sum = num[i]+num[left]+num[right];                  
                    if (sum == 0){
                        answer.add(Arrays.asList(num[i], num[left], num[right]));
                        //can't change this while loop out if, and can't change to num[left] == num[left-1]
                        while(left<right && num[left] == num[left+1]  )  {
                            left++;
                        }

                        while( right > left && num[right] == num[right-1]){
                            right--;
                        } 
                        left++;
                        right--;
                    }
                    else if(sum > 0 ){
                        right --;
                    }
                    else{
                        left ++;
                    }
                }

            }
        }
        return answer;
    }
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = {-1,0,1,2,-1,-4,-2,-3,3,0,4};
        List<List<Integer>> result = solution.threeSum(nums);
        System.out.println(result);
    }
}