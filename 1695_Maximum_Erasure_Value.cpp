class Solution {
public:
    int maximumUniqueSubarray(vector<int>& nums) {

        unordered_set<int> s;
        int l = 0; int n = nums.size();
        int currWindow = 0; int maxWindow = 0;

        for(int r = 0; r < n; r++) {
            s.insert(nums[r]); currWindow += nums[r]; // add to our currWindow
            if(s.size() < r - l + 1) {
                while(nums[l] != nums[r]) { // shrink the window  till u find duplicate 
                    s.erase(nums[l]); 
                    currWindow -= nums[l++];
                }
                currWindow -= nums[l++];
            }
            maxWindow = max(maxWindow, currWindow);
        }
        return maxWindow;

        
    }
};