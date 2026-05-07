# Lists Lesson
import numbers

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(*bicycles) #this removes brackets and commas

print(bicycles[2]) #this is how to call an item in a list using index in brackets

print(bicycles[2].title())  # you can use string methods while calling the item from a list for example, .title(); .upper(); .lower() and find more methods on tg channel

print(bicycles[-1])  # -1 in brackets call the last item in a list so, whenever you want to call the items from the end of the list u can use negative sign which minus -

message = f"{bicycles[-1].title()} is my first childhood toy" # this is the method how to use the item in your variable using f or u can open "" and curly brackets and add + between them
print(message)

# Task 1:
#
names = ['Malika', 'Shukrona', 'Makhfuza', 'Nodira', 'Aziza']

print('Hello, my dear friend - ' +names[0])
print('Hello, my dear friend - ' +names[1])
print('Hello, my dear friend - ' +names[2])
print('Hello, my dear friend - ' +names[3])
print('Hello, my dear friend - ' +names[4])

# Task 2:

cars = ['Damas', 'Cobalt', 'Malibu', 'Dongfeng', 'Lacetti']

message1 = f'Our first car when we moved to Tashkent was {cars[0]}'
print(message1)

message2 = f'But when we got more money we bought {cars[1]}'
print(message2)

message3 = f'Guess what? Then we are already rich, we purchased {cars[2].upper()}'
print(message3)

message4 = f"So this is the card we're currently using - {cars[3].lower()}"
print(message4)

# Task completed

# Changing, adding, and removing elements in a list
cars = ['Damas', 'Cobalt', 'Malibu', 'Dongfeng', 'Lacetti']
cars[4] = 'Spark' # by this call you can change the element to the new item => listname[} = newname

cars.append('Epica') # .append('newitem') => this will add new element to the list, it will show up on the end of the list
cars = []
cars.append('Something')
cars.append('Nothing')
cars.append('anything')
print(cars)

name = input("Enter your name: ")
namelist = []
namelist.append(name)
print(namelist)
#this was my cool idea bro 😎

cars = ['Damas', 'Cobalt', 'Malibu', 'Dongfeng', 'Lacetti']
cars.insert(2, 'Tracker') # by using .insert(index (=> where you want to put the item), newitemname with "" )
print(cars)

cars = ['Damas', 'Cobalt', 'Malibu', 'Dongfeng', 'Lacetti']
del cars[0] # this will remove the selected item from the list, REMINDER: you can no longer access the value that was removed from the list after the del statement is used.
print(cars)

cars.pop() # you can remove the last item from the list and it can be removed from the list but still u can use it
thirdcar= cars.pop()
# print(cars)
print("The third card we owner was " + thirdcar.title() + ".")
print(f'I never wanted to us {thirdcar} and then i used {cars[0]}')


# Removing an item by Value
cars = ['Damas', 'Cobalt', 'Malibu', 'Dongfeng', 'Lacetti']
cars.remove("Damas") # using .remove("") you can remove the items by calling the item name
print(cars) #Quick Note: The remove() method deletes only the first occurrence of the value you specify. If there’s a possibility the value appears more than once in the list, you’ll need to use a loop to determine if all occurrences of the value have been removed.


#Task 3 start

guests = ["Marcus", "Melanie", "George", "Yasmina"]
print("Hello " + guests[0] + " I wanted you to come to tomorrow's party!")
print("Hello " + guests[1] + " I wanted you to come to tomorrow's party!")
print("Hello " + guests[2] + " I wanted you to come to tomorrow's party!")
print("Hello " + guests[3] + " I wanted you to come to tomorrow's party!")
cannotcome = guests.pop(2)
print(cannotcome + " will not come to the party")
print(guests)
print("Hello " + guests[0] + " I wanted you to come to tomorrow's party!")
print("Hello " + guests[1] + " I wanted you to come to tomorrow's party!")
print("Hello " + guests[2] + " I wanted you to come to tomorrow's party!")
guests.insert(0, "Aziza")
guests.insert(2, "Laziza")
guests.append("Sardor")
print(guests)
#
print("Sorry, but I can invite only 2 guests.")
guests.pop()
guests.pop()
guests.pop()
guests.pop()
del guests[0]
del guests[0]
print(guests)

# Changing, adding, and removing elements in a list end

#Organizing a List

#to PERMANENTLY sort our list

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort() # .sort() => this is the method that can be used to PERMANENTLY sort our list alphabetically
cars.sort(reverse=True) # => this is the method that can be used to PERMANENTLY sort in reverse from Z to A
print(cars)

#to PERMANENTLY sort our list END

#to TEMPORARILY sort our list

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f'Here is the original list of cars: \n{cars}')
print(f'And here is the sorted list of cars: \n{sorted(cars)}') #To alphabetically  maintain the original order of a list but present it in a sorted order, you can use the sorted() function to alphabetically sort out.
print(f'Here is the again original list of cars: \n{cars}')


cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse() #Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
print(cars)

#to TEMPORARILY sort our list end


#Finding the Length of a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) #quickly find the length of a list by using the len() function
#Python counts the items in a list starting with ONE, so you shouldn’t run into any OFFBY-ONE errors when determining the length of a list.
#Finding the Length of a List end

#Organizing a List end

#TASKS START

places = ['Madina', 'Beijing', 'Paris', 'Giza', 'Wadi Musa' ]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse = True)
print(places)
#Completed✅

guests = ["Marcus", "Melanie", "George", "Yasmina"]
print(len(guests[2]))
print(len(places))

languages = ['english', 'french', 'spanish', 'arabic', 'uzbek']
print(len(languages))
print(sorted(languages))
languages.sort(reverse=True)
print(languages)
languages.reverse()
print(languages)
print(sorted(languages, reverse=True))
print(languages)

#TASKS START END

#Avoiding Index Errors When Working with Lists

motorcycles = []
print(motorcycles[-1]) #The only time this approach will cause an error is when you request the last item from an empty list:


