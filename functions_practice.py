def greet_user(username):
    print(f"Welcome, {username}!")
    print("Happy Coding!")


def calculate_rectangle_area(length, width):
    return length * width


def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even number"
    else:
        return f"{number} is odd number"


greet_user("John Doe")
greet_user("Jane Doe")

rect1 = calculate_rectangle_area(5, 10)
print(f"The area of rectange rect1 is {rect1}")

rect2 = calculate_rectangle_area(50, 100)
print(f"The area of rectange rect2 is {rect2}")

is_even1 = check_even_odd(5)
is_even2 = check_even_odd(10)

print(is_even1)
print(is_even2)
