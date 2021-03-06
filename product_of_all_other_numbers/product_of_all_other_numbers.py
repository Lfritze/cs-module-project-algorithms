'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    king_index = []
    # x is index
    for x, i in enumerate(arr):
        #start from index -> + index + 1 (ignore current index and go to the next one)
        lst = arr[:x] + arr[x + 1:]
        answer = 1
        for item in lst:
            #for item in lst multiply by item
            answer = answer * item
            #append answer to the king
        king_index.append(answer)
    return king_index


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")


'''
Write a function that receives an array of integers and returns an array consisting of the product of all numbers in the array except the number at that index.

For example, given

[1, 7, 3, 4]
your function should return

[84, 12, 28, 21]
by calculating

[7*3*4, 1*3*4, 1*7*4, 1*7*3]
In the above example, the final value at index 0 is the product of every number in the input array except the number at index 0.

Can you do this in O(n) time with O(1) space without using division?
'''