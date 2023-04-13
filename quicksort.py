Raw_list = [4,5,1,6,2,7,3,8]

def quicksort(array, n):
    if len(array)<2:
        return array
    else:
        pivot =array[0]
        less = [i for i in array[1:] if i<pivot]
        big = [i for i in array[1:] if i>pivot]
        return quicksort(less) + [pivot] + quicksort(big)

if __name__ == "__main__":
    print(quicksort(Raw_list))

