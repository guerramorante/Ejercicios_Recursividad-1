col = str(input('Introduce los colores (R), (V), (Otros), (A): '))
color = col.upper()
r  = 0
v = 0
a = len(color) - 1
colores = []
for j in range(0, a+1):
  colores.append(color[j:j+1])
while(v<=a):
  if(colores[v] == 'R'):
    v = v + 1
  else:
    if(colores[v] == 'R'):
      aux = colores[v]
      colores[v] = colores[r]
      colores[r] = aux
      v = v + 1
      r = r + 1
      