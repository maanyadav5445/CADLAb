data = ((1, "A"), (2, "B"), (3, "C"), (4, "D"))

result = []
for num, char in data:
    result.append((num, char.lower(), num * 2))

for item in result:
    print(item)

filtered = tuple(x for x in result if x[0] % 2 == 0)
print(filtered)