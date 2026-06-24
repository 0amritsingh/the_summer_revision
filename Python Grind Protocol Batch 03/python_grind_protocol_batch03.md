    # 🔁 Python Grind Protocol — Batch 03

**Topics:** For Loops · While Loops · Loops over all data types · Classic Loop Problems · Functions · Recursion · Lambda · Map · Filter · Local & Global · `is` vs `==`
**Builds on:** Batch 01 (strings, if-else, typecasting) + Batch 02 (list, dict, set, tuple, comprehension)
**Format:** 10 Easy · 10 Intermediate · 10 Hard · 10 Impossible — No MCQ · No Projects

---

## 📋 Questions

---

### 🟢 Easy (10)

**#1 — For Loop · Classic**
Write a for loop that prints numbers 1 to 20, but skips all multiples of 3.

---

**#2 — While Loop · Classic**
Write a while loop that keeps asking the user to enter a positive number. The loop only stops when the user enters a negative number. Print the sum of all entered numbers at the end.

---

**#3 — For Loop · String**
Take a string from the user. Using a for loop, print each character on a new line along with its index number.

---

**#4 — For Loop · List**
Given a list of mixed values: `[4, 'hello', 7.5, True, 'world', 9]` — loop through it and print only the items that are of type `int`.

---

**#5 — Function · Basics**
Write a function `greet(name, city)` that returns the string `'Hello [name] from [city]!'`. Call it 3 times with different arguments and print each result.

---

**#6 — For Loop · Dict**
Create a dict of 5 countries and their populations. Loop through it and print each country and population in a formatted sentence.

---

**#7 — Lambda · Basics**
Write a lambda function that takes a number and returns its cube. Store it in a variable and call it with 5 different numbers.

---

**#8 — Function · Return**
Write a function `is_even(n)` that returns `True` if n is even and `False` if odd. Then loop through a list `[1,2,3,4,5,6,7,8,9,10]` and use the function to print only even numbers.

---

**#9 — For Loop · Tuple + Set**
Create a tuple of 6 numbers (with some duplicates). Loop through the tuple and build a set of only unique numbers seen so far. Print the set after the loop.

---

**#10 — `is` vs `==` · Classic**
Create two variables: `a = [1,2,3]` and `b = [1,2,3]` and `c = a`. Now check: `a == b`, `a is b`, `a is c` — print all three results and write a comment explaining why each is True or False.

---

### 🟡 Intermediate (10)

**#11 — For Loop · Classic Problem · Mathematical**
Without using `sum()` or any built-in — write a function `total(lst)` that manually computes the sum of all numbers in a list using a for loop. Test it with `[10, 20, 30, 40, 50]`.

---

**#12 — While Loop · Classic Problem**
Write a program that reverses a number without converting it to a string. Only use while loop and arithmetic operators (`%`, `//`).
Example: `1234` → `4321`

---

**#13 — Function · Local & Global**
Create a global variable `count = 0`. Write a function `increment()` that increases count by 1 each time it's called using the `global` keyword. Call it 5 times and print count after each call.

---

**#14 — Map · Classic**
You have a list of temperatures in Celsius: `[0, 20, 37, 100, -10]`. Use `map()` with a lambda to convert all of them to Fahrenheit. Print the result as a list.

---

**#15 — Filter · Classic**
Given a list of words: `['apple', 'ant', 'banana', 'avocado', 'cherry', 'apricot']` — use `filter()` with a lambda to keep only words that start with the letter `'a'`. Print the result as a list.

---

**#16 — For Loop · Nested · Classic Problem**
Write a program to print the multiplication table of numbers 1 to 5 using nested for loops.

---

**#17 — Recursion · Classic**
Write a recursive function `factorial(n)` that returns the factorial of n. Test it for n = 0, 1, 5, 10.

---

**#18 — For Loop · String · Batch 01**
Write a function `count_vowels(s)` that counts and returns the number of vowels in a string using a for loop. Test with at least 3 different strings.

---

**#19 — `is` vs `==` · Strings · Interview**
Run and explain the output of:
```python
x = "hello"
y = "hello"
z = "".join(["h","e","l","l","o"])
print(x == y, x is y)
print(x == z, x is z)
```
Write comments explaining string interning and why `is` can be unpredictable.

---

**#20 — Function · Batch 02 · Dict**
Write a function `word_frequency(sentence)` that takes a string and returns a dictionary of each word and how many times it appears. Test with `'the cat sat on the mat the cat'`.

