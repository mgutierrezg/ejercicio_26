import numpy as np
import matplotlib.pyplot as plt 
import random 
def alcan(vo, theta):
    g = 9.8
    v_c = vo*vo
    arriba = v_c*np.sin(2*theta)
    d = arriba/g
    return d

# generamos los numeros aleatorios de vo entre 35 y 45
v0 = np.random.uniform(35,45,100000000)

#generamos lo numeros aleatorios de theta 0

theta_0 = np.random.uniform(0,np.pi/2,100000000)


#primer histograma

plt.hist(v0, normed= True, bins = 80)
plt.xlabel("Velocidad m/s")
plt.ylabel("Frecuencias")
plt.title("Histograma para v0")
plt.savefig("solo_v0.pdf")
plt.figure()

#d1 
d0 = alcan(v0, theta_0)
index = np.where( (d0 < 66) & (d0 > 57))
v1 = v0[index]

#segundo histograma

plt.hist(v1, normed= True, bins = 80)
plt.xlabel("Velocidad m/s")
plt.ylabel("Frecuencias")
plt.title("Histograma para v1")
plt.savefig("solo_v1.pdf")
plt.figure()

#d2
x = len(v1)
theta_1 =  np.random.uniform(0,np.pi/2,x)
d1 = alcan(v1, theta_1)
index1 = np.where( (d1 > 110) & (d1 < 120))
v2 = v1[index1]

#tercer histograma

plt.hist(v2, normed= True, bins = 80)
plt.xlabel("Velocidad m/s")
plt.ylabel("Frecuencias")
plt.title("Histograma para v2")
plt.savefig("solo_v2.pdf")
plt.figure()
    
#d3
x1 = len(v2)
theta_2 =  np.random.uniform(0,np.pi/2,x1)
d2 = alcan(v2, theta_2)
index2 = np.where( (d2 > 26) & (d2 < 36))
v3 = v2[index2]

#cuarto histograma

plt.hist(v3, normed= True, bins = 80)
plt.xlabel("Velocidad m/s")
plt.ylabel("Frecuencias")
plt.title("Histograma para v3")
plt.savefig("solo_v3.pdf")
plt.figure()

#d4
x2 = len(v3)
theta_3 =  np.random.uniform(0,np.pi/2,x2)
d3 = alcan(v3, theta_3)
index3 = np.where( (d3 > 172) & (d3 < 182))
v4 = v3[index3]

#quinto histograma

plt.hist(v4, normed= True, bins = 80)
plt.xlabel("Velocidad m/s")
plt.ylabel("Frecuencias")
plt.title("Histograma para v4")
plt.savefig("solo_v4.pdf")
plt.figure()
