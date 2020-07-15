'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    solo = []

    for x in arr:
        if x not in solo:
            solo.append(x)
            # print(solo)
        else:
            solo.remove(x)
            # print(solo)
    return solo[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

'''
Given a non-empty array of integers where every element appears twice except for one. Find that single number. You may assume that there will always be one odd-number-out and every other number in the input shows up exactly twice.

Examples
Sample input: [2, 2, 1]
Expected output: 1
Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
Can you implement a solution that finds the single number in one pass through the input array with O(1) space complexity?

'''