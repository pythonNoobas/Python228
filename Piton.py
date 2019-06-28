what = input( 'что делаем?' '(+, -, *, /, %): ' )
a = int ( input( 'введи число 1: ' ) )
b = int ( input( 'введи число/проценты от числа "1" 2: ' ) )
p = 100

if what == '-':
    c = a - b
    print( str(a) + "-" + str(b) + "=" + str(c) )

elif what == '+':
   c = a + b
   print( str(a) + "+" + str(b) + "=" + str(c) )
   
if what == '*':
	c = a * b
	print( str(a) + "*" + str(b) + "=" + str(c) )

elif what == '/':
	c = a / b
	print( str(a) + "/" + str(b) + "=" + str(c) )

if what == '%':
	c = b * p / a
	 print( str(b) + "*" + str(p) + "/" + str(a) + "=" + int(c) + "%") 


