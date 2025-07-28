# 📝 Day 04 - Notes

## 🔍 Problem:
**LeetCode 4 – Median of Two Sorted Arrays**

> Given two sorted arrays `nums1` and `nums2` of size `m` and `n`, return the median of the two sorted arrays.

You must solve the problem in `O(log (m+n))` time complexity (Note: this implementation solves it in `O(m+n)`).

---

## ✅ Approach Used:
**Simple Merge and Sort**

- Merge both arrays using `+` and apply `sorted()` to get the final sorted list.
- If the total number of elements is:
  - **Even**: Median is the average of the two middle elements.
  - **Odd**: Median is the middle element.

---

## 💡 Key Concepts:

- Median of an array of length `n` is:
  - `n//2` if odd (middle element)
  - `(n//2 - 1 + n//2) / 2` if even (average of two middle elements)
- Use Python's built-in `sorted()` to simplify merging.

---

## 📦 Complexity:

- **Time:** `O(m + n log (m + n))` due to sorting.
- **Space:** `O(m + n)` to store the merged array.

> ⚠️ Not optimal for large input sizes; a binary search approach exists for `O(log (m+n))` complexity.

---

## ⚠️ Mistakes to Avoid:

- ❌ Indexing errors in even/odd median cases.
- ❌ Forgetting to convert to float in even case.
- ✅ Handle both `even` and `odd` number of elements correctly.

---

## ✅ Learnings:

- Quick and simple method using sort is good for small inputs.
- Efficient solutions require binary search over partitions.

---

## 🔗 Python Solution File:

- [Day04/question4.py](./question4.py)
