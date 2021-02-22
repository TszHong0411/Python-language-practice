age = input("Please enter your age: ")

if age.isdigit():
    age = int(age)
    if age < 18:
        print("You can't enter our website. Because your age small than 18.")
    else:
        print("Successfully entered our website")
else:
    print("Please enter a number.")