#clearing console window
import os
def cls():
   os.system('cls')
cls()
########################

# ---------------strings-----------------
cls()
name = '  maaz bin khawar  '

print(name.rstrip() + '.')
print(name.lstrip() + '.')
name = name.strip()
print(name + '.')

print('\n' + name.title())
print(name.upper())
print(name.lower())


#----------------Numbers----------------
cls()
print('2**3 =', 2**3)
print('15/2 =', 15/2)
print('15//2=', 15//2)
print('8%3=', 8%3)
print('0.2+0.1 =', 0.2+0.1)
print('2*0.2 =', 2*0.2)
print('2.3**4 =', 2.3**4)

#------convert numbers to strings-------
cls()
print('Age = ' + str(19))
print('Height = ' + str(5.11) + ' feet')

