class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int prev_continuity = 1;
        int continuity = 1;
        int size = nums.size();
        while (true) {
            for (int i = 0; i < size; i++) {
                // iterate over every value in the array O(n).
                if (nums[i] == continuity) {
                    // num has been found in nums
                    continuity++;
                }
            }
            if (continuity == prev_continuity) {
                // the value was not found
                break;
            }
            // the value was found
            prev_continuity = continuity;
        }
        return continuity;
    }
};
