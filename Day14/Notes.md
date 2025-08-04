# 📝 Day 14 - Notes

## 🔍 Problem:
**LeetCode 704 – Binary Search**

> Given a sorted array of integers `nums` and an integer `target`,  
> return the index of `target` if it exists in the array. Otherwise, return `-1`.

The array is sorted in ascending order. You must implement the solution in `O(log n)` time.

---

## ✅ Approach Used:
**Classic Binary Search**

- Initialize two pointers: `l = 0` (left), `r = len(nums) - 1` (right).
- While `l <= r`, calculate mid: `m = (l + r) // 2`.
- If `nums[m] == target`, return `m` (index found).
- If `nums[m] > target`, shift the search to the left half (`r = m - 1`).
- If `nums[m] < target`, shift the search to the right half (`l = m + 1`).
- If the loop ends, return `-1` (target not found).

---

## 💡 Key Concepts:

- Binary search is optimal for sorted arrays.
- The goal is to **halve the search space** at each step.
- Uses integer division (`//`) to find the mid-point.

---

## 📦 Complexity:

- **Time:** `O(log n)` – halving the range in each iteration.
- **Space:** `O(1)` – only uses a few pointers.

---

## ⚠️ Mistakes to Avoid:

- ❌ Forgetting to update the left or right pointer.
- ❌ Using `l < r` instead of `l <= r` can skip the last check.
- ✅ Always check `nums[mid]` before adjusting pointers.

---

## ✅ Learnings:

- Binary search is a **foundational algorithm** in DSA.
- Great for problems involving **sorted arrays**, **searching positions**, or **min/max constraints**.

---

## 🔗 Python Solution File:

- [Day14/question.py](./question.py)
