"""
problems/registry.py
All 39 C++ programs derived from the DSA lab assignment sheet.

Structure
─────────
Row  = one table row (S.No.) in the assignment sheet
Each row may contain 1 or 2 programs separated by a comma.
Programs are numbered 1-39 sequentially.

ProblemEntry fields
───────────────────
  num      : 1-based sequential program number
  session  : S.No. row from the original table
  title    : short display title
  category : used for colour-coded section badges
  code     : complete, compilable C++ source
"""
from dataclasses import dataclass
from typing import Dict


@dataclass
class ProblemEntry:
    num: int
    session: int
    title: str
    category: str
    code: str


# ─────────────────────────────────────────────────────────────────────────────
# Full registry — 39 programs
# ─────────────────────────────────────────────────────────────────────────────
PROBLEMS: Dict[int, ProblemEntry] = {

# ── Session 1 ────────────────────────────────────────────────────────────────
1: ProblemEntry(num=1, session=1,
    title="Prefix Sum Array",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

vector<int> buildPrefixSum(vector<int>& arr) {
    int n = arr.size();
    vector<int> prefix(n);
    prefix[0] = arr[0];
    for (int i = 1; i < n; i++)
        prefix[i] = prefix[i-1] + arr[i];
    return prefix;
}

// Query range sum [l, r] in O(1)
int rangeQuery(vector<int>& prefix, int l, int r) {
    return prefix[r] - (l > 0 ? prefix[l-1] : 0);
}

int main() {
    vector<int> arr = {3, 1, 4, 1, 5, 9, 2};
    vector<int> ps = buildPrefixSum(arr);

    cout << "Array     : ";
    for (int x : arr) cout << x << " ";

    cout << "\\nPrefix Sum: ";
    for (int x : ps)  cout << x << " ";

    cout << "\\nSum [2..5]: " << rangeQuery(ps, 2, 5) << endl;
    return 0;
}
"""),

2: ProblemEntry(num=2, session=1,
    title="Equilibrium Index",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// An index i is an equilibrium index if
// sum(arr[0..i-1]) == sum(arr[i+1..n-1])
int equilibriumIndex(vector<int>& arr) {
    int n = arr.size();
    int totalSum = 0;
    for (int x : arr) totalSum += x;

    int leftSum = 0;
    for (int i = 0; i < n; i++) {
        totalSum -= arr[i];          // rightSum
        if (leftSum == totalSum) return i;
        leftSum += arr[i];
    }
    return -1;
}

int main() {
    vector<int> arr = {-7, 1, 5, 2, -4, 3, 0};
    int idx = equilibriumIndex(arr);
    if (idx != -1)
        cout << "Equilibrium Index: " << idx
             << "  (value = " << arr[idx] << ")" << endl;
    else
        cout << "No equilibrium index found." << endl;
    return 0;
}
"""),

# ── Session 2 ────────────────────────────────────────────────────────────────
3: ProblemEntry(num=3, session=2,
    title="Two Numbers in Sorted Array with Target Sum",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Two-pointer approach — O(n) time, O(1) space
pair<int,int> twoSumSorted(vector<int>& arr, int target) {
    int left = 0, right = (int)arr.size() - 1;
    while (left < right) {
        int sum = arr[left] + arr[right];
        if (sum == target) return {arr[left], arr[right]};
        else if (sum < target) left++;
        else                   right--;
    }
    return {-1, -1};
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 6};
    int target = 6;

    auto [a, b] = twoSumSorted(arr, target);
    if (a != -1)
        cout << "Pair found : " << a << " + " << b
             << " = " << target << endl;
    else
        cout << "No such pair exists." << endl;
    return 0;
}
"""),

# ── Session 3 ────────────────────────────────────────────────────────────────
4: ProblemEntry(num=4, session=3,
    title="Majority Element",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Boyer-Moore Voting Algorithm — O(n) time, O(1) space
int majorityElement(vector<int>& nums) {
    int candidate = nums[0], count = 1;
    for (int i = 1; i < (int)nums.size(); i++) {
        if (count == 0) { candidate = nums[i]; count = 1; }
        else if (nums[i] == candidate) count++;
        else                           count--;
    }
    return candidate;
}

int main() {
    vector<int> nums = {2, 2, 1, 1, 1, 2, 2};
    cout << "Majority Element: " << majorityElement(nums) << endl;
    return 0;
}
"""),

