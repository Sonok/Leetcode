class Solution {
public:
    vector<int> cost; // we make a copy of the cost to go each stair
    vector<int> memo; // top down appoach
    int minCostClimbingStairs(vector<int>& cost) {
        this->cost = cost; 
        memo = vector(cost.size()+1, -1);
        return dp(cost.size()); // dp(int s) is dp on the state
    }
    int dp(int state) {
        if (state <= 1) {
            return 0;
        }

        if (memo[state] != -1) { // have it memoized
            return memo[state];
        }

        int oneStep = dp(state - 1) + cost[state - 1];
        int twoStep = dp(state - 2) + cost[state - 2];
        memo[state] = min(oneStep, twoStep);
        return memo[state];
    }
};