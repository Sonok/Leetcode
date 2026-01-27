class Solution {
public:
    vector<int> colorTheArray(int n, vector<vector<int>>& queries) {
        vector<int> count;
        count.reserve(queries.size());

        int pairs = 0;

        vector<int> colors(n);
        for(auto& q : queries) {
            int& index = q[0];
            int& color = q[1];

            if(colors[index] == color) { // no change
                count.push_back(pairs);
                continue;
            } 

            if(colors[index] != 0) { // you might have to decrease
                // left
                if(index >= 1 && colors[index] == colors[index - 1]) pairs--;
                // right
                if(index < n-1 && colors[index] == colors[index + 1]) pairs--;
            }
            colors[index] = color; // count how many pairs are generated
            // left
            if(index >= 1 && colors[index] == colors[index - 1]) pairs++;
            // right
            if(index < n-1 && colors[index] == colors[index + 1]) pairs++;
            count.push_back(pairs);

        }
        return count;
    }
};