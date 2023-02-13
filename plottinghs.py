import matplotlib.pyplot as plt
x = []
# corresponding y axis values
y = []

x1 = []

y1 = []

def isHappyCheck(n):
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

def isHappy(n):
  firstN = n
  pastNums = set()
  iterations = 0
  while n != 1:
    n = sum(int(i)**2 for i in str(n))
    iterations += 1
    if n in pastNums:
      x1.append(firstN)
      y1.append(iterations)
      return (f'The number ({firstN}) is a sad number after {iterations} iterations.')
    pastNums.add(n)
  x.append(firstN)
  y.append(iterations)
  return (f'The number ({firstN}) is a happy number after {iterations} iterations.')
  

for i in range(0, 1_000_001):
  isHappy(i)
# plotting the points 
plt.plot(x, y, label = 'happy')
# plt.scatter(x1, y1, label = 'sad')
# naming the x axis
plt.xlabel('x - number')
# naming the y axis
plt.ylabel('y - iterations')
  
# giving a title to my graph
plt.title('Number relationship to iterations')
  
# function to show the plot
# plt.legend()
plt.show()