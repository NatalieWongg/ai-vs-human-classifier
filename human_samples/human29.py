horizontal_count = []
vertical_count = []

for x in list1:
    horizontal_count.append(x.count(0))

print(horizontal_count)

for i in range(len(list1[0])):
    count = 0
    for j in range(len(list1)):
        if list1[j][i] == 1:
            if count > 0:
                vertical_count.append(count)
            count = 0
        else:
            count += 1
    if count > 0:
        vertical_count.append(count)

print(vertical_count)

print(max(max(horizontal_count), max(vertical_count)))