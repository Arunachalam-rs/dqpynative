str1=input("Enter the String in Upper and lower case");
lis1=list(str1);
length=len(lis1);
count=0;
up=0;
for char in lis1:
    if char.islower() == True:
        count=count+1;
        print(list(char));
    elif char.isupper() == True:
        up=up+1;
        print(list(char));

