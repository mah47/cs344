'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden
@version Jan 1, 2013

Marcos Hernandez
Feb 29, 2020
'''

from tools.aima.probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P) #change Toothcache to cavity to get answer
print(PC.show_approx())

'''
Exercise 4.1
B)
i. 0.108 / 0.34 = 0.529
  P(Cavity | catch) = P(Cavity and catch)
ii. False: 0.471, True: 0.529
'''
P = JointProbDist(['Coin1','Coin2'])
Heads, Tails = True, False
P[T, T] = 0.25
P[F, T] = 0.25
P[T, F] = 0.25
P[F, F] = 0.25

PC = enumerate_joint_ask('Coin2', {'Coin1': Heads}, P)
print(PC.show_approx())

'''
Answer does confirm what I believe to be true about probability.
Flipping a coin is independent. Chances of getting heads or tails are 50%. or on other words
each flip is 0.5/0.5 split
'''