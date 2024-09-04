user_number = int(input("Enter a four-digit number:"))

fourth_number = user_number % 10
user_number //= 10
third_number = user_number % 10
user_number //= 10
second_number = user_number % 10
user_number //= 10
first_number = user_number

print(first_number)
print(second_number)
print(third_number)
print(fourth_number)

# Людяний варіант, де не потрібно ломати мозок та сивіти )))
user_number = input("Enter a four-digit number:")
for num in user_number:
    print(int(num))
