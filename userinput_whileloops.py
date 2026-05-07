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
