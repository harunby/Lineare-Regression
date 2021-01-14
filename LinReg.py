# DIE NÖTIGEN LIBRARIES IMPLEMENTIEREN
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATENSATZ LADEN
df = pd.read_csv("autos_prepared.csv")

# DIE SPALTEN MIT DER KILOMETER ANZAHL UND DEM PREIS EXTRAHIEREN
# DIESE VERWENDEN WIR FÜR DIE VORHERSAGE DES PREISES
points = df[["kilometer", "price"]].values

# DEFINITION DER LINEAREN FUNKTION
def f(a, b, x):
    return a * x + b

# DEFINITION DER KOSTENFUNKTION
def J(a, b, x, y):
    return np.mean((y - (a * x + b))**2)


def J_ableitung_a(a, b, x, y):
    return np.mean(-2 * x * (-a * x -b + y))


def J_ableitung_b(a, b, x, y):
    return np.mean(((-2) * (((-a) * x) -b + y)))


lr = 0.0000000000005

a = 1
b = 1

 
for i in range(0, 10000):

    da = J_ableitung_a(a, b, points[:,0], points[:,1])
    db = J_ableitung_b(a, b, points[:,0], points[:,1])
    a = a - lr * da
    b = b - lr * db * 1e10 # angepasst, da die Daten nicht skaliert sind

    cost = J(a, b, points[:,0], points[:,1])

    print(str(i) + ": Kosten wenn a = " + str(a) + ": " + str(cost))


xs = np.arange(0, 130000, 1000)

ys = f(a, b, xs)

plt.plot(xs, ys)

 
plt.scatter(points[:,0], points[:,1])

plt.show()