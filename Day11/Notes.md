# 📝 Day 11 - Notes

## 🔍 Problem:
**LeetCode 26 – Remove Duplicates from Sorted Array**

> Given a **sorted** array `nums`, remove the duplicates **in-place** such that each element appears only once and return the new length `k`.

Do not allocate extra space; modify the input array in-place with O(1) extra memory.

---

## ✅ Approach Used:
**Two Pointers (Slow-Fast Pointer)**

- Use pointer `k` to mark the next unique position.
- Start loop from index 1 to end:
  - If current element is different from previous, place it at index `k`, and increment `k`.
- After the loop, `k` will hold the number of unique elements.

---

## 💡 Key Concepts:

- Since the array is sorted, all duplicates will be adjacent.
- `nums[0:k]` contains the unique elements after the function finishes.
- In-place overwrite ensures constant space usage.

---

## 📦 Complexity:

- **Time:** `O(n)` – one pass through the array
- **Space:** `O(1)` – in-place modification

---

## ⚠️ Mistakes to Avoid:

- ❌ Using a new array (violates the in-place constraint)
- ✅ Always compare with previous element since array is sorted

---

## ✅ Learnings:

- This is a classic two-pointer problem.
- Sorting helps reduce complexity when searching for unique values.

---

## 🔗 Python Solution File:

- [Day11/question.py](./question.py)
****
