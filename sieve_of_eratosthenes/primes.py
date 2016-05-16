def primes(n):
  assert n > 1
  m = []
  for i in [2] + range(3, n + 1, 2):
    if i not in m:
      yield i
    for j in range(i * i, n + 1, i):
      m.append(j)

for x in primes(2):
  print x