---

### 🔴 Hard (10)

**#21 — Recursion · Classic · Mathematical**
Write a recursive function `fibonacci(n)` that returns the nth Fibonacci number. Then use a for loop to print the first 10 Fibonacci numbers.

---

**#22 — While Loop · Classic Problem · Mathematical**
Write a program to check if a number is a palindrome using only a while loop and arithmetic (no string conversion, no slicing). Example: `121` → True, `123` → False.

---

**#23 — Map + Filter + Lambda · Chained**
Given a list of numbers `[1,2,3,4,5,6,7,8,9,10]` — in a single line, filter out odd numbers, then square all remaining even numbers using `map()` and `filter()` chained together.

---

**#24 — Function · Local & Global · Interview**
What is the output of this code and why? Write a full explanation as comments:
```python
x = 10
def foo():
    x = 20
    print(x)
foo()
print(x)
```
Then modify it so that `foo()` actually changes the global `x` to 20.

---

**#25 — For Loop · Classic Problem · Mathematical**
Write a function `is_prime(n)` that checks if a number is prime using a for loop. Then use it to print all prime numbers between 1 and 50.

---

**#26 — Recursion · Sum · Mathematical**
Write a recursive function `digit_sum(n)` that returns the sum of digits of a number. Example: `digit_sum(1234)` → `10`. Test with at least 4 numbers.

---

**#27 — For Loop · Batch 02 · Dict + List**
Write a function `group_by_length(words)` that takes a list of words and returns a dictionary where keys are word lengths and values are lists of words with that length.
Test with `['hi','bye','cat','to','dog','hello','he']`.

---

**#28 — Lambda + Map · Batch 02**
You have a list of student dicts:
```python
[{'name':'Ali','marks':88}, {'name':'Sara','marks':72}, {'name':'Raj','marks':95}]
```
Use `map()` with a lambda to create a new list of strings like `'Ali: 88/100'` for each student.

---

**#29 — While Loop · Classic Problem · Interview**
Write a program that finds the GCD (Greatest Common Divisor) of two numbers using the Euclidean algorithm with a while loop. No imports allowed.

---

**#30 — Function + Recursion · Batch 01**
Write a recursive function `reverse_string(s)` that reverses a string without using slicing or any built-in reverse method. Test with at least 3 strings.

---

### 💀 Impossible (10)

**#31 — Recursion · Mathematical · Interview**
Write a recursive function `power(base, exp)` that computes `base ** exp` without using the `**` operator or `pow()`. Then extend it to handle negative exponents too.

---

**#32 — For Loop · Classic Problem · Mathematical**
Write a function `flatten(nested)` that takes a list which may contain lists inside it (one level deep only) and returns a single flat list — using only a for loop and `isinstance()`. No imports.
Example: `[1, [2,3], 4, [5,6]]` → `[1,2,3,4,5,6]`

---

**#33 — Lambda + Filter + Map · Chained · Batch 02**
Given a sentence string — in a single expression using `map()`, `filter()`, and `lambda` only — produce a list of lengths of words that have more than 3 characters. No for loop, no list comprehension.

---

**#34 — Function · Local & Global · Interview · Tricky**
What is the output and why? Explain every line:
```python
x = 5
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 1
    inner()
    print(x)
outer()
print(x)
```

---

**#35 — While Loop · Recursion · Mathematical**
Write both a while loop version AND a recursive version of a program that counts the number of digits in a number. Then compare the two approaches in comments — which is more readable and why.

---

**#36 — For Loop · `is` vs `==` · Interview**
Explain and demonstrate with code why this is dangerous in production:
```python
a = 256
b = 256
print(a is b)  # True

a = 257
b = 257
print(a is b)  # False (maybe)
```
Write an explanation of Python integer caching (-5 to 256) as comments in your code.

---

**#37 — Function + Map + Filter · Batch 01 + 02**
Write a function `process(data)` that takes a list of strings, filters out strings shorter than 4 characters, converts remaining ones to uppercase, and returns a list of their lengths — all using `map()` and `filter()` inside the function body. No loops, no comprehension inside the function.

---

**#38 — Recursion · Classic · Mathematical · Interview**
Write a recursive function `sum_of_list(lst)` that returns the sum of all elements in a list without using `sum()`, loops, or any built-in aggregate function.
Then trace through the call stack manually for `[1,2,3,4]` in comments.

---

