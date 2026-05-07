
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
