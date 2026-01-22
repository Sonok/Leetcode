class Solution {
public:
    vector<int> ways;
    // not neeeded to do this type of dp 
    // for a question this easy but I wanted 
    // to get the format down
    int climbStairs(int n) {
        if (n <= 3) {
            return n;
        }
        ways = vector(n+1, -1);
        ways[0] = 0; ways[1] = 1; ways[2] = 2;
        return dp(n);
    }
    
    int dp(int state) {
        if (ways[state] != -1) {
            return ways[state];
        }
        ways[state] = dp(state - 2) + dp(state - 1);
        return ways[state];
    }
    
}; 