languages = ['english', 'french',  'uzbek']
print(languages[4]) #IndexError: list index out of range, because the count starts with 0 and we have 3 items, so 0; 1; 2

# Avoiding Index Errors When Working with Lists end

#Working with Lists

#Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
magician = ()
for magician in magicians:
    print(magician)

list_of_items = ['mummy', 45, 'daddy', 48, 'apple', 357]
for item in list_of_items:
    print(list_of_items)
number = ()
for number in list_of_items:
    if isinstance(number, int):
     print(number)



magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f'{magician.title()}, You did great job!')
    print(f'I cannot wait till your next trick, {magician.title()}\n')


print(f'Thank you for performing {", ".join(magicians).title()}!')

#Looping Through an Entire List end

#Avoiding Indentation Errors

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician) #The print statement at u should be indented, but it’s not. When Python expects an indented block and doesn’t find one, it lets you know which line it had a problem with.


magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
print("I can't wait to see your next trick, " + magician.title() + ".\n") #the first print statement is executed once for each name in the list because it is indented. The second print statement is not indented, so it is executed only once after the loop has finished running. Because the final value of magician is 'carolina', she is the only one who receives the “looking forward to the next trick” message

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
 print(magician.title() + ", that was a great trick!")
 print("I can't wait to see your next trick, " + magician.title() + ".\n")
 print("Thank you everyone, that was a great magic show!")

#  #Make sure that you don't forget about colon => : after for i in _______ : Okay?

#Avoiding Indentation Errors end

#TASKS

pizzas = ['pepperoni', 'macarella', 'chicken', 'donar']
for pizza in pizzas:
    print(f'I like {pizza} pizza!')
print('I really love pizza! \nI know there are many kinds of pizza, for example \n italian, american and canadian')

animals = ['horse', 'donkey', 'sheep']
for animal in animals:
    print(animal)
    print(f'A {animal} eat grass.')
print('All of these animals are domestic.')

#TASKS END

#Making Numerical Lists

#Using the range() Function

for value in range(1,5):
 print(value)

numbers = list(range(1, 7)) #=> If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a list of numbers.
print(numbers)

even_numbers = list(range(2, 15, 2)) # => the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11, and produces this result:
print(even_numbers)

squares = []
for value in range(1,20):
    squares.append(value**2)

print(squares)

#Using the range() Function End

#Simple Statistics with a List of Numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#Simple Statistics with a List of Numbers End

#List Comprehensions

squares = [ value**2 for value in range(1,11)]
print(squares)

#List Comprehensions end

#TASKS

for number in range(1,20):
    print(number)

numbers = [number for number in range(1, 1000000)]
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [number for number in range(1,20,2)]
print(odd_numbers)

for number in range(1,20,2):
    print(number)

multiplied_numbers = [number**3 for number in range(3, 30)]
print(multiplied_numbers)

cube_numbers = [number**3 for number in range(1,10)]
print(cube_numbers)

for number in range(1, 10):
    value = number**3
    print(value)

#TASKS END

#Making Numerical Lists End


#Working with Part of a List

#Slicing a List

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #To output the first three elements in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2
print(players[:4]) #If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[2:]) #if you want all items from the third item through the last item, you can start with index 2 and omit the second index
print(players[-3:]) #This prints the names of the last three players and would continue to work as the list of players changes in size.

#Slicing a List end

#Looping Through a Slice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
 print(player.title())

#Looping Through a Slice End

#Copying a List

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(*friend_foods)

my_foods.append('cucember')
friend_foods.append('apple pie')

print("My favorite foods are:")
print(*my_foods)



print("\nMy friend's favorite foods are:")
print(*friend_foods)

# This doesn't work:
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#Copying a List End

#Tasks

my_foods = ['pizza', 'falafel', 'carrot cake', 'salmon', 'beef']
print(f"My first three items in the list are:  {my_foods[:3]}")
print(f"Three items from the middle of the list are: {my_foods[1:5]}")
print(f"My last three items in the list are: {my_foods[-3:]}")

pizzas = ['pepperoni', 'macarella', 'chicken', 'donar']
friends_pizzas = pizzas[:]
print(friends_pizzas)
print(pizzas.append("americano"))
print(friends_pizzas.append('frencho'))
print("My favorite pizzas are: ")
for pizza in pizzas:
 print(pizza)
#
print("My friends favorite pizzas are: ")
for pizza in friends_pizzas:
    print(pizza)


#Extra Tasks
#task1
movies = ['harry', 'twilight', 'joker', 'agazada', 'umaribnhattob']
print(movies[0])
print(movies[-1:])
middle_index = len(movies) // 2
print(movies[middle_index])
#task2
cars =['toyota', 'mers', 'cobalt']
cars[1] ='hyundai'
cars.append('audi')
cars.insert(0, 'matiz')
print(cars)

#task3
cars.remove('cobalt')
print(cars)
print(cars.pop())
del cars[0]
print(cars)


#task4
names =  ['jalol', 'qodir', 'muslim', 'salim', 'laziz']

names.sort()
print(names)
print(sorted(names))
names.reverse()
print(names)
print(len(names))

countries =['malaysia', 'france', 'germany', 'usa']

#task5
for country in countries:
    print(country.upper())

#task6
numbers = [1,2,3,4,5,6,7,8]
print(numbers[:3])
print(numbers[-3:])
number_middle = len (numbers) // 2
print(number_middle)
print(numbers[0:8])

#task7
numbers = [value**2 for value in range(1,11)]
print(numbers)
numbers = [values for values in range(1,11)]
print(numbers[1:11:2])

#task8
numbers =list(range(1,21))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


#task9
fruits = ['apple', 'pear', 'banana', 'grape']
print('apple' in fruits)
print('mango' in fruits)

team =[
    ['Alice', 'Bob', 'Charlie'],
    ['David', 'Emil', 'Frank'],
    ['grace', 'hank', 'ivy']
]

print(team[1][1])

animals =['bear', 'parrot', 'rabbit', 'wolf', 'fox']
print(animals[0])
print(animals[-1:])
middle_animal =len(animals) // 2
print(animals [middle_animal])

