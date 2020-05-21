import numpy as np
import matplotlib.pyplot as plt
mass = []
mass_two=[]
time = []
time_avg = []
time_pow = []
accel = []
delta_accel = []
delta_accel_avg = []
n = 0
mass_n = (int(input('Enter number of masses : ')))
number_mass = 1
for k in range(mass_n):
    mass.append(float(input('Enter mass :' )))
    print(mass)
n_time = int(input('Enter number of time value : ' ))
v_time = n_time*len(mass)
print(v_time)
while n < v_time:
    time.append(float(input('Enter registered time')))
    print(time)
    n+=1
time = np.array(time)
time = time.reshape(mass_n, n_time)
print(time)
for x in range(mass_n):
    avg_time = sum(time[x])
    time_avg.append(avg_time/len(time[x]))
    print('The average time for each mass is : ', time_avg[x])
print(time_avg)
ind = 0
while ind < len(time_avg):
    accel.append(2*mass[ind]/time_avg[ind]**2)
    print('Acceleration value: ', accel[ind])
    ind+=1
accel_avg = sum(accel)/len(accel)
print('Acceleration values are', accel)
print('Average acceleration is ' , accel_avg)   
for y in range(len(accel)):
    delta_accel_avg = accel[y]/accel_avg
    delta_accel.append(delta_accel_avg)
print('Delta aceleration is' , delta_accel)
for k in range(len(delta_accel)):
    delta_accel_pow = []
    delta_accel_pow.append(delta_accel[k]**2)
    print('Delta acc by the power of 2', delta_accel_pow)
for j in range(len(time_avg)):
    time_pow.append(time_avg[j]**2)
    print('Time by pow of 2 ',time_pow[j])
for g in range(len(mass)):
    mass_two.append(mass[g]*2)
    print('The mass multiplied by two is', mass_two[g])
plt.style.use('fivethirtyeight') #visualisation part
plt.plot(time_pow, mass_two , color='black', marker='x',linestyle='dashed',markerfacecolor='yellow', mew= 2, markersize=16,label = 'Acceleration')
plt.xlabel('Time')
plt.ylabel('Mass')
plt.legend()
plt.grid(True)
plt.show()
