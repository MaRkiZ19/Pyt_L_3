def merge_sort(nums):
    if len(nums) > 1:
        mid= len(nums)//2
        left = nums[:mid]
        right=nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            nums[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k]=right[j]
            j+=1
            k+=1

list1= [1,5,6,3,4,56,7,98,4,2,2,56,7,3,4,5,6,7,98,111,2,3,44,5,78,45]
merge_sort(list1)
print(list1)
