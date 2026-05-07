
#NEW CHAPTER DICTIONARIES

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])


alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

#Adding New Key-Value Pairs
user = {'name': "Madina", 'age': "20"}
print(user)
user['tg_username'] = '@madina20'
user['tg_password'] = 'MadinA02'
print(user)
#Adding New Key-Value Pairs ENd


#Starting with an Empty Dictionary
alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#Starting with an Empty Dictionary End

#Modifying Values in a Dictionary
user = {'name': "Madina", 'age': "20"}
user['name'] = 'Mokhi'
print(user)



alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = x_increment+alien_0['x_position']
print("New x-position: " + str(alien_0['x_position']))

#Modifying Values in a Dictionary  ENd

#Removing Key-Value Pairs
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
del alien_0['x_position']
print(alien_0)

#NOTE!!!! Be aware that the deleted key-value pair is removed permanently.

#Removing Key-Value Pairs End

#A Dictionary of Similar Objects

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print(favorite_languages)
print(f"Sarah's favorite languages is: {favorite_languages['sarah'].title()}")
print(f"Edward's favorite languages is: {favorite_languages['edward'].title()}")

#A Dictionary of Similar Objects END

#Task

person = {'first name': 'Mokhi', 'last name': 'Usman', 'age': 22, 'city': 'Tashkent' }
print(f"{person['first name']}'s last name is {person['last name']}, and her age is {person['age']}, so she lives in {person['city']}")


fav_numbers = {'molly': 7, 'david': 10, 'zara': 8, 'emily':9, 'bell':4}
for name, number in fav_numbers.items():
    print(f"{name}'s favorite number is {number}")

glossary = {
    'if':'is condition',
    'for':'it is used for loop',
    'range':'is used to count in range',
    'else':'if the 1st condition doesn\'t work, program runs else condition',
    'list':'lists are mutable'
}

print(f"if \n{glossary['if']}")
print(f"for \n{glossary['for']}")
print(f"range \n{glossary['range']}")
print(f"else - \n{glossary['else']}")
print(f"list - \n{glossary['list']}")

#Task end

# Looping Through a Dictionary
# Looping Through All Key-Value Pairs
user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for key in user_0.keys():
    print(key)
for key, value in user_0.items():
    print(key, value)
for value in user_0.values():
    print(value)

for k,v in user_0.items():
    print(f"Key: {k} \nValue: {v}\n\n")

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, language in favorite_languages.items():
    print(f"{name.title()} loves {language.title()}\n")

#Looping Through All Key-Value Pairs End

#Looping Through All the Keys in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in favorite_languages.keys():
 print(name.title())



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Hi, {name.title()}! I see your favorite language is {favorite_languages[name]}.")
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll')
#Looping Through All the Keys in a Dictionary End


#Looping Through a Dictionary’s Keys in Order

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name in sorted(favorite_languages.keys()):
    print(f"Thank you for taking the poll, {name.title()}!")

#Looping Through a Dictionary’s Keys in Order End

#Looping Through All Values in a Dictionary

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #set() => A set is similar to a list except that each item in the set must be unique
    print(language.title())

#Looping Through All Values in a Dictionary End

#Task

glossary = {
    'if':'is condition',
    'for':'is used for loop',
    'range':'is used to count in range',
    'else':'if the 1st condition doesn\'t work, program runs else condition',
    'list':'lists are mutable',
    'or': 'is another condition we can give when using if statement',
    'elif': 'is used whenever you want to include mutiple conditions on your if statement',
    'variable': ' is the kind a box where you can store your items'
}

for key, value in glossary.items():
 print(key, value)

rivers = {
     'Danube': 'Germany',
     'Nile':'Austria',
     'Mekong': 'China'
}

for key, value in rivers.items():
 print(f"{key} runs through {value.upper()}. ")

for key in rivers.keys():
 print(key)
for value in rivers.values():
 print(value)

favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
}

required_person = ['sarah', 'edward', 'mokhi', 'mumtoza']

for person in required_person:
 if person in favorite_languages:
  print(f"Thank you for joining in {person}")
 else:
  print(f'Please take the poll, {person}')


#Additional tasks

person = {
 'first_name': 'mokhi',
 'last_name': 'usman',
 'age': '22',
 'city': 'tashkent'
}

for key, value in person.items():
 print(f"{key}: {value}")


statistics = {
 'jhonny':'marvel',
 'clara' : 'spiderman',
 'phiona':'cinderella',
 'mark':'five stars',
 'anna': 'titanic',
}

for key, value in statistics.items():
 print(f"{key.title()} loves to watch {value.title()}")

preffered_person = ['clara', 'melanie', 'mark']

for person in preffered_person:
 if person in statistics:
  print(f"We know your favorite movie!")
 else:
  print(f"Tell us your favorite movie!")


capitals = {
 'uzbekistan':'tashkent',
 'france':'paris',
 'germany':'berlin',
 'russia':'moscow',
 'italy':'rome'
}

for key, value in capitals.items():
 print(f"{value.title()} is the capital of {key.title()}.")

for key in capitals.keys():
 print(key.title())

for value in capitals.values():
 print(value.title())

country_name = input('Please type your country name: ')

if country_name in capitals:
  print(f"{country_name.title()}'s capital is {capitals[country_name].title()}.")
else:
 print("Country not found!")


reyting = {
 'madina': 99,
 'aziza': 87,
 'davron': 69,
 'ziyoda': 75,
 'tangem': 100
}

for name, grade in reyting.items():
 print(f"{name.title()}'s grade is {str(grade)}")
