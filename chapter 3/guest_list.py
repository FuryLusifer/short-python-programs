guest_list = ['Ram', 'Shyam', 'Hari', 'Sita', 'Gita', 'Rita']

print(guest_list)

print(f"You're Invited!, Mr. {guest_list[0].title()}")
print(f"You're Invited!, Mr. {guest_list[1].title()}")
print(f"You're Invited!, Mr. {guest_list[2].title()}")
print(f"You're Invited!, Mr. {guest_list[3].title()}")
print(f"You're Invited!, Mr. {guest_list[4].title()}")
print(f"You're Invited!, Mr. {guest_list[5].title()}")

print()

print(f"Mr. {guest_list[2].title()} could not attend the dinner.")

print()

guest_list[2] = "Ghanshyam"
print(guest_list)

print(f"You're Invited!, Mr. {guest_list[0].title()}")
print(f"You're Invited!, Mr. {guest_list[1].title()}")
print(f"You're Invited!, Mr. {guest_list[2].title()}")
print(f"You're Invited!, Mr. {guest_list[3].title()}")
print(f"You're Invited!, Mr. {guest_list[4].title()}")
print(f"You're Invited!, Mr. {guest_list[5].title()}")

print()

print("I have just found a bigger table so some more guest will be invited")

guest_list.insert(0, "Radheshyam")
guest_list.insert(3, "Aakriti")
guest_list.append("Sushmita")

print(guest_list)

print(f"You're Invited!, Mr. {guest_list[0].title()}")
print(f"You're Invited!, Mr. {guest_list[1].title()}")
print(f"You're Invited!, Mr. {guest_list[2].title()}")
print(f"You're Invited!, Mr. {guest_list[3].title()}")
print(f"You're Invited!, Mr. {guest_list[4].title()}")
print(f"You're Invited!, Mr. {guest_list[5].title()}")
print(f"You're Invited!, Mr. {guest_list[6].title()}")
print(f"You're Invited!, Mr. {guest_list[7].title()}")
print(f"You're Invited!, Mr. {guest_list[-1].title()}")

print()

print("The bigger table could not arrive on time so, I can invite only 2 person now")
print(guest_list)

print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")
print(f"I am sorry to inform you that i could not accomodate you!, Mr. {guest_list.pop().title()}")

print()

print(guest_list)

print(f"You're still Invited!, Mr. {guest_list[0].title()}")
print(f"You're still Invited!, Mr. {guest_list[1].title()}")

del guest_list[-1]
del guest_list[-1]

print()
print("Final guest list:")
print(guest_list)
