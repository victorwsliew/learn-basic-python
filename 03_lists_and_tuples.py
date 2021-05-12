# lists
friends = ["Kevin", "Karen", "Jim"]
print(friends[0])

friends.append('John')
friends.insert(1, 'Wick')
# friends.clear()
friends.count("Karen")
friends.sort()

friends2 = friends.copy()
friends2.reverse()

print(friends)
print(friends2)

# tuples
# immutable variable
coordinates = [(4, 5), (6,7)]
# coordinates[1] = 10 -- opps

print(coordinates[1])