fruits = ['banana', 'apple', 'melon']
fruits[1] = 'mango'
print(fruits)

colors =['black', 'white', 'blue',  'yellow']
del colors[0]
colors.remove('blue')
print(colors)

numbers = list(range(1,11))
print(numbers[:4])
print(numbers[-3:])
numbersss = numbers[:]
print(numbersss)
print(numbers[::2]) #har 2chi sonni yoki valueni chiqarib beradi


cities = ['tashkent', 'london', 'moscow', 'new york', 'riyad']
for city in cities:
    print('I want to visit ', city.title())

cubes = [value**3 for value in range(1,11)]
print(cubes)
divisble = [value for value in range(1, 30)
            if value % 3 == 0]
print(divisble)

randoms = [14,534, 5,32,50,34, 98]
print(min(randoms))
print(max(randoms))
print(sum(randoms))
print(len(randoms))

program_lang = ['python', 'java', 'css', 'c++', 'javascript']
language = input('Please,, input your preffered language ')
if language.lower() in program_lang: #here we can add formatting
    print('Acceptable')
else:
    print('Not acceptable')


students =[
    ['Bill', 'Julie', 'Ann', 'Sam'],
    ['Ron', 'Romeo', 'Emma', 'Salim'],
    ['Melanie', 'Molly', 'Sarah', 'George']
]

print(students[1])
print(students[0][2])
for student in students:
    print(student)

numbers = list(range(1,11))
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
print(max(even_numbers))
print(min(even_numbers))
print(sum(even_numbers))
middle = len(even_numbers)//2
print(even_numbers[middle])

#Extra Tasks End

#Tasks End

# Lists Lesson End


#Tuples

dimensions = (200, 50)
print(dimensions[0])
dimensions[0] = 300
print(dimensions[0]) # we cannot make any changes on tuple and in this case python gives error

#Looping Through All Values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# #Looping Through All Values in a Tuple End

#Writing over a Tuple
dimensions = (200, 50)
print('Original Dimensions: ')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 50, 40)
print("\nModified Dimensions: ")
for dimension in dimensions:
    print(dimension)

#Writing over a Tuple End

#Tasks

foods = ('bulochka', 'Sosiska', 'somsa', 'bilinchik', 'shashlik')
for food in foods:
    print(food)
foods[2]= 'semechka'
foods = ('saryog"', 'tort', 'somsa', 'bilinchik', 'shashlik')
for food in foods:
    print(food)
#Tasks End

#Tuples End

#Styling Your Code

#Line Length => each line should be less than 80 characters

#Styling Your Code ENd



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

