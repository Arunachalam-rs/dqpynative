string = input("Enter the String");
length = len(string);
middle= int(length/2);
letter= list(string);
for i in range(0,length):
    if  i==middle:
        this= (string[i-1],string[i],string[i+1]);
print(''.join(this));