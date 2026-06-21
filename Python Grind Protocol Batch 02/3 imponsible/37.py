# Given a sentence from user input — use a single list comprehension to extract all unique characters that are: alphabets only, lowercase, and appear more than once in the string.

sen = input('Enter a sentence: ')
unique_list = [
    i
    for i in sen.split()
    if len(i) == 1 or i.lower() == True or sen.split().count(i) > 1
]
print(set(unique_list))