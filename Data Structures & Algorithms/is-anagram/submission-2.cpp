class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) return false;

        std::unordered_map<char, int> countS{};
        std::unordered_map<char, int> countT{};

        for(std::size_t index{}; index < s.size(); ++index)
        {
            countS[s[index]]++;
            countT[t[index]]++;
        }

        return countS == countT;
    }
};
