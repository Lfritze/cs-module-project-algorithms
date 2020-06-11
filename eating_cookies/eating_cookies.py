'''
Input: an integer
Returns: an integer

Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in the cookie jar? Implement a function `eating_cookies` that counts the number of possible ways Cookie Monster can eat all of the cookies in the jar. 

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies 
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once. 

Thus, `eating_cookies(3)` should return an answer of 4.

Can you implement a solution that runs fast enough to pass the large input test?
'''
## RECURSION
# if n < 0 - pass
# if n == 0 return 1
# if n ==1 and n ==2 return n
#if n == 3 return 4
#else make it recursive like eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
# def eating_cookies(n):
#     # Your code here
#     # if n < 0 - pass
#     if n < 0:
#         pass
#     elif n == 0:
#         return 1
#     if n == 1 and n == 2:
#         #if 1 cookie then n = 1
#         #if it is already 2 then the possibilities = 2
#         return n
#     elif n == 3:
#         return 4
#     else:
#         cookie_beast = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
#         return cookie_beast
def eating_cookies(n, cache=None):    
    if cache == None:
        cache = [0] * (n + 1)
    # if n is <= 1 return 1
    if n <= 1:
        cache[n] = 1
        # if n is 2 return 2
    elif n == 2:
        cache[n] = 2
    elif cache[n] == 0:
        # n-1 + n-2 + n-3
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 15

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
