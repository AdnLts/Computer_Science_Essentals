# stores earned points
UserPointsE=0
# stores possible points
UserPointsP=0
#-----------------------------
# Title
print('Did I Fail?')
print('A calculator that tells you if you failed.')
#-----------------------------
# User Input
UserPointsP=int(input('how many points in the grade out of? '))
UserPointsE=int(input('how many points did you earn? '))
#------------------------------
# Prints % and Passing
Perc=UserPointsE/UserPointsP*100
print('Percentive Grade:')
print(Perc)

if Perc >=60:
  print('You Passed!')
else:
  print('You Failed!')
