class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string newString;
        int pointer = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i == spaces[pointer]) {
                newString.append(" ");
                if (pointer + 1 < spaces.size()) {
                    pointer++;
                }
            }
            newString += s[i];
        }
        return newString;
    }
};
