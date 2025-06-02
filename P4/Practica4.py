import numpy as np
from matplotlib import pyplot as plt


def convolucion(x,h):
    #Se define una matriz de 0's de tamaño x,h+exceso para la convolucion
    V=np.zeros((len(x),len(h)+len(x)))

    #Se itera en un for anidado
    for i in range(len(x)):
        for j in range(len(h)):
            V[i][j+i]=(h[j]*x[i])   #Producto de cada valor de x con cada valor de h

    return sum(V)   #Se retorna la suma por columnas de la matriz resultante




def correlacion(x,y,n):
    r=list(np.zeros(n))   #Se define el arreglo de la señal de salida

    y=y[:]  #Genera una copia de y
    k=n//2      #Exceso
    for i in range(k):  #Se añaden 0's a los extremos de la señal y
        y.insert(0,0)
        y.insert(len(y),0)

    """
    Se aplica un producto punto para la suma de productos
    De tal forma que cada producto resulte en un valor de r 
    """
    for l in range(-k,k+1):    #Se itera de -k a k pasando por 0
        r[k+l]=np.dot(x,y[k-l:(k-l)+len(x)])    #Producto punto de la señal desplazada L unidades
    
    return r


#CONVOLUCION
#Se define el intervalo de n
nx= np.arange(-3, 4, 1)   
#Se declara la señal x1 como una funcion por partes
x1=np.piecewise(nx, [nx == 0, nx ==1,nx==2,nx<0,nx>2], [2,3,2,0,0])

#Se define el intervalo de n
nh=np.arange(-2, 3, 1)     
#Se declara la señal h como una funcion por partes 
h=np.piecewise(nh, [nh == 1, nh ==-1,nh==0,nh<-1,nh>1], [1,1,2,0,0])


#Se aplica la convolucion a la primer señal X
y=convolucion(x1,h)
print("Señal x[n]:",x1)
print("Señal h[n]:",h)
print("Suma de convolucion:",y)


#Se plotean las señales
plt.figure(figsize=(12,4))
plt.suptitle("Convolucion")
plt.subplot(1,3,1),plt.stem(nx,x1),plt.title("Señal x[n]")
plt.subplot(1,3,2),plt.stem(nh,h),plt.title("Señal h[n]")
plt.subplot(1,3,3),plt.stem(np.arange(-(len(y)//2),(len(y)//2), 1),y),plt.title("Señal y[n]")
plt.show()




#CORRELACION
n=9     #Tamaño de la muestra (impar)
x2=[2,-1,3,7,1,2,-3] #Señal x2
y=[1,-1,2,-2,4,1,-2,5]  #Señal y

#Se aplica la correlacion a la nueva señal X
r=correlacion(x2,y,n)

print("Señal x[n]:",x2)
print("Señal y[n]:",y)
print("Correlacion rxy",r)

#Se definene los intervalos para graficar cada señal
nx=np.linspace(-(len(x2)//2)-1,(len(x2)//2), len(x2))
ny=np.linspace(-(len(y)//2)-1,(len(y)//2), len(y))
nr=np.arange(-(n//2),(n//2)+1, 1)

#Se plotean las señales
plt.figure(figsize=(12,4))
plt.suptitle("Correlacion XY")
plt.subplot(1,3,1),plt.stem(nx,x2),plt.title("Señal x[n]")
plt.subplot(1,3,2),plt.stem(ny,y),plt.title("Señal y[n]")
plt.subplot(1,3,3),plt.stem(nr,r),plt.title("Señal r[n]")
plt.show()