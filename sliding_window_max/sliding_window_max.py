'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers

# Sliding Window Max

Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

## Example
```
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
 ```

 Can you implement a solution that calculates all of the maximum sliding window values in O(n) time?
'''
def sliding_window_max(nums, k):
    # Your code here
    king_array = []
    # x is index
    for x, i in enumerate(nums):
        # array for nums index: index + k numbers in array
        box = nums[x: x + k]
        #if box array is less than k numbers in array
        if len(box) < k:
            pass
        else:
            # get the largest number from the box array
            max_arr = max(box)
            # append it to the king array
            king_array.append(max_arr)
            # return the king
    return king_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
