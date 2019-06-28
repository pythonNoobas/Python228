what = input( 'что делаем?' '(+, -, *, /): ' )
a = int ( input( 'введи число 1: ' ) )
b = int ( input( 'введи число 2: ' ) )

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
	print( str(a) + "/" + str(b) + "/" + str(c) )

