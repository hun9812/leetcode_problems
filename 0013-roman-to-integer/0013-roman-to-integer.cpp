class Solution {
public:
    int romanToInt(string s) {
        int i = 0;
        int l = s.size();
        int acc = 0;
        int res = 0;

        while (i < l) {
            if (s[i] == 'C') {
                acc += 1;
                while (i+1 < l && s[i+1] == 'C') {
                    acc += 1;
                    i += 1;
                }
                if (i+1 < l && (s[i+1] == 'D' || s[i+1] == 'M')) {
                    if (s[i+1] == 'D') {
                        res += (500 - (100*acc));
                    }
                    else {
                        res += (1000 - (100*acc));
                    }
                    i += 2;
                }
                else {
                    res += (acc*100);
                    i += 1;
                }
                acc = 0;
            }
            else if (s[i] == 'X') {
                acc += 1;
                while (i+1 < l && s[i+1] == 'X') {
                    acc += 1;
                    i += 1;
                }
                if (i+1 < l && (s[i+1] == 'L' || s[i+1] == 'C')) {
                    if (s[i+1] == 'L') {
                        res += (50 - (acc*10));
                    }
                    else {
                        res += (100 - (acc*10));
                    }
                    i += 2;
                }
                else {
                    res += 10*acc;
                    i += 1;
                }
                acc = 0;
            }
            else if (s[i] == 'I') {
                acc += 1;
                while (i+1 < l && s[i+1] == 'I') {
                    acc += 1;
                    i += 1;
                }
                if (i+1 < l && (s[i+1] == 'V' || s[i+1] == 'X')) {
                    if (s[i+1] == 'V') {
                        res += (5 - (acc));
                    }
                    else {
                        res += (10 - acc);
                    }
                    i += 2;
                }
                else {
                    res += acc;
                    i += 1;
                }
                acc = 0;
            }
            else{
                if (s[i] == 'M') {
                    res += 1000;
                }
                else if (s[i] == 'D') {
                    res += 500;
                }
                else if (s[i] == 'L') {
                    res += 50;
                }
                else {
                    res += 5;
                }
                i += 1;
            }
        }
        return res;
    }
};