str = input("Enter the string");
split = list(str);
length = len(split);
for i in range(0,length):
    if i % 2 ==0:
        print(split[i]);