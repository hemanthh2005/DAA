# import random
# def gen_data(a,n):
#     for i in range(n):
#         x=random.randint(0,100)
#         a.append(x)

def merge(a,low,high):
    if high-low<1:
        return
    mid=((low+high)//2)
    merge(a,low,mid)
    merge(a,mid+1,high)
    sort(a,low,mid,high)

def sort(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    k=low
    i=0
    j=0

    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            a[k]=left[i]
            i+=1
        else:
            a[k]=right[j]
            j+=1
        k+=1

    if i<len(left):
        while i<len(left):
            a[k]=left[i]
            i+=1
            k+=1
    else:
        while j<len(right):
            a[k]=right[j]
            j+=1
            k+=1

a=[37,45,36,44,85]
# print("Enter Size: ")
# n=int(input())
# gen_data(a,n)
print("The Numbers are")
print(a)
merge(a,0,len(a))
print("Sorted Numbers")
print(a)