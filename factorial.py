# Code up a factorial function

#Understand
# Google what is a factorial
# What is our goal?
# Get a visual representation

# n!  (n-bang)  n * (n-1)...1

# Plan
# Should we do it recursively or iteratively?
# What language is best to use here?

## Recursive Recursive  Recursive  Recursive Recursive Recursive Recursive 
  # Define base case (return if n =1)
  # Move toward the base case
  # Call itself

  # call each number, then -1 and multiply it to previous until we hit base case

  # Execute

def factorial(n):
  if n == 1:
    return n
  return n * factorial(n-1)

print(factorial(3) == 6)
print(factorial(4) == 24) # TESTS


# Review 
  # TIme complexity and space complexity O(n)


# Iterative Iterative Iterative Iterative

# Plan
  # Go from 1 to n, or n to 1
  # make a tracker: total 
  # make a while loop and decrement n as we go
  # multiply our tracker at every step
  # n == 1 return

def iter_factorial(n):
  # Tracker
  total = 1
  # make a while loop and decrement n as we go
  while n != 1:
    # multiply our tracker at every step
    total *=n
    n -= 1
    # Return Tracker
  return total

print(iter_factorial(3) == 6)
print(iter_factorial(4) == 24) # TESTS

# REVIEW BOTH
  # Iterative vs Factorial
  ## space complexity: iterative wins
  ##Time complexity: O(n) for both
  # Readability? 
  # Both solutions are okay. 
  


    

