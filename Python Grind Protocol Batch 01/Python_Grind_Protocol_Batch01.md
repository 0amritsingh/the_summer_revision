# 🔥 Python Grind Protocol — Batch 01

> **Topics Covered:** Print · Comments & Escape Sequences · Variables & Data Types · Arithmetic Operators · Data Typecasting · Input Function · Strings · Slicing of Strings · String Methods · If-Else Conditional Statements

> **Rules:** No loops, no lists, no tuples, no dicts, no functions, no fancy modules — stick to the topics above only.

---

## Progress Tracker

| Level | Total | Done |
|-------|-------|------|
| 🟢 Easy | 10 | ☐☐☐☐☐☐☐☐☐☐ |
| 🟡 Intermediate | 10 | ☐☐☐☐☐☐☐☐☐☐ |
| 🔴 Hard | 10 | ☐☐☐☐☐☐☐☐☐☐ |
| 💀 Impossible | 10 | ☐☐☐☐☐☐☐☐☐☐ |
| 🚀 Projects | 2 | ☐☐ |
| **Total** | **42** | |

---

## 🟢 Easy (10 Questions)

### Q1 — Print · Code
Write a Python statement to print your full name and age on the same line, separated by a comma.

> 💡 **Hint:** Use `print()` with multiple arguments or string concatenation.

---

### Q2 — Escape Sequences · MCQ
**What does `\n` do inside a string?**

- A) Adds a tab space
- B) Adds a new line
- C) Escapes the next character
- D) Prints the letter n

> 💡 **Hint:** Answer: B — it moves output to a new line.

---

### Q3 — Variables · Code
Create two variables: one storing your city name, one storing the year you were born. Print both in one sentence.

> 💡 **Hint:** Variables are assigned with `=`. You may need `str()` for the year.

---

### Q4 — Data Types · MCQ
**What is the data type of the value `3.14` in Python?**

- A) int
- B) str
- C) float
- D) bool

> 💡 **Hint:** Answer: C — numbers with decimals are float.

---

### Q5 — Arithmetic Operators · Code
You have ₹500. A pen costs ₹12 and a notebook costs ₹45. Write code to calculate how many complete sets (pen + notebook) you can buy.

> 💡 **Hint:** Use `//` for integer division after computing cost per set.

---

### Q6 — Input Function · Code
Ask the user to enter their name. Then print: `Hello [name], welcome to Python!`

> 💡 **Hint:** `input()` always returns a string. f-strings or `+` can help format output.

---

### Q7 — Strings · Code
Store the string `'Python is awesome'` and print its length. Also print only the word `'awesome'`.

> 💡 **Hint:** `len()` gives length. Slicing or `.split()` can isolate a word.

---

### Q8 — Typecasting · MCQ
**What will `int('7') + int('3')` return?**

- A) `'73'`
- B) `10`
- C) `73`
- D) Error

> 💡 **Hint:** Answer: B — both strings are cast to int, then added numerically.

---

### Q9 — If-Else · Code
Ask the user to input a number. If it's positive, print `'Positive'`. If negative, print `'Negative'`. If zero, print `'Zero'`.

> 💡 **Hint:** Use `if / elif / else`. Remember to convert input to `int` or `float`.

---

### Q10 — String Methods · Code
Take the string `'  hello world  '`. Strip the spaces, capitalize only the first letter, and print the result.

> 💡 **Hint:** `.strip()` removes whitespace. `.capitalize()` does the rest.

---

## 🟡 Intermediate (10 Questions)

### Q11 — Escape Sequences · Code
Print the following exactly (with quotes and newline):
```
He said, "Python is fun!"
She replied, "I agree!"
```

> 💡 **Hint:** Use `\"` to escape quotes inside a string, or switch to single quotes outside.

---

### Q12 — Variables · MCQ
**What will Python print?**
```python
x = 10
x = x + 5
x *= 2
print(x)
```
- A) 10
- B) 20
- C) 30
- D) 25

> 💡 **Hint:** Answer: C — `10 + 5 = 15`, then `15 * 2 = 30`.

---

