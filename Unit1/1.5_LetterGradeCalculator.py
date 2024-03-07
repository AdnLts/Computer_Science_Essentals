# stores earned points
UserPointsE=0
# stores possible points
UserPointsP=0
#-----------------------------
# Title
print('Letter Grade Calculator')
print('A calculator that tells your grade as a letter.')
#-----------------------------
# User Input
UserPointsP=int(input('How many points in the grade out of? '))
UserPointsE=int(input('How many points did you earn? '))
#------------------------------
# Prints % and Letter
Perc=UserPointsE/UserPointsP*100
print('Percentive Grade:')
print(Perc)

if Perc >=90:
  print('You got an A!')
elif Perc >=80:
  print('You got a B!')
elif Perc >=70:
  print('You got a C!')
elif Perc >=60:
  print('You got a D!')
elif Perc >=0:
  print('You got a F!')
else:
  print('Congrats! You messed up so badly your getting an ERROR message')

