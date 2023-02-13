import matplotlib.pyplot as plt
# while num<=1000:
#   numsq=num*num
#   listnumsq = [int(i) for i in str(numsq)]
#   resultinglst = sum([i**2 for i in listnumsq])
#   print(resultinglst)
#   num+=1

# while num <= 1000:

#   num+=1

# write one that takes input then checks
def isHappy(n):
  firstN = n
  pastNums = set()
  iterations = 0
  while n != 1:
    n = sum(int(i)**2 for i in str(n))
    iterations += 1
    if n in pastNums:
      return (f'The number ({firstN}) is a sad number after {iterations} iterations.')
    pastNums.add(n)
  return (f'The number ({firstN}) is a happy number after {iterations} iterations.')


# f = open("/Users/grahamfielding/side projects/realpb/src/happyorsad100k.txt", "a")
# for i in range(1, 100_000+1):
#   f.write(isHappy(i)+"\n")
# f.close()

# i = input("what num ")
# print(isHappy(i))

for i in range(1, 100_000+1):
  if isHappy(i).__contains__("after 7 iterations"):
    print(isHappy(i))

# number x iterations y