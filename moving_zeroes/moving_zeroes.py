'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # x is the index
    for x, i in enumerate(arr): 
        # enumerate accepts arguments like -for c, value in enumerate(my_list, 1): print(c, value)
        # and creates a counter [(1, 'apple') (2, 'banana')...]
        if arr[x] != 0:
            #if x does not equal 0
            arr.pop(x)
            # pop x
            arr.insert(0, i)
            # insert it at the beginning 
    return arr


# The pop() method removes the item at the given index from the list and returns the removed item.



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 1, 3, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

'''
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, then returns the altered array. The order of the non-zero integers does not matter in the mutated array.

Examples
Sample input: [0, 3, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]
Sample input: [4, 2, 1, 5]
Expected output: 4
Expected output array state: [4, 2, 1, 5]
Can you do this in a single pass through the input array with O(1) space?
'''