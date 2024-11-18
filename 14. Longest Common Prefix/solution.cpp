class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        int shortest_string_length = strs[0].length();
        int current_position = 0;

        for (string str : strs) {
            if (str.length() < shortest_string_length){
                // the longest prefix can be lo longer than the shortest string in the vector
                shortest_string_length = str.length();
            }
        }
        if (shortest_string_length == 0) {
            return prefix;
        }

        bool all_same = true;
        for (int i = 0; i < shortest_string_length; i++) {
            char c = strs[0][i];

            for (string str : strs) {
                if (str[i] == c) {
                    all_same = true;
                } else {
                    // if any fail, break
                    all_same = false;
                    return prefix;
                }
            }
            if (all_same) {
                prefix += c;
            }
        }

        return prefix;
    }
};
