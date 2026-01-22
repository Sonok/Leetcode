class Solution {
public:
    vector<vector<int>> ans; 
    unordered_set<vector<int>> s;
    vector<int> curr = {};
    vector<int> nums;
    int n;

    vector<vector<int>> subsets(vector<int>& nums) {
        ans = {}; 
        this->nums = nums;
        this->n = nums.size();
        backtrack(curr);
        for(auto x: s) {
            ans.push_back(x);
        }
        return ans;
    }
    void backtrack(vector<int>& curr) {
        s.insert(curr); 
        if(curr.size() == n) return;
        for(int x: curr) {
            auto it = curr.find(x);
            if(it == curr.end()) {
                curr.push_back(x);
                backtrack(curr);
                curr.pop();
            }
        }
    }
};