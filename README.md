# 3sum
Solution of 3sum

## 題目 https://leetcode.com/problems/3sum/description/

找出三個相加為 0 的數，且解答不得包含重複的組合。

**ex:** <br> 

Input: <br> 
nums = [-1,0,1,2,-1,-4] <br>

Output: <br>
[[-1,-1,2],[-1,0,1]]

## Workaround &nbsp; 1

**想法** <br> 

1. 先確認 nums list 中的數是否小於三個，若是小於三個，則直接 return []，若是大於等於三個，則進入以下檢查。
2. 使用以下檢查來避免出現重複的組合 for i in range(len(nums)-2): if i > 0 and nums[i-1] == nums[i]: continue。
3. 使用 i 與 j 從前往後進行，k 則由後往前進行。
4. 若是 nums[i] + nums[j] + nums[k] > 0 ，則將 k 往前一位。
5. 若是 nums[i] + nums[j] + nums[k] < 0 ，則將 j 往後一位。
