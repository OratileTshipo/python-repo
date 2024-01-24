"""In this project, I am learning data structures by building the merge sort algorithm.
This is a sorting algorithm that uses the divide-and-conquer principle to sort collections of data.
That is, it 'divides' a collection into smaller sub-parts, and 'conquers' 
the sub-parts by sorting them independently, then merges the sorted sub-parts."""

# initialise global variables
mylist = [4,10,6,15,2,1,7,9,5]

def merge_sort(array):
    # initialise variables to keep track of sorting
    left_array_index = 0
    right_array_index = 0
    sorted_array_index = 0

    # find mid-point and divide the list into 2
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]
    print(f'Mid: {middle_point} R: {right_part} L: {left_part}')
    
    if len(array) <= 1:
        return

    # recursively divide the lists until every item has its own list
    merge_sort(right_part)
    merge_sort(left_part)

    # compare elements from lists, and sort them in ascending order by merging with originat list
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_array_index].append(left_part[left_array_index])
            left_array_index += 1
        else:
            array[sorted_array_index].append(right_part[right_array_index])
            right_array_index += 1
        sorted_array_index += 1

    while left_array_index < len(left_part):
        array[sorted_array_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_array_index += 1

    while right_array_index < len(right_part):
        array[sorted_array_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_array_index += 1

if __name__ == '__main__':
    print(f'Unsorted list: {mylist}')
    print(f'\nSorted list:')
    merge_sort(str(mylist))


