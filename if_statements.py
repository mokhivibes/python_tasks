#NEW CHAPTER IF Statements

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'audi':
        print(car.title())
    else:
        print(car.lower())


#Checking for Inequality

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': #!= means not equal to
    print("Hold the anchovies!")

#Checking for Inequality ENd

#Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushroom' in requested_toppings:
    print(True)
else:
    print(False)

#Checking Whether a Value Is in a List End

#Checking Whether a Value Is Not in a List

banned_users =['salim', 'ali', 'marlie']
user = input('Enter your username: ')
if user not in banned_users:
    print('Welcome ' + user.title() + '!')
else:
    print('Please, choose another username!')

#Checking Whether a Value Is Not in a List End

#Tasks

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 1. EQUALITY & INEQUALITY with strings
print('apple' == 'apple')
print('orange' == 'pear')

print('banana'.title() =='banana')
print('banana'.title() == 'Banana')

print(4 != 5)
print(345>354)
print(43<68)
print(345>=53)

for age in range(1,11):
    birth_year = input('What is your birth year? ')
    age = 2026 - int(age)
    if age > 18:
        print('You can access this source!')
    else:
        print('Sorry, you cannot access this source!')

birth_year = input('What is your birth year? ')
age = 2026 - int(birth_year)
name = input('What is your name? ')
name = name.title()
if age > 18 and name == 'Madina':
    print('Welcome' + ' ' + name +', you are the administrator!')
else:
    print('Sorry, you are not the admin')


birth_year = input('What is your birth year? ')
age = 2026 - int(birth_year)
name = input('What is your name? ')
name = name.title()
if age > 18 or name == 'Madina':
    print('Welcome' + ' ' + name +', you are the administrator!')
else:
    print('Sorry, you are not the admin')


plans = ['read', 'clean', 'code', 'write', 'cook']
plan = input('Which task do you want to choose? ')
plan = plan.lower()
if plan not in plans:
    print('This task is not available on your check list!')
elif plan == 'code':
    answer = input((f"Do you want me to {plan}? "))
    if answer == 'yes':
        codes = ['I like you', "You're the best!"]
        for code in codes:
            print(codes[1])
    else:
        print('Got it, let me know what to do!')
elif plan == 'read':
    answer = input((f"Do you want me to {plan}? "))
    if answer == 'yes':
        options = input(f'What do you want me to {plan}? ')
        options = options.title()
        if options == "Books":
             print("Okay, I'm reading!")
        else:
             print('Sorry, I can\'t read!')
    else:
        print('Got it, let me know what to do!')
elif plan == 'clean':
    answer = input((f"Do you want me to {plan}? "))
    if answer == 'yes':
        options = input(f'Where do you want me to {plan}? ')
        options = options.title()
        if options == "Rooms":
             print("Okay, I'm cleaning")
        else:
             print('Sorry, I can\'t clean there!')
    else:
        print('Got it, let me know what to do!')

elif plan == 'cook':
    answer = input((f"Do you want me to {plan}? "))
    if answer == 'yes':
        options = input(f'What do you want me to {plan}? ')
        options = options.title()
        if options == "Food":
            print("Okay, I'm cooking")
        else:
            print('Sorry, I can\'t cook it!')
    else:
        print('Got it, let me know what to do!')
elif plan == 'write':
    answer = input((f"Do you want me to {plan}? "))
    if answer == 'yes':
        options = input(f'What do you want me to {plan}? ')
        options = options.title()
        if options == "Poems":
            print("Okay, I'm writing")
        else:
            print('Sorry, I can\'t write it!')
    else:
        print('Got it, let me know what to do!')



plans = ['read', 'clean', 'code', 'write', 'cook']
plan = input('Which task do you want to choose? ')
plan = plan.lower()
if plan not in plans:
    print('This task is not available on your check list!')
else:
    print(f"I'm ready to execute this task: {plan}")
#Tasks End


#Testing Multiple Conditions

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


colors = ['red', 'black', 'white', 'green', 'violet']
requested_colors = input("What color do you want to add to your theme?\n")
if requested_colors == 'red' in colors:
    print(f"{requested_colors} is added to your theme.")
if requested_colors == 'white' in places:
    print(f"{requested_colors} is added to your theme.")
if requested_colors == 'black' in places:
    print(f"{requested_colors} is added to your theme.")
else:
    print(f"{requested_colors} is not a valid color.")

#TIP: if you want only one block of code to run, use an if-elifelse chain. If more than one block of code needs to run, use a series of independent if statements.

#Task

alien_color = ['green']
if "green" in alien_color:
    print(f"Congrats, you earned 5 points")

alien_color = ['red']
if "black" in alien_color:
    print(f"Congrats, you earned 5 points")

alien_color = ['green']
if "green" in alien_color:
    print(f"Congrats, you earned 5 points")
elif "red" in alien_color:
    print(f"Congrats, you earned 10 points")
elif "yellow" in alien_color:
    print(f"Congrats, you earned 15 points")

age = input("Please insert your age:\n")
if int(age) < 2:
    print("You're a baby")
elif 2 == int(age) < 4 :
    print("You're a toddler")
elif 4 == int(age) < 13:
    print("You're a kid")
elif 13 == int(age)  < 20:
    print("You're a teenager")
elif 20 == int(age) < 65:
    print("You're an adult")
elif int(age) >= 65:
    print("You're an elder")


fav_fruits = ['apple', 'pear', 'pineapple', 'banana']
if 'apple' in fav_fruits:
    print("You really like apple!")
if 'pear' in fav_fruits:
    print("You really like pear!")
if 'pineapple' in fav_fruits:
    print("You really like pineapple!")
if 'banana' in fav_fruits:
    print("You really like banana!")
if "kiwi" in fav_fruits:
    print("You really like kiwi!")


alien_color = ['green', 'yellow', 'red']
if "yellow"in colors:
    print(f"Congrats, you earned 5 points")
if "red" in colors:
    print(f"Congrats, you earned 5 points")
if "black" in colors:
    print(f"Congrats, you earned 5 points")

#Task End

#Testing Multiple Conditions End

#Using if Statements with Lists

fav_toppings = input("Please, insert your favorite toppings: ")
requested_toppings = fav_toppings.split(',')
print(requested_toppings)


available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")


#Task

usernames = ['bubble', 'bento', 'admin', 'mentol', 'solar']
for username in usernames:
    if username == "admin":
        print(f"Hello {username}, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again!")

usernames = []
for username in usernames:
    if username == "":
        print("We need to find some users!")
# WARNING when the list is empty, the for loop never runs at all!

#
usernames = []
if usernames:
    for username in usernames:
        if username == "admin":
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again!")
else:
    print("We need to find some users!")


current_users = ['mokhi', 'usman', 'terry', 'khan', 'ferry']
current_users_lower = [user.lower() for user in current_users]
new_users = ['usman', 'terry', 'hydro', 'harmony']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Please, enter new user name")
    else:
        print(f"{new_user} is available")

numbers = list(range(1,10))
for number in numbers:
    if number == 1:
        str(number)
        print(f"{number}st")
    elif number == 2:
        str(number)
        print(f"{number}nd")
    elif number == 3:
        str(number)
        print(f"{number}rd")
    else:
        str(number)
        print(f"{number}th")

#Styling Your if Statements

# if age < 4:
#is better than:
# if age<4:

#Styling Your if Statements End

#Using if Statements with Lists End

#NEW CHAPTER IF Statements END

