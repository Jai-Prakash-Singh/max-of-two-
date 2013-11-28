#/usr/bin/env python 

import sys
def max_fun(num1, num2):
    if num1 > num2 :
        return "%d is bigger" %(num1)
    elif num1 == num2:
        return "Both are equal"
    else:
        return "%d is bigger" %(num2)




if __name__=="__main__":
    try:
        num1 = int(raw_input(" Enter the first number:"))
        num2 = int(raw_input(" Enter the second number: "))
	result = max_fun(num1, num2)
	print result
	#sys.exit(0)
    except:
        print " wrong input"
	#sys.exit(-1)
    

