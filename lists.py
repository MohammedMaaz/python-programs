#clearing console window
import os
def cls():
   os.system('cls')
cls()
########################

names = ['maaz', 'anas', 'huda', 'safia', 'khawar']

#------------- Modifying lists' elemens -------------
cls()
print(names[1])
print(names[-1])
names.append('TB')
print(names)
names.insert(1,'latkan')
print(names)
del names[2] #removing any item using del
print(names)
print(names.pop())
print(names)
names.pop(2) #removing any item using pop (pop also returns the removed item)
print(names)
names.remove('latkan') #removing an item by giving its valus/name
print(names)


#------------------ JAgged List -----------------------
cls()
jaggedArr = [ ['maaz', 'anas', 'huda', 'safia', 'khawar'],
              ['hamza', 'zain', 'rafay', 'talha'],
              ['wajeeha', 'sania', 'mashood'],
              ['abdullah', 'rumaisa'],
              ['mubashir', 'tehreem', 'hamza']
            ]
print(jaggedArr)


#----------------- Sorting a list ---------------------
cls()
names = ['anas', 'maaz', 'huda', 'khawar', 'safia']
names.sort() #permanent sort, returns nothing
print(names)

names = ['maaz', 'anas', 'huda', 'safia', 'khawar']
print(sorted(names)) #return the temporarily sorted list
print(names)

names.reverse() #reverse a list
print(names)
print(len(names)) #returns length of the list
