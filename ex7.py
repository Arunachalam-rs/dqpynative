sen1="Emma is good developer. Emma is a writer. Emma is lovely"
sen2="Emma"
word1= sen1.split();
word2= sen2.split();
length1 = len(word1);
length2 = len(word2);
cnt=0;
for i in range(length1):
    for j in range(length2):
        if word1[i] == word2[j]:
            cnt=cnt+1;
print("Emma apperared", cnt, "times");
