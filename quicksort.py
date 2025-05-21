import random

def gen(a,n):
    for i in range(n):
        x=random.randint(0,100)
        a.append(x)

def partition(a,left,right):
    key=a[left]
    i=left+1
    j=right
    while True:
        while a[i]<key and i<right:
            i+=1
        while a[j]>key and j>left:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
        else:
            break
    a[left],a[j]=a[j],a[left]
    return j

def q_sort(a,low,high):
    if low<high:
        s=partition(a,low,high)
        q_sort(a,low,s-1)
        q_sort(a,s+1,high)


a=[]
n=int(input("Enter Size: "))
gen(a,n)
print("The numbers are")
print(a)
q_sort(a,0,n-1)
print("sorted elements")
print(a)