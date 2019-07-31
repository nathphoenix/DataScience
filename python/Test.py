
import datetime
print(datetime.datetime.today())
shippingFee = 10
totalShipping = 0

name = input('Please Enter Your Name ')
amount = float(input('Enter The Amount You Spent? '))

if amount < 50 :
      totalShipping = float(shippingFee) + amount
      print('Your total amount is %.2f' % totalShipping)
# else :
#   print('SHipping is free')
if amount > 50 :
    print('Your order is on the way ')
print ('Thank you for shopping with us ' + name)