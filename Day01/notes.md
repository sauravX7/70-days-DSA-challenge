# 📝 Day 01 - Notes

## 🔍 Problem:
**LeetCode 1695 – Maximum Erasure Value**

> Given an array of positive integers `nums`, return the maximum sum of a subarray with all **unique elements**.

---

## ✅ Approach Used:
**Sliding Window + HashSet**

- Use two pointers `start` and `end` to maintain a sliding window of unique elements.
- Use a `set()` to keep track of which numbers are in the current window.
- Move the `end` pointer forward.
- If a duplicate is found (`nums[end]` is already in the set):
  - Remove elements from the left (`start`) until the duplicate is removed.
- Update the `current_sum` and track the maximum.

---

## 💡 Key Concepts:

- Subarray: must be **contiguous**.
- HashSet ensures uniqueness.
- Sliding window avoids brute force checking of all subarrays.

---

## 📦 Complexity:

- **Time:** `O(n)` – each element is added/removed at most once.
- **Space:** `O(n)` – for the `seen` set storing current unique elements.

---

## ⚠️ Mistakes to Avoid:

- ❌ Tried sorting and skipping duplicates (wrong – breaks subarray property).
- ✅ Subarrays must preserve original order and be contiguous.

---

## ✅ Learnings:

- Sliding window is powerful for problems with subarrays + constraints like uniqueness.
- Avoid altering the array (like sorting) when working with subarrays.

---

## 🔗 Useful Links:

- [Problem Link](https://leetcode.com/problems/maximum-erasure-value/)
- [Python Solution File](./question1.py)