for name, grade in reyting.items():
 if grade > 90:
  print(f"{name.title()} is the best student.")
 elif 70 < grade > 90:
  print(f"{name.title()} is the normal student.")
 else:
  print(f"{name.title()} is the worst student.")


print(max(reyting.values()))
print(min(reyting.values()))

words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']

words_count ={}

for word in words:
 if word in words_count:
  words_count[word] += 1
 else:
  words_count[word] = 1

for word, count in words_count.items():
 print(f"{word}: {count}")
#Additional tasks End
#Task End
#Looping Through a Dictionary End

#Nesting

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
print(aliens)


student_01 ={
 'name': 'Jack',
 'age': 23,
 'city': 'paris'
}

student_02 ={
 'name': 'sarah',
 'age': 18,
 'city': 'paris'
}

student_03 ={
 'name': 'monica',
 'age': 27,
 'city': 'paris'
}

students =[student_01, student_02, student_03]
print(students)

new_students =[]
for newstudent in range(30):
 news_student = {'name':'Ron', 'age': 25, 'city':'tashkent'}
 new_students.append(news_student)
 print(new_students)

for student in new_students[:4]:
 print(student)

print(f'Total number of aliens: {str(len(new_students))}')


aliens = []
# Make 30 green aliens.
for alien_number in range (0,30):
 new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 aliens.append(new_alien)

for alien in aliens[0:3]:
 if alien['color'] == 'green':
  alien['color'] = 'yellow'
  alien['speed'] = 'medium'
  alien['points'] = 10

for alien in aliens[0:3]:
 print(alien)

for alien in aliens:
 if alien['color'] == 'green':
  alien['speed'] = 'medium'
  alien['points'] = 10
 elif alien['color'] == 'yellow':
  alien['speed'] = 'fast'
  alien['points'] = 15
for alien in aliens:
  print(alien)
#Nesting End

#A List in a Dictionary

# Store information about a pizza being ordered.
pizza = {
 'crust': 'thick',
 'toppings': ['mushrooms', 'extra cheese'],
 }
print(f'You ordered {pizza['crust']} pizza with the following toppings:')
for topping in pizza['toppings']:
 print(topping)

favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell']
}

for name, language in favorite_languages.items():
 if len(language) <=1:
  print(f'{name.title()} loves to learn this type of coding language: {",".join(language)}') #Use ', '.join() to remove brackets!
 else:
  print(f'{name.title()} loves to learn these types of coding languages: {",".join(language)}') #Use ', '.join() to remove brackets!

for name, languages in favorite_languages.items():
 print(f"{name.title()}'s favorite language are:")
 for language in languages:
  print(language)

#A List in a Dictionary End

#A Dictionary in a Dictionary

users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
  'mcurie': {
  'first': 'marie',
  'last': 'curie',
  'location': 'paris',
  },
}

for username, user_info in users.items():
 print(f'\nUsername: {username}')
 full_name = user_info['first'] + ' ' + user_info['last']
 user_location = user_info['location']

 print("Full name:" + full_name.title())
 print("User location:" + user_location.title())

#A Dictionary in a Dictionary End

#Task
mokhi = {
 'first name': 'Mokhi',
 'last name': 'Usman',
 'age': 22,
 'city': 'tashkent'
}

daddy = {
 'first name': 'dilshod',
 'last name': 'Usmon',
 'age': 49,
 'city': 'kokand'
}

mommy = {
'first name': 'zumrad',
 'last name': 'usmnva',
 'age': 45,
 'city': 'beshariq'
}
people = [mommy, daddy, mokhi]
for person in people:
  print(f"\nFirst Name: {person['first name'].title()}")
  print(f"Last Name: {person['last name'].title()}")
  print(f"Age: {person['age']}")
  print(f"City: {person['city'].title()}")



daisy = {
 "name": 'daisy',
 "kind": 'dog',
 'owner': 'Mark'
}

chloe = {
"name": 'chloe',
 "kind": 'cat',
 'owner': 'Mira'
}

pets = [daisy, chloe]
for pet in pets:
 print(f"\n{pet['name'].title()} is {pet['owner'].title()}'s {pet['kind']}.")


favorite_places = {
 'abdulloh': ['london'],
 'lola': ['iowa', 'montana', ],
 'bahrom': ['navoiy', 'samarkand', 'andijan']
}

for person, places in favorite_places.items():
 print(f"\nWhat's your favorite place {person.title()}?")
 if len(places) == 1:
    print(f"{person.title()}'s favorite place is {",".join(places).title()} ")
 else:
   print(f"{person.title()}'s favorite place are: {",".join(places).title()} ")


people = {
 'marie': [24, 45, 87],
 'doston': [4, 15, 54],
 'toxir': [76, 42, 78]
}

for person, numbers in people.items():
  print(f"{person.title()}'s favorite numbers are:")
  for number in numbers:
   print(number)


for person, numbers in people.items():
  print(f"{person.title()}'s favorite numbers are: {','.join(str(number) for number in numbers)}")




cities = {
 'madina': {
 'population': "10,000",
 'country' : 'saudiaA',
 'fact':'sakiynat'
 },
 'mecca':{
 'population': "20,000",
 'country' : 'saudiaa',
 'fact':'core of islam'
 },
 'jiddah': {
'population': "15,000",
 'country' : 'Ssaudia',
 'fact':'modern'
 }
}


for city, details in cities.items():
 print(city.title() + ":")
 print(f"Population: {details['population']}, Country: {details['country']}, Fact: {details['fact']}")

#Task End

#NEW CHAPTER DICTIONARIES END