#
# #NEW CHAPTER DICTIONARIES
#
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
#
#
# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print("You just earned " + str(new_points) + " points!")
#
# #Adding New Key-Value Pairs
# user = {'name': "Madina", 'age': "20"}
# print(user)
# user['tg_username'] = '@madina20'
# user['tg_password'] = 'MadinA02'
# print(user)
# #Adding New Key-Value Pairs ENd
#
#
# #Starting with an Empty Dictionary
# alien_0 = {}
# print(alien_0)
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# #Starting with an Empty Dictionary End
#
# #Modifying Values in a Dictionary
# user = {'name': "Madina", 'age': "20"}
# user['name'] = 'Mokhi'
# print(user)
#
#
#
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print("Original x-position: " + str(alien_0['x_position']))
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# alien_0['x_position'] = x_increment+alien_0['x_position']
# print("New x-position: " + str(alien_0['x_position']))
#
# #Modifying Values in a Dictionary  ENd
#
# #Removing Key-Value Pairs
# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# del alien_0['x_position']
# print(alien_0)
#
# #NOTE!!!! Be aware that the deleted key-value pair is removed permanently.
#
# #Removing Key-Value Pairs End
#
# #A Dictionary of Similar Objects
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# print(favorite_languages)
# print(f"Sarah's favorite languages is: {favorite_languages['sarah'].title()}")
# print(f"Edward's favorite languages is: {favorite_languages['edward'].title()}")
#
# #A Dictionary of Similar Objects END
#
# #Task
#
# person = {'first name': 'Mokhi', 'last name': 'Usman', 'age': 22, 'city': 'Tashkent' }
# print(f"{person['first name']}'s last name is {person['last name']}, and her age is {person['age']}, so she lives in {person['city']}")
#
#
# fav_numbers = {'molly': 7, 'david': 10, 'zara': 8, 'emily':9, 'bell':4}
# for name, number in fav_numbers.items():
#     print(f"{name}'s favorite number is {number}")
#
# glossary = {
#     'if':'is condition',
#     'for':'it is used for loop',
#     'range':'is used to count in range',
#     'else':'if the 1st condition doesn\'t work, program runs else condition',
#     'list':'lists are mutable'
# }
#
# print(f"if \n{glossary['if']}")
# print(f"for \n{glossary['for']}")
# print(f"range \n{glossary['range']}")
# print(f"else - \n{glossary['else']}")
# print(f"list - \n{glossary['list']}")
#
# #Task end
#
# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
# user_0 = {
#  'username': 'efermi',
#  'first': 'enrico',
#  'last': 'fermi',
#  }
#
# for key in user_0.keys():
#     print(key)
# for key, value in user_0.items():
#     print(key, value)
# for value in user_0.values():
#     print(value)
#
# for k,v in user_0.items():
#     print(f"Key: {k} \nValue: {v}\n\n")
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# for name, language in favorite_languages.items():
#     print(f"{name.title()} loves {language.title()}\n")
#
# #Looping Through All Key-Value Pairs End
#
# #Looping Through All the Keys in a Dictionary
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# for name in favorite_languages.keys():
#  print(name.title())
#
#
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(f"Hi, {name.title()}! I see your favorite language is {favorite_languages[name]}.")
# if 'erin' not in favorite_languages.keys():
#     print('Erin, please take our poll')
# #Looping Through All the Keys in a Dictionary End
#
#
# #Looping Through a Dictionary’s Keys in Order
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
#
# for name in sorted(favorite_languages.keys()):
#     print(f"Thank you for taking the poll, {name.title()}!")
#
# #Looping Through a Dictionary’s Keys in Order End
#
# #Looping Through All Values in a Dictionary
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
#  }
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()): #set() => A set is similar to a list except that each item in the set must be unique
#     print(language.title())
#
# #Looping Through All Values in a Dictionary End
#
# #Task
#
# glossary = {
#     'if':'is condition',
#     'for':'is used for loop',
#     'range':'is used to count in range',
#     'else':'if the 1st condition doesn\'t work, program runs else condition',
#     'list':'lists are mutable',
#     'or': 'is another condition we can give when using if statement',
#     'elif': 'is used whenever you want to include mutiple conditions on your if statement',
#     'variable': ' is the kind a box where you can store your items'
# }
#
# for key, value in glossary.items():
#  print(key, value)
#
# rivers = {
#      'Danube': 'Germany',
#      'Nile':'Austria',
#      'Mekong': 'China'
# }
#
# for key, value in rivers.items():
#  print(f"{key} runs through {value.upper()}. ")
#
# for key in rivers.keys():
#  print(key)
# for value in rivers.values():
#  print(value)
#
# favorite_languages = {
#  'jen': 'python',
#  'sarah': 'c',
#  'edward': 'ruby',
#  'phil': 'python',
# }
#
# required_person = ['sarah', 'edward', 'mokhi', 'mumtoza']
#
# for person in required_person:
#  if person in favorite_languages:
#   print(f"Thank you for joining in {person}")
#  else:
#   print(f'Please take the poll, {person}')
#
#
# #Additional tasks
#
# person = {
#  'first_name': 'mokhi',
#  'last_name': 'usman',
#  'age': '22',
#  'city': 'tashkent'
# }
#
# for key, value in person.items():
#  print(f"{key}: {value}")
#
#
# statistics = {
#  'jhonny':'marvel',
#  'clara' : 'spiderman',
#  'phiona':'cinderella',
#  'mark':'five stars',
#  'anna': 'titanic',
# }
#
# for key, value in statistics.items():
#  print(f"{key.title()} loves to watch {value.title()}")
#
# preffered_person = ['clara', 'melanie', 'mark']
#
# for person in preffered_person:
#  if person in statistics:
#   print(f"We know your favorite movie!")
#  else:
#   print(f"Tell us your favorite movie!")
#
#
# capitals = {
#  'uzbekistan':'tashkent',
#  'france':'paris',
#  'germany':'berlin',
#  'russia':'moscow',
#  'italy':'rome'
# }
#
# for key, value in capitals.items():
#  print(f"{value.title()} is the capital of {key.title()}.")
#
# for key in capitals.keys():
#  print(key.title())
#
# for value in capitals.values():
#  print(value.title())
#
# country_name = input('Please type your country name: ')
#
# if country_name in capitals:
#   print(f"{country_name.title()}'s capital is {capitals[country_name].title()}.")
# else:
#  print("Country not found!")
#
#
# reyting = {
#  'madina': 99,
#  'aziza': 87,
#  'davron': 69,
#  'ziyoda': 75,
#  'tangem': 100
# }
#
# for name, grade in reyting.items():
#  print(f"{name.title()}'s grade is {str(grade)}")
# for name, grade in reyting.items():
#  if grade > 90:
#   print(f"{name.title()} is the best student.")
#  elif 70 < grade > 90:
#   print(f"{name.title()} is the normal student.")
#  else:
#   print(f"{name.title()} is the worst student.")
#
#
# print(max(reyting.values()))
# print(min(reyting.values()))
#
# words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
#
# words_count ={}
#
# for word in words:
#  if word in words_count:
#   words_count[word] += 1
#  else:
#   words_count[word] = 1
#
# for word, count in words_count.items():
#  print(f"{word}: {count}")
# #Additional tasks End
# #Task End
# #Looping Through a Dictionary End
#
# #Nesting
#
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
# print(aliens)
#
#
# student_01 ={
#  'name': 'Jack',
#  'age': 23,
#  'city': 'paris'
# }
#
# student_02 ={
#  'name': 'sarah',
#  'age': 18,
#  'city': 'paris'
# }
#
# student_03 ={
#  'name': 'monica',
#  'age': 27,
#  'city': 'paris'
# }
#
# students =[student_01, student_02, student_03]
# print(students)
#
# new_students =[]
# for newstudent in range(30):
#  news_student = {'name':'Ron', 'age': 25, 'city':'tashkent'}
#  new_students.append(news_student)
#  print(new_students)
#
# for student in new_students[:4]:
#  print(student)
#
# print(f'Total number of aliens: {str(len(new_students))}')
#
#
# aliens = []
# # Make 30 green aliens.
# for alien_number in range (0,30):
#  new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#  aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#  if alien['color'] == 'green':
#   alien['color'] = 'yellow'
#   alien['speed'] = 'medium'
#   alien['points'] = 10
#
# for alien in aliens[0:3]:
#  print(alien)
#
# for alien in aliens:
#  if alien['color'] == 'green':
#   alien['speed'] = 'medium'
#   alien['points'] = 10
#  elif alien['color'] == 'yellow':
#   alien['speed'] = 'fast'
#   alien['points'] = 15
# for alien in aliens:
#   print(alien)
# #Nesting End
#
# #A List in a Dictionary
#
# # Store information about a pizza being ordered.
# pizza = {
#  'crust': 'thick',
#  'toppings': ['mushrooms', 'extra cheese'],
#  }
# print(f'You ordered {pizza['crust']} pizza with the following toppings:')
# for topping in pizza['toppings']:
#  print(topping)
#
# favorite_languages = {
#  'jen': ['python', 'ruby'],
#  'sarah': ['c'],
#  'edward': ['ruby', 'go'],
#  'phil': ['python', 'haskell']
# }
#
# for name, language in favorite_languages.items():
#  if len(language) <=1:
#   print(f'{name.title()} loves to learn this type of coding language: {",".join(language)}') #Use ', '.join() to remove brackets!
#  else:
#   print(f'{name.title()} loves to learn these types of coding languages: {",".join(language)}') #Use ', '.join() to remove brackets!
#
# for name, languages in favorite_languages.items():
#  print(f"{name.title()}'s favorite language are:")
#  for language in languages:
#   print(language)
#
# #A List in a Dictionary End
#
# #A Dictionary in a Dictionary
#
# users = {
#  'aeinstein': {
#  'first': 'albert',
#  'last': 'einstein',
#  'location': 'princeton',
#  },
#   'mcurie': {
#   'first': 'marie',
#   'last': 'curie',
#   'location': 'paris',
#   },
# }
#
# for username, user_info in users.items():
#  print(f'\nUsername: {username}')
#  full_name = user_info['first'] + ' ' + user_info['last']
#  user_location = user_info['location']
#
#  print("Full name:" + full_name.title())
#  print("User location:" + user_location.title())
#
# #A Dictionary in a Dictionary End
#
# #Task
# mokhi = {
#  'first name': 'Mokhi',
#  'last name': 'Usman',
#  'age': 22,
#  'city': 'tashkent'
# }
#
# daddy = {
#  'first name': 'dilshod',
#  'last name': 'Usmon',
#  'age': 49,
#  'city': 'kokand'
# }
#
# mommy = {
# 'first name': 'zumrad',
#  'last name': 'usmnva',
#  'age': 45,
#  'city': 'beshariq'
# }
# people = [mommy, daddy, mokhi]
# for person in people:
#   print(f"\nFirst Name: {person['first name'].title()}")
#   print(f"Last Name: {person['last name'].title()}")
#   print(f"Age: {person['age']}")
#   print(f"City: {person['city'].title()}")
#
#
#
# daisy = {
#  "name": 'daisy',
#  "kind": 'dog',
#  'owner': 'Mark'
# }
#
# chloe = {
# "name": 'chloe',
#  "kind": 'cat',
#  'owner': 'Mira'
# }
#
# pets = [daisy, chloe]
# for pet in pets:
#  print(f"\n{pet['name'].title()} is {pet['owner'].title()}'s {pet['kind']}.")
#
#
# favorite_places = {
#  'abdulloh': ['london'],
#  'lola': ['iowa', 'montana', ],
#  'bahrom': ['navoiy', 'samarkand', 'andijan']
# }
#
# for person, places in favorite_places.items():
#  print(f"\nWhat's your favorite place {person.title()}?")
#  if len(places) == 1:
#     print(f"{person.title()}'s favorite place is {",".join(places).title()} ")
#  else:
#    print(f"{person.title()}'s favorite place are: {",".join(places).title()} ")
#
#
# people = {
#  'marie': [24, 45, 87],
#  'doston': [4, 15, 54],
#  'toxir': [76, 42, 78]
# }
#
# for person, numbers in people.items():
#   print(f"{person.title()}'s favorite numbers are:")
#   for number in numbers:
#    print(number)
#
#
# for person, numbers in people.items():
#   print(f"{person.title()}'s favorite numbers are: {','.join(str(number) for number in numbers)}")
#
#
#
#
# cities = {
#  'madina': {
#  'population': "10,000",
#  'country' : 'saudiaA',
#  'fact':'sakiynat'
#  },
#  'mecca':{
#  'population': "20,000",
#  'country' : 'saudiaa',
#  'fact':'core of islam'
#  },
#  'jiddah': {
# 'population': "15,000",
#  'country' : 'Ssaudia',
#  'fact':'modern'
#  }
# }
#
#
# for city, details in cities.items():
#  print(city.title() + ":")
#  print(f"Population: {details['population']}, Country: {details['country']}, Fact: {details['fact']}")
#
# #Task End
#
# #NEW CHAPTER DICTIONARIES END


