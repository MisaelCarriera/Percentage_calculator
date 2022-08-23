print("What percentage would you like to calculate?")

percentage = float(input("Percentage: "))

number = float(input("Number: "))

print("What is ",percentage,"%", "of", number )

total = number * percentage / 100

print(percentage,"%","of", number ," is", total)
