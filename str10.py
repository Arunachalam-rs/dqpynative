str = input("Enter letters,digits and Special Symbols");
outputlist = [];
for char in str:
    if char.isdigit():
        outputlist.append(int(char))
print(outputlist);
len1=len(outputlist);
sum1= sum(outputlist);
average= sum1 / len1;
print("Sum",sum1);
print("Average",average);