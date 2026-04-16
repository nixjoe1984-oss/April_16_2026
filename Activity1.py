word=input("Enter a word or sentnce: ") .strip()
cha=input("Enter the character that you want to check how many times it is in your word or sentence: ")
i=0
c=0
while(i<len(word)):
    if (word [i]==cha):
        c=c+1
    i=i+1
print("The total number of times",cha,"has occured: ",c)