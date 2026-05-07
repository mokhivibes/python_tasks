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

Changing, adding, and removing elements in a list
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
