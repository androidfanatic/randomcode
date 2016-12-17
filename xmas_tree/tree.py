import sys

def xmas_tree(n = 10):
  for i in range(1, n):
    print (" " * (n - i)) + ("* " * i)
  for i in range(0, n/5):
    print (" " * (n - n/4)) + "=" * (n/4)


if len(sys.argv) == 2:
  try:
    xmas_tree(int(sys.argv[1]))
  except:
    xmas_tree()
else:
  xmas_tree()
