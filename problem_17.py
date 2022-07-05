_1_to_9 = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
_10_to_19 = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
_20_to_99 = (_1_to_9 * 8) + (10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6))  # Twenty, Thirty ... Ninety all repeated 10 times, 1 to 9 repeated each time
_1_to_99 = _1_to_9 + _10_to_19 + _20_to_99

_100s = (100 * _1_to_9) + (900 * (7 + 3)) - (9 * 3) + (9 * _1_to_99)

total = _1_to_99 + _100s + 11
print(total)