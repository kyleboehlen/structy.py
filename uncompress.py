def uncompress(s):
  d = ''
  index = 0
  num = ''
  while index < len(s):
    if s[index].isdigit():
      num = num + s[index]
    else:
      d = d + (s[index] * int(num))
      num = ''
    index = index + 1
  return d