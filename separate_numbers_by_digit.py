n=input()
def runtrue(n):
    if n[0]=='0':
        for i in range(1,len(n)):
            if n[i]=='0':
                print('0')
            else:
                print(n[i]+'0'*(len(n)-i-1))
    else:
        for i in range(len(n)):
            if n[i]=='0':
                print('0')
            else:
                print(n[i]+'0'*(len(n)-i-1))
def check_input(input):
    try:
        val = int(input)
        return val
    except ValueError:
        try:
            val = float(input)
            print("Invalid", val)
        except ValueError:
            print("Invalid")          
val =check_input(n)
check_int = isinstance(val, int)
if check_int == True:
    if val < 0:
        print("UNDER")   
    elif val > 1000000:
        print("OVER")    
    else:runtrue(n)