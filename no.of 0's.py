def zeros(arr):
    zero_count=0
    for i in arr:
        if i==0:
            zero_count+=1
    return zero_count

arr=[0,5,0,0,0,6,0]
result=zeros(arr)
print(result)