#======================================

#NEW CHAPTER USER INPUT AND WHILE LOOPS

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt) #WE CAN INSERT PROMT IN A VARIABLE AND USE IT AS AN INPUT
print("\nHello, " + name + "!")


#Using int() to Accept Numerical Input

height = input('How tall you are (inches)? ')
height = int(height)
if height > 100:
 print("You can ride a roller coaster!")
else:
 print("You cannot ride a roller coaster!")

#Using int() to Accept Numerical Input END


#The Modulo Operator

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print(f"Your number {number} is even!")
else:
 print(f"Your number {number} is odd!")

#The Modulo Operator end

#Task

car = input("What kind of rental car you would like to get? ")
car = car.title()
print(f"Let me see if I can find you a {car}...")


people = input("Please tell me, how many people are in your dinner group? ")
people = int(people)
if people > 8:
 print("You will have to wait for a table!")
else:
 print("Your table is ready!")

number = input("Tell me the number and I'll tell you if this number is multiple of 10: ")
number = int(number)
if number % 10 == 0:
 print(f"Your number {number} is multiple of 10")
else:
 print(f"Your number {number} is not multiple of 10")

#Task End


#Introducing while Loops

current_number = 1
while current_number <= 5:
 print(current_number)
 current_number += 1

#Letting the User Choose When to Quit:

prompt = "\nTell me something, and I wil repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
 message = input(prompt)
 print(message)
 if message == 'quit':
  print(f"{message.title()}ed!")

#Letting the User Choose When to Quit End

#Using a Flag

prompt = "\nTell me something, and I wil repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "
active = True
message = ""
while active:
 message = input(prompt)
 if message == "quit":
  active = False
 else:
  print(message)

#Using a Flag End

#Using break to Exit a Loop

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
 city = input(prompt)

 if city == 'quit':
  break
 else:
  print("I'd love to go to " + city.title() + "!")

#Using break to Exit a Loop End

current_number = 0
while current_number < 10:
 current_number += 1
 if current_number % 2 == 0:
  continue
 print(current_number)

#continue  # skip THIS round, keep going ⏭️
#continue means skip everything below and
#go back to the top of the loop immediately!
#break     # stop the loop completely 🛑


#Avoiding Infinite Loops

