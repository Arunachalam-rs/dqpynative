string = input("Enter the String");
length = len(string);
first=0;
middle= int(length/2);
last= int(length);
letter= list(string);
for i in range(0,length):
    if i == first:
        a=string[i];
    if i==middle :
        b=string[i];
    if i == length-1:
        c=string[i];
new=list(a+b+c);
print(''.join(new));