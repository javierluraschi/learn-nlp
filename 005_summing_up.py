import re

##Abrir y trabajar con txt
with open('texto.txt', encoding = 'utf-8') as t:
    texto = t.read()

#equivalente a:
doc = open('texto.txt', encoding = 'utf-8')
tex = doc.read()
doc.close() #No olvidar cerrar el archivo!!!

#Hay diferentes modos para abrir el archivo 
#r - read - (default) | a - adding | w - write | x - create file 
with open('texto.txt', 'r', encoding = 'utf-8') as t:
    texto = t.read()
    #t.write('Escribir una oracion mas.')
    
with open('texto.txt', 'w', encoding = 'utf-8') as t:
    t.write('Si escribo esto desaparece lo que tenia escrito. ')

with open('texto.txt', 'r', encoding = 'utf-8') as t:
    texto = t.read()
    
with open('texto.txt', 'a', encoding = 'utf-8') as t:
    t.write('Pero si lo escribo asi, si se mantiene. ')
    
with open('texto.txt', 'r', encoding = 'utf-8') as t:
    texto = t.read()
    
#Tambien se pueden combinar con +    
with open('texto.txt', 'r+', encoding = 'utf-8') as t:
    t.write('Quiero cambiar lo que dice el documento')
    #t.seek(0)
    texto= t.read()
    print(texto)

    
##Recordatorio de cosas vistas
with open('text.txt', 'r', encoding = 'utf-8') as t:
    doc = t.read()
    #t.seek(0)  #Importante incluir
    doc_lines = t.readlines()

print(doc.split())
print(f'El texto tiene {len(doc.split())} palabras y {len(doc_lines)} lineas')

#extraer los numeros del texto
p1 = '[0-9]+'
numeros = re.findall(p1, doc)
print(numeros)

p2 = '\d{4}'
anios = re.findall(p2, doc)
print(anios)

doc_sin_numeros = re.sub('[0-9]', '*', doc, re.DOTALL)

with open('doc_edit.txt', "w") as f:
    f.write(f'Los numeros que aparecen en el texto son: {numeros}')
    



    




