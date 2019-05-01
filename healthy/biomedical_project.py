import matplotlib.pyplot as plt


file = open('Data1.txt','r')
input = file.read().split('\n')

time = [0]
#parse input to array
for i in range (len(input)):
    if input[i] != '':
        input[i] = float(input[i])
    else:
        del(input[i])
# print(input)
for i in range (len(input)):
    time.append(time[i]+(1/512))

del time[len(time)-1]

plt.plot(time,input)
plt.show()

T = 1/512
derivative = []
for x in range(len(input)-2):
    if x == 0 or x == 1:
        continue
    else:
        derivative.append((1/8*T)*(-input[x-2]-2*input[x-1]+2*input[x+1]+input[x+2]))

del(time[-4:])
plt.plot (time,derivative)
plt.show()

square = []
for x in derivative:
    square.append(x*x)

plt.plot(time,square)
plt.show()

smoothed = []
for i in range(30 ,len(square)):
    smoothed.append(0)
    for j in range (31):
        smoothed [i - 30] += square [i-j]
    smoothed [i-30] *= 1/31

del (time[-30:])
plt.plot(time,smoothed)
plt.show()

Am = []

for i in range (len(smoothed)):
    Am.append(0)
    for j in range (i, len(smoothed)):
        if i+j < len(smoothed):
            Am[i] += smoothed[j+i]*smoothed[j]



for i in range (len(Am)):
    if i == 0:
        continue
    Am[i] /= Am[0]

Am[0] = 1

feb_rate = 0
for i in Am:
    if i > 0.1:
        feb_rate += 1

print (feb_rate)


plt.plot(time,Am)
plt.show()
