# 📝 Day 03 - Notes

## 🔍 Problem:
**LeetCode (Custom) – Check Word Validity**

> Given a string `word`, return `True` if:
- The word has **at least 3 characters**
- It contains **at least one vowel**
- It contains **at least one consonant**
- All characters must be **letters or digits** (no symbols)

Return `False` otherwise.

---

## ✅ Approach Used:
**Character Scanning with Flags**

- Traverse each character and track if there's at least:
  - One vowel
  - One consonant
- If any invalid (non-alphanumeric) character is found, return `False`.
- Ensure length is ≥ 3.

---

## 💡 Key Concepts:

- `isalpha()` and `isdigit()` help validate allowed characters.
- Vowels are checked using `c.lower() in 'aeiou'`.
- Flags `v` and `co` keep track of vowel and consonant presence.

---

## 📦 Complexity:

- **Time:** `O(n)` – scan each character once.
- **Space:** `O(1)` – only uses a few variables.

---

## ⚠️ Mistakes to Avoid:

- ❌ Forgetting to check word length first.
- ❌ Not handling symbols or special characters properly.
- ✅ Check both vowel and consonant presence, not just one.

---

## ✅ Learnings:

- Use boolean flags for condition tracking in linear scans.
- `isalpha()` and `isdigit()` are very useful for such string validations.

---

## 🔗 Python Solution File:

- [Day03/question3.py](./question3.py)
