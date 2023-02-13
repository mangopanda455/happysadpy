def isHappy(n):
  firstN = n
  pastNums = set()
  iterations = 0
  while n != 1:
    n = sum(int(i)**2 for i in str(n))
    iterations += 1
    if n in pastNums:
      return
    pastNums.add(n)
  return firstN

for i in range(1, 100_000+1 + 1):
  if isHappy(i) != None:
    print(isHappy(i))