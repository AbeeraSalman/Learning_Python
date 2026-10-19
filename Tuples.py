person = ("Abeera", "Abeera", 23, "A")
print(person)

# person[0] = "hooria"   # TypeError: tuples are immutable

print(person.count("Abeera"))   # 2
print(person.index("Abeera"))   # 0