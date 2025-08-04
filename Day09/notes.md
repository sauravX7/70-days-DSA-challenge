# 📝 Day 09 - Notes

## 🔍 Problem:
**LeetCode 1 – Two Sum**

> Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

---

## ✅ Approach Used:
**Hash Map Lookup (One-pass)**

- Use a dictionary `hmap` to store `number → index` pairs while iterating.
- For each element `n` at index `i`, compute `diff = target - n`.
- If `diff` exists in the hash map → return the pair of indices: `(hmap[diff], i)`.
- Else, store the current number in the map.

---

## 💡 Key Concepts:

- Hash maps allow constant-time lookup for complements.
- Only one pass through the list is needed to find the pair.

---

## 📦 Complexity:

- **Time:** `O(n)` – one pass through the array.
- **Space:** `O(n)` – for storing elements in the hash map.

---

## ⚠️ Mistakes to Avoid:

- ❌ Using a nested loop (brute-force `O(n^2)` approach).
- ❌ Returning the number values instead of their indices.
- ✅ Store elements as you go, not after the full pass.

---

## ✅ Learnings:

- This is a classic hash map pattern: **check before insert**.
- Hashing is a powerful optimization for lookup-based problems.

---

## 🔗 Python Solution File:

- [Day09/question.py](./question.py)
