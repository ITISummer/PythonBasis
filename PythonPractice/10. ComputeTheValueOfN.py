num = int(input("input a number: "))
a = num*10+num
b = num*100+a
print(num+a+b)
# ------ 2
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)
