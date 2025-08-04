# 📝 Day 10 - Notes

## 🔍 Problem:
**LeetCode 15 – 3Sum**

> Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:
- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- The solution set must not contain duplicate triplets.

---

## ✅ Approach Used:
**Two Pointers + Sorting**

- First, sort the array to help efficiently skip duplicates and use two-pointer strategy.
- Iterate through the array with index `i`:
  - Skip duplicates using `if i > 0 and nums[i] == nums[i - 1]`.
  - For each `nums[i]`, apply two-pointer method from `i+1` to end of array.
  - If the sum is:
    - `> 0`: move `r` left
    - `< 0`: move `l` right
    - `== 0`: store triplet and skip duplicates

---

## 💡 Key Concepts:

- Sorting helps in:
  - Skipping duplicates efficiently
  - Using two-pointer pattern in `O(n)` per iteration
- Efficient way to avoid nested triple loops.

---

## 📦 Complexity:

- **Time:** `O(n^2)` – outer loop + inner two-pointer traversal
- **Space:** `O(1)` (ignoring output list)

---

## ⚠️ Mistakes to Avoid:

- ❌ Forgetting to skip duplicate elements at both `i`, `l`, and `r`.
- ❌ Not sorting the array initially.
- ✅ Always move pointers carefully after storing a valid triplet.

---

## ✅ Learnings:

- Sorting + two-pointer is a powerful technique for sum-related problems.
- Always consider duplicates when generating combinations.

---

## 🔗 Python Solution File:

- [Day10/question.py](./question.py)