### Q13 — Typecasting · Code
The user enters `'7.9'` as input. You need to print it as an integer. What happens if you directly do `int(input())`? Fix this properly.

> 💡 **Hint:** You can't directly cast a float-string to int. Try `int(float(...))`.

---

### Q14 — Slicing · Code
Given `s = 'Meerut, UP, India'` — extract only `'UP'` using slicing (no methods allowed).

> 💡 **Hint:** Find the index of U using `s.index()` or count manually. Then slice `s[start:end]`.

---

### Q15 — String Methods · Code
Take a user input sentence. Count how many times the letter `'a'` (lowercase) appears. Also print the sentence in UPPER case.

> 💡 **Hint:** `.count('a')` and `.upper()` are your friends here.

---

### Q16 — If-Else · MCQ
**What gets printed?**
```python
x = 15
if x > 10:
    if x > 20:
        print('A')
    else:
        print('B')
else:
    print('C')
```
- A) A
- B) B
- C) C
- D) Nothing

> 💡 **Hint:** Answer: B — outer `if` is True, inner `if` is False → `else` runs.

---

### Q17 — Arithmetic + Typecasting · Code
Ask the user for two numbers as input. Print their sum, difference, product, quotient, and remainder — each on a new line with a label.

> 💡 **Hint:** `input()` gives strings — cast to `float`. Use `\n` or separate `print()` calls.

---

### Q18 — Strings + Slicing · Code
Given `name = 'Abdul Kalam'` — print the initials `A.K.` using slicing only. No `split()` allowed.

> 💡 **Hint:** Find where the space is. Take `name[0]` and `name[space_index+1]` with indexing.

---

### Q19 — If-Else + Input · Code
Build a simple login system: hardcode `username='admin'` and `password='1234'`. Ask the user for both. Print `'Access granted'` or `'Wrong credentials'`.

> 💡 **Hint:** Use `and` operator in your condition. Both must match.

---

### Q20 — Slicing · MCQ
**What does `'Python'[::-1]` return?**

- A) `'nohtyP'`
- B) `'Python'`
- C) `'P'`
- D) Error

> 💡 **Hint:** Answer: A — step of `-1` reverses the string.

---

## 🔴 Hard (10 Questions)

### Q21 — Strings + Arithmetic · Code
Without using `len()` or any method, write code that counts the number of characters in a string using a different trick.

> 💡 **Hint:** Think about how `%` formatting works with strings, or try indexing at position `i` until `IndexError`, or use `enumerate()` alternative with creative use of slicing.

---

### Q22 — Typecasting · MCQ
**What is the output?**
```python
x = bool(0)
y = bool('')
z = bool(' ')
print(x, y, z)
```
- A) False False False
- B) False False True
- C) True False True
- D) False True True

> 💡 **Hint:** Answer: B — `0` is False, empty string is False, a space `' '` is non-empty → True.

---

### Q23 — If-Else + Strings · Code
A username is 'valid' only if: it's between 5–15 characters, starts with a letter, and contains no spaces. Validate a hardcoded username and print the exact reason if invalid.

> 💡 **Hint:** Use `len()`, `s[0].isalpha()`, and `' ' in s` for checks. Chain `if-elif`.

---

### Q24 — Slicing + String Methods · Code
Given `email = 'user.name@gmail.com'` — extract just the domain name (`gmail`) using slicing. No `split()`, no `find()`. Only indexing tricks.

> 💡 **Hint:** Use `.index('@')` and `.index('.com')` to get positions, then slice between them.

---

### Q25 — Arithmetic + Data Types · MCQ
**What is the output?**
```python
print(type(3 / 2))
print(type(3 // 2))
```
- A) float, float
- B) int, int
- C) float, int
- D) int, float

> 💡 **Hint:** Answer: C — `/` always returns float, `//` returns int when both operands are int.

---

### Q26 — Print + Escape Sequences · Code
Print a formatted receipt using a **single `print()` call**:
```
---- BILL ----
Item    Price
Tea     ₹20
Samosa  ₹15
Total   ₹35
--------------
```

> 💡 **Hint:** Use `\t` for tab, `\n` for newline, all inside one `print("...")`.

---

