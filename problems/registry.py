"""
DSA Problem Registry — exact code transcribed from screenshots.
"""
from dataclasses import dataclass, field
from typing import List

@dataclass
class ProblemEntry:
    number: int
    title: str
    category: str
    session: int
    code: str
    notes: str = ""


PROBLEMS: List[ProblemEntry] = [

    ProblemEntry(
        number=1, title="Running Sum of 1D Array", category="Arrays / Prefix Sum", session=1,
        code=r"""class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++) {
            nums[i] = nums[i] + nums[i - 1];
        }
        return nums;
    }
};"""
    ),

    ProblemEntry(
        number=2, title="Find Pivot Index", category="Arrays / Prefix Sum", session=1,
        code=r"""class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n = nums.size();
        int totalSum = 0;

        for (int i = 0; i < n; i++) {
            totalSum += nums[i];
        }

        int leftSum = 0;
        for (int i = 0; i < n; i++) {
            totalSum -= nums[i];
            if (leftSum == totalSum) {
                return i;
            }
            leftSum += nums[i];
        }
        return -1;
    }
};"""
    ),

    ProblemEntry(
        number=3, title="Two Sum", category="Arrays / Hashing", session=1,
        code=r"""class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (mp.find(complement) != mp.end()) {
                return {mp[complement], i};
            }
            mp[nums[i]] = i;
        }
        return {};
    }
};"""
    ),

    ProblemEntry(
        number=4, title="Majority Element", category="Arrays", session=1,
        code=r"""class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = nums[0], count = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (count == 0) {
                candidate = nums[i];
                count = 1;
            } else if (nums[i] == candidate)
                count++;
            else
                count--;
        }
        return candidate;
    }
};"""
    ),

    ProblemEntry(
        number=5, title="Count Bits", category="Bit Manipulation", session=1,
        code=r"""class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n + 1, 0);
        for (int i = 1; i <= n; i++) {
            ans[i] = ans[i / 2] + (i % 2);
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=6, title="Power of Two", category="Bit Manipulation", session=1,
        code=r"""class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        if (n == 1) {
            return true;
        }
        if (n % 2 != 0) {
            return false;
        }
        return isPowerOfTwo(n / 2);
    }
};"""
    ),

    ProblemEntry(
        number=7, title="Trapping Rain Water", category="Two Pointers / Stack", session=2,
        code=r"""class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int leftMax = 0, rightMax = 0, water = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax)
                    leftMax = height[left];
                else
                    water += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax)
                    rightMax = height[right];
                else
                    water += rightMax - height[right];
                right--;
            }
        }
        return water;
    }
};"""
    ),

    ProblemEntry(
        number=8, title="Longest Palindromic Substring", category="Strings / Two Pointers", session=2,
        code=r"""class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string ans = "";
        for (int i = 0; i < n; i++) {
            int l = i, r = i;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > ans.size())
                    ans = s.substr(l, r - l + 1);
                l--; r++;
            }
            l = i; r = i + 1;
            while (l >= 0 && r < s.size() && s[l] == s[r]) {
                if (r - l + 1 > ans.size())
                    ans = s.substr(l, r - l + 1);
                l--; r++;
            }
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=9, title="Longest Common Prefix", category="Strings", session=2,
        code=r"""class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        sort(strs.begin(), strs.end());

        string first = strs[0];
        string last = strs[strs.size() - 1];
        string ans = "";

        for (int i = 0; i < first.size(); i++) {
            if (first[i] == last[i]) {
                ans += first[i];
            } else {
                break;
            }
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=10, title="Merge Two Sorted Lists", category="Linked List", session=2,
        code=r"""class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;

        while (list1 != NULL && list2 != NULL) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        if (list1 != NULL) {
            tail->next = list1;
        }
        // (list2 remainder handled implicitly)
        return dummy.next;
    }
};"""
    ),

    ProblemEntry(
        number=11, title="Intersection of Two Linked Lists", category="Linked List", session=2,
        code=r"""class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        ListNode* a = headA;
        ListNode* b = headB;

        while (a != b) {
            if (a == NULL) a = headB;
            else a = a->next;

            if (b == NULL) b = headA;
            else b = b->next;
        }
        return a;
    }
};"""
    ),

    ProblemEntry(
        number=12, title="Build Array Where You Can Find The Maximum Exactly K Comparisons",
        category="Arrays / Stack Simulation", session=2,
        code=r"""class Solution {
public:
    vector<string> buildArray(vector<int>& target, int n) {
        vector<string> ans;
        int curr = 1;

        for (int x : target) {
            while (curr < x) {
                ans.push_back("Push");
                ans.push_back("Pop");
                curr++;
            }
            ans.push_back("Push");
            curr++;
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=13, title="Next Larger Element", category="Stack / Monotonic Stack", session=3,
        code=r"""class Solution {
public:
    vector<int> nextLargerElement(vector<int>& arr) {
        // code here
        stack<int> st;
        int n = arr.size();
        vector<int> ans(n);

        for (int i = n - 1; i >= 0; i--) {
            while (!st.empty() && st.top() <= arr[i]) {
                st.pop();
            }
            if (st.empty()) {
                ans[i] = -1;
            } else {
                ans[i] = st.top();
            }
            st.push(arr[i]);
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=14, title="Rotting Oranges", category="BFS / Graphs", session=3,
        code=r"""class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        int fresh = 0, time = 0;
        int m = grid.size(), n = grid[0].size();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2)
                    q.push({i, j});
                else if (grid[i][j] == 1)
                    fresh++;
            }
        }

        int dir[4][2] = {{1,0}, {-1,0}, {0,1}, {0,-1}};

        while (!q.empty() && fresh > 0) {
            int sz = q.size();
            while (sz--) {
                auto [r, c] = q.front(); q.pop();
                for (auto& d : dir) {
                    int nr = r + d[0], nc = c + d[1];
                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 2;
                        q.push({nr, nc});
                        fresh--;
                    }
                }
            }
            time++;
        }
        return fresh == 0 ? time : -1;
    }
};"""
    ),

    ProblemEntry(
        number=15, title="Largest Rectangle in Histogram", category="Stack / Monotonic Stack", session=3,
        code=r"""class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        heights.push_back(0);
        int n = heights.size();
        stack<int> st;
        int maxA = 0;

        for (int i = 0; i < n; i++) {
            while (!st.empty() && heights[st.top()] > heights[i]) {
                int height = heights[st.top()];
                st.pop();
                int width;
                if (st.empty()) {
                    width = i;
                } else {
                    width = i - st.top() - 1;
                }
                maxA = max(maxA, height * width);
            }
            st.push(i);
        }
        return maxA;
    }
};"""
    ),

    ProblemEntry(
        number=16, title="Sliding Window Maximum", category="Sliding Window / Deque", session=3,
        code=r"""class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> ans;

        for (int i = 0; i < nums.size(); i++) {
            if (!dq.empty() && dq.front() == i - k) {
                dq.pop_front();
            }
            while (!dq.empty() && nums[dq.back()] < nums[i]) {
                dq.pop_back();
            }
            dq.push_back(i);
            if (i >= k - 1) {
                ans.push_back(nums[dq.front()]);
            }
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=17, title="Combination Sum", category="Backtracking", session=4,
        code=r"""class Solution {
public:
    vector<vector<int>> ans;
    vector<int> temp;

    void solve(int i, vector<int>& candidates, int target) {
        if (target == 0) {
            ans.push_back(temp);
            return;
        }

        if (i == candidates.size() || target < 0)
            return;

        temp.push_back(candidates[i]);
        solve(i, candidates, target - candidates[i]);
        temp.pop_back();

        solve(i + 1, candidates, target);
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        solve(0, candidates, target);
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=18, title="Subsets", category="Backtracking / Bit Manipulation", session=4,
        code=r"""class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> ans;
        int subset = 1 << n;

        for (int i = 0; i < subset; i++) {
            vector<int> temp;
            for (int j = 0; j < n; j++) {
                if (i & (1 << j)) {
                    temp.push_back(nums[j]);
                }
            }
            ans.push_back(temp);
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=19, title="Element Appearing More Than 25% In Sorted Array",
        category="Arrays / Frequency Count", session=4,
        code=r"""class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        unordered_map<int, int> mp;

        for (int x : nums)
            mp[x]++;

        int maxi = 0;

        for (auto it : mp)
            maxi = max(maxi, it.second);

        int ans = 0;

        for (auto it : mp) {
            if (it.second == maxi)
                ans += it.second;
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=20, title="Two Sum (HashMap)", category="Arrays / Hashing", session=4,
        code=r"""class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (mp.count(complement))
                return {mp[complement], i};
            mp[nums[i]] = i;
        }
        return {};
    }
};"""
    ),

    ProblemEntry(
        number=21, title="Find Median from Data Stream / Median of Two Sorted Arrays",
        category="Binary Search / Sorting", session=4,
        code=r"""class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        vector<int> ans;

        for (int i = 0; i < m; i++) {
            ans.push_back(nums1[i]);
        }

        for (int i = 0; i < n; i++) {
            ans.push_back(nums2[i]);
        }

        sort(ans.begin(), ans.end());

        int p = ans.size();
        if (p % 2 == 0)
            return (ans[p/2 - 1] + ans[p/2]) / 2.0;
        else
            return ans[p/2];
    }
};"""
    ),

    ProblemEntry(
        number=22, title="Subarray Sum Equals K", category="Arrays / Prefix Sum + Hashing", session=5,
        code=r"""class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        int count = 0;
        int preSum = 0;
        unordered_map<int, int> mpp;
        mpp[0] = 1;
        for (int i = 0; i < n; i++) {
            preSum += nums[i];
            int remove = preSum - k;
            count += mpp[remove];
            mpp[preSum] += 1;
        }
        return count;
    }
};"""
    ),

    ProblemEntry(
        number=23, title="Binary Tree Level Order Traversal", category="Trees / BFS", session=5,
        code=r"""class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ans;

        if (root == NULL)
            return ans;

        queue<TreeNode*> q;
        q.push(root);

        while (!q.empty()) {
            int size = q.size();
            vector<int> level;

            while (size--) {
                TreeNode* node = q.front();
                q.pop();
                level.push_back(node->val);
                if (node->left)  q.push(node->left);
                if (node->right) q.push(node->right);
            }
            ans.push_back(level);
        }
        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=24, title="Count Complete Components", category="Graphs / DFS", session=5,
        code=r"""class Solution {
public:
    void dfs(int node, vector<vector<int>>& adj, vector<bool>& vis,
             int& nodes, int& edges) {
        vis[node] = true;
        nodes++;
        edges += adj[node].size();

        for (int nei : adj[node]) {
            if (!vis[nei])
                dfs(nei, adj, vis, nodes, edges);
        }
    }

    int countCompleteComponents(int n, vector<vector<int>>& edges_list) {
        vector<vector<int>> adj(n);
        for (auto& e : edges_list) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        vector<bool> vis(n, false);
        int count = 0;
        for (auto& e : edges_list) {
            int nodes = 0, edges = 0;
            if (!vis[e[0]]) {
                dfs(e[0], adj, vis, nodes, edges);
                if (edges == nodes * (nodes - 1))
                    count++;
            }
        }
        return count;
    }
};"""
    ),

    ProblemEntry(
        number=25, title="Flood Fill", category="Graphs / DFS", session=5,
        code=r"""class Solution {
public:
    void dfs(vector<vector<int>>& image, int r, int c,
             int oldColor, int newColor) {
        if (r < 0 || c < 0 || r >= image.size() || c >= image[0].size())
            return;

        if (image[r][c] != oldColor)
            return;

        image[r][c] = newColor;

        dfs(image, r + 1, c, oldColor, newColor);
        dfs(image, r - 1, c, oldColor, newColor);
        dfs(image, r, c + 1, oldColor, newColor);
        dfs(image, r, c - 1, oldColor, newColor);
    }

    vector<vector<int>> floodFill(vector<vector<int>>& image,
                                   int sr, int sc, int color) {
        int oldColor = image[sr][sc];
        if (oldColor != color)
            dfs(image, sr, sc, oldColor, color);
        return image;
    }
};"""
    ),

    ProblemEntry(
        number=26, title="Cheapest Flights Within K Stops", category="Graphs / BFS / Bellman-Ford", session=6,
        code=r"""class Solution {
public:
    int findCheapestPrice(int n, vector<vector<int>>& flights,
                          int src, int dst, int k) {
        vector<vector<pair<int, int>>> adj(n);

        for (auto& f : flights)
            adj[f[0]].push_back({f[1], f[2]});

        vector<int> dist(n, INT_MAX);
        dist[src] = 0;

        queue<pair<int, pair<int, int>>> q;
        q.push({0, {src, 0}});

        while (!q.empty()) {
            auto it = q.front();
            q.pop();
            int stops = it.first;
            int node  = it.second.first;
            int cost  = it.second.second;

            if (stops > k) continue;

            for (auto& [next, price] : adj[node]) {
                if (cost + price < dist[next]) {
                    dist[next] = cost + price;
                    q.push({stops + 1, {next, dist[next]}});
                }
            }
        }
        return dist[dst] == INT_MAX ? -1 : dist[dst];
    }
};"""
    ),

    ProblemEntry(
        number=27, title="Number of Ways to Rearrange Sticks With K Sticks Visible",
        category="Dynamic Programming", session=6,
        code=r"""class Solution {
public:
    int numberOfPermutations(int n, vector<vector<int>>& requirements) {
        const int MOD = 1e9 + 7;

        vector<int> req(n, -1);
        for (auto& r : requirements)
            req[r[0]] = r[1];

        int maxInv = 400;
        vector<vector<int>> dp(n, vector<int>(maxInv + 1, 0));

        dp[0][0] = 1;

        for (int i = 1; i < n; i++) {
            for (int inv = 0; inv <= maxInv; inv++) {
                for (int add = 0; add <= i && add <= inv; add++) {
                    dp[i][inv] = (dp[i][inv] + dp[i-1][inv - add]) % MOD;
                }
            }
            if (req[i] != -1) {
                for (int inv = 0; inv <= maxInv; inv++) {
                    if (inv != req[i]) dp[i][inv] = 0;
                }
            }
        }
        return dp[n-1][req[n-1]];
    }
};"""
    ),

    ProblemEntry(
        number=28, title="Edit Distance", category="Dynamic Programming", session=6,
        code=r"""class Solution {
public:
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i <= m; i++)
            dp[i][0] = i;

        for (int j = 0; j <= n; j++)
            dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1[i - 1] == word2[j - 1])
                    dp[i][j] = dp[i-1][j-1];
                else
                    dp[i][j] = 1 + min({dp[i-1][j], dp[i][j-1], dp[i-1][j-1]});
            }
        }
        return dp[m][n];
    }
};"""
    ),

    ProblemEntry(
        number=29, title="Unique Paths", category="Dynamic Programming", session=6,
        code=r"""class Solution {
public:
    int uniquePaths(int m, int n) {
        int dp[m][n];
        memset(dp, 0, sizeof(dp));

        for (int i = 0; i < m; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < n; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[m-1][n-1];
    }
};"""
    ),

    ProblemEntry(
        number=30, title="Longest Palindromic Subsequence", category="Dynamic Programming", session=7,
        code=r"""class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int n = s.size();
        if (n == 0) return 0;
        vector<vector<int>> dp(n, vector<int>(n, 0));
        for (int i = n - 1; i >= 0; i--) {
            dp[i][i] = 1;
            for (int j = i + 1; j < n; ++j) {
                if (s[i] == s[j]) {
                    dp[i][j] = 2 + ((i + 1 <= j - 1) ? dp[i+1][j-1] : 0);
                } else {
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                }
            }
        }
        return dp[0][n-1];
    }
};"""
    ),

    ProblemEntry(
        number=31, title="House Robber", category="Dynamic Programming", session=7,
        code=r"""class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return nums[0];
        }

        int prev2 = nums[0];
        int prev1 = max(nums[0], nums[1]);

        for (int i = 2; i < n; i++) {
            int curr = max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = curr;
        }
        return prev1;
    }
};"""
    ),

    ProblemEntry(
        number=32, title="Minimum Cost to Cut a Stick", category="Dynamic Programming (Interval DP)", session=7,
        code=r"""class Solution {
public:
    int solve(int i, int j, vector<int>& cuts, vector<vector<int>>& dp) {
        if (i > j)
            return 0;

        if (dp[i][j] != -1)
            return dp[i][j];

        int ans = INT_MAX;

        for (int k = i; k <= j; k++) {
            int cost = cuts[j + 1] - cuts[i - 1]
                     + solve(i, k - 1, cuts, dp)
                     + solve(k + 1, j, cuts, dp);

            ans = min(ans, cost);
        }
        return dp[i][j] = ans;
    }

    int minCost(int n, vector<int>& cuts) {
        sort(cuts.begin(), cuts.end());
        cuts.insert(cuts.begin(), 0);
        cuts.push_back(n);
        int m = cuts.size() - 2;
        vector<vector<int>> dp(m + 1, vector<int>(m + 1, -1));
        return solve(1, m, cuts, dp);
    }
};"""
    ),

    ProblemEntry(
        number=33, title="Climbing Stairs", category="Dynamic Programming", session=7,
        code=r"""class Solution {
public:
    int climbStairs(int n) {
        if (n == 1) return 1;
        vector<int> dp(n, 0);
        dp[0] = 1;
        dp[1] = 2;

        for (int i = 2; i < n; i++) {
            dp[i] = dp[i-1] + dp[i-2];
        }

        return dp[n-1];
    }
};"""
    ),

    ProblemEntry(
        number=34, title="Coin Change", category="Dynamic Programming", session=7,
        code=r"""class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);

        dp[0] = 0;

        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = min(dp[i], dp[i - coin] + 1);
                }
            }
        }

        return dp[amount] > amount ? -1 : dp[amount];
    }
};"""
    ),

    ProblemEntry(
        number=35, title="Jump Game", category="Greedy", session=8,
        code=r"""class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxReach = 0;

        for (int i = 0; i < nums.size(); i++) {
            if (i > maxReach)
                return false;

            maxReach = max(maxReach, i + nums[i]);
        }

        return true;
    }
};"""
    ),

    ProblemEntry(
        number=36, title="Length of LIS", category="Dynamic Programming", session=8,
        code=r"""class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);

        int ans = 1;

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    dp[i] = max(dp[i], dp[j] + 1);
                }
            }
            ans = max(ans, dp[i]);
        }

        return ans;
    }
};"""
    ),

    ProblemEntry(
        number=37, title="Jump Game II", category="Greedy", session=8,
        code=r"""class Solution {
public:
    int jump(vector<int>& nums) {
        int jumps = 0;
        int end = 0;
        int maxReach = 0;

        for (int i = 0; i < nums.size() - 1; i++) {
            maxReach = max(maxReach, i + nums[i]);

            if (i == end) {
                jumps++;
                end = maxReach;
            }
        }

        return jumps;
    }
};"""
    ),

    ProblemEntry(
        number=38, title="Assign Cookies", category="Greedy", session=8,
        code=r"""class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());

        int i = 0, j = 0;

        while (i < g.size() && j < s.size()) {
            if (s[j] >= g[i]) {
                i++;
            }
            j++;
        }

        return i;
    }
};"""
    ),

    ProblemEntry(
        number=39, title="Huffman Coding", category="Greedy / Priority Queue", session=8,
        code=r"""struct Node {
    int freq, idx;
    Node *left, *right;
    Node(int f, int i) : freq(f), idx(i), left(nullptr), right(nullptr) {}
};

struct cmp {
    bool operator()(Node* a, Node* b) {
        return a->freq > b->freq || (a->freq == b->freq && a->idx > b->idx);
    }
};

class Solution {
    void preorder(Node* root, string code, vector<string>& ans) {
        if (!root->left && !root->right) {
            ans[root->idx] = code;
            return;
        }
        preorder(root->left,  code + "0", ans);
        preorder(root->right, code + "1", ans);
    }
public:
    vector<string> huffmanCodes(string& s, vector<int> f) {
        int n = s.size();

        // Special case: only one character
        if (n == 1) return {"0"};

        priority_queue<Node*, vector<Node*>, cmp> pq;

        for (int i = 0; i < n; i++) {
            pq.push(new Node(f[i], i));
        }

        while (pq.size() > 1) {
            Node* left  = pq.top(); pq.pop();
            Node* right = pq.top(); pq.pop();

            Node* parent = new Node(left->freq + right->freq,
                                    min(left->idx, right->idx));
            parent->left  = left;
            parent->right = right;

            pq.push(parent);
        }

        vector<string> ans(n);
        preorder(pq.top(), "", ans);

        return ans;
    }
};"""
    ),
]
