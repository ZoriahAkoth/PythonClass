#Return function
def check_balance():
    balance = 1000
    return balance
my_balance =check_balance()
print(my_balance)

def division(x,y):
    z = x/y
    return z

def mulplication(a,b):
    c=a*b
    return c

def addition (p,q):
    r = p + q
    return r

#40 + 3 / 4 * 6 + 5
g = division(3,4)
h = mulplication(g,6)
i = addition(40,h)
answer = addition(i,5)
print(answer)

def is_divisible(num,x):
    divisible = " "
    if num%x == 0:
        divisible = "{} is divisible by {}".format(num,x)
    else :
        divisible = "{} is not divisible by {}".format(num,x)
    return divisible
result = is_divisible(20,2)
print(result)
result = is_divisible(287,5)
print(result)

def simple_interest (principal,rate,time):
    interest = (principal * rate * time)
    return interest
result = simple_interest(40000,0.10,2)
print(result)