5: ProblemEntry(num=5, session=3,
    title="Counting Bits",
    category="Bit",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// dp[i] = dp[i >> 1] + (i & 1)
// For every i, right-shift drops LSB; add 1 if LSB was set.
vector<int> countBits(int n) {
    vector<int> dp(n + 1, 0);
    for (int i = 1; i <= n; i++)
        dp[i] = dp[i >> 1] + (i & 1);
    return dp;
}

int main() {
    int n = 8;
    vector<int> res = countBits(n);
    cout << "i  | bits\\n" << string(14, '-') << "\\n";
    for (int i = 0; i <= n; i++)
        cout << i << "  -> " << res[i] << "\\n";
    return 0;
}
"""),

# ── Session 4 ────────────────────────────────────────────────────────────────
6: ProblemEntry(num=6, session=4,
    title="Power of Two",
    category="Bit",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// A power-of-two has exactly one bit set.
// n & (n-1) clears the lowest set bit; result is 0 iff n was a power of two.
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
}

int main() {
    vector<int> tests = {1, 2, 3, 4, 16, 18, 1024, 1025};
    for (int n : tests)
        cout << n << " is"
             << (isPowerOfTwo(n) ? "" : " NOT")
             << " a power of two.\\n";
    return 0;
}
"""),

# ── Session 5 ────────────────────────────────────────────────────────────────
7: ProblemEntry(num=7, session=5,
    title="Trapping Rainwater",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Two-pointer approach — O(n) time, O(1) space
int trap(vector<int>& height) {
    int left = 0, right = (int)height.size() - 1;
    int leftMax = 0, rightMax = 0, water = 0;

    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) leftMax = height[left];
            else                         water += leftMax - height[left];
            left++;
        } else {
            if (height[right] >= rightMax) rightMax = height[right];
            else                           water += rightMax - height[right];
            right--;
        }
    }
    return water;
}

int main() {
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    cout << "Trapped Water Units: " << trap(height) << endl;
    return 0;
}
"""),

# ── Session 6 ────────────────────────────────────────────────────────────────
8: ProblemEntry(num=8, session=6,
    title="Longest Palindromic Substring",
    category="String",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Expand-around-centre — O(n^2) time, O(1) space
string longestPalindrome(const string& s) {
    int n = s.size(), start = 0, maxLen = 1;

    auto expand = [&](int l, int r) {
        while (l >= 0 && r < n && s[l] == s[r]) { l--; r++; }
        // After loop: s[l+1..r-1] is palindrome of length r-l-1
        if (r - l - 1 > maxLen) {
            maxLen = r - l - 1;
            start  = l + 1;
        }
    };

    for (int i = 0; i < n; i++) {
        expand(i, i);       // odd-length
        expand(i, i + 1);   // even-length
    }
    return s.substr(start, maxLen);
}

int main() {
    cout << longestPalindrome("babad") << "\\n";   // bab or aba
    cout << longestPalindrome("cbbd")  << "\\n";   // bb
    return 0;
}
"""),

9: ProblemEntry(num=9, session=6,
    title="Longest Common Prefix",
    category="String",
    code="""\
#include <bits/stdc++.h>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
    if (strs.empty()) return "";
    string prefix = strs[0];

    for (int i = 1; i < (int)strs.size(); i++) {
        // Shrink prefix until strs[i] starts with it
        while (strs[i].find(prefix) != 0) {
            prefix = prefix.substr(0, prefix.size() - 1);
            if (prefix.empty()) return "";
        }
    }
    return prefix;
}

int main() {
    vector<string> v1 = {"flower", "flow", "flight"};
    vector<string> v2 = {"dog", "racecar", "car"};
    cout << "LCP: \\"" << longestCommonPrefix(v1) << "\\"\\n"; // "fl"
    cout << "LCP: \\"" << longestCommonPrefix(v2) << "\\"\\n"; // ""
    return 0;
}
"""),

# ── Session 7 ────────────────────────────────────────────────────────────────
10: ProblemEntry(num=10, session=7,
    title="Merge Two Sorted Linked Lists",
    category="Linked List",
    code="""\
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* cur = &dummy;
    while (l1 && l2) {
        if (l1->val <= l2->val) { cur->next = l1; l1 = l1->next; }
        else                    { cur->next = l2; l2 = l2->next; }
        cur = cur->next;
    }
    cur->next = l1 ? l1 : l2;
    return dummy.next;
}

void printList(ListNode* head) {
    while (head) { cout << head->val << " -> "; head = head->next; }
    cout << "NULL\\n";
}

int main() {
    // l1: 1 -> 3 -> 5
    ListNode* l1 = new ListNode(1);
    l1->next = new ListNode(3);
    l1->next->next = new ListNode(5);

    // l2: 2 -> 4 -> 6
    ListNode* l2 = new ListNode(2);
    l2->next = new ListNode(4);
    l2->next->next = new ListNode(6);

    printList(mergeTwoLists(l1, l2));   // 1 2 3 4 5 6
    return 0;
}
"""),

