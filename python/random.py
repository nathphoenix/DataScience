import random
magic_numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# magic_numbers = [random.randint(0, 9), random.randint(0, 9)]
chances = 1

name = input('What is Your Name ')
guess_number = int(input('Please Guess the magic number '))

for attempt in range(chances) :
  # //no of attempt
   print('This is attempt {}' .format(attempt))  
   if guess_number in magic_numbers :
          print('You guess Right ')
   elif guess_number not in magic_numbers :
        print('Please Try Again Later ')
else :
    print('Thank You ' + name )
