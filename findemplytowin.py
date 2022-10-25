import string
import operator
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
a=''
w, h = [int(i) for i in input().split()]
fo={}
row=''
for i in range(h):
    row += input()
for k in row:
    if k in alphabet_list:
        fo[k]=row.count(k)
mydic=dict(sorted(fo.items(), key=operator.itemgetter(1),reverse=True))
for key in mydic:
    a+=key
print(a)    