i = 0  # initialization
skipped = {2, 4}
while i <= 5:
    i += 1
    if i in skipped:
        continue

    print(i)
