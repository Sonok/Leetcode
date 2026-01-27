class Solution {
public:
    vector<vector<int>> ans = {};
    vector<int> curr = {};
    vector<int> nums;
    int n;

    vector<vector<int>> subsets(vector<int>& nums) {
        this->nums = nums;
        this->n = nums.size();

        backtrack(curr, 0);
        return ans;
    }
    void backtrack(vector<int>& curr, int i) {
        ans.push_back(curr); 
        if(curr.size() == n) return;
        for (int j = i; j < n; j++) {
            // pick the next element! from i onwards 
            curr.push_back(nums[j]);
            backtrack(curr, j + 1);
            curr.pop_back();
        }
    }
};