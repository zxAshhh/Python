def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    else:
        return "Adult"

age = int(input("Enter the age: "))
print(categorize_age(age))
