sen1=input("Enter the string");
sen2=input("Enter the word to be checked");
word1= sen1.split();
word2= sen2.split();
length1 = len(word1);
length2 = len(word2);
cnt=0;
for i in range(length1):
    for j in range(length2):
        if word1[i] == word2[j]:
            cnt=cnt+1;
print(cnt);