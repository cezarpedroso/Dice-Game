import random
import sys
if len(sys.argv) > 1:
  random.seed(int(sys.argv[1]))

print('Welcome to Go Big or Go Small')

print('++++++++++BEGIN ROUND++++++++++')

#PLAYER ONE'S TURN

print('Player 1\'s turn')

p1sldie = input('Do you want to use the smaller or larger of the dice (s or l)?')
p1score = 0
ran1 = str(random.randint(1, 6))
ran2 = str(random.randint(1, 6))

print('You roll a ' + ran1 +' and ' + ran2)

maxp1 = str(max(ran1, ran2))
minp1 = str(min(ran1, ran2))
if p1sldie == 'l':
  print('Your score for this roll is ' + maxp1)
  p1score = p1score + int(maxp1)
else:
  print('Your score for this roll is ' + minp1)
  p1score = p1score + int(minp1)
print("Your current total for this round is " + str(p1score))
ra = input("Do you want to roll again (y or n)?")

while ra == "y":

  ran1 = str(random.randint(1, 6))
  ran2 = str(random.randint(1, 6))

  print('You roll a ' + ran1 +' and ' + ran2)

  maxp1 = str(max(ran1, ran2))
  minp1 = str(min(ran1, ran2))

  if p1sldie == 'l':
    print('Your score for this roll is ' + maxp1)
    p1score = p1score + int(maxp1)
  else:
    print('Your score for this roll is ' + minp1)
    p1score = p1score + int(minp1)
  print("Your current total for this round is " + str(p1score))

  #Your current total for this round is 5

  if p1score <= 15:
      ra = input("Do you want to roll again (y or n)?")
  else:
      break

while p1score > 15:
      p1score = 0


print("Your turn is over -- you scored " + str(p1score) +  " points for this round")

#PLAYER TWO'S TURN

print('Player 2\'s turn')
p2sldie = input('Do you want to use the smaller or larger of the dice (s or l)?')
p2score = 0

ran3 = str(random.randint(1, 6))
ran4 = str(random.randint(1, 6))

print('You roll a ' + ran3 +' and ' + ran4)

maxp2 = str(max(ran3, ran4))
minp2 = str(min(ran3, ran4))

if p2sldie == 'l':
    print('Your score for this roll is ' + str(maxp2))
    p2score = p2score + int(maxp2)
else:
    print('Your score for this roll is ' + str(minp2))
    p2score = p2score + int(minp2)
print("Your current total for this round is " + str(p2score))
ra = input("Do you want to roll again (y or n)?")

while ra == "y":
  ran3 = str(random.randint(1, 6))
  ran4 = str(random.randint(1, 6))
  print('You roll a ' + ran3 +' and ' + ran4)
  maxp2 = str(max(ran3, ran4))
  minp2 = str(min(ran3, ran4))

  if p2sldie == 'l':
    print('Your score for this roll is ' + str(maxp2))
    p2score = p2score + int(maxp2)
  else:
    print('Your score for this roll is ' + str(minp2))
    p2score = p2score + int(minp2)
  print("Your current total for this round is " + str(p2score))
  if p2score <= 15:
      ra = input("Do you want to roll again (y or n)?")
  else: 
      break

while p2score > 15:
    p2score = 0

print("Your turn is over -- you scored " + str(p2score) +  " points for this round")
print("--Here is the updated score for the game--")
print("Player 1 has " + str(p1score) + " points total")
print("Player 2 has " + str(p2score) + " points total")

