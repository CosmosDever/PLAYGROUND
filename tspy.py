p="He)yo boi what('s(up)"
#output = Heyo boi what's(up)
c=0
v=0
st=0
new1=''
new2=''
for i in range(len(p)):
    if p[i] == ')' and st==0:
        continue
    elif p[i] == '(' and st==0:
        st=1      
    new1+=p[i]   
for i in range(len(new1)):
    if new1[i] =='(':
        c+=1
    elif new1[i] ==')':
        v+=1    
print(new1,c,v)    