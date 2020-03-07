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
sunny = BayesNet([
    ('Sunny', '', 0.07),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])


#A)
"""
Both Raise and Sunny are both independent, meaning that both do not influence each other
P(Raise | Sunny) 
= P(Raise) 
= 0.01, 0.99
"""
print('P(Raise | sunny): ')
print(enumeration_ask('Raise', dict(Sunny=T), sunny).show_approx())

"""
∝ * P(Happy | Sunny, Raise) * P(Raise)
= ∝ 1.0 * 0.01
= 0.0142, 0.986
"""
print('\nP(Raise | happy ∧ sunny): ')
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), sunny).show_approx())

#B)
print('\nP(Raise | happy): ')
print(enumeration_ask('Raise', dict(Happy=T), sunny).show_approx())

print('\nP(Raise | happy ∧ ¬sunny): ')
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), sunny).show_approx())


"""
Results do make sense because Raise has a small probability. Happy and Sunny have
high probabilities so it causes the probabilities to raise
"""