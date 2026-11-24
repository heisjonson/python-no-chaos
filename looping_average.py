


total = 0
count = 0

while True:
    number = float(input("Enter a number (-1 to stop): "))

    if number == -1:
        break

    total += number
    count += 1
    average = total / count
    print(f"The average is {average}")

if count > 0:
    print(f"Final average of {count} numbers: {total / count}")
else:
    print("No numbers were entered")