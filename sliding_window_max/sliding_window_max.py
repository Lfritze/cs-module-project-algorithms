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
# def sliding_window_max(nums, k):
#     # Your code here
#     king_array = []

#     for index, i in enumerate(nums):
#         # array for nums index: index + k numbers in array
#         box = nums[index: index + k]
#         #if box array is less than k numbers in array
#         if len(box) < k:
#             pass
#         else:
#             # get the largest number from the box array
#             max_arr = max(box)
#             # append it to the king array
#             king_array.append(max_arr)
#     # return the king
#     return king_array


def sliding_window_max(nums, k):
    # max num = [0] multiplied times the length of nums - k + 1
    max_number = [0] * (len(nums) - k + 1)
    # set max num at zero index equal to the maximum number from the beginning to k (the amount of items) 
    max_number[0] = max(nums[:k])

    # in range from 1 ... length nums - k + 1
    for i in range(1, len(nums) - k + 1):
        # if nums [i - 1] matches max num[i-1]
        if nums[i - 1] == max_number[i - 1]:
            # then max num[i] is equal to the... max method...max(nums[from i by i add k])
            max_number[i] = max(nums[i:i + k])
        else:
            # otherwise max num[i] is equal to...max method...max(max_num[i then iterate down 1]) nums[i + k iterate down 1]
            max_number[i] = max(max_number[i - 1], nums[i + k - 1])

    return max_number

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
