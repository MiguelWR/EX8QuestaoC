#Exercício 8

#c)

def Sc(a, b, n):
  if n == 0:
    return a
  elif n == 1:
    return b
  elif n > 1:
    return Sc(a, b, n - 2) + Sc(a, b, n - 1)


print(Sc(1, 2, 1))