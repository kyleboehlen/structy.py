def is_prime(n):
  for i in range(2, squirt(n) + 1):
    if (n % i) == 0:
      return False
  return n != 1

def squirt(n):
  pairs = []
  strN = str(n)
  for i in range(len(strN) - 1, -1, -2):
    if i >= 1:
      strPair = strN[i - 1] + strN[i]
    else:
      strPair = strN[i]
    pairs.insert(0, strPair)

  remainder = 0
  left = ''
  top = ''
  for i, p in enumerate(pairs):
    if i == 0:
      for s in range(2, 9):
        if int(p) < (s * s):
          top = top + str(s - 1)
          left =  str((s - 1) + (s - 1))
          remainder = int(p) - ((s - 1) * (s - 1))
          break
    else:
      remainder = int(str(remainder) + p)
      for s in range(2, 10):
        if remainder < (int(left + str(s)) * s):
          remainder = remainder - (int(left + str(s - 1)) * (s - 1))
          top = top + str(s - 1)
          left = str(int(left + str(s - 1)) + (s - 1))
          break
        elif s == 9:
          remainder = remainder - (int(left + str(s)) * (s))
          top = top + str(s)
          left = str(int(left + str(s)) + (s))
          
  return int(top)