# License
'''
Code by Laxman Reddy
April 22,2020
Released under GNU GPL
'''

#Bode plot using scipy in python
from scipy import signal
import matplotlib.pyplot as plt
from pylab import*
import control
from control import tf

#if using termux
import subprocess
import shlex
#end if



#Defining the transfer function 
s1 = signal.lti([98,98*1.28], [1,13.6,63.2,118.6,76.8,0]) #Transfer Function = 98(s+ 1.28)/(s+2)(s+4)(s+6)(s+1.6)

#signal.bode takes transfer function as input and returns frequency,magnitude and phase arrays
w,mag,phase = signal.bode(s1)

sys = tf([98,98*1.28], [1,13.6,63.2,118.6,76.8,0])
gm, pm, Wpc, Wgc = control.margin(sys)



subplot(2,1,1)
#plt.xlabel('Frequency(rad/s)')
plt.ylabel('Magnitude(deg)')
# plt.title('Magnitude plot')
plt.semilogx(w, mag,'b')        # Bode Magnitude plot
# plt.axhline(y = 0,xmin=0,xmax= .35,color = 'r',linestyle='dashed')
# plt.axvline(x = .22,ymin=0,color='k',linestyle='dashed')
plt.axvline(x = 1.38,ymin=0,color='k',linestyle='dashed')
plt.axhline(y = 0,xmin=0,color = 'r',linestyle='dashed')


plt.plot(1.38,0,'o')
plt.text(1.5,8, '({}, {})'. format( 1.38,0 ) )
# plt.grid() 
plt.title("C(s)G(s)")
subplot(2,1,2)
plt.xlabel('Frequency(rad/s)')
plt.ylabel('Phase(deg)')
# plt.title('Phase plot')
plt.semilogx(w,phase)          # Bode phase plot
plt.axhline(y = -150.2,xmin=0,color = 'r',linestyle='dashed')
plt.axvline(x = 1.38,ymin=0,color='k',linestyle='dashed')

plt.plot(1.38,-150.2,'o')
plt.text(1.5,-140, '({}, {})'.format ( 1.38,-150.2 ))
# plt.grid() 
print("Phase Margin = ",pm)
print("Gain crossover freq = ",Wgc)



# if using termux
plt.savefig('./figs/ee18btech11049/ee18btech11049_2.pdf')
plt.savefig('./figs/ee18btech11049/ee18btech11049_2.eps')
subprocess.run(shlex.split("termux-open ./figs/ee18btech11049/ee18btech11049_2.pdf"))
# else
# plt.show()