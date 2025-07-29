# 📝 Day 08 - Notes

## 🔍 Problem:
**LeetCode 2529 – Maximum Count of Positive Integer and Negative Integer**

> Given a sorted integer array `nums`, return the maximum count between the number of positive integers and the number of negative integers.

---

## ✅ Approach Used:
**Binary Search (Twice)**

- Perform binary search to count:
  1. **Negative numbers** – find the last index of a number `< 0`
  2. **Positive numbers** – find the first index of a number `> 0`
- Return the maximum of both counts.

---

## 🔁 Steps:

1. **Count Negatives**  
   - Find first index where `nums[m] >= 0`
   - The index (`l`) is the count of negative numbers.

2. **Count Positives**  
   - Find first index where `nums[m] > 0`
   - `len(nums) - l` gives the count of positives.

---

## 🧠 Key Concepts:

- Use of **binary search** to count specific types of elements in `O(log n)` time.
- Since the array is sorted, binary search is ideal for locating transitions (like `0 to 1`, `-1 to 0`, etc.)

---

## 📦 Complexity:

- **Time:** `O(log n)`  
  - Two binary searches.
- **Space:** `O(1)` – no extra space used.

---

## ✅ Learnings:

- Efficient counting using **binary search patterns**.
- Useful trick: In sorted arrays, count range of values without linear scan.

---

## 🔗 Python Solution File:

- [Day08/question.py](./question.py)
