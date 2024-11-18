class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        sort(strs.begin(),strs.end());
        string first = strs[0];
        string last = strs[strs.size() - 1];
        // with a sorted vector, only the first and last strings need to be compared
        for (int i = 0; i < min(first.size(), last.size()); i++) {
            // the smaller size is the only one you have to iterate through
            if (first[i] != last[i]) {
                return prefix;
            }
            prefix += first[i];
        }
        return prefix;
    }
};
