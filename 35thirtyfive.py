# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = int(input("Enter an integer: "))


result = n + n * n + n * n * n

# Print the result in the desired format
print("The value of", n, "+", n, "*", n, "+", n, "*", n, "*", n, "is: ", result)