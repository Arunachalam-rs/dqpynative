str1 = input("Enter the First String");
str2 = input("Enter the second String");
length1 = len(str1);
length2 = len(str2);
a1=0;
a2=int(length1/2);
a3=length1-1
b1=0;
b2=int(length2/2);
b3=length2-1
name1=(str1[a1],str2[b1]);
name2=(str1[a2],str2[b2]);
name3=(str1[a3],str2[b3]);
list1=list(name1);
list2=list(name2);
list3=list(name3);
list1.extend(list2);
list1.extend(list3);
print(''.join(list1));