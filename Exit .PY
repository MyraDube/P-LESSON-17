for i in range(10):
    if i == 8:
        print(exit)
        exit()
    print(i)


ages = [19, 45, 12, 78]
for age in ages:
    if age < 18:
        print(age, "not allowed")
        print(exit)
        exit()
    else:
        print(age, "allowed")