# DSA Manual Pipeline

A CLI automation pipeline that scans a folder of submission screenshots,
auto-maps them to the correct C++ program, and generates a styled A4 `.docx`
DSA Reference Manual — no manual copy-paste needed.

---

## Setup

```bash
cd dsa_pipeline
pip install -r requirements.txt
```

---

## Usage

### 1. Auto-scan a screenshots folder

Name your screenshots by problem number:
- `1.png`, `01.png`, `prog_1.png`, `lc1.png` → Problem 1
- `15_subarray_sum.png` → Problem 15

```bash
python main.py --screenshots C:\screenshots --output DSA_Manual.docx
```

### 2. Override opaque filenames

If your screenshot has a random name (e.g. `image_daac7f.png`), use `--map`:

```bash
python main.py --screenshots C:\screenshots \
  --map 20:image_daac7f.png 1:screenshot_abc.png \
  --output DSA_Manual.docx
```

### 3. Generate specific programs only

```bash
python main.py --screenshots C:\screenshots --problems 1,2,3,20
```

### 4. Code-only mode (no screenshots)

```bash
python main.py --output DSA_Manual.docx
```

---

## Program List (39 programs across 26 sessions)

| # | Title | Category | Session |
|---|-------|----------|---------|
| 1 | Prefix Sum Array | Array | 1 |
| 2 | Equilibrium Index | Array | 1 |
| 3 | Two Numbers in Sorted Array with Target Sum | Array | 2 |
| 4 | Majority Element | Array | 3 |
| 5 | Counting Bits | Bit | 3 |
| 6 | Power of Two | Bit | 4 |
| 7 | Trapping Rainwater | Array | 5 |
| 8 | Longest Palindromic Substring | String | 6 |
| 9 | Longest Common Prefix | String | 6 |
| 10 | Merge Two Sorted Linked Lists | Linked List | 7 |
| 11 | Intersection of Two Linked Lists | Linked List | 7 |
| 12 | Two Stacks in a Single Array | Stack | 8 |
| 13 | Next Greater Element | Stack | 9 |
| 14 | Rotting Oranges | Graph | 9 |
| 15 | Largest Rectangle in Histogram | Stack | 10 |
| 16 | Sliding Window Maximum | Array | 11 |
| 17 | Combination Sum | Array | 11 |
| 18 | Generate All Subsets (Power Set) | Array | 12 |
| 19 | Maximum Frequency After K Operations | Array | 13 |
| 20 | Two Sum | Array | 13 |
| 21 | Median of Two Sorted Arrays | Array | 14 |
| 22 | Subarray Sum Equals K | Array | 15 |
| 23 | Level Order Traversal (BFS) | Tree | 15 |
| 24 | Number of Connected Components | Graph | 16 |
| 25 | Flood Fill | Graph | 17 |
| 26 | Cheapest Flights Within K Stops | Graph | 17 |
| 27 | Count Inversions in an Array | Array | 18 |
| 28 | Edit Distance | DP | 19 |
| 29 | Unique Paths | DP | 19 |
| 30 | Longest Palindromic Subsequence | DP | 20 |
| 31 | House Robber Problem | DP | 21 |
| 32 | Minimum Cost to Cut a Stick | DP | 21 |
| 33 | Climbing Stairs | DP | 22 |
| 34 | Coin Change (Minimum Coins) | DP | 23 |
| 35 | Jump Game | Greedy | 23 |
| 36 | Longest Increasing Subsequence (LIS) | DP | 24 |
| 37 | Jump Game II (Minimum Jumps) | Greedy | 25 |
| 38 | Assign Cookies | Greedy | 25 |
| 39 | Huffman Encoding | Greedy | 26 |

---

## Project Structure

```
dsa_pipeline/
├── main.py          # CLI entry point
├── config.py        # Design tokens (colours, fonts, sizes)
├── scanner.py       # Auto-maps screenshot filenames → problem numbers
├── problems/
│   ├── __init__.py
│   └── registry.py  # All 39 C++ programs
├── builder/
│   ├── __init__.py
│   ├── document.py  # Assembles the full Word document
│   └── sections.py  # Renders individual problem sections
├── requirements.txt
└── README.md
```