11: ProblemEntry(num=11, session=7,
    title="Intersection of Two Linked Lists",
    category="Linked List",
    code="""\
#include <bits/stdc++.h>
using namespace std;

struct ListNode {
    int val; ListNode* next;
    ListNode(int x) : val(x), next(nullptr) {}
};

// Two-pointer trick: each pointer traverses both lists → same total distance
ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
    ListNode* a = headA, *b = headB;
    while (a != b) {
        a = a ? a->next : headB;
        b = b ? b->next : headA;
    }
    return a;   // nullptr if no intersection
}

int main() {
    // Shared tail: 8 -> 4 -> 5
    ListNode* shared = new ListNode(8);
    shared->next = new ListNode(4);
    shared->next->next = new ListNode(5);

    ListNode* headA = new ListNode(4);
    headA->next = new ListNode(1);
    headA->next->next = shared;

    ListNode* headB = new ListNode(5);
    headB->next = new ListNode(6);
    headB->next->next = new ListNode(1);
    headB->next->next->next = shared;

    ListNode* res = getIntersectionNode(headA, headB);
    cout << "Intersection at node value: "
         << (res ? res->val : -1) << endl;   // 8
    return 0;
}
"""),

# ── Session 8 ────────────────────────────────────────────────────────────────
12: ProblemEntry(num=12, session=8,
    title="Two Stacks in a Single Array",
    category="Stack",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Stack 1 grows from the left, Stack 2 from the right.
class TwoStacks {
    vector<int> arr;
    int top1, top2, capacity;
public:
    TwoStacks(int n) : arr(n), top1(-1), top2(n), capacity(n) {}

    void push1(int x) {
        if (top1 + 1 < top2) arr[++top1] = x;
        else cout << "Stack 1 overflow\\n";
    }
    void push2(int x) {
        if (top1 + 1 < top2) arr[--top2] = x;
        else cout << "Stack 2 overflow\\n";
    }
    int pop1() {
        if (top1 >= 0) return arr[top1--];
        cout << "Stack 1 underflow\\n"; return INT_MIN;
    }
    int pop2() {
        if (top2 < capacity) return arr[top2++];
        cout << "Stack 2 underflow\\n"; return INT_MIN;
    }
    int peek1() { return top1 >= 0 ? arr[top1] : INT_MIN; }
    int peek2() { return top2 < capacity ? arr[top2] : INT_MIN; }
};

int main() {
    TwoStacks ts(10);
    ts.push1(5);  ts.push1(15);
    ts.push2(10); ts.push2(20);
    cout << "Pop S1: " << ts.pop1() << "\\n";  // 15
    cout << "Pop S2: " << ts.pop2() << "\\n";  // 20
    cout << "Peek S1: " << ts.peek1() << "\\n"; // 5
    return 0;
}
"""),

# ── Session 9 ────────────────────────────────────────────────────────────────
13: ProblemEntry(num=13, session=9,
    title="Next Greater Element",
    category="Stack",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Monotonic stack — O(n) time
vector<int> nextGreaterElement(vector<int>& nums) {
    int n = nums.size();
    vector<int> res(n, -1);
    stack<int> st;   // stores indices

    for (int i = 0; i < n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            res[st.top()] = nums[i];
            st.pop();
        }
        st.push(i);
    }
    return res;
}

int main() {
    vector<int> nums = {4, 5, 2, 25};
    vector<int> res  = nextGreaterElement(nums);
    cout << "Element -> Next Greater\\n";
    for (int i = 0; i < (int)nums.size(); i++)
        cout << "  " << nums[i] << "  ->  " << res[i] << "\\n";
    return 0;
}
"""),

14: ProblemEntry(num=14, session=9,
    title="Rotting Oranges",
    category="Graph",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Multi-source BFS — O(m*n) time
int orangesRotting(vector<vector<int>>& grid) {
    int m = grid.size(), n = grid[0].size();
    queue<pair<int,int>> q;
    int fresh = 0;

    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == 2) q.push({i, j});
            if (grid[i][j] == 1) fresh++;
        }

    if (fresh == 0) return 0;

    int minutes = 0;
    int dirs[4][2] = {{0,1},{0,-1},{1,0},{-1,0}};

    while (!q.empty()) {
        int sz = q.size();
        minutes++;
        while (sz--) {
            auto [r, c] = q.front(); q.pop();
            for (auto& d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                if (nr >= 0 && nr < m && nc >= 0 && nc < n
                    && grid[nr][nc] == 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push({nr, nc});
                }
            }
        }
    }
    return fresh == 0 ? minutes - 1 : -1;
}

