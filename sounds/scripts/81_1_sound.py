
import math

t=int(input("введите: температуру в градусах "))
f=float(input(" введите абсолютню влажность в СГС "))
def soun1without_co2(t,f):
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
    #подсчет давления водяныз паров
    Ph2o=f/mh20*T*R
    #поик отношения концентраций (без со2)
    nh2o=f/mh20
    n1=(Pa-Ph2o)/R/T
    #подсчет молярной массы смеси
    mu=(n1*m1/(n1+nh2o)+nh2o*mh20/(n1+nh2o))*0.001
    # подсчет гаммы
    gamma=(Cp1*n1*m1/(n1+nh2o)+Cph2o*nh2o*mh20/(n1+nh2o))/(Cv1*n1*m1/(n1+nh2o)+Cvh2o*nh2o*mh20/(n1+nh2o))
    #подсчет скорости
    a=math.sqrt(gamma*R*T/mu)
    return(a)
print(soun1without_co2(t,f))
