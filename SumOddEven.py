# Read n numbers and find the sum separately for odd numbers and even numbers and
# print the sum of odd numbers and even  numbers.

NUMBERS, ODD, EVEN = [], [], []
for count in range(int(input("How many numbers do you have : "))):
    NUMBERS.append(int(input(f"Enter the {count+1} number : ")))
for num in NUMBERS:
    EVEN.append(num) if num % 2 == 0 else ODD.append(num)

# print(ODD)
# print(EVEN)

print(f"The sum of odd numbers are : {sum(ODD)}")
print(f"The sum of even numbers are : {sum(EVEN)}")
