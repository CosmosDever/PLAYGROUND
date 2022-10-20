l=input()
a,b,c,d=0,0,0,0
for i in l:
    if i.lower()=='a':
        a+=1
    if i.lower()=='b':
        b+=1
    if i.lower()=='c':
        c+=1
    if i.lower()=='d':
        d+=1
sl={'a':a,'b':b,'c':c,'d':d}
l=[a,b,c,d]
j=''
l.sort(reverse=True)
for i in range(len(l)):
    for k in sl:
        if k in j:
            continue
        elif sl[k]==l[i]:
                print(k,'have',l[i])
                j+=k