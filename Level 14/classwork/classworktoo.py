age = int(input("input your age:"))
user_experience = input("input your job or student status:")

user_age_confirm = age >= 18 and age < 60
user_confirm = user_experience == "employed" or user_experience == "student"
print('user is', user_age_confirm ,'user is a', user_confirm)