int main() {
    vector<vector<int>> grid = {{2,1,1},{1,1,0},{0,1,1}};
    cout << "Minutes to rot all: " << orangesRotting(grid) << endl; // 4
    return 0;
}
"""),

# ── Session 10 ───────────────────────────────────────────────────────────────
15: ProblemEntry(num=15, session=10,
    title="Largest Rectangle in Histogram",
    category="Stack",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Monotonic stack — O(n) time
int largestRectangleArea(vector<int>& heights) {
    stack<int> st;
    int maxArea = 0, n = heights.size();

    for (int i = 0; i <= n; i++) {
        int h = (i == n) ? 0 : heights[i];
        while (!st.empty() && heights[st.top()] > h) {
            int height = heights[st.top()]; st.pop();
            int width  = st.empty() ? i : i - st.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        st.push(i);
    }
    return maxArea;
}

int main() {
    vector<int> heights = {2, 1, 5, 6, 2, 3};
    cout << "Largest Rectangle Area: "
         << largestRectangleArea(heights) << endl;  // 10
    return 0;
}
"""),

# ── Session 11 ───────────────────────────────────────────────────────────────
16: ProblemEntry(num=16, session=11,
    title="Sliding Window Maximum",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Monotonic deque — O(n) time
vector<int> maxSlidingWindow(vector<int>& nums, int k) {
    deque<int> dq;   // stores indices; front = max of window
    vector<int> res;

    for (int i = 0; i < (int)nums.size(); i++) {
        // Remove indices outside window
        if (!dq.empty() && dq.front() <= i - k)
            dq.pop_front();
        // Maintain decreasing order
        while (!dq.empty() && nums[dq.back()] < nums[i])
            dq.pop_back();
        dq.push_back(i);
        if (i >= k - 1)
            res.push_back(nums[dq.front()]);
    }
    return res;
}

int main() {
    vector<int> nums = {1, 3, -1, -3, 5, 3, 6, 7};
    int k = 3;
    vector<int> res = maxSlidingWindow(nums, k);
    cout << "Window Maximums: ";
    for (int x : res) cout << x << " ";
    cout << endl;   // 3 3 5 5 6 7
    return 0;
}
"""),

17: ProblemEntry(num=17, session=11,
    title="Combination Sum",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& cands, int target, int start,
               vector<int>& curr, vector<vector<int>>& res) {
    if (target == 0) { res.push_back(curr); return; }
    for (int i = start; i < (int)cands.size(); i++) {
        if (cands[i] > target) break;
        curr.push_back(cands[i]);
        backtrack(cands, target - cands[i], i, curr, res);
        curr.pop_back();
    }
}

vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
    sort(candidates.begin(), candidates.end());
    vector<vector<int>> res;
    vector<int> curr;
    backtrack(candidates, target, 0, curr, res);
    return res;
}

int main() {
    vector<int> cands = {2, 3, 6, 7};
    int target = 7;
    auto res = combinationSum(cands, target);
    cout << "Combinations summing to " << target << ":\\n";
    for (auto& v : res) {
        for (int x : v) cout << x << " ";
        cout << "\\n";
    }
    return 0;
}
"""),

# ── Session 12 ───────────────────────────────────────────────────────────────
18: ProblemEntry(num=18, session=12,
    title="Generate All Subsets (Power Set)",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Bitmask enumeration — O(2^n * n) time
vector<vector<int>> subsets(vector<int>& nums) {
    int n = nums.size();
    vector<vector<int>> res;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++)
            if (mask & (1 << i))
                subset.push_back(nums[i]);
        res.push_back(subset);
    }
    return res;
}

int main() {
    vector<int> nums = {1, 2, 3};
    auto res = subsets(nums);
    cout << "All " << res.size() << " subsets:\\n";
    for (auto& s : res) {
        cout << "{ ";
        for (int x : s) cout << x << " ";
        cout << "}\\n";
    }
    return 0;
}
"""),

# ── Session 13 ───────────────────────────────────────────────────────────────
19: ProblemEntry(num=19, session=13,
    title="Maximum Frequency After K Operations",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Sliding window on sorted array — O(n log n)
// Make at most k increments so one element appears maximum times.
int maxFrequency(vector<int>& nums, int k) {
    sort(nums.begin(), nums.end());
    int left = 0, res = 1;
    long long total = 0;

    for (int right = 1; right < (int)nums.size(); right++) {
        // Cost to raise all window elements to nums[right]
        total += (long long)(nums[right] - nums[right-1]) * (right - left);
        while (total > k)
            total -= nums[right] - nums[left++];
        res = max(res, right - left + 1);
    }
    return res;
}

int main() {
    vector<int> nums = {1, 2, 4};
    int k = 5;
    cout << "Max frequency after " << k << " ops: "
         << maxFrequency(nums, k) << endl;  // 3
    return 0;
}
"""),

20: ProblemEntry(num=20, session=13,
    title="Two Sum",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Hash-map approach — O(n) time, O(n) space
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> seen;   // value -> index
    for (int i = 0; i < (int)nums.size(); i++) {
        int complement = target - nums[i];
        if (seen.count(complement))
            return {seen[complement], i};
        seen[nums[i]] = i;
    }
    return {};
}

