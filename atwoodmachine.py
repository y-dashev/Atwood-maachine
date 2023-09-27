import numpy as np
import matplotlib.pyplot as plt

mass = []
time = []
time_avg = []
accel = []

mass_n = int(input('Enter number of masses: '))

for k in range(mass_n):
    mass.append(float(input(f'Enter mass {k + 1}: ')))

n_time = int(input('Enter number of time values: '))

v_time = n_time * mass_n

for n in range(v_time):
    time.append(float(input(f'Enter registered time {n + 1}: ')))

time = np.array(time).reshape(mass_n, n_time)

for x in range(mass_n):
    avg_time = np.mean(time[x])
    time_avg.append(avg_time)
    print(f'The average time for mass {x + 1} is: {avg_time:.2f} seconds')

for ind in range(mass_n):
    accel.append(2 * mass[ind] / (time_avg[ind] ** 2))
    print(f'Acceleration for mass {ind + 1} is: {accel[ind]:.2f} m/s^2')

accel_avg = np.mean(accel)
print(f'Average acceleration for all masses is: {accel_avg:.2f} m/s^2')

mass_two = [2 * m for m in mass]

plt.style.use('fivethirtyeight')
plt.plot([t ** 2 for t in time_avg], mass_two, color='black', marker='x', linestyle='dashed', markerfacecolor='yellow', mew=2, markersize=16, label='Acceleration')
plt.xlabel('Time^2 (s^2)')
plt.ylabel('Mass (kg)')
plt.legend()
plt.grid(True)
plt.show()
