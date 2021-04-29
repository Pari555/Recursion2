'''
4/29/21
Recursion
'''

# Factorial
# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!
# 5! = 5 * 4 * 3 * 2 * 1 * 0!
# 5! = 5 * 4 * 3 * 2 * 1 * 1

# 1. With a Loop
num = int(input("Choose a Positive Int: "))

factorial = 1

for i in range(1, num + 1):
	factorial *= i

print(" The factorial of " + str(num) + " is " + str(factorial))

# 2. With a Recursive Function
def factorial(n):
	if(n == 0):
		return 1
	else:
		return n * factorial(n - 1)

num = int(input("Choose a Positive Int: "))

print(" The factorial of " + str(num) + " is " + str(factorial(num)))



# Fibonacci Sequence
# NOTE: Keep Adding the Last 2 Numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 45, .....

# 1. With a Loop