int main() {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    auto res = twoSum(nums, target);
    cout << "Indices: [" << res[0] << ", " << res[1] << "]" << endl; // [0,1]
    return 0;
}
"""),

# ── Session 14 ───────────────────────────────────────────────────────────────
21: ProblemEntry(num=21, session=14,
    title="Median of Two Sorted Arrays",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Binary search — O(log(min(m,n))) time
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > nums2.size()) swap(nums1, nums2);
    int m = nums1.size(), n = nums2.size();
    int lo = 0, hi = m;

    while (lo <= hi) {
        int i = (lo + hi) / 2;
        int j = (m + n + 1) / 2 - i;

        int maxL1 = (i == 0) ? INT_MIN : nums1[i-1];
        int minR1 = (i == m) ? INT_MAX : nums1[i];
        int maxL2 = (j == 0) ? INT_MIN : nums2[j-1];
        int minR2 = (j == n) ? INT_MAX : nums2[j];

        if (maxL1 <= minR2 && maxL2 <= minR1) {
            if ((m + n) % 2 == 0)
                return (max(maxL1, maxL2) + min(minR1, minR2)) / 2.0;
            return max(maxL1, maxL2);
        } else if (maxL1 > minR2) hi = i - 1;
        else                       lo = i + 1;
    }
    return 0.0;
}

int main() {
    vector<int> a = {1, 3}, b = {2};
    cout << "Median: " << findMedianSortedArrays(a, b) << endl;  // 2.0

    vector<int> c = {1, 2}, d = {3, 4};
    cout << "Median: " << findMedianSortedArrays(c, d) << endl;  // 2.5
    return 0;
}
"""),

# ── Session 15 ───────────────────────────────────────────────────────────────
22: ProblemEntry(num=22, session=15,
    title="Subarray Sum Equals K",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Prefix-sum hash map — O(n) time
int subarraySum(vector<int>& nums, int k) {
    unordered_map<int,int> prefixCount;
    prefixCount[0] = 1;
    int sum = 0, count = 0;
    for (int x : nums) {
        sum += x;
        count += prefixCount[sum - k];
        prefixCount[sum]++;
    }
    return count;
}

int main() {
    vector<int> nums = {1, 1, 1};
    int k = 2;
    cout << "Subarrays with sum " << k << ": "
         << subarraySum(nums, k) << endl;  // 2
    return 0;
}
"""),

23: ProblemEntry(num=23, session=15,
    title="Level Order Traversal (BFS)",
    category="Tree",
    code="""\
#include <bits/stdc++.h>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left, *right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

vector<vector<int>> levelOrder(TreeNode* root) {
    vector<vector<int>> res;
    if (!root) return res;

    queue<TreeNode*> q;
    q.push(root);

    while (!q.empty()) {
        int sz = q.size();
        vector<int> level;
        while (sz--) {
            TreeNode* node = q.front(); q.pop();
            level.push_back(node->val);
            if (node->left)  q.push(node->left);
            if (node->right) q.push(node->right);
        }
        res.push_back(level);
    }
    return res;
}

int main() {
    //       3
    //      / \\
    //     9  20
    //        / \\
    //       15   7
    TreeNode* root = new TreeNode(3);
    root->left  = new TreeNode(9);
    root->right = new TreeNode(20);
    root->right->left  = new TreeNode(15);
    root->right->right = new TreeNode(7);

    for (auto& level : levelOrder(root)) {
        for (int x : level) cout << x << " ";
        cout << "\\n";
    }
    return 0;
}
"""),

# ── Session 16 ───────────────────────────────────────────────────────────────
24: ProblemEntry(num=24, session=16,
    title="Number of Connected Components",
    category="Graph",
    code="""\
#include <bits/stdc++.h>
using namespace std;

class UnionFind {
    vector<int> parent, rank_;
public:
    int components;
    UnionFind(int n) : parent(n), rank_(n, 0), components(n) {
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int x) {
        return parent[x] == x ? x : parent[x] = find(parent[x]);
    }
    void unite(int x, int y) {
        x = find(x); y = find(y);
        if (x == y) return;
        if (rank_[x] < rank_[y]) swap(x, y);
        parent[y] = x;
        if (rank_[x] == rank_[y]) rank_[x]++;
        components--;
    }
};

int countComponents(int n, vector<vector<int>>& edges) {
    UnionFind uf(n);
    for (auto& e : edges) uf.unite(e[0], e[1]);
    return uf.components;
}

int main() {
    int n = 5;
    vector<vector<int>> edges = {{0,1},{1,2},{3,4}};
    cout << "Connected Components: "
         << countComponents(n, edges) << endl;  // 2
    return 0;
}
"""),

# ── Session 17 ───────────────────────────────────────────────────────────────
25: ProblemEntry(num=25, session=17,
    title="Flood Fill",
    category="Graph",
    code="""\
#include <bits/stdc++.h>
using namespace std;

void dfs(vector<vector<int>>& img, int r, int c, int orig, int color) {
    if (r < 0 || r >= (int)img.size() ||
        c < 0 || c >= (int)img[0].size() ||
        img[r][c] != orig) return;
    img[r][c] = color;
    dfs(img, r+1, c, orig, color);
    dfs(img, r-1, c, orig, color);
    dfs(img, r, c+1, orig, color);
    dfs(img, r, c-1, orig, color);
}

vector<vector<int>> floodFill(vector<vector<int>>& image,
                               int sr, int sc, int newColor) {
    int orig = image[sr][sc];
    if (orig != newColor) dfs(image, sr, sc, orig, newColor);
    return image;
}

int main() {
    vector<vector<int>> image = {{1,1,1},{1,1,0},{1,0,1}};
    floodFill(image, 1, 1, 2);
    for (auto& row : image) {
        for (int x : row) cout << x << " ";
        cout << "\\n";
    }
    return 0;
}
"""),

26: ProblemEntry(num=26, session=17,
    title="Cheapest Flights Within K Stops",
    category="Graph",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Bellman-Ford variant with K relaxation rounds — O(K * E)
int findCheapestPrice(int n, vector<vector<int>>& flights,
                      int src, int dst, int k) {
    vector<int> prices(n, INT_MAX);
    prices[src] = 0;

    for (int i = 0; i <= k; i++) {
        vector<int> tmp = prices;
        for (auto& f : flights) {
            int from = f[0], to = f[1], cost = f[2];
            if (prices[from] != INT_MAX)
                tmp[to] = min(tmp[to], prices[from] + cost);
        }
        prices = tmp;
    }
    return prices[dst] == INT_MAX ? -1 : prices[dst];
}

int main() {
    int n = 4;
    vector<vector<int>> flights = {
        {0,1,100},{1,2,100},{2,0,100},{1,3,600},{2,3,200}
    };
    cout << "Cheapest price (src=0, dst=3, K=1): "
         << findCheapestPrice(n, flights, 0, 3, 1) << endl;  // 700
    return 0;
}
"""),