### Q27 — String Methods + If-Else · Code
Ask the user for a sentence. Check if it's a palindrome (ignoring case and spaces). Print `True` or `False`.

> 💡 **Hint:** Use `.replace(' ','')` and `.lower()`. Then compare string with its reverse `[::-1]`.

---

### Q28 — Variables + Typecasting · MCQ
**What is the output?**
```python
a = '5'
b = 3
print(a * b)
```
- A) `15`
- B) `'15'`
- C) `'555'`
- D) Error

> 💡 **Hint:** Answer: C — multiplying a string by int **repeats** it, not arithmetic multiply.

---

### Q29 — Input + Typecasting + Arithmetic · Code
Ask the user for a temperature in Celsius. Convert it to **Fahrenheit AND Kelvin**. Display results rounded to 2 decimal places.

> 💡 **Hint:** `F = (C * 9/5) + 32`. `K = C + 273.15`. Use `round()` or f-string with `:.2f`.

---

### Q30 — Slicing · Code
Given `s = '0123456789'` — using **only slicing**, print:
1. Every even-indexed character
2. Every odd-indexed character
3. The string in reverse

> 💡 **Hint:** `s[::2]` for even, `s[1::2]` for odd, `s[::-1]` for reverse.

---

## 💀 Impossible (10 Questions)

### Q31 — All Topics · Code
Without using any loop, list, or function — write code that takes a user's full name as input and prints it in `'Last, First'` format. Handle extra spaces anywhere in the input.

> 💡 **Hint:** Use `.strip()`, then `.index(' ')` and slicing to separate first and last name.

---

### Q32 — All Topics · MCQ
**What is the final value of `x`?**
```python
x = '100'
x = int(x) + int(bool(x)) + len(x)
```
- A) 104
- B) 103
- C) 101
- D) 100

> 💡 **Hint:** Answer: A — `int('100')=100`, `bool('100')=True=1`, `len('100')=3` → `104`.

---

### Q33 — Strings + If-Else · Code
Ask the user for a sentence. Print it back but with every word's first letter capitalized — **without using `.title()` or `.capitalize()`**. Only slicing and string methods allowed.

> 💡 **Hint:** `.title()` is banned. Think `.upper()` on first char + `[1:]` per word — but no loops! Can you chain `.replace()` creatively? Or use `.split()` + string tricks?

---

### Q34 — Arithmetic + If-Else · Code
A shopkeeper gives **10% discount** if total > ₹500, else **5% discount**. Tax is always **18%** on the discounted price. Ask for the original price, compute and print the final price.

> 💡 **Hint:** `discount = price * 0.10 if price > 500 else price * 0.05`. Apply tax after discount.

---

### Q35 — Escape + Print · MCQ
**What exactly does this print?**
```python
print('It\'s a \"test\"')
```
- A) `It's a "test"`
- B) `It\'s a \"test\"`
- C) Syntax Error
- D) `It's a test`

> 💡 **Hint:** Answer: A — `\'` becomes `'` and `\"` becomes `"`. The backslashes are escape characters, not printed.

---

### Q36 — All Topics · Code
Build a **'secret message encoder'**: take a string from the user, replace every vowel (a, e, i, o, u — both upper and lower case) with `'*'`. Print the result. Use only string methods — no loops, no lists.

> 💡 **Hint:** Chain `.replace('a','*').replace('e','*')...` for all 10 vowel variants.

---

### Q37 — If-Else + Arithmetic · Code
Compute **compound interest**: `A = P * (1 + r/n)^(nt)`. Ask the user for principal, rate (%), time in years, and compounding frequency. Print the final amount. **No `math` module.**

> 💡 **Hint:** Python has `**` for exponentiation. Convert rate from % by dividing by 100.

---

### Q38 — Slicing · MCQ
**`s = 'abcdefgh'`. What does `s[2:7:2]` return?**

- A) `'ceg'`
- B) `'cdf'`
- C) `'bdf'`
- D) `'ace'`

> 💡 **Hint:** Answer: A — start at index 2 (c), go to 7 (exclusive), step 2: c(2), e(4), g(6).

---

