   
'''
Author: Md. Rahat
Department: Computer Science & Engineering
Batch: 5th Batch
University: University Of Barisal

'''
A=list(map(int,input("Enter Numbers Sepaarting By Spavce:").split()))        
def InsertionSort(A):
    for j in range(1,len(A)):
        key=A[j];i=j-1
        while(i>-1 and A[i]>key):
            A[i+1]=A[i]
            i-=1
        A[i+1]=key
    print("The Insertion Sort Result: ",*A)
InsertionSort(A)

def swap(a,b):
    tmp=a;a=b;b=tmp;
    #return a,b

def selectionSort(A):
    C=[]
    for i in range(len(A)):
        mn=min(A[i:])
        swap(A[i],A[A.index(mn)])
    print("The Selection Sort Result: ",*A)
selectionSort(A)
        
def bubbleSort(A):
    for i in A:
        for j in range(i,len(A)):
            if (A[i]<=A[j]):
                swap(A[i],A[j])
    print("The Bubble Sort Result: ",*A)
bubbleSort(A)
                
def mergeSort(A):
    if len(A) > 1:
        mid=len(A)//2;left=A[:mid];right = A[mid:];mergeSort(left);mergeSort(right);i=j=k=0;
        
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                A[k]=left[i];i+=1
            else:
                A[k]=right[j];j+=1
            k+=1
        # For all the remaining values
        while i<len(left):
            A[k]=left[i];i+=1;k+=1
        while j<len(right):
            A[k]=right[j];j+=1;k+=1

mergeSort(A)
print("The Merge Sort Result: ",*A)

def countingSort(A):
    mx=max(A);ln=len(A)
    C=[0]*(mx+1)
    for i in A:
        C[i]=C[i]+1
    C[0]=C[0]-1 # to decrement each element for zero-based indexing
    for i in range(1,mx+1):
        C[i]=C[i]+C[i-1]
    B=[0]*len(A)
    for x in reversed(A):
        B[C[x]]=x
        C[x]=C[x]-1
    return B
#A=[7,0,4,4,89,45,267777,2,4,2,2,243]
print("The Counting Sort Result: ",*countingSort(A))
