class Solution {
public:
    bool isPalindrome(int x) {
        std::string snum = std::to_string(x);
        std::string cnum = "";
        for (int i = (snum.size()-1); i > -1; i--){
            cnum += snum[i];
        }
        if (snum == cnum){
            return true;
        }
        return false;
    }
};