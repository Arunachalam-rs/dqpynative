str1=input("Enter the String");
str2=input("Enter the Second String");
lis1 = list(str1);
lis2 = list(str2);
len1 = len(lis1);
len2 = len(lis2);
i=0;
for i in range(len1):
    a=print(lis1[i]);
    b=print(lis2[-1-i]);
i=i+1;
c = a+b;
print(c);