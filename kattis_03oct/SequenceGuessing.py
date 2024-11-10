import sys
def dump(x):
  #print("Python: printing out {}".format(x), file=sys.stderr)
  print(x)
  #print("Python: NOW FLUSHING {}".format(x), file=sys.stderr)
  sys.stdout.flush()
  #print("Python: TRYING TO READ", file=sys.stderr)
  ans = int(input())
  #print("Python: read in {}".format(ans), file=sys.stderr)
  return ans

# sys.setrecursionlimit(650000)

curr = dump(50001)

while curr != -1:
    if curr % 2 == 0:
        curr = dump(curr // 2 + 1)
    else:
        curr = dump(-1)

for i in range(0, 100001, 2):
    print(i)
sys.stdout.flush()


'''
Below is from offical solution.
Still couldn't figure out what is the expected result of this question.
'''
'''
import sys
def dump(x):
  #print("Python: printing out {}".format(x), file=sys.stderr)
  print(x)
  #print("Python: NOW FLUSHING {}".format(x), file=sys.stderr)
  sys.stdout.flush()
  #print("Python: TRYING TO READ", file=sys.stderr)
  ans = int(input())
  #print("Python: read in {}".format(ans), file=sys.stderr)
  return ans

seen = [False] * 100001
have = [False] * 100001
x = 0
while x < 100000:
  have[x] = True
  x += 3
have[-1] = True
curr = dump(66668)

while curr != -1:
  if curr == 100000:
    curr = dump(66668)
  elif curr%3 == 0:
    curr = dump(2 * (curr // 3) + 1)
  else:
    bucket = curr // 3
    if not seen[3*bucket+1] and not seen[3*bucket+2]:
      seen[curr] = True
      curr = dump(-1)
    else:
      have[curr] = True
      curr = dump(2*(bucket + 1))
assert curr == -1
ret = []
curr = 0
while curr < 99999:
  ret.append(curr)
  if have[curr+1] or seen[curr+2]:
    ret.append(curr+1)
  else:
    ret.append(curr+2)
  curr += 3
ret.append(99999)
ret.append(100000)
for x in ret:
  assert not seen[x], "{} is seen".format(x)
  print(x)
sys.stdout.flush()
'''