class Solution {
public:
    bool compareInts(int num1, int num2) {
        string string1 = "";
        while (num1 > 0) {
            string1 = to_string(num1 % 2) + string1;
            num1 /= 2;
        }
        string string2 = "";
        while (num2 > 0) {
            string2 = to_string(num2 % 2) + string2;
            num2 /= 2;
        }
        int ones1 = 0;
        int ones2 = 0;
        for(char& c : string1) {
            if (c == '1') {
                ones1++;
            }
        }
        for(char& c : string2) {
            if (c == '1') {
                ones2++;
            }
        }

        if (ones1 == ones2) {
            return true;
        }
        return false;
    }

    bool canSortArray(vector<int>& nums) {
        // comparison subfunction
        
        // start program
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                if (!(i == 0 || nums[i] > nums[j])) {
                    if (!compareInts(nums[j], nums[i])) {
                        return false;
                    }
                }
            }
        }
        return true;

    }
};
