def largest_array(arr):
    largest =arr[0]
    for num in arr:
        if num>largest:
            largest=num
    return largest
array = list(map(int,input().split()))
result=largest_array(array)
print(result)
