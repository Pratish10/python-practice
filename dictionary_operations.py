"""
Demonstrates various dictionary operations using a user profile.
Operations include accessing, updating, adding, deleting, and iterating keys and values.
"""

user_profile = dict(
  username="john doe",
  email="johndoe@gmail.com",
  age=24,
  is_active=True,
  city="Nagpur"
)

print(f"My name is: {user_profile['username']}")
print(f"My email is: {user_profile.get('email', 'Not Provided')}")
print(f"My phone number is: {user_profile.get('phone_number', 'Not Provided')}")

user_profile["age"] = 30
print(f"My new updated age is: {user_profile.get('age', 'Not Provided')}")

user_profile["last_login"] = "2025-06-18 20:00:00"

del user_profile["is_active"]

print(f"My profile keys are: {list(user_profile.keys())}")
print(f"My profile values are: {list(user_profile.values())}")
print('------ using for loop to print all the keys -------')

for key in user_profile:
  print(key)

print('------ using for loop to print all the keys and values -------')
for key, value in user_profile.items():
  print(f"Key: {key}, Value: {value}")