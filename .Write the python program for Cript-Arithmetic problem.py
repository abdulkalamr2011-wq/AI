Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from itertools import permutations
... 
... letters = "SENDMORY"
... for p in permutations(range(10), len(letters)):
...     d = dict(zip(letters, p))
... 
...     if d['S'] == 0 or d['M'] == 0:
...         continue
... 
...     SEND = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
...     MORE = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
...     MONEY = 10000*d['M'] + 1000*d['O'] + 100*d['N'] + 10*d['E'] + d['Y']
... 
...     if SEND + MORE == MONEY:
...         print("Solution:", d)
...         print(SEND, "+", MORE, "=", MONEY)
