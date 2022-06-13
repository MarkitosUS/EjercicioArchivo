import os

nombre = "titulo.txt"

if not os.path.exists(nombre):
    open(nombre, "x")


with open(nombre, "w") as f:
    f.write(" r: lectura \n a: append \n w: escritura \n x: create \n t: texto \n b: binary")