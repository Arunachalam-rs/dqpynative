def remove_chars(string,n):
    i =0;
    length=len(string);
    for i in range(length):
        if i <= length:
            print(string[n]);
            n=n+1;
ans=remove_chars("pynative",2)
print(ans);