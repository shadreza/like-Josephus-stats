kill_factor = int(input("Which person dies? "))

print("People were ------ Last Man Standing Was At")

for i in range (1, 101):
    res = 0
    if i == 1:
        res = 1

    else:
        people_line = []
        for j in range(i):
            people_line.append(j+1)
        index = 0
        counter = 1
        while len(people_line)>1:
            if counter == kill_factor:
                counter = 1
                tmp_index = index
                index = (index) % len(people_line)
                people_line.pop(tmp_index)
            else:
                counter = counter + 1
                index = (index + 1) % len(people_line)
        res = people_line[0]
    print(i, " -> ", res)
print()
print("Just getting the stats for like Josephus Problem by shadreza!")