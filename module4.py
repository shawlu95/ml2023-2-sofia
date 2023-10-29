n  = int(input("Enter N: "))
numbers = []
for i in range(n):
  m = int(input(f"Enter M number ({i+1}/{n}): "))
  numbers.append(m)
x = int(input("Enter X: "))

# outputs: "-1" if there were no such X among N read numbers,
#  or the index (from 1 to N) of this X if the user inputed it before.
if x in numbers:
  print(numbers.index(x) + 1)
else:
  print(-1)