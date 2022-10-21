atext='The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.'    
ans=''
ltext = atext.lower().split(" ")
def replace_the_map(text):
    rtext = list(map(lambda i : 'xxx' if i =='the' else i,ltext))        
    return ' '.join(rtext)
print(replace_the_map(atext))   
