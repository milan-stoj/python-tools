lucky_numbers = [3, 7, 14, 21]
friends = ["Miro", "Mitchell", "Justen", "Jovan", "Mitchell", "Gunther"]

print(lucky_numbers)
print(friends)

friends.sort()
lucky_numbers.reverse()
friends.extend(lucky_numbers)
friends.append("Steven")

friends.insert(0, "Milan")

print(friends)

friends.remove("Steven")
print(friends)

friends.pop()
print(friends)

print(friends.index("Milan"))
print(friends.count("Mitchell"))
print(friends)

friends2 = friends.copy()


friends.clear()
print(friends)
print(friends2)
