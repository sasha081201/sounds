import numpy as np
import matplotlib.pyplot as plt
import math

t=int(input("введите: температуру в градусах "))
T=t+273.15
#f=float(input(" введите абсолютню влажность в СГС "))
mh20=18.01
fi=float(input(" влажность в процентах "))
Pa=101325
Pa=Pa+133.322*t
#подсчет давления водяныз паров
Ps=6.1121*math.exp((18.678-T/234.5)*T/(257.14+T))
Ph2o=Ps*fi/100
R=8.314 
xh2o=Ph2o/R/T
print(xh2o)
#xh2o=f/mh20
#print(xh2o)

#___________________________________________________________________________________________

def ss(t,xh2o,x,Ph2o):
    m1=28.97 # в граммах
    mh20=18.01
    mco2=44.01
    Cp1=1.0036
    Cph2o=1.863
    Cpco2=0.838
    Cv1=0.7166
    Cvh2o=1.403
    Cvco2=0.649
    Pa=101325
    R=8.314  
    T=t+273.15
    Pa=Pa+133.322*t
    x1=(Pa-Ph2o)/R/T
    x1=x1/(x1+xh2o)-x
    xh2o=1-x1-x
    #подсчет молярной массы смеси
    mu=(x1*m1+xh2o*mh20+x*mco2)*0.001
    # подсчет гаммы
    gamma=(Cp1*x1*m1+Cph2o*xh2o*mh20+Cpco2*mco2*x)/(Cv1*x1*m1+Cvh2o*xh2o*mh20+Cvco2*x*mco2)
    #подсчет скорости
    a=math.sqrt(gamma*R*T/mu)
    return(a)
#______________________________________________________________________________________________

def speedOfSound(t, xh2o, co2Max,dot,Ph2o):
    co2X = []
    soundSpeed = []
    dot=int(dot)
    for i in range(0,dot+1):
        co2X.append(co2Max*i/dot)
        soundSpeed.append(ss(t,xh2o,co2Max*i/dot,Ph2o))
    #print(co2X, soundSpeed)
    mesure_str=[str(item) for item in soundSpeed]
    with open("da.txt","w") as outfile:
        outfile.write("\n".join(mesure_str))
    return soundSpeed
#___________________________________________________________________________________________________

co2Max=float(input("введите пердельную долю углерода"))
dot=int(input("число точек "))-1
co2X = []
for i in range(0,dot+1):
        co2X.append(co2Max*i*100/dot)
#speedOfSound(t,xh2o,co2Max,dot)
#________________________________________________________________________________________________________
fig, ax = plt.subplots(figsize=(10,10), dpi=100)
ax.plot(co2X, speedOfSound(t,xh2o,co2Max,dot,Ph2o),label='Аналититическая зависимость')
#________________________________________________________________________________________________________
k=(speedOfSound(t,xh2o,0.2,3,Ph2o)[0]-speedOfSound(t,xh2o,0.2,3,Ph2o)[3])/20
#print(speedOfSound(t,xh2o,0.2,3,Ph2o)[0])
#print(speedOfSound(t,xh2o,0.2,3,Ph2o)[3])
print('Коэффициент наклона прямой',k)
b=speedOfSound(t,xh2o,0.2,3,Ph2o)[0]
#________________________________________________________________________________________________________
a=1158/float(input("Введите время прохождения звука в воздухе (мс) "))
b2=(b-a)/k
#print(b2)
s1='Значения в воздухе '+str(int(a*10)/10)+' [м.с], '+str(int(b2*10)/10)+'[%]'
ax.plot(b2,a,"c", linewidth = '1.0', marker = '>', markevery=50, markersize = '12.0',label=s1)
a1=1158/float(input("Введите время прохождения звука в выдызаемом воздухе (мс) "))
b1=(b-a1)/k
#print(b1)
s2='Значение в выдохе'+str(int(a1*10)/10)+' [м.с], '+str(int(b1*10)/10)+'[%]'
ax.plot(b1,a1,"m", linewidth = '1.0', marker = '<', markevery=50, markersize = '12.0',label=s2)
plt.minorticks_on()
plt.title("Зависимость скорости звука от концентрации углекислого газа", fontstyle = 'italic', horizontalalignment = 'center')
plt.xlabel('Концентрация $CO_2$[%]')
plt.ylabel("Скорость звука [м/с]")
ax.legend()
plt.grid(which='major', color='green', linestyle='-', linewidth = 0.5)
plt.grid(which='minor', linestyle='--', linewidth = 0.25)
plt.show()
fig.savefig('laba_vlazhnosti.pdf')

