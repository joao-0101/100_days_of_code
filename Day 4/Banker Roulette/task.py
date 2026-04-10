import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

random_name = random.randint(0, 4)

if random_name == 0:
    print(friends[0])
elif random_name == 1:
    print(friends[1])
elif random_name == 2:
    print(friends[2])
elif random_name == 3:
    print(friends[3])
else:
    print(friends[4])
