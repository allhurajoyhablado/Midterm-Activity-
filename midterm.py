my_list = []

for x in range(1, 10):   # generates numbers from 1 to 9
    my_list.append(x)

print("Original list:", my_list)

print("Length of list:", len(my_list))

unique_list = []
for num in my_list:
    if num not in unique_list:
        unique_list.append(num)

print("\nThe list with unique elements only.")
print(unique_list)