# ── Session 18 ───────────────────────────────────────────────────────────────
27: ProblemEntry(num=27, session=18,
    title="Count Inversions in an Array",
    category="Array",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Modified Merge Sort — O(n log n) time
long long mergeCount(vector<int>& arr, int l, int mid, int r) {
    vector<int> left(arr.begin()+l,   arr.begin()+mid+1);
    vector<int> right(arr.begin()+mid+1, arr.begin()+r+1);
    long long count = 0;
    int i = 0, j = 0, k = l;

    while (i < (int)left.size() && j < (int)right.size()) {
        if (left[i] <= right[j]) {
            arr[k++] = left[i++];
        } else {
            arr[k++] = right[j++];
            count += (long long)(left.size() - i);  // all remaining left[] > right[j]
        }
    }
    while (i < (int)left.size())  arr[k++] = left[i++];
    while (j < (int)right.size()) arr[k++] = right[j++];
    return count;
}

long long countInversions(vector<int>& arr, int l, int r) {
    if (l >= r) return 0;
    int mid = (l + r) / 2;
    return countInversions(arr, l, mid)
         + countInversions(arr, mid+1, r)
         + mergeCount(arr, l, mid, r);
}

int main() {
    vector<int> arr = {8, 4, 2, 1};
    cout << "Inversions: "
         << countInversions(arr, 0, (int)arr.size()-1) << endl;  // 6
    return 0;
}
"""),

# ── Session 19 ───────────────────────────────────────────────────────────────
28: ProblemEntry(num=28, session=19,
    title="Edit Distance",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Classic Levenshtein DP — O(m*n) time and space
int minDistance(const string& word1, const string& word2) {
    int m = word1.size(), n = word2.size();
    vector<vector<int>> dp(m+1, vector<int>(n+1));

    for (int i = 0; i <= m; i++) dp[i][0] = i;
    for (int j = 0; j <= n; j++) dp[0][j] = j;

    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            if (word1[i-1] == word2[j-1])
                dp[i][j] = dp[i-1][j-1];
            else
                dp[i][j] = 1 + min({dp[i-1][j],   // delete
                                     dp[i][j-1],   // insert
                                     dp[i-1][j-1]  // replace
                                    });
        }
    return dp[m][n];
}

int main() {
    cout << minDistance("horse", "ros")    << "\\n";  // 3
    cout << minDistance("intention", "execution") << "\\n";  // 5
    return 0;
}
"""),

