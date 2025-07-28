# 📝 Day 06 - Notes

## 🔍 Problem:
**LeetCode 162 – Find Peak Element**

> A peak element is an element that is strictly greater than its neighbors.  
> Given an integer array `nums`, find a peak element, and return its index.  
> You may imagine that `nums[-1] = nums[n] = -∞`.

You must solve it in `O(log n)` time.

---

## ✅ Approach Used:
**Binary Search (Divide and Conquer)**

- Compare middle element with its neighbor.
- If `nums[mid] > nums[mid + 1]`, then the **peak lies on the left side (including mid)**.
- Else, the **peak lies on the right side**.

---

## 💡 Key Concepts:

- Peak element exists due to boundary conditions (`-∞`).
- Always move towards the side with a higher neighbor → ensures a peak exists in that direction.
- Greedy choice with binary search ensures `O(log n)` time.

---

## 📦 Complexity:

- **Time:** `O(log n)` – binary search on the array.
- **Space:** `O(1)` – constant space.

---

## ⚠️ Mistakes to Avoid:

- ❌ Checking all elements linearly → gives `O(n)` which is not optimal.
- ✅ Don't forget to handle the edge elements.

---

## ✅ Learnings:

- This problem reinforces the idea that binary search can be used **even when the condition is not equality-based**.
- Important to leverage properties like **monotonicity** or **trend direction**.

---

## 🔗 Python Solution File:

- [Day06/question.py](./question.py)
