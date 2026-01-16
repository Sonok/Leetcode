class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        for (int i = 0; i < n; i++) {
            int left = i + 1; int right = n-1;
            while(left <= right) {
                int mid = (left + right) / 2;
                int total = numbers[mid] + numbers[i];
                if(total == target) {
                    return {i+1, mid + 1};
                } else if (total > target) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return {1,1}; // not supposed to happen
    }
};