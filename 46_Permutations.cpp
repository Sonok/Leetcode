class Solution {
public:
    vector<vector<int>> ret;
    vector<int> curr;
    vector<int> nums;
    int n; // how big our permutation is 

    vector<vector<int>> permute(vector<int>& nums) {
        ret = {}; curr = {}; n = nums.size();
        this -> nums = nums;
        backtrack(curr); // send adress of curr? 
        return ret; 
    }

    void backtrack(vector<int>& curr) {
        if (curr.size() == n) {
            ret.push_back(curr);
            return;
        }
        for(auto x: nums) {
            auto it = curr.find(x);
            if (it == curr.end()) { // x is not found
                curr.push_back(x);
                backtrack(curr);
                curr.pop_back(); // get rid of last element 
            }
        }
    }
    
}; 