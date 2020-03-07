'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013

Name: Marcos Hernandez (mah47)
'''

from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

################################################################
#Lab 5

#P(Alarm | burglary ∧ ¬earthquake)
# 0.06, 0.94
print("P(Alarm | burglary ∧ ¬earthquake): ")
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

#P(John | burglary ∧ ¬earthquake)
"""
= 0.151, 0.849
"""
print("\nP(John | burglary ∧ ¬earthquake): ")
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

#P(Burglary | alarm)
"""
= 0.626, 0.374
"""
print("\nP(Burglary | alarm): ")
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

#P(Burglary | john ∧ mary)
""" 
0.716, 0.284
"""
print("\nP(Burglary | john ∧ mary): ")
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())



print('\n')
# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.

"""
Exercise 5.4
The results do match of those of the exact inference algorithm 
- enumeration_ask() and elimination_ask() get the same answer because both give a direct simplification. 
- enumeration_ask() calculates every variable when needed and elimination_ask() calculates one variable and stores the
result.
- gibbs_ask() simplifies the problem which it makes the program to find the right estimate of each probability.
Using gibbs_ask() is helpful, fast, and efficient for these kinds of problems.
"""