x = 1
while x <= 5:
    x += 1
    print(x)



#Avoiding Infinite Loops ENd


#Task

prompt = ("Please enter your favorite topping and I will add to the pizza: ")
prompt += ("\nPlease enter 'quit to complete the pizza! ")

topping = prompt
while topping != "quit":
 topping = input(prompt)
 if topping == "quit":
  print(f"{topping.title()} is added to your pizza !")

print("Your pizza is complete!")



while True:
 age = input("What is your age? ")
 if age == "Over":
  break
 age = int(age)
 if age <= 3:
  print("The ticket is free")
 elif 3 < age <= 12:
  print("The ticket is $10")
 else:
  print("The ticket is $15")


#Step by step explanation:

# while True — loops forever until we explicitly say stop. No condition to check upfront.
# age = input(...) — we get the input as a string first, before doing anything to it.
# if age == "Over": break — we check the string before converting. If the user typed "Over", we exit the loop immediately. This is the key fix — in your version, you converted first, making this check impossible.
# age = int(age) — only after confirming it's not "Over", we safely convert to integer.
# The if/elif/else — handles the three price cases. Notice 3 < age <= 12 (not 3 <= age <= 12) to avoid overlap with the first condition.


#Task End


#Additional tasks

prompt = ('Please enter your favorite movie name (q to quit): ')
movie = ""
while movie != 'quit':
 movie = input(prompt)
 if movie != 'quit':
  print(f"Great choice! Adding {movie} to watchlist")

print('Your watchlist is ready!')


prompt = ("Please enter an item to buy (q to quit): ")
item = ""
items_list = []
while item != 'q':
 item = input(prompt)
 if item != 'q':
  items_list.append(item)
  print(f'{item.title()} is added to your shopping list!')

print(f"{",".join(items_list).title()} are added to your shopping list!")

prompt = ("Please enter a number (stop to quit): ")
number = ""
number_list = []
while number != "stop":
 number = input(prompt)
 if number != "stop":
  number_list.append(int(number))
  print(f"Your number is {number}")
print(f"Your numbers are {",".join(str(n) for n in number_list)}")

print(sum(number_list))
print(max(number_list))

counter = 0

while counter != 3:
 number = input('Enter a number: ')
 number = int(number)
 counter =+ 1
 if number % 2 == 0:
  print(f"Your number {number} is even.")
 else:
  print(f"Your {number} is odd.")




while True:
 guess_number = input("Guess the number: ")
 guess_number = int(guess_number)

 if guess_number == 7:
  print("You win!")
  break
 else:
  print("False, your number is not correct.")


while True:
 positive_number = input("Enter a positive number: ")
 positive_number = int(positive_number)
 if positive_number >= 0:
    print(positive_number**2)
    break
 else:
  print("Invalid!")

words = []
while True:
 word = input("Enter a word: ")
 if word != "stop":
  words.append(word)
 else:
  break
print(words)

numbers = []
while True:
 number = input('Enter a number: ')
 if number == 'done':
  break
 else:
  numbers.append(int(number))

sum_num = sum(numbers)
print(sum_num)
ave_num = sum_num // len(numbers)
print(ave_num)

numbers = []
while True:
 number = input('Enter a number: ')
 if number == "done":
  break
 else:
  numbers.append(int(number))
print(max(numbers))
print(min(numbers))

while True:
 password = input("Please create a password: ")
 if len(password) < 8:
  print("Password is too short, try again!")
 else:
  print("Password accepted!")
  break


numbers = []
while True:
 number = input('Enter a number: ')
 if number == "stop":
  break
 else:
  numbers.append(int(number))
for number in numbers:
 if number % 2 == 0:
  print(number)

previous = None
while True:
 number = input('Enter a number: ')
 number = int(number)
 if number == previous :
  print("Duplicate!")
  break
 else:
  previous = number

count = 0
positives = []
negatives = []
zeros = []
while count < 5:
 count += 1
 number = input("Enter a number: ")
 number = int(number)
 if number < 0:
  negatives.append(number)
 elif number > 0:
  positives.append(number)
 elif number == 0:
  zeros.append(number)

print(len(positives))
print(len(negatives))
print(len(zeros))


while True:
 word = input("Enter a word: ")
 if word == "quit":
  break
 else:
  print(word[::-1])

odd_numbers = []
even_numbers = []
count = 0
while count < 10:
 number = input('Enter a number: ')
 number = int(number)
 count += 1
 if number % 2 == 0:
  even_numbers.append(number)
 else:
  odd_numbers.append(number)


print(len(odd_numbers))
print(len(even_numbers))

while True:
 number = input('Enter a number: ')
 number = int(number)
 for i in range(1,11):
  print(f"{number} x {i} = {number*i}")

words = []
while True:
 word = input("Enter a word: ")
 if word == "stop":
  break
 else:
  print(word)
  words.append(word)

print(max(words, key=len))

max(words, key=len)   # longest word
min(words, key=len)   # shortest word
sorted(words, key=len) # sort by length

numbers = []
while True:
  number = input('Enter a number: ')
  if number == 'done':
   break
  else:
   print(number)
   numbers.append(int(number))

sum_number = sum(numbers)
len_number = len(numbers)
average = sum_number / len_number
count = 0

for number in numbers:
 if number > average:
  count = count + 1
print(count)

while True:
 age = input("What is your age? ")
 age = int(age)
 if age < 3:
  print("Ticket is free")
 elif  3 <= age < 12:
   print("Ticket is $10")
 else:
  print("Ticket is $15")

#Additional tasks end

#Introducing while Loops End

#Using a while Loop with Lists and Dictionaries
#Moving Items from One List to Another

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user:", current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

waiting_students = ["Anna", 'Ben', 'Carol']
seated_students = []
while waiting_students:
    seated_student = waiting_students.pop()
    seated_students.append(seated_student)
    print(f" {seated_student} sat down")

list_of_orders = ['pizza', 'burger', 'pasta', 'sushi']
completed_orders = []
while list_of_orders:
    serving_order = list_of_orders.pop()
    print("Now serving:" + serving_order)
    completed_orders.append(serving_order)
