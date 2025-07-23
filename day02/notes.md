# 📝 Day 02 - Notes

## 🔍 Problem:
**LeetCode (Custom) – Maximum Gain by Removing Substrings**

> Given a string `s` and two integers `x` and `y`, representing the gain for removing the substrings `"ab"` and `"ba"` respectively:
- Remove substrings greedily to maximize the total gain.
- Return the maximum gain possible.

---

## ✅ Approach Used:
**Greedy + Stack-based Substring Removal**

- First remove the higher-value pair (either `"ab"` or `"ba"`) greedily using a **stack**.
- Then remove the remaining lower-value pair from the leftover string.
- This ensures **maximum score** since higher-value substrings are prioritized.

---

## 💡 Key Concepts:

- Use `stack` to simulate removing adjacent characters when a valid pair is found.
- Modify the string `s` after each pass to avoid re-checking already removed characters.
- Run the stack-pass twice:
  - Once for the higher-scoring pair
  - Once for the lower-scoring one on the updated string

---

## 📦 Complexity:

- **Time:** `O(n)` – one or two passes over the string with stack operations.
- **Space:** `O(n)` – for the stack.

---

## ⚠️ Mistakes to Avoid:

- ❌ Removing substrings in arbitrary order: can lead to suboptimal total gain.
- ✅ Always prioritize the higher-value substring first.

---

## ✅ Learnings:

- Greedy + Stack is an effective combo for **substring removal** problems.
- Problem decomposition (two-phase removal) helps optimize greedy solutions.

---

## 🔗 Python Solution File:

- [Day02/question2.py](./question2.py)