### Q39 — All Topics · Code
Ask the user for their date of birth as `'DD-MM-YYYY'`. Extract day, month, and year **using slicing only** (no `split()`). Then print a message like:
`'You were born in 2005 on the 15th of March'`

> 💡 **Hint:** `s[0:2]` for day, `s[3:5]` for month, `s[6:10]` for year. Use `if-elif` for month names (no imports).

---

### Q40 — String Methods + If-Else · Code
Ask the user for a password. It's **strong** only if:
- Length ≥ 8
- Has at least one digit
- Has at least one uppercase letter

Print **which specific condition(s) failed**.

> 💡 **Hint:** Use `len()` for length. For uppercase: `s != s.lower()` checks if any uppercase exists. For digit: `s != s.replace('0','').replace('1','')...` — chain all digit replacements and compare.

---

## 🚀 Projects (2)

### PROJECT 1 — Easy 🛒 Smart Receipt Generator

Build an **interactive bill calculator**. Ask the user for:
- Their name
- 3 item names and their prices

Then print a formatted receipt with:
- Header with shop name and customer name
- Each item with its price
- Subtotal
- 10% tax
- Grand total (rounded to 2 decimal places)
- A thank-you message

**Topics to use:** `print`, `input`, variables, arithmetic, typecasting, f-strings/string formatting, if-else for tax bracket

> 💡 **Hint:** Plan: collect inputs → compute → print formatted output. Use `\t` for alignment. No loops needed.

**Sample Output:**
```
===========================
       PYTHON STORE
  Customer: Rahul Sharma
===========================
Tea             ₹20.00
Samosa          ₹15.00
Water           ₹10.00
---------------------------
Subtotal:       ₹45.00
Tax (10%):      ₹4.50
---------------------------
GRAND TOTAL:    ₹49.50
===========================
Thank you, Rahul! Come again!
```

---

### PROJECT 2 — Hard 🔐 Text-Based Login + Profile System

Build a **multi-step CLI app** using only the allowed topics:

**Step 1 — Registration:**
- Ask: username, password, age, city
- Validate: username ≥ 4 chars with no spaces; password ≥ 6 chars; age must be numeric
- If invalid, print the specific error and exit

**Step 2 — Login:**
- Ask username + password again
- Check against stored values from Step 1

**Step 3 — Profile Display:**
- On success, display a formatted profile card:
```
╔══════════════════╗
║   USER PROFILE   ║
╠══════════════════╣
║ Name: ...        ║
║ Age : ...        ║
║ City: ...        ║
╚══════════════════╝
```
- Show if user is a **minor** (age < 18) or **adult**
- Show city in UPPERCASE

**Only use:** `print`, `input`, variables, `if-elif-else`, string methods, slicing, typecasting, arithmetic, escape sequences.

> 💡 **Hint:** No loops means one shot at login. Use nested if-else for validation. String formatting with `\n` and spacing for the profile card.

---

## 📋 Quick Reference Sheet

### Escape Sequences
| Sequence | Meaning |
|----------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

### Data Types
| Type | Example | `type()` output |
|------|---------|----------------|
| int | `10` | `<class 'int'>` |
| float | `3.14` | `<class 'float'>` |
| str | `'hello'` | `<class 'str'>` |
| bool | `True` | `<class 'bool'>` |

### Typecasting
| Function | Converts to |
|----------|------------|
| `int()` | Integer |
| `float()` | Float |
| `str()` | String |
| `bool()` | Boolean |

### Slicing Syntax
```python
s[start:stop:step]
s[::-1]      # Reverse
s[::2]       # Every 2nd char
s[2:5]       # Index 2,3,4
```

### Key String Methods
| Method | What it does |
|--------|-------------|
| `.upper()` | ALL CAPS |
| `.lower()` | all lowercase |
| `.strip()` | Remove whitespace |
| `.replace(a,b)` | Replace a with b |
| `.count(x)` | Count occurrences of x |
| `.index(x)` | Find index of x |
| `.isalpha()` | Check if all letters |
| `.isdigit()` | Check if all digits |

---

*Python Grind Protocol — Batch 01 | Topics: Print to If-Else | 42 Questions*
