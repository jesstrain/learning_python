num_list = []

for i in range(1,13):
    num_list.append(i)

count = len(num_list) - 1
while count >= 0:
    print(num_list[count])
    count -= 1