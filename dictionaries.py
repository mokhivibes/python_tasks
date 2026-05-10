#NEW CHAPTER DICTIONARIES
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
# # Looping Through a Dictionary
# # Looping Through All Key-Value Pairs
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
#Additional tasks End
#Task End
#Looping Through a Dictionary End

#Nesting
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
#Nesting End

#A List in a Dictionary

# Store information about a pizza being ordered.
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

#A List in a Dictionary End

#A Dictionary in a Dictionary
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

#A Dictionary in a Dictionary End

#Task
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

#Task End



#SariqDevTasks

# daddy = {'name': 'dilshodbek', 'surname': 'usmonov', 'date of birth': '1977'}
# mummy = {'name': 'zumradxon', 'surname': 'usmonova', 'date of birth': '1981'}
# sister = {'name': 'mumtozabegim', 'surname': 'mukhammadaliyeva', 'date of birth': '2010'}
# print(f"Otamning ismi {daddy['name'].title()}, ularning familiyasi {daddy['surname'].title()} va ular {daddy['date of birth']} da tu'gilgan.")
# print(f"Onamning ismi {mummy['name'].title()}, ularning familiyasi {mummy['surname'].title()} va ular {mummy['date of birth']} da tu'gilgan.")
# print(f"Singlimning ismi {sister['name'].title()}, uni familiyasi {sister['surname'].title()} va u {sister['date of birth']} da tu'gilgan.")

# fav_food = {
#  'daddy': 'napaleon',
#  'mummy': 'norin',
#  'sister' :'fast food',
#  'brother': 'osh',
#  'old_sister': 'somsa'
# }
#
# print(f"Otamning sevimli taomi bu {fav_food['daddy']}")
# print(f"Onamning sevimli taomi bu {fav_food['mummy']}")
# print(f"Katta opamning sevimli taomi bu {fav_food['old_sister']}")


# vocab = {
#  'integer': 'Bu butun sonlar',
#  'float': 'Bu o\'nlik sonlar',
#  'string': 'Bu esa matn',
#  'if': 'Bu biror bir shart'
# }
#
# while True:
#  kalit_soz = input('Kalit so\'z kiriting (chiqish uchun "q" harfini yozing): ')
#  if kalit_soz == 'q':
#   break
#  elif kalit_soz in vocab:
#   print(vocab[kalit_soz])
#  else:
#   print('Bunday so\'z mavjud emas')
# print('Yana kutamiz!')
#
# vocab = {
#  'integer': 'Bu butun sonlar',
#  'float': 'Bu o\'nlik sonlar',
#  'string': 'Bu esa matn',
#  'if': 'Bu biror bir shart',
#  'boolean': 'Mantiqiy qiymat',
#  'max.()': 'Maksimum qiymat',
#  'min.()': 'Minimum qiymat',
#  '.upper()':'Barcha harflarni katta harfga o\'zgartiradi',
#  '.capitalize()':'So\'zlarni bosh haqrfini katta harflargaa o\'zgartiradi'
# }
#
# for key, value in vocab.items():
#     print(f"{key.title()} - {value}")

# countries = {
#  'aqsh': 'washingnton d.c',
#  'italiya': 'rim',
#  'malayziya': 'kuala-lumpur',
#  'o\'zbekiston': 'toshkent',
#  'qirg\'iziston': 'bishkek',
#  'qozog\'iston': 'dushanbe',
#  'rossiya':'moskva',
#  'singapur': 'sungapur',
#  'tojikiston': 'nursulton'
# }

# print('Dunyo davlatlari:')
# for davlatlar in sorted(countries):
#  print(davlatlar.title())
#
# print('Davlatlarning poytaxtlari:')
# for poytaxtlar in sorted(countries.values()):
#  print(poytaxtlar.title())

# country = input("What is your country? ")
# if country in countries:
#  print(f"{country.title()}ning poytaxti bu {countries[country].title()}.")
# else:
#  print("We don\'t have enough information about this country!")


# menu = {
#  'lavash': 35000,
#  'burger': 30000,
#  'donar': 40000,
#  'spagetti': 43000,
#  'set': 50000,
#  'pizza': 55000,
#  'sendwich': 28000,
#  'somsa': 6000,
#  'strips': 25000,
#  'naggets': 18000
# }
#
#
# print('3 ta taom buyurtma bering.')
# taom1 = input('1-taom: ')
# taom2 = input('2-taom: ')
# taom3 = input('3-taom: ')
# if taom1 in menu:
#  print(f"{taom1.title()}ning narxi: {menu[taom1]}")
# else:
#  print(f"Kechirasiz, bizda {taom1} yo\'q")
# if taom2 in menu:
#  print(f"{taom2.title()}ning narxi: {menu[taom2]}")
# else:
#  print(f"Kechirasiz, bizda {taom3} yo\'q")
# if taom3 in menu:
#  print(f"{taom3.title()}ning narxi: {menu[taom3]}")
# else:
#  print(f"Kechirasiz, bizda {taom3} yo\'q")

#
# shaxs1 = {
#     'ism': 'Abu Abdulloh Muhammad ibn Ismoil',
#     "t_yil": 810,
#      'umr': 60,
#      'asarlari': ['Al-jome\' as-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir']
# }
# shaxs2 = {
#     'ism': 'Alisher Navoiy',
#     "t_yil": 1441,
#      'umr': 60,
#      'asarlari': ['Muhokamat-ul-lug\'otayn', 'Xamsa', 'G\'azallar']
# }
# shaxs3 = {
#     'ism': 'Zahiriddin Muhammad Bobur',
#     "t_yil": 1483,
#      'umr': 47,
#     'asarlari': ['Boburnoma', 'Harb ishi', 'Mubayyan']
# }
#
# shaxslar = [shaxs1, shaxs2, shaxs3]
# for shaxs in shaxslar:
#     print(f"{shaxs['ism']}  {shaxs['t_yil']} yilda tavallud topgan. {shaxs['umr']} yil umr ko\'rgan.")
#
# for shaxs in shaxslar:
#     print(f"\n{shaxs['ism']} ning mashxur asarlari:")
#     for asar in shaxs['asarlari']:
#         print(asar)


countries = {
    'O\'zbekiston':
        {'poytaxti':'Toshkent', 'hududi': 448978, 'aholi': 38045000, 'pul': 'so\'m' },
    'Rossiya':
        {'poytaxti':'Moskva', 'hududi': 17098246, 'aholi': 144000000, 'pul': 'rubl' },
    'AQSH':
        {'poytaxti':'Vashington', 'hududi': 9631418, 'aholi': 327000000, 'pul': 'dollar' },
    'Malayziya':
        {'poytaxti':'Kuala-Lumpur', 'hududi': 329750, 'aholi': 25000000, 'pul': 'ringgit' }
}
#
# for country in countries:
#     print(f"\n{country}ning poytaxti {countries[country]['poytaxti']}")
#     print(f"Hududi: {countries[country]['hududi']} kv.km")
#     print(f"Aholisi: {countries[country]['aholi']}")
#     print(f"Pul birligi: {countries[country]['pul']}")

davlat = input('Davlat nomini kiriting: ')
davlat = davlat.capitalize()
if davlat in countries:
    print(f"\n{davlat}ning poytaxti {countries[davlat]['poytaxti']}")
    print(f"Hududi: {countries[davlat]['hududi']} kv.km")
    print(f"Aholisi: {countries[davlat]['aholi']}")
    print(f"Pul birligi: {countries[davlat]['pul']}")
else:
    print("Bizda bu davlat haqida ma'lumot yo'q")

#SariqDevTasks End

#NEW CHAPTER DICTIONARIES END