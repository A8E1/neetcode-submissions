class Solution {
#include <set>
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> mySet = {};
        for (int i = 0; i<nums.size(); i++){
            mySet.insert(nums.at(i));
        }

        return mySet.size() < nums.size();
    }

};