# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

from itertools import combinations
array = list(map(int, input("enter values of array separated by space : ").split()))
given_num = int(input("enter needed sum value: "))
comb = combinations(array, 2)
ans = [i for i in comb if sum(i) == given_num]
print("ans:", ans)

# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. 
#You have to update the original array.

array = list(map(int, input("enter values of array separated by space : ").split()))
for i in range(len(array)//2):
  array[i], array[-(i+1)] = array[-(i+1)], array[i]
print(array)

# Q3. Write a program to check if two strings are a rotation of each other?

str1 = input("Enter orignal string: ")
str2 = input("Enter test string: ")
str1_str2 = "".join([str1, str2])
if str1 == str2 or len(str1) != len(str2):
  print("Strings are not rotations of each other")
else:
  if str2 in str1_str2:
    print("Strings are rotations of each other")
  else:
    print("Strings are not rotations of each other")

# Q4. Write a program to print the first non-repeated character from a string?

from collections import Counter
inp_str = input("Enter string: ")
counter = Counter(inp_str)
non_repeated = {inp_str.index(i):i for i in counter.keys() if counter[i] == 1}
if non_repeated:
  first_non_repeated = min(non_repeated.keys())
  print("first non-repeated character is", non_repeated[first_non_repeated])
else:
  print("all characters are repeated")

# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def print_instruction(n, st1, st2):
  print(f"move disk no {n} from rod {st1} to rod {st2}")

def tower_of_hanoi(n, start, end):
  if n == 1:
    print_instruction(n, start, end)
  else:
    other = 6 - (start + end)
    tower_of_hanoi(n-1, start, other)
    print_instruction(n, start, end)
    tower_of_hanoi(n-1, other, end)

n = int(input("Enter number of disks: "))

tower_of_hanoi(n, 1, 3)

# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

postfix = input("Enter postfix expression: ")
s = []
for i in postfix:
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(i+op2+op1)
print("prefix expression is",*s)


# Q7. Write a program to convert prefix expression to infix expression.

prefix = input("Enter prefix expression: ")
s = []
for i in reversed(prefix):
  if i.isalnum():
    s.append(i)
  else:
    op1 = s[-1]
    op2 = s[-2]
    s.pop()
    s.pop()
    s.append(f"({op1}{i}{op2})")
print("infix expression is",*s)


# Q8. Write a program to check if all the brackets are closed in a given code snippet.

expression = input("Enter Brackets expression: ")
s = []
o = "{[("
c = "}])"
for i in expression:
    if i in o:
        s.append(i)
    else:
        if len(s) == 0:
            print("Not Balanced")
            break
            
        b = s.pop()
        if o.index(b) != c.index(i):
            print("Not Balanced")
            break
else:
    if len(s) == 0:
        print("Balanced")
    else:
        print("Not Balanced")

# Q9. Write a program to reverse a stack.

stack = list(map(int, input("enter values of stack separated by space : ").split()))
rev_stack = []
for _ in range(len(stack)):
  rev_stack.append(stack.pop())
print("reversed stack is",*rev_stack)


# Q10. Write a program to find the smallest number using a stack.

stack = list(map(int, input("enter values of stack separated by space : ").split()))
sm_num = stack.pop()
for _ in range(len(stack)):
  i = stack.pop()
  if i < sm_num:
    sm_num = i
print(f"smallest number in given stack is {sm_num}")
