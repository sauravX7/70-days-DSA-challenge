# 📝 Day 15 - Notes

## 🔍 Problem:
**LeetCode 2594 – Minimum Time to Repair Cars**

> You are given an integer `cars` representing the number of cars that need to be repaired and an array `ranks` representing mechanics, where the time it takes a mechanic with rank `r` to repair `n` cars is `r * n^2`.

Find the **minimum time** needed to repair all cars using any number of available mechanics.

---

## ✅ Approach Used:
**Binary Search on Time**

- Use binary search to find the **minimum possible time** in which all cars can be repaired.
- For a given time, simulate how many cars each mechanic can repair:
  - A mechanic with rank `r` can repair at most `floor(√(time / r))` cars.
- If the total number of cars repaired within `mid` time ≥ `cars`, move search left.
- Otherwise, move it right.

---

## 💡 Key Concepts:

- **Binary Search on Answer**:
  - Works well when the function is **monotonic** (time ↑ → cars repaired ↑).
- Pre-calculate `right = min(ranks) * cars^2` as the upper time bound.
- Helper function `can_repair_all(time)` checks feasibility.

---

## 📦 Complexity:

- **Time:** `O(n log(maxTime))`  
  - `n` = number of mechanics  
  - `maxTime` = `min(ranks) * cars^2`
- **Space:** `O(1)` – constant extra space

---

## ⚠️ Mistakes to Avoid:

- ❌ Not using binary search — brute-force will timeout.
- ✅ Always use floor (`int`) when calculating cars per mechanic.

---

## ✅ Learnings:

- A great example of applying **binary search on the answer range**.
- Useful technique when the solution space is large but **searchable** via monotonic functions.

---

## 🔗 Python Solution File:

- [Day15/question.py](./question.py)