print(f"Here are the list of completed orders: {', '.join(completed_orders)}")

dirty_dishes = ['plate', 'cup', 'pan', 'bowl']
clean_dishes = []
while dirty_dishes:
    cleaned_dish = dirty_dishes.pop()
    print(f"Cleaning: {cleaned_dish}")
    clean_dishes.append(cleaned_dish)

print(f"Here are the cleaned dishes: {", ".join(clean_dishes)}")

waiting_passengers = ['alice', 'bob', 'charlie', 'diana', 'eve']
boarded_passengers = []
while waiting_passengers and len(boarded_passengers) < 3:
    boarding = waiting_passengers.pop()
    boarded_passengers.append(boarding.title())
print(f"Here are the remaining passenger: {', '.join(waiting_passengers).title()}")

#Moving Items from One List to Another End

#Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
 pets.remove('cat')

print(pets)

numbers = [1, 2, 3, 2, 4, 2, 5]
while 2 in numbers:
    numbers.remove(2)
print(numbers)

words = ['apple', 'banana', 'apple', 'cherry', 'apple']
while "apple" in words:
    words.remove('apple')

print(words)

responses = ['yes', 'no', 'yes', 'maybe', 'no', 'yes']
while 'no' in responses:
    responses.remove('no')
while 'maybe' in responses:
    responses.remove('maybe')
print(responses)

votes = ['alice', 'bob', 'alice', 'charlie', 'bob', 'alice']
while 'alice' in votes:
    votes.remove('alice')
print(f"Here is the list of remaining votes: {', '.join(votes).title()} and the number of votes: {len(votes)}")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers[:]:
   if number % 2 == 0:
        numbers.remove(number)

print(f"Odd numbers:")
for number in numbers:
    print(number)
#Removing All Instances of Specific Values from a List End


#Filling a Dictionary with User Input

responses = {}
polling_active = True

while polling_active:
 # Prompt for the person's name and response.
  name = input("\nWhat is your name? ")
  response = input("Which mountain would you like to climb someday? ")
 # Store the response in the dictionary:
  responses[name] = response
 # Find out if anyone else is going to take the poll.
  repeat = input("Would you like to let another person respond? (yes/ no) ")
  if repeat == 'no':
    polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
 print(name.title() + " would like to climb " + response.title() + ".")


users = {}
polling_status = True
while polling_status:
    full_name = input("Please enter your name: ")
    color = input("Please enter your favorite color: ")
    users[full_name] = color
    choice = input("Do you want to continue? ")
    if choice == "no":
        polling_status = False

for name , color in users.items():
    print(f"{name.title()} loves this color: {color.title()}")


users = {}
polling_status = True
while polling_status:
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    users[name] = int(age)
    choice = input("Do you want other to continue: ")
    if choice == 'no':
        polling_status = False
for name, age in users.items():
    print(f"{name.title()} is {age} years old")
print(f"{max(users, key=users.get).title()} is the oldest")

max(users, key=users.get)  # find key with highest value
#Just like key=len measures by length, key=users.get measures by dictionary value!

phonebook = {}
polling_status = True
while polling_status:
    name = input("Please enter your name: ")
    phone = input("Please enter your phone number: ")
    phonebook[name] = phone
    finish = input("The status of addition: ")
    if finish == "done":
        polling_status = False
search = input("Please enter your preffered name of your contact: ")
if search in phonebook.keys():
    print(phonebook[search])
else:
    print("Contact not found!")


users ={}
polling_status = True
while polling_status:
    name = input("Please enter your name: ")
    food = input("Please enter your favorite food: ")
    users[name] = food
    question = input("Do you want to continue?  ")
    if question == "no":
        polling_status = False

for name, food in users.items():
    if food == "pizza":
        print(f"{name.title()} loves a pizza")


gradebook = {}
polling_status = True
while polling_status:
    name = input("Please enter your name: ")
    grade = input("Please enter your grade: ")
    gradebook[name] = int(grade)
    status = input("Please enter your status: ")
    if status == 'done':
        polling_status = False
for name, grade in gradebook.items():
    if grade >= 60:
        print(f"{name.title()} scored {grade} and passed!")
    else:
        print(f"{name.title()} scored {grade} and failed!")
#Filling a Dictionary with User Input End

#Task
sandwich_orders = ['Vietnamese Bánh Mì', 'Italian Panuozzo', 'Cuban', 'Tuna']
finished_sandwiches = []
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)
print(f"Made sandwiches: {", ".join(finished_sandwiches)}.")


sandwich_orders = ['Vietnamese Bánh Mì','pastrami', 'Italian Panuozzo', 'pastrami', 'Cuban', 'Tuna', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
print("Deli has run out of pastrami")

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)

users = {}
polling_status = True
while polling_status:
    name = input("Please enter your name: ")
    fav_place = input("If you could visit one place in the world, where would you go? ")
    users[name] = fav_place
    finish = input("Do you want to finish? (y/n) ")
    if finish == "y":
        polling_status = False
for name, place in users.items():
    print(f"{name.title()} would go to {place.title()}!")

#Task end
#Using a while Loop with Lists and Dictionaries End
#NEW CHAPTER USER INPUT AND WHILE LOOPS END


#NEW CHAPTER FUNCTIONS

def greet_user():
 """Display a simple greeting."""
 print("Hello!")

greet_user()


#Passing Information to a Function
def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")

greet_user('jesse')


#Passing Information to a Function END
# task
def display_message():
    """Display a simple message."""
    print("I'm learning how to work with functions and what are the rules of using function method in python.")

display_message()

def favorite_book(title):
    print("One of my favorite books is:",title,".")

favorite_book("Alice in Wonderland")
#task end
#Positional Arguments

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

#Positional Arguments end

#Multiple Function Calls

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

#Multiple Function Calls End

#Keyword Arguments

def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(animal_type='hamster', pet_name='harry')

#Keyword Arguments End

#Default Values

def describe_pet(pet_name, animal_type='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')
Default Values End

