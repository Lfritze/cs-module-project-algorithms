# Given a and b, return a **b, without using the power builtin operator 

# UNDERSTAND

# Powers are a single number being multiplied by itself, as many times as the second number
# valid and invalid inputs (numbers, letters)?
# maybe no negative numbers for b 2 ** -2 = 1/4  (so if b is negative then 1/(2**2)) put a 1/ in front of it  PUT A 1 OVER THE WHOLE OPERATION
## 1/(2**2)

# i = sqrt(-1)  is the same as (-1)**0.5

# what if b ==0? Anything to the power of 0 is 1
# Lets' not handle decimal numbers for b

# PLAN PLAN PLAN

# WE have 2 numbers, one or both may be negative
# Iterative vs recursive



## 2 **3
# ITERATIVE PSEUDOCODE
# def iter_power_v1(a,b):
# ### check if b == 0, if so return 1
#   if b == 0:
#     return 1
# ### have a counter == a
#   product = a
# ### While loop: while b is not 1
#   while b != 1:
# ### multiply the counter by a
#     product *= a
# ### decrement our b to approach 1
#     b -= 1
# ### return counter
#   return product

# print(iter_power_v1(2, 3)== (2 ** 3))
# print(iter_power_v1(10, 2)== (10 ** 2))
# print(iter_power_v1(10, 0)== (10 ** 0))



def iter_power(a,b):
  # Check if b is int, other wise return error
  if type(b) is not int:
    return "Sorry no decimals"
### check if b == 0, if so return 1
  if b == 0:
    return 1
# CHeck if b < 0: if so, multiply by -1, set invert to True
  invert = False
  if b < 0:
    b*= -1
    invert = True
### have a counter == a
  product = a
### While loop: while b is not 1
  while b != 1:
### multiply the counter by a
    product *= a
### decrement our b to approach 1
    b -= 1
### return counter
  if invert:
    return 1 / product
  else:
    return product

print(iter_power(2, 3)== (2 ** 3))
print(iter_power(10, 2)== (10 ** 2))
print(iter_power(10, 0)== (10 ** 0))
print(iter_power(2, -2)== (2 ** -2))
print(iter_power(100, 1) == 100)

# I