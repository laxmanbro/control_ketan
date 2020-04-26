# License
'''
Code by Laxman Reddy
April 26,2020
Released under GNU GPL
'''
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
# import control
# from control import tf



#if using termux
import subprocess
import shlex
#end if

#Defining the transfer function 
s1 = signal.lti([1,1.28], [1,1.6]) #Transfer Function = (s+ 1.28)/(s+1.6)

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

# sys = tf([1,1.28], [1,1.6])
# gm, pm, Wpc, Wgc = control.margin(sys)

subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
# plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
# plt.axhline(y = 0,xmin=0,xmax= .35,color = 'r',linestyle='dashed')
# plt.axvline(x = .22,ymin=0,color='k',linestyle='dashed')

plt.grid() 
plt.axvline(x = 1.49,ymin=0,color='k',linestyle='dashed')
plt.axhline(y =-0.95,xmin=0,color = 'r',linestyle='dashed')
plt.plot(1.49,-0.95,'o')
plt.text(1.6,-1.2, '({}, {})'.format(1.49,-0.95))


plt.title("Lead Compensator C(s)")
subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
# plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.axhline(y = 6.45,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 1.49,ymin=0,color='k',linestyle='dashed')
plt.plot(1.49,6.45,'o')
plt.text(2,5.8, '({}, {})'.format(1.49,6.45))
plt.grid() 
# print("Phase Margin = ",pm)
# print("Gain crossover freq = ",Wgc)




# #if using termux
plt.savefig('./figs/ee18btech11049/ee18btech11049_1.pdf')
plt.savefig('./figs/ee18btech11049/ee18btech11049_1.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11049/ee18btech11049_1.pdf"))
#else
# plt.show()