#task

def make_shirt(size, text):
    print(f"\nThe size of shirt is {size} and {text}.")

make_shirt('small', 'the most modern one in our shop.')

make_shirt(size = 'medium', text ='I think this mathches for you!')



def make_shirt(size = "large", text = "I love Python"):
    print(f"\nThe size of shirt is {size} and {text}")
make_shirt()
make_shirt('medium')
make_shirt('small', 'I love coding!')

def describe_city(city, country= "Iceland"):
    print(f"\n {city} is in {country}")
describe_city(city="Paris")
describe_city(city="Tashkent")
describe_city(city="London", country="Great Britain")

def make_album(artist_name, album_name):
    album = {'artist': artist_name, "album" :album_name}
    return album
result = make_album( artist_name='Micheal', album_name= 'Sunrise')
print(result)

#task end

#Return Values

def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
#Return Values End

#Making an Argument Optional
def get_formatted_name(first_name, last_name, middle_name=''):
 """Return a full name, neatly formatted."""
 if middle_name:
  full_name = first_name + ' ' + middle_name + ' ' + last_name
 else:
  full_name = first_name + ' ' + last_name
 return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

#Making an Argument Optional end

#Returning a Dictionary
def build_person(first_name, last_name):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
 """Return a dictionary of information about a person."""
 person = {'first': first_name, 'last': last_name}
 if age:
  person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#Returning a Dictionary End

#Using a Function with a while Loop
def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
# This is an infinite loop!
while True:
 print("\nPlease tell me your name:")
 f_name = input("First name: ")
 l_name = input("Last name: ")

 formatted_name = get_formatted_name(f_name, l_name)
 print("\nHello, " + formatted_name + "!")
 option = input("Would you like to play again? (y/n): ")
 if option == "n":
     break
 else:
     continue
print("Thank you for playing!")

# #2nd option:

def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = first_name + ' ' + last_name
 return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
     break
    l_name = input("Last name: ")
    if l_name == 'q':
       break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

#Using a Function with a while Loop end

#TASK

def city_country(city, country):
    return f"{city}, {country}"


print(city_country("Tashkent", 'Uzbekistan'))
print(city_country("London", 'Great Britain'))
print(city_country("Paris", 'France'))

def make_album (artist, album_title):
    album = {"artist_name": artist, "album_title": album_title}
    return album
print(make_album("Yulduz", "Baxtli kunlar"))
print(make_album("Beiber", "Sunshine"))
print(make_album("Dossary", "Quran"))

def make_album (artist, album_title, tracks = None):
    album = {"artist_name": artist, "album_title": album_title}
    if tracks:
        album["tracks"] = tracks
    return album


print(make_album("Yulduz", "Baxtli kunlar", 24))
print(make_album("Beiber", "Sunshine"))
print(make_album("Dossary", "Quran"))

def make_album (artist, album_title):
    album = {'artist_name': artist, 'title': album_title}
    return album
while True:
    artist = input('Enter artist name: ')
    album_title = input('Enter album title: ')
    print(make_album(artist.title(), album_title.title()))
    option = input('Do you want to add another album? (y/n): ')
    if option == 'n':
        break
    else:
        continue
print("Thank you for playing!")

def make_person(name,age):
    user = {"name_of":name,"age_is":age}
    return user
list_of_users = []
while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    info = make_person(name,age)
    list_of_users.append(info)
    # print(make_person(name,age))
    option = input("Type quit to quit the game: ")
    if option == "quit":
        break
print(list_of_users)

def describe_pet(pet_name, animal_type):
    return f"I have a {animal_type} named {pet_name}"
while True:
    animal_type = input("Insert your animal type: ")
    pet_name = input("Insert your pet name: ")
    print(describe_pet(pet_name.title(), animal_type))
    option = input("To end the game type 'quit' ")
    if option == 'quit':
        break


def make_student(name, grade):
    student = {'name_of': name, 'grade_is': grade}
    return student

students = []
grades = []
while True:
    name = input('Enter your name: ')
    grade = input('Enter your grade: ')
    grade = int(grade)
    students.append(name)
    grades.append(grade)
    option = input("To end the game type 'quit' ")
    if option == 'quit':
        break

def full_name(first, last):
    return f"{first} {last}"

print(full_name('Madina', 'Sayyidova'))
print(full_name('Mumtoza', 'Muhammadali'))
print(full_name('Sora', 'Azizova'))



def make_pet(animal_type, name, age = None):
   animal = {"type_of": animal_type, "name_of": name}
   if age is not None:
       animal["age_of"] = age
   return animal
print(make_pet('dog', 'ben', '10'))
print(make_pet('dog', 'ben'))
print(make_pet('dog', 'ben', 4))


def make_shirt(size, message):
    return f"A {size} shirt that says: {message}"
print(make_shirt('medium', 'Just Do It'))


def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info
print(build_profile('Madina', 'Sardorova', age =18, grade=87, job ='engineer'))
print(build_profile('Jasur', 'Toshqondiy', married ='no', childeren = '8'))



def fav_food_user(name, list_foods):
    return f"{name.title()}'s favorite foods are: {','.join(list_foods)}."
print(fav_food_user('Ali', ['tacos', 'pizza', 'sushi']))


def fav_food_user(name, list_foods):
    foods = list_foods[:]  # makes a copy — original stays safe
    return f"{name.title()}'s favorite foods are: {', '.join(foods)}."

foods = ['tacos', 'pizza', 'sushi']
print(fav_food_user('Ali', foods))
print(foods)  # still unchanged


def show_magicians(name_list):
        for name in name_list:
         return name_list



names = ['ALice', 'Bob', 'Bell']
print(show_magicians(names))

def make_great(message, names_of = names):
    for name in names:
     return f"{name}: {message}"
print(make_great('The great!'))

#TASK END

#NEW CHAPTER FUNCTIONS END

#
# import random
#
# print(random.randrange(14, 21))
#
# message = "I love my zavj, zavj, zavj"
# print(message.count("zavj"))

# name = ""
# print(bool(name))