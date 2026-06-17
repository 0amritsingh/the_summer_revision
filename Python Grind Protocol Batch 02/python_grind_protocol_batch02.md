# ⚡ Python Grind Protocol — Batch 02

**Topics:** List · List Comprehension · Tuple · Dict · Set · Loops (range-based input only)
**Builds on:** Batch 01 — strings, if-else, typecasting, slicing, print, input

---

## 🟢 Easy (10 Questions)

**#1 — Code | List**
Create a list of 5 of your favourite foods. Print the first item, the last item, and the total count of items.
> 💡 Hint: Use index `[0]` for first, `[-1]` for last, `len()` for count.

---

**#2 — MCQ | List**
What is the output?
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[1])
```
- A) apple
- B) banana ✅
- C) cherry
- D) Error

> 💡 Indexing starts at 0, so `[1]` is the second item.

---

**#3 — Code | List**
Create a list of 4 numbers. Append the number 99 to it. Remove the first item. Print the final list.
> 💡 Hint: Use `.append()` to add and `.pop(0)` or `.remove()` to delete the first item.

---

**#4 — MCQ | Tuple**
Which of these is a valid tuple?
- A) `t = [1, 2, 3]`
- B) `t = (1, 2, 3)` ✅
- C) `t = {1, 2, 3}`
- D) `t = <1, 2, 3>`

> 💡 Tuples use round brackets `( )`.

---

**#5 — Code | Tuple**
Create a tuple storing `(city, country, pin_code)` of your area. Try to change the city. Observe and explain what happens in a comment.
> 💡 Hint: Tuples are immutable — you'll get a `TypeError`. Write a `# comment` explaining it.

---

**#6 — MCQ | Dict**
What does this print?
```python
d = {'name': 'Aryan', 'age': 18}
print(d['name'])
```
- A) Aryan ✅
- B) name
- C) 18
- D) Error

> 💡 `d['name']` accesses the value mapped to the key `'name'`.

---

**#7 — Code | Dict**
Create a dictionary for a student: name, age, city, marks. Print each value using its key. Then add a new key `'grade'` with value `'A'`.
> 💡 Hint: Access with `d['key']`. Add with `d['new_key'] = value`.

---

**#8 — Code | Set**
Create two sets: one with your weekday subjects, one with weekend subjects. Print both. Add a new subject to the first set.
> 💡 Hint: Sets use `{ }`. Use `.add()` to insert a new element.

---

**#9 — MCQ | Set**
What is the output?
```python
s = {1, 2, 2, 3, 3, 3}
print(len(s))
```
- A) 6
- B) 3 ✅
- C) 1
- D) Error

> 💡 Sets store only unique values. Duplicates are removed automatically.

---

**#10 — Code | List + Loop**
Ask the user to enter 5 names one by one (use a for loop with range). Store them in a list. Print the full list at the end.
> 💡 Hint:
> ```python
> names = []
> for i in range(5):
>     names.append(input('Enter name: '))
> print(names)
> ```

---

## 🟡 Intermediate (10 Questions)

**#11 — Code | List**
You have a list of marks: `[45, 82, 67, 90, 55, 78]`. Find the highest and lowest mark using `max()` and `min()`. Also calculate the average.
> 💡 Hint: `max()`, `min()`, `sum()`, `len()` are all you need. `average = sum / len`.

---

**#12 — MCQ | List**
What is the output?
```python
a = [1, 2, 3]
b = a
b.append(4)
print(a)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]` ✅
- C) `[4]`
- D) Error

> 💡 `b = a` does NOT copy. Both point to the same list. Use `a.copy()` to avoid this.

---

**#13 — Code | Dict**
Create a dict of 3 students and their marks. Print only the names (keys) and only the marks (values) separately using `.keys()` and `.values()`.
> 💡 Hint: `dict.keys()` returns all keys. `dict.values()` returns all values. Wrap in `list()` to print cleanly.

---

**#14 — MCQ | Dict**
What happens when you access a key that doesn't exist?
```python
d = {'a': 1}
print(d['b'])
```
- A) None
- B) 0
- C) KeyError ✅
- D) False

> 💡 Use `d.get('b')` to safely return `None` instead of crashing.

---

**#15 — Code | Set**
Create `set A = {1,2,3,4,5}` and `set B = {3,4,5,6,7}`. Print: union, intersection, difference (A-B), and check if 3 is in both sets.
> 💡 Hint: Use `|` or `.union()`, `&` or `.intersection()`, `-` or `.difference()`. `in` keyword for membership.

---

**#16 — Code | Tuple + List**
You have a tuple of 5 city names. Convert it to a list, add 2 more cities, sort it alphabetically, then convert back to a tuple. Print the final tuple.
> 💡 Hint: `list(tuple)` converts it. `.sort()` sorts in place. `tuple(list)` converts back.

---

**#17 — MCQ | List Comprehension**
What does this produce?
```python
result = [x*2 for x in [1,2,3,4,5]]
```
- A) `[1,2,3,4,5]`
- B) `[2,4,6,8,10]` ✅
- C) `[1,4,9,16,25]`
- D) Error

> 💡 List comprehension applies `x*2` to each item in the list.

---

**#18 — Code | List Comprehension**
Given a list of words: `['python','java','c++','rust','go']` — use list comprehension to create a new list with only words longer than 3 characters, in UPPER case.
> 💡 Hint: `[w.upper() for w in words if len(w) > 3]` — comprehension with a filter condition.

---

**#19 — Code | Dict + Input**
Ask user to enter 3 items and their prices (use range loop for input). Store them in a dictionary. Print the most expensive item.
> 💡 Hint: Use `max(d, key=d.get)` to find the key with the highest value.

---

**#20 — MCQ | Set**
What is the output?
```python
s = {3, 1, 4, 1, 5, 9, 2, 6}
print(s)
```
- A) `{3,1,4,1,5,9,2,6}`
- B) `{1,2,3,4,5,6,9}`
- C) `{1,1,2,3,4,5,6,9}`
- D) Output order not guaranteed, but no duplicates ✅

> 💡 Sets are unordered and unique. The print order may vary each run.

---

## 🔴 Hard (10 Questions)

**#21 — Code | List + Batch 01**
Ask the user to enter 5 words. Store in a list. Then create two new lists: one with words that start with a vowel, one with words that start with a consonant. Print both.
> 💡 Hint: Use `if word[0].lower() in 'aeiou'` to check. Build two lists with if/else inside a range loop.

---

**#22 — MCQ | List Comprehension**
What does this return?
```python
nums = [1,2,3,4,5,6]
result = [x for x in nums if x%2==0 if x>2]
```
- A) `[2,4,6]`
- B) `[4,6]` ✅
- C) `[2,6]`
- D) Error

> 💡 Two conditions: x must be even AND greater than 2. Only 4 and 6 pass both.

---

**#23 — Code | Dict + Batch 01**
Create a dictionary where keys are 5 student names (input from user) and values are their marks. Then print a report: name, mark, and whether they passed (>=40) or failed.
> 💡 Hint: Use `range` loop to collect both inputs. Access `dict.items()` to print pairs. Use if/else for pass/fail.

---

**#24 — Code | Tuple**
A tuple stores monthly sales: `(12000, 8500, 15000, 9200, 17000, 11000)`. Find: total sales, average, best month number, worst month number.
> 💡 Hint: `sum()`, `max()`, `min()` work on tuples. `t.index(max(t)) + 1` gives the month position.

---

**#25 — MCQ | Dict**
What is the output?
```python
d = {'a':1, 'b':2, 'c':3}
d.update({'b':99, 'd':4})
print(d)
```
- A) `{'a':1,'b':2,'c':3}`
- B) `{'a':1,'b':99,'c':3,'d':4}` ✅
- C) `{'a':1,'b':2,'c':3,'d':4}`
- D) Error

> 💡 `.update()` overwrites existing keys and adds new ones.

---

**#26 — Code | Set + Batch 01**
Ask user to enter two sentences. Convert each to a set of unique words. Print: words common to both sentences, words only in the first, words only in the second.
> 💡 Hint: `sentence.split()` gives a list. `set()` of that gives unique words. Use `&` for common, `-` for exclusive.

---

**#27 — Code | List Comprehension + Batch 01**
You have a string: `'Hello World Python Grind Protocol'`. Use list comprehension to make a list of the length of each word. Then find which length appears most using `max()`.
> 💡 Hint: `string.split()` gives words list. `[len(w) for w in words]` gives lengths. `max()` on that list.

---

**#28 — MCQ | Tuple vs List vs Set**
Which statement is TRUE?
- A) Tuples can be changed after creation
- B) Sets maintain insertion order
- C) Lists allow duplicate values ✅
- D) Dicts can have duplicate keys

> 💡 Lists allow duplicates. Tuples are immutable. Sets are unordered. Dict keys must be unique.

---

**#29 — Code | Dict + List**
Create a dictionary of 3 countries and their capitals. Store all country names in one list and all capitals in another. Then check if a user-entered city is a capital or not.
> 💡 Hint: Use `list(d.keys())` and `list(d.values())`. Then use `in` keyword to check membership.

---

**#30 — Code | List Comprehension + Batch 01**
Ask user to enter 6 numbers. Use list comprehension to create: a list of squares of even numbers only, and a list of cubes of odd numbers only. Print both.
> 💡 Hint: `[x**2 for x in nums if x%2==0]` and `[x**3 for x in nums if x%2!=0]`

---

## 💀 Impossible (10 Questions)

**#31 — Code | Dict + List + Batch 01**
Given `lst = [5,2,8,1,9,3]` — use list comprehension to create a new list where each element is replaced by how many elements in the original list are smaller than it. (This gives the sorted rank of each element.)
> 💡 Hint: `[len([y for y in lst if y < x]) for x in lst]`

---

**#32 — MCQ | List Comprehension**
What does this produce?
```python
m = [[1,2],[3,4],[5,6]]
flat = [n for row in m for n in row]
```
- A) `[[1,2],[3,4],[5,6]]`
- B) `[1,2,3,4,5,6]` ✅
- C) `[1,3,5]`
- D) Error

> 💡 Nested list comprehension flattens a 2D list. Read as: for each row, for each n in row.

---

**#33 — Code | Set + Dict + Batch 01**
Ask user to enter 5 words (user may repeat words intentionally). Using a dict, count how many times each unique word appears. Print `word: count` for each.
> 💡 Hint: `d[word] = d.get(word, 0) + 1` inside a range loop.

---

**#34 — Code | List + Tuple + Dict**
You have this data as a list of tuples:
```python
[('Alice',85),('Bob',72),('Alice',90),('Bob',68),('Charlie',95)]
```
Compute each student's average mark using a dict. No imports allowed.
> 💡 Hint: Build a dict of `{name: [list of marks]}`. Use `d.get(name, [])` to handle first occurrence. Then compute average per name.

---

**#35 — MCQ | All Batch 02**
What is the output?
```python
a = [1,2,3]
b = a.copy()
b.append(4)
c = set(a) | set(b)
print(sorted(c))
```
- A) `[1,2,3]`
- B) `[1,2,3,4]` ✅
- C) `{1,2,3,4}`
- D) `[1,2,3,3,4]`

> 💡 `a=[1,2,3]`, `b=[1,2,3,4]`. Union set = `{1,2,3,4}`. `sorted()` returns a list → `[1,2,3,4]`.

---

**#36 — Code | Dict + Batch 01**
A dict stores product names and stock:
```python
{'rice':50,'wheat':20,'sugar':0,'oil':15,'dal':0}
```
Print two lists: in-stock items (stock > 0) and out-of-stock items — using list comprehension on `dict.items()`.
> 💡 Hint: `[k for k,v in d.items() if v>0]` for in-stock. `[k for k,v in d.items() if v==0]` for out-of-stock.

---

**#37 — Code | List Comprehension + Batch 01**
Given a sentence from user input — use a single list comprehension to extract all unique characters that are: alphabets only, lowercase, and appear more than once in the string.
> 💡 Hint: `[c for c in set(sentence.lower()) if c.isalpha() and sentence.lower().count(c) > 1]`

---

**#38 — MCQ | Dict**
What does `d.get('x', 'missing')` return if `'x'` is not in `d`?
- A) None
- B) KeyError
- C) `'missing'` ✅
- D) False

> 💡 `.get(key, default)` returns the default value if key doesn't exist. Safer than `d['x']`.

---

**#39 — Code | All Batch 02 + Batch 01**
Ask user to input 5 numbers. Store in a list. Then:
- Make a set of unique numbers
- Make a tuple of numbers > 50
- Make a dict where key = number, value = `'even'` or `'odd'`

Print all three.
> 💡 Hint: `{x: 'even' if x%2==0 else 'odd' for x in lst}` for the dict comprehension.

---

**#40 — Code | List + Dict + Batch 01**
Build a mini phonebook. Ask the user to enter 4 contacts (name + phone number). Store in a dict. Then ask for a name to search. If found, print the number. If not, print `'Contact not found'`. Also print total contacts stored.
> 💡 Hint: Use `range(4)` loop to collect. `d[name] = phone`. Then `d.get(search, 'Contact not found')` for lookup.

---

## 🏪 Mega Project

**#41 — Mini Inventory & Billing System**

Build a complete shop system using ONLY Batch 01 + Batch 02 tools.

### Part 1: Setup Inventory
- Hardcode a dict of 6 products with their prices:
  ```python
  {'Rice': 60, 'Dal': 90, 'Oil': 150, 'Sugar': 45, 'Tea': 80, 'Biscuit': 30}
  ```
- Store out-of-stock items in a set (pick 2 items as out-of-stock)

### Part 2: Shopping
- Ask user to enter how many items they want to buy (max 5)
- Use range loop to collect item names
- For each item:
  - If in inventory AND not out-of-stock → add to cart (dict: item → price)
  - If out-of-stock → inform user and skip
  - If not found → inform user and skip

### Part 3: Bill
- Print formatted bill with all cart items + prices
- Compute subtotal using `sum(cart.values())`
- Apply 5% discount if subtotal > ₹200
- Add 18% GST on discounted amount
- Print grand total rounded to 2 decimals

### Part 4: Summary
- Print a tuple of successfully purchased items
- Print set of unique item categories attempted
- Print how many items were skipped

> 💡 Hint: Plan first — inventory dict → out_of_stock set → cart dict → bill computation → summary. This is a 50–80 line program. Totally doable with your tools.

---

*Python Grind Protocol — Batch 02 | Topics: List, Tuple, Dict, Set, List Comprehension, Range Loops*
