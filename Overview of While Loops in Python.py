nums = list(range(1, 100))

#while the count of the nums is greater than zero it will conitune until the length of numbers is greater than zero
while len(nums) > 0:
  print(nums.pop())



def guessing_game():
  while True:
    print('What is your guess?')
    guess = input()


    if guess == '42':
      print('You have correctly guessed the number!')
      return False
    else:
      print(f'No, {guess} is not the answer, please try again\n')


guessing_game()


#use when you do not know when it will end