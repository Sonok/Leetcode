class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size();
        // kahn's algoritihn for finding a cycle? 
        vector<char> seen(n, 0); queue<int> q; 
        seen[0] = 1; q.push(0);
        int seenCount = 1;

        while(q.size()) {
            int val = q.front(); 
            q.pop();
            for(auto x: rooms[val]) {
                if (!seen[x]) {
                    q.push(x);
                    seen[x] = 1;
                    seenCount++;
                }
            }
        }

        return seenCount == n ? true : false;
    }
};