29: ProblemEntry(num=29, session=19,
    title="Unique Paths",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// 2-D DP — O(m*n) time
int uniquePaths(int m, int n) {
    vector<vector<int>> dp(m, vector<int>(n, 1));
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
    return dp[m-1][n-1];
}

int main() {
    cout << "3x7 grid: " << uniquePaths(3, 7) << "\\n";  // 28
    cout << "3x2 grid: " << uniquePaths(3, 2) << "\\n";  // 3
    return 0;
}
"""),

# ── Session 20 ───────────────────────────────────────────────────────────────
30: ProblemEntry(num=30, session=20,
    title="Longest Palindromic Subsequence",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// LPS = LCS(s, reverse(s)) — O(n^2) time
int longestPalindromeSubseq(const string& s) {
    int n = s.size();
    string t(s.rbegin(), s.rend());
    vector<vector<int>> dp(n+1, vector<int>(n+1, 0));

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++) {
            if (s[i-1] == t[j-1]) dp[i][j] = dp[i-1][j-1] + 1;
            else                   dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
        }
    return dp[n][n];
}

int main() {
    cout << longestPalindromeSubseq("bbbab")  << "\\n";  // 4
    cout << longestPalindromeSubseq("cbbd")   << "\\n";  // 2
    return 0;
}
"""),

