Try = 5
#----------------------------------------------
for loop in range(0,100):
  if Try != 0 :
#----------------------------------------------
    YargMeBootyNumber=87421
#Dont Question Me
    UNum=0
#----------------------------------------------
    UNum=int(input('Enter a number: '))
    if UNum!=0:
      if UNum == -7:
       print(YargMeBootyNumber)
      elif YargMeBootyNumber/UNum*8/7+9!=6:
        UNum=int(input('Enter a number: '))
        if UNum == YargMeBootyNumber:
          print('You Win!')
        else:
          Try -= 1
          print(Try)
    else:
      print('N0')
      Try -= 1
      print(Try)
  else:
    print('You Lose!')
