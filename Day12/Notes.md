# 📝 Day 12 - Notes

## 🔍 Problem:
**LeetCode 88 – Merge Sorted Array**

> You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.  
> Merge `nums2` into `nums1` as one sorted array **in-place**.

Note: `nums1` has enough space (size `m + n`) to hold additional elements from `nums2`.

---

## ✅ Approach Used:
**Two Pointers from the End (Reverse Merge)**

- Start filling `nums1` from the **end**, using three pointers:
  - `x` → last valid element in `nums1` (`m-1`)
  - `y` → last element in `nums2` (`n-1`)
  - `z` → last position in `nums1` (`m + n - 1`)
- Compare `nums1[x]` and `nums2[y]`, and place the larger one at `nums1[z]`.
- Decrement pointers accordingly.

---

## 💡 Key Concepts:

- Reverse merging avoids overwriting elements in `nums1`.
- Efficient because it avoids the need for extra space.
- Handles edge cases where one of the arrays is empty.

---

## 📦 Complexity:

- **Time:** `O(m + n)` – every element is visited once.
- **Space:** `O(1)` – done in-place without extra memory.

---

## ⚠️ Mistakes to Avoid:

- ❌ Starting merge from the beginning (would require shifting).
- ✅ Always compare and write from the end to avoid overwriting.

---

## ✅ Learnings:

- In-place merge is possible when writing **backwards**.
- Knowing array constraints helps determine pointer directions.

---

## 🔗 Python Solution File:

- [Day12/question12.py](./question12.py)
