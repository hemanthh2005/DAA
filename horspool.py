def horspool(text,pattren):
    m=len(text)
    n=len(pattren)
    if m<n:
        return -1
    shift=[n]*256
    for i in range(n-1):
        shift[ord(pattren[i])]=n-i-1
    pos=0
    while pos<=m-n:
        j=n-1
        while j>=0 and pattren[j]==text[pos+j]:
            j=j-1
        if j<0:
            return pos
        else:
            pos += shift[ord(text[pos + n - 1])]
    return -1

text=input("Enter string: ")
pattern=input("Enter Pattern: ")
pos=horspool(text,pattern)
if pos>=0:
    print("pattern string found at position",pos+1)
else:
    print("not found")