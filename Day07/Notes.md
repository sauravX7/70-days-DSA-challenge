# 📝 Day 07 - Notes

## 🔍 Problem:
**LeetCode 2109 – Adding Spaces to a String**

> You are given a string `s` and a list of integers `spaces` indicating the indices where you need to insert a single space.

Return the modified string after inserting spaces.

---

## ✅ Approach Used:
**Two-pointer style slicing + Join**

- Initialize a result list `r` and a pointer `p = 0`.
- For every index `i` in `spaces`:
  - Append the substring `s[p:i]`.
  - Append a space `" "`.
  - Update the pointer `p = i`.
- After the loop, append the remaining string `s[p:]`.
- Finally, join all parts in `r` to form the final result.

---

## 💡 Key Concepts:

- String slicing is efficient in Python.
- `List[str]` is preferred over direct concatenation due to Python string immutability.
- `str.join()` is faster than repeated `+`.

---

## 📦 Complexity:

- **Time:** `O(n + k)`  
  - `n` = length of string,  
  - `k` = number of spaces.
- **Space:** `O(n + k)` – for storing the result.

---

## ⚠️ Mistakes to Avoid:

- ❌ Don’t insert space *after* the index — it should be *at* the index.
- ✅ Ensure no extra spaces are added at the end unless needed.

---

## ✅ Learnings:

- This type of problem builds skill in **pointer manipulation**, **string slicing**, and **efficient string construction**.
- Shows how simple operations can be optimized for larger input sizes.

---

## 🔗 Python Solution File:

- [Day07/question.py](./question.py)
