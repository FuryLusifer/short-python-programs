num_list = [num for num in range(1,10)]
print(num_list)

for num in num_list:
    if(num == 1):
        print(f"{num}st Element.")

    elif(num == 2):
        print(f"{num}nd Element.")

    elif(num == 3):
        print(f"{num}rd Element.")

    else:
        print(f"{num}th Element:")
    