class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indexMap{}; // value -> index

        for(int i{}; i < nums.size(); ++i)
        {
            int diff = target - nums[i];
            if(indexMap.find(diff) != indexMap.end())
            {
                return {indexMap[diff], i};
            }
            indexMap.insert({nums[i], i});
        }
        
    }
};
