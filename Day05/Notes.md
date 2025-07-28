# 📝 Day 05 - Notes

## 🔍 Problem:
**LeetCode 34 – Find First and Last Position of Element in Sorted Array**

> Given a sorted array `nums` and a target value `target`, find the starting and ending position of the target in `O(log n)` time.

If the target is not found in the array, return `[-1, -1]`.

---

## ✅ Approach Used:
**Binary Search (Modified)**

- Use two separate binary searches:
  1. One to find the **first occurrence** of the target.
  2. One to find the **last occurrence** of the target.
- Adjust the search boundaries based on whether you are looking for the first or last index.

---

## 💡 Key Concepts:

- Standard binary search logic is **modified**:
  - While searching for the **first**, continue moving `end` left if `nums[mid] == target`.
  - While searching for the **last**, continue moving `start` right if `nums[mid] == target`.
- Use helper functions to encapsulate logic for clarity.

---

## 📦 Complexity:

- **Time:** `O(log n)` – due to binary search on a sorted array.
- **Space:** `O(1)` – only constant space used.

---

## ⚠️ Mistakes to Avoid:

- ❌ Stopping search immediately when `nums[mid] == target` — might miss earlier/later instances.
- ✅ Always adjust boundaries after a match to ensure correct `first` or `last` index is found.

---

## ✅ Learnings:

- Binary search is versatile and can be customized for **first/last occurrence** problems.
- Wrapping custom search logic into helper functions improves code readability.

---

## 🔗 Python Solution File:

- [Day05/question.py](./question.py)
