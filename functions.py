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
# Default Values End

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
musician = build_person('jimi', 'hendrix', age =27)
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
