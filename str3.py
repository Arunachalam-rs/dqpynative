str1 = input("Enter the First String");
str2 = input("Enter the second string");
split1= list(str1);
length1 = len(str1);
length2 = len(str2);
middle= int(length1/2);
name1=list(str1);
name2=list(str2);
for i in range(length2):
    name1.insert(i+middle,name2[i])
print(''.join(name1));
