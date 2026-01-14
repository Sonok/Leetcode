class Solution {
public:
    string makeGood(string s) {
        vector<char> st;
        for(int i = 0; i < s.size(); i++) {
            st.push_back(s[i]);
            
            while(st.size() >= 2) {
                char up1 = toupper(st[st.size() - 1]); 
                char up2 = toupper(st[st.size() - 2]);
                if (up1 == up2 and st[st.size() - 1] !=  st[st.size() - 2]) {
                    st.pop_back(); st.pop_back();
                } else break;
            }
        }
        string ret;
        for(auto x: st) {
            ret.push_back(x);
        }
        return ret;
    }
};