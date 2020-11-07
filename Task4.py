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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

callers = {}

for call in calls:
    if call[0] not in callers:
        callers[call[0]] = [1, 0, 0, 0]
    else:
        callers[call[0]][0] += 1
for call in calls:
    if call[1] in callers:
        callers[call[1]][1] += 1

for text in texts:
    if text[0] not in callers:
        callers[text[0]] = [0, 0, 1, 0]
    else:
        callers[text[0]][2] += 1
for text in texts:
    if text[1] in callers:
        callers[call[1]][3] += 1
    #     callers[text[0]][2] += 1
    # if text[1] in callers:
    #     callers[text[1]][3] += 1

suspicious = []
for caller in callers:
    if callers[caller][1] == 0 and callers[caller][2] == 0 and callers[caller][3] == 0:
        suspicious.append(caller)

print("These numbers could be telemarketers: ")
print(len(suspicious))
# for s in sorted(suspicious):
    # print(s)