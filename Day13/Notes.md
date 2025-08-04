# 📝 Day 13 - Notes

## 🔍 Problem:
**LeetCode 2109 – Adding Spaces to a String**

> You are given a string `s` and a list of integers `spaces`, where each integer represents a position in `s` where a space should be inserted.  
> Return the final string after inserting spaces at the specified positions.

---

## ✅ Approach Used:
**String Slicing + Join**

- Use a pointer `p` to track the start of the next segment.
- Loop through the `spaces` list:
  - Slice the string from `p` to the current index `i`, append to result.
  - Append a space `" "` after each segment.
  - Move the pointer `p` to `i`.
- After the loop, add the remaining string from `p:` to the result.
- Join all parts with `"".join()` to construct the final result efficiently.

---

## 💡 Key Concepts:

- Slicing (`s[start:end]`) gives clean and efficient segment extraction.
- `"".join(list)` is preferred over repeated string concatenation in Python.
- This approach ensures **linear time complexity** even with many insertions.

---

## 📦 Complexity:

- **Time:** `O(n + k)`  
  - `n` = length of `s`,  
  - `k` = number of spaces.
- **Space:** `O(n + k)` – for building the result list.

---

## ⚠️ Mistakes to Avoid:

- ❌ Inserting spaces after the wrong index.
- ❌ Using string concatenation in a loop (`+=`) which is inefficient.
- ✅ Always update the pointer after each slice, and join at the end.

---

## ✅ Learnings:

- Efficient string manipulation is often about balancing clarity and performance.
- Precomputing and slicing is more readable than tracking indexes mid-loop.

---

## 🔗 Python Solution File:

- [Day13/question.py](./question.py)
