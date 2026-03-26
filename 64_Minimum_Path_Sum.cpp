class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {

        const int max = 1e9;
        const int m = grid.size();
        const int n = grid[0].size();

        vector<vector<int>> dp(m, vector<int>(n, max));
        dp[0][0] = grid[0][0];
        // if you have a state i, j then 
        // the value of state[i][j] = 
        // min(state[i-1][j] + grid[i][j], state[i][j-1] + grid[i][j])
        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(i == 0 && j == 0) continue;
                int leftPath = (j > 0 ? dp[i][j-1] + grid[i][j] : max);
                int topPath = (i > 0 ? dp[i-1][j] + grid[i][j] : max);
                dp[i][j] = min(leftPath, topPath);
            }
        }
        return dp[m-1][n-1];
    }
};