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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.9, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.9, F: 0.2}),
    ])

"""
Calculations:
∝ * P(Test1, Test2 | Cancer) * P(Cancer)
= ∝ * P(Test1 | Cancer) * P(Test2 | C) * P(Cancer)
= ∝ * 0.9 * 0.9 * 0.01
= 0.17, 0.83
"""
print('P(Cancer | positive results on both tests): ')
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

"""
Calculations:
∝ * P(Test1, ¬Test2 | Cancer) * P(Cancer)
= ∝ * P(Test1 | Cancer) * P(¬Test2 | Cancer) * P(Cancer)
= ∝ * 0.9 * 0.2 * 0.01
= 0.00565, 0.99435
"""

print('\nP(Cancer | a positive result on test 1, but a negative result on test 2): ')
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())


"""
The results do make sense because there is a low chance(0.01) of having cancer
and the probability for each test determining if there is cancer is high (0.9).

Multiplying the probability in Test1 and Test2 gives a positive result.
"""