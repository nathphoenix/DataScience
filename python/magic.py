magic_numbers = [3, 6, 1]
chances = 3

name = input('What is Your Name ')
guess_number = int(input('Please Guess the magic number '))

# if user_number in magic_numbers :
#       print('You Are Correct ')
# elif user_number not in magic_numbers :
#       print('You Are Wrong ' )
# else:
#       print('Please Try Again Later ' + name)
for attempt in range(chances) :
  # //no of attempt
   print('This is attempt {}' .format(attempt))  
   if guess_number in magic_numbers :
          print('You guess Right ')
   elif guess_number not in magic_numbers :
        print('Please Try Again Later ')
else :
    print('Thank You ' + name )

#     if guess_number == magic_numbers :
#           print('You guess Right ')
#     elif guess_number != magic_numbers :
#         print('Please Try Again Later ')
# else :
#     print('Thank You ' + name )


# if guess_number != magic_numbers :
#      print('You Are Wrong Please Try Again ' + name)
# elif guess_number == magic_numbers :
#     print('You Are Correct ' + name)
# else :
#   print('Thank you ' + name)


