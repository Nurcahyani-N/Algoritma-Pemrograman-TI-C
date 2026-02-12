def bilPrima(n):
   listPrima = []

   for x in range(1, n+1):
      prima = True
      if x == 1:
         continue
      for y in range (2, x):
         if (x % y) == 0:
            prima = False
            break
      if prima:
         listPrima.append(x)  
   return (listPrima)

print('Bilangan-bilangan prima nya adalah ', bilPrima(50))