# ── Session 21 ───────────────────────────────────────────────────────────────
31: ProblemEntry(num=31, session=21,
    title="House Robber Problem",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Space-optimised DP — O(n) time, O(1) space
int rob(vector<int>& nums) {
    int prev2 = 0, prev1 = 0;
    for (int x : nums) {
        int curr = max(prev1, prev2 + x);
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

int main() {
    vector<int> a = {1, 2, 3, 1};
    vector<int> b = {2, 7, 9, 3, 1};
    cout << "Max loot [1,2,3,1]: "   << rob(a) << "\\n";  // 4
    cout << "Max loot [2,7,9,3,1]: " << rob(b) << "\\n";  // 12
    return 0;
}
"""),

32: ProblemEntry(num=32, session=21,
    title="Minimum Cost to Cut a Stick",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Interval DP — O(m^3) where m = number of cut points + 2
int minCost(int n, vector<int>& cuts) {
    cuts.push_back(0);
    cuts.push_back(n);
    sort(cuts.begin(), cuts.end());
    int m = cuts.size();
    vector<vector<int>> dp(m, vector<int>(m, 0));

    for (int len = 2; len < m; len++) {
        for (int l = 0; l + len < m; l++) {
            int r = l + len;
            dp[l][r] = INT_MAX;
            for (int k = l + 1; k < r; k++) {
                int cost = cuts[r] - cuts[l] + dp[l][k] + dp[k][r];
                dp[l][r] = min(dp[l][r], cost);
            }
        }
    }
    return dp[0][m-1];
}

int main() {
    int n = 7;
    vector<int> cuts = {1, 3, 4, 5};
    cout << "Min cost: " << minCost(n, cuts) << "\\n";  // 16
    return 0;
}
"""),

# ── Session 22 ───────────────────────────────────────────────────────────────
33: ProblemEntry(num=33, session=22,
    title="Climbing Stairs",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Fibonacci-style DP — O(n) time, O(1) space
// At each step you can climb 1 or 2 stairs.
int climbStairs(int n) {
    if (n <= 2) return n;
    int a = 1, b = 2;
    for (int i = 3; i <= n; i++) {
        int c = a + b;
        a = b; b = c;
    }
    return b;
}

int main() {
    for (int n : {1, 2, 3, 4, 5, 10})
        cout << "Ways to climb " << n << " stairs: "
             << climbStairs(n) << "\\n";
    return 0;
}
"""),

# ── Session 23 ───────────────────────────────────────────────────────────────
34: ProblemEntry(num=34, session=23,
    title="Coin Change (Minimum Coins)",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Bottom-up DP — O(amount * |coins|)
int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, INT_MAX);
    dp[0] = 0;
    for (int i = 1; i <= amount; i++)
        for (int c : coins)
            if (c <= i && dp[i-c] != INT_MAX)
                dp[i] = min(dp[i], dp[i-c] + 1);
    return dp[amount] == INT_MAX ? -1 : dp[amount];
}

int main() {
    vector<int> coins1 = {1, 5, 6, 9};
    cout << "Min coins for 11: " << coinChange(coins1, 11) << "\\n"; // 2
    vector<int> coins2 = {2};
    cout << "Min coins for  3: " << coinChange(coins2, 3)  << "\\n"; // -1
    return 0;
}
"""),

35: ProblemEntry(num=35, session=23,
    title="Jump Game",
    category="Greedy",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Greedy — O(n) time, O(1) space
// Track the farthest index reachable so far.
bool canJump(vector<int>& nums) {
    int maxReach = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        if (i > maxReach) return false;
        maxReach = max(maxReach, i + nums[i]);
    }
    return true;
}

int main() {
    vector<int> a = {2, 3, 1, 1, 4};
    vector<int> b = {3, 2, 1, 0, 4};
    cout << "Can jump [2,3,1,1,4]: " << (canJump(a) ? "Yes" : "No") << "\\n"; // Yes
    cout << "Can jump [3,2,1,0,4]: " << (canJump(b) ? "Yes" : "No") << "\\n"; // No
    return 0;
}
"""),

# ── Session 24 ───────────────────────────────────────────────────────────────
36: ProblemEntry(num=36, session=24,
    title="Longest Increasing Subsequence (LIS)",
    category="DP",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Patience sorting (binary search) — O(n log n) time
int lengthOfLIS(vector<int>& nums) {
    vector<int> tails;  // tails[i] = smallest tail of all IS of length i+1
    for (int x : nums) {
        auto it = lower_bound(tails.begin(), tails.end(), x);
        if (it == tails.end()) tails.push_back(x);
        else                   *it = x;
    }
    return (int)tails.size();
}

int main() {
    vector<int> nums = {10, 9, 2, 5, 3, 7, 101, 18};
    cout << "LIS length: " << lengthOfLIS(nums) << "\\n";  // 4
    return 0;
}
"""),

# ── Session 25 ───────────────────────────────────────────────────────────────
37: ProblemEntry(num=37, session=25,
    title="Jump Game II (Minimum Jumps)",
    category="Greedy",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Greedy BFS-like — O(n) time, O(1) space
int jump(vector<int>& nums) {
    int jumps = 0, curEnd = 0, farthest = 0;
    for (int i = 0; i < (int)nums.size() - 1; i++) {
        farthest = max(farthest, i + nums[i]);
        if (i == curEnd) {
            jumps++;
            curEnd = farthest;
        }
    }
    return jumps;
}

int main() {
    vector<int> a = {2, 3, 1, 1, 4};
    vector<int> b = {2, 3, 0, 1, 4};
    cout << "Min jumps [2,3,1,1,4]: " << jump(a) << "\\n";  // 2
    cout << "Min jumps [2,3,0,1,4]: " << jump(b) << "\\n";  // 2
    return 0;
}
"""),

38: ProblemEntry(num=38, session=25,
    title="Assign Cookies",
    category="Greedy",
    code="""\
#include <bits/stdc++.h>
using namespace std;

// Greedy: match smallest sufficient cookie to greediest child
int findContentChildren(vector<int>& g, vector<int>& s) {
    sort(g.begin(), g.end());
    sort(s.begin(), s.end());
    int child = 0, cookie = 0;
    while (child < (int)g.size() && cookie < (int)s.size()) {
        if (s[cookie] >= g[child]) child++;  // child satisfied
        cookie++;
    }
    return child;
}

int main() {
    vector<int> g1 = {1, 2, 3}, s1 = {1, 1};
    vector<int> g2 = {1, 2},    s2 = {1, 2, 3};
    cout << "Content children (g1,s1): " << findContentChildren(g1, s1) << "\\n"; // 1
    cout << "Content children (g2,s2): " << findContentChildren(g2, s2) << "\\n"; // 2
    return 0;
}
"""),

# ── Session 26 ───────────────────────────────────────────────────────────────
39: ProblemEntry(num=39, session=26,
    title="Huffman Encoding",
    category="Greedy",
    code="""\
#include <bits/stdc++.h>
using namespace std;

struct HuffNode {
    char ch; int freq;
    HuffNode *left, *right;
    HuffNode(char c, int f)
        : ch(c), freq(f), left(nullptr), right(nullptr) {}
};

struct Compare {
    bool operator()(HuffNode* a, HuffNode* b) { return a->freq > b->freq; }
};

void printCodes(HuffNode* root, const string& code) {
    if (!root) return;
    if (!root->left && !root->right) {
        cout << "  '" << root->ch << "'  :  " << code << "\\n";
        return;
    }
    printCodes(root->left,  code + "0");
    printCodes(root->right, code + "1");
}

void huffmanEncoding(const string& text) {
    unordered_map<char,int> freq;
    for (char c : text) freq[c]++;

    priority_queue<HuffNode*, vector<HuffNode*>, Compare> pq;
    for (auto& [c, f] : freq) pq.push(new HuffNode(c, f));

    while (pq.size() > 1) {
        HuffNode* l = pq.top(); pq.pop();
        HuffNode* r = pq.top(); pq.pop();
        HuffNode* m = new HuffNode('\\0', l->freq + r->freq);
        m->left = l; m->right = r;
        pq.push(m);
    }

    cout << "Huffman Codes for \\"" << text << "\\":\\n";
    printCodes(pq.top(), "");
}

int main() {
    huffmanEncoding("huffman encoding");
    return 0;
}
"""),

}  # end PROBLEMS dict
