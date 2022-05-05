/*
 * @lc app=leetcode.cn id=70 lang=cpp
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
public:
    int climbStairs(int n) {
        if(n==1){
            return 1;
        }
        vector <int> num(n,0);
        num[0]=1;num[1]=2;
        for(int i=2;i<n;i++)
        {
            num[i]=num[i-2]+num[i-1];
        }
        return num[n-1];
    }
};
// @lc code=end
// 动态规划

// n=1, c[1]=1
// n=2, c[2]=2
// n=3, c[3]=c[2]+c[1]
// n=4, c[4]=c[3]=c[2]

