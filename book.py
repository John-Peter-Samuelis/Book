guests = ['Samuelis', 'John', 'Peter']

for guest in guests:
    print(f"You, {guest}, are privileged to be invited to a dinner")

print(f"\n It has come to my notice that {guests[1]} cannot make it to the dinner")
guests[1] = "Etornam"
print(guests)

for each_guest in guests:
    print(f"New invitation card.\n{each_guest} has been invited\n")


print("\n\n I have found a bigger dinner table. This implies more people")
guests.insert(0, 'Kwabena')
guests.insert(3, 'John')
guests.append('Jeremiah')

print(guests)
print("Unfortunately, only two people can be invited to the dinner")

for removed_guests in guests:
    while len(guests) > 2:
        removed_guests = guests.pop()
        print(f"Sorry, {removed_guests}")

    
for guest in range(0,len(guests)-1):
    del guests[0]

print(guests)