**#39 — For Loop + Function · Classic Problem · Mathematical**
Write a function `is_perfect(n)` that checks if a number is a perfect number (sum of its proper divisors equals itself). Example: `28` → divisors are `1,2,4,7,14` → sum = `28` → Perfect. Print all perfect numbers between 1 and 1000.

---

**#40 — All Topics · Interview · Boss Level**
Without using any built-in sort function — write a function `bubble_sort(lst)` that sorts a list in ascending order using bubble sort (nested while loops or for loops). Then:
- Use a lambda to reverse the sorted result
- Use `filter()` to keep only even numbers from the sorted list
- Use `map()` to square all those even numbers
Print every intermediate step.

---

## 💡 Hints

**#1** — Use `if i % 3 == 0: continue` inside the for loop to skip multiples of 3.

**#2** — Initialize `total = 0` before the loop. Condition: `while True`, break when input < 0.

**#3** — Use `enumerate(string)` to get both index and character together in the loop.

**#4** — Use `type(item) == int` inside the loop. Note: `True` is also technically int — think about that.

**#5** — `def greet(name, city): return f'Hello {name} from {city}!'` — then call 3 times.

**#6** — Use `for country, population in d.items():` to unpack key-value pairs directly.

**#7** — `cube = lambda x: x**3` — then call `cube(2)`, `cube(3)` etc.

**#8** — Define the function first, then loop through the list and call `is_even(x)` inside the if condition.

**#9** — Start with `seen = set()`. Inside loop: `seen.add(num)`. Print after loop ends.

**#10** — `==` checks value equality. `is` checks if both point to the same object in memory. `c = a` makes c point to the same object, not a copy.

**#11** — `total = 0`, then `for x in lst: total += x`. Return total.

**#12** — Extract last digit with `n % 10`. Build reversed number with `reversed = reversed * 10 + digit`. Remove last digit with `n //= 10`.

**#13** — Write `global count` as the first line inside the function. Without it, Python treats count as a local variable and throws an error.

**#14** — Formula: `F = (C * 9/5) + 32`. Use `list(map(lambda c: ..., temps))`.

**#15** — `list(filter(lambda w: w.startswith('a'), words))`.

**#16** — Outer loop `for i in range(1,6)`, inner loop `for j in range(1,11)`. Print `i * j`.

**#17** — Base case: `if n <= 1: return n`. Recursive case: `return n * factorial(n-1)`.

**#18** — `count = 0`. Loop through string: `if char.lower() in 'aeiou': count += 1`. Return count.

**#19** — Python interns (reuses) short strings automatically. Dynamically built strings may not be interned. `==` is always safe for value comparison. Never use `is` to compare string values.

**#20** — Start with empty dict. Loop through `sentence.split()`. Use `d[word] = d.get(word, 0) + 1`.

**#21** — Base cases: `fib(0) = 0`, `fib(1) = 1`. Recursive: `return fib(n-1) + fib(n-2)`. Then loop `for i in range(10): print(fibonacci(i))`.

**#22** — Store original number. Reverse it using `%` and `//` in a while loop. Compare reversed with original.

**#23** — `list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))` — filter first, then map.

**#24** — Without `global`, the `x` inside `foo` is a completely separate local variable. Add `global x` inside the function to modify the outer one.

**#25** — For each n, check divisibility from 2 to `n-1`. If any number divides n evenly, it's not prime. Edge case: 1 is not prime.

**#26** — Base case: `if n < 10: return n`. Recursive: `return n%10 + digit_sum(n//10)`.

**#27** — Start with empty dict. For each word: `d[len(word)] = d.get(len(word), []) + [word]`.

**#28** — `list(map(lambda s: f"{s['name']}: {s['marks']}/100", students))`.

**#29** — Euclidean algorithm: while `b != 0`, do `a, b = b, a % b`. GCD is `a` when loop ends.

**#30** — Base case: `if s == '': return ''`. Recursive: `return reverse_string(s[1:]) + s[0]`.

**#31** — Base case: `if exp == 0: return 1`. Recursive: `return base * power(base, exp-1)`. For negative: `return 1 / power(base, -exp)`.

**#32** — Loop through outer list. Use `isinstance(item, list)` to check if item is a list. If yes, loop through inner list and append each. If no, append directly.

**#33** — `list(map(lambda w: len(w), filter(lambda w: len(w) > 3, sentence.split())))`.

**#34** — `nonlocal` lets inner function access and modify the variable from the enclosing (outer) function's scope — not global. Global `x=5` is untouched. `outer`'s `x` starts at 10, becomes 11 after `inner()` runs.

**#35** — While version: `count=0`, divide by 10 each iteration until n=0. Recursive: base case `n<10 return 1`, else `return 1 + count_digits(n//10)`.

**#36** — Python caches small integers from -5 to 256 for memory efficiency. Numbers outside this range create new objects each time. This is why `is` must never be used to compare values.

**#37** — Chain them: `list(map(lambda s: len(s), filter(lambda s: len(s) >= 4, map(lambda s: s.upper(), data))))`.

**#38** — Base case: `if lst == []: return 0`. Recursive: `return lst[0] + sum_of_list(lst[1:])`. Call stack for `[1,2,3,4]`: `1 + (2 + (3 + (4 + 0)))`.

**#39** — For each n, find all divisors from 1 to n-1 using a for loop with `if n%i==0`. Sum them. If sum equals n, it's perfect.

**#40** — Bubble sort: two nested loops, compare adjacent elements, swap if out of order. Repeat until no swaps happen. Reverse: `sorted_list[::-1]` via lambda. Then filter evens, then map squares.

---

## 👁️ Output Previews

**#1** → `1 2 4 5 7 8 10 11 13 14 16 17 19 20` (each on new line, multiples of 3 missing)

**#2** → `Sum of positive numbers entered: 45` (if user entered 5,10,15,20,-1)

**#3** → `0: P  1: y  2: t  3: h  4: o  5: n` (each on new line)

**#4** → `4  9` (only ints printed, 7.5 and True and strings skipped)

**#5** → `Hello Ali from Delhi!  Hello Sara from Mumbai!  Hello Raj from Bareilly!`

**#6** → `India has a population of 1400000000` (repeated for each country)

**#7** → `8  27  64  125  216` (cubes of 2,3,4,5,6)

**#8** → `2  4  6  8  10`

**#9** → `{1, 2, 3, 4, 5}` (order may vary — it's a set)

**#10** → `True  False  True`

**#11** → `150`

**#12** → `4321`

**#13** → `1  2  3  4  5` (count printed after each call)

**#14** → `[32.0, 68.0, 98.6, 212.0, 14.0]`

**#15** → `['apple', 'ant', 'avocado', 'apricot']`

**#16** → Full 5×10 multiplication table grid

**#17** → `1  1  2  6  24  120  ...  3628800` (for 0,1,1,2,3,5,10)

**#18** → `3  2  1` (vowels in 'Python', 'hello', 'gym')

**#19** → `True True  True False` (second `is` is False due to dynamic construction)

**#20** → `{'the': 3, 'cat': 2, 'sat': 1, 'on': 1, 'mat': 1}`

**#21** → `0 1 1 2 3 5 8 13 21 34`

**#22** → `True` for 121, `False` for 123

**#23** → `[4, 16, 36, 64, 100]`

**#24** → `20` then `10` (local x changed, global x untouched)

**#25** → `2 3 5 7 11 13 17 19 23 29 31 37 41 43 47`

**#26** → `10` for 1234, `1` for 1000, `9` for 9, `15` for 555

**#27** → `{2: ['hi', 'to', 'he'], 3: ['bye', 'cat', 'dog'], 5: ['hello']}`

**#28** → `['Ali: 88/100', 'Sara: 72/100', 'Raj: 95/100']`

**#29** → `GCD of 48 and 18 is 6`

**#30** → `'nohtyP'` for `'Python'`

**#31** → `power(2,3)=8`, `power(2,-2)=0.25`, `power(3,0)=1`

**#32** → `[1, 2, 3, 4, 5, 6]`

**#33** → `[6, 6, 8]` for sentence `'hello world python'` (words > 3 chars, their lengths)

**#34** → `11` then `5`

**#35** → `4` for both versions when input is `1234`

**#36** → `True` for 256, `False` for 257 (may vary by Python implementation)

**#37** → `[5, 6, 6]` for `['hi', 'hello', 'python', 'grind', 'ok']`

**#38** → `10` for `[1,2,3,4]`

**#39** → `6  28  496`

**#40** → sorted: `[1,2,3,...]`, reversed via lambda, evens filtered, evens squared

---

*Python Grind Protocol — Batch 03 | Topics: Loops · Functions · Recursion · Lambda · Map · Filter · Local/Global · is vs ==*
