str= input("Enter letters,digits and Special Symbols");
count=0;
leng=0;
c=0;
lis1=list(str);
length = len(str);
for char in lis1:
    if char.isalpha() == True:
        count= count+1;
    if char.isdigit() == True:
        leng= leng+1;
c=length-leng-count;
print("Special Character",c);
print("Alphabets",count);
print("Digits:",leng);
