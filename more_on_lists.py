#clearing console window
import os
def cls():
   os.system('cls')
cls()
########################

names = ['huda', 'anas', 'maaz', 'safia', 'khawar']
#--------------Looping Through a List --------------
for i in range(0, len(names)): #approach 1
    print(names[i])
cls()
for name in names:
    print(name) #approach 2: a better one


#----------- Making a list with list() -------------
cls()
numbers = range(1,6) #numbers is not an array untill now
print(numbers)

numbers = list(range(1,6)) #numbers is now a list
print(numbers)

evenNumbers = list(range(2,11,2))
print(evenNumbers)


#------------- Filling an empty list ---------------
cls()
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)


#------------- Statistics with lists ---------------
cls()
print(min(squares))
print(max(squares))
print(sum(squares))


#--------------- List Comprehensions----------------
cls()
cubes = [i**3 for i in range(1,11)]
print(cubes)


#----------------- Slicing a List ------------------
cls()
names = ['huda', 'anas', 'maaz', 'safia', 'khawar']
print(names[:3]) #slicing does not modify original list
print(names[2:])
print(names[1:5])
print(names[:]) #slice the whole list
print(names[-2:]) #start slicig from the 2nd last element
print(names[:-2]) #do slicing till the 2nd last element


#---------- copying one list into another ----------
cls()
names = ['huda', 'anas', 'maaz', 'safia', 'khawar']
#wrong method
newNames = names #new names becomes an alia of names but not another list
names.append('tb') #tb will also append in newNames
print(newNames) 

#right method
names.pop() #remove tb
newNames = names[:]
names.append('tb')
print(newNames) #newNames = ['huda', 'anas', 'maaz', 'safia', 'khawar']


#--------------------- Tuples ---------------------
cls()
fixedNames = ('huda', 'anas', 'maaz', 'safia', 'khawar') #tuples are lists that can not be mutated
print(fixedNames)
#fixedNames[0] = 'Noor ul Huda' !error
fixedNames = ('Noor ul Huda', 'anas', 'maaz', 'safia', 'khawar') #allowed
print(fixedNames)