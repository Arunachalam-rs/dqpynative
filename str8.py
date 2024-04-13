str1=input("Enter the First String");
str2=input("Enter the Second String");
lis1=list(str1);
lis2=list(str2);
length1 = len(lis1);
length2 = len(lis2);
cnt=0;
for i in range(length1):
    for j in range(length2):
        if lis1[i] == lis2[j]:
            cnt=cnt+1;
if cnt == length1:
    print("True");
else:
    print("False");