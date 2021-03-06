"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
count = 0
numbers = set()
for call in calls:
    for item in call[0:2]:
        if item not in numbers:
            numbers.add(item)
            count += 1
for text in texts:
    for item in text[0:2]:
        if item not in numbers:
            numbers.add(item)
            count += 1
print("There are {} different telephone numbers in the records.".format(count))