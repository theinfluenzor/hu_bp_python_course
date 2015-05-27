import matplotlib as mpl
import matplotlib.pylab as plt
from pylab import *

A0 = 3.0; B0 = 2.0; C0 = 2.5; D0 = 1.0; E0 = 1.5;  k1 = 0.2; k2 = 0.1; k3 = 0.3; k4 = 0.2; k5 = 0.12; k6 = 0.2; k7 = 0.1; dt = 0.1; count = 0; rounds = 1001
k8 = 0.3
resultsA = []
resultsB = []
resultsC = []
resultsD = []
resultsE = []

time_list = []
A = A0
B = B0
C = C0
D = D0
E = E0

def my_solver(A,B,C,D,E, dt):
    dA = (k3*A - (A*C*k4) - (A*B*k1))*dt
    dB = ((-B*C*k2) + (A*B*k1))*dt
    dC = ((A*C*k4) + (B*C*k2) - C*k5)*dt
    dD = (k6 * C - D*E*k7)*dt
    dE = (D*E*k7 - E*k8)*dt
    return dA, dB, dC, dD, dE

my_solver(A0,B0,C0,D0,E0,0.1)[0]
for count in xrange(rounds):
    resultsA.append(A)
    resultsB.append(B)
    resultsC.append(C)
    resultsD.append(D)
    resultsE.append(E)
    time_list.append(count*dt)
    A = A + my_solver(A,B,C,D,E,dt)[0]
    B = B + my_solver(A,B,C,D,E,dt)[1]
    C = C + my_solver(A,B,C,D,E,dt)[2]
    D = D + my_solver(A,B,C,D,E,dt)[3]
    E = E + my_solver(A,B,C,D,E,dt)[4]
    count += 1

test_dict = {'dna':{'time_course':resultsA, 'sequence':'ATATATAATTATA', 'mass':12.},
             'mrna_1':{'time_course':resultsB, 'sequence':'AUAUGCGUU', 'mass':13.},
             'mrna_2':{'time_course':resultsC, 'sequence':'AGAUGCG', 'mass':14.},
             'protein_1':{'time_course':resultsD, 'sequence':'WXY', 'mass':133.},
             'protein_2':{'time_course':resultsE, 'sequence':'WXYWX', 'mass':144.}}


#for key in test_dict.keys():
#    plt.plot(time_list, test_dict[key]['time_course'], label = key)
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#plt.show()
