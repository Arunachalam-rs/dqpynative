str = input("Enter the String");
lis1 = list(str);
len1=len(lis1);
chdict= dict();
count=0;
for i in len1:
    if i == lis1[i]:
        count=count+1; 
    print(count);