'''
Name: Marcos Hernandez (mah47)
CS 344
'''


from tools.aima.probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
climate = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy', {T: 0.1, F: 0.5}),
    ('Rain', 'Cloudy', {T: 0.8, F: 0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.9, (F, T): 0.9, (F, F): 0.0})
])

'''
i. P(Cloudy) = 0.5
= 0.5, 0.5
'''

print(enumeration_ask('Cloudy', dict(), climate).show_approx())

'''
ii.P(Sprinker | cloudy) = 0.1
= 0.1, 0.9
'''
print(enumeration_ask('Sprinkler', dict(Cloudy=T), climate).show_approx())

'''
iii. P(Cloudy| the sprinkler is running and it’s not raining) 
= ∝ * P(Sprinkler, ¬Rain | Cloudy * P(Cloudy)
= ∝ * 0.1 * 0.2 * 0.5
= ∝ * 0.01, 0.2
= 0.0476, 0.952
'''
print(enumeration_ask('Cloudy', dict(Sprinkler=T, Rain=F), climate).show_approx())

'''
iv.P(WetGrass | it’s cloudy, the sprinkler is running and it’s raining) = 0.99
= 0.01, 0.99
'''
print(enumeration_ask('WetGrass', dict(Cloudy=T, Sprinkler=T, Rain=T), climate).show_approx())


'''
v. P(Cloudy | the grass is not wet)
∝ * P(Cloudy, Sprinkler, Rain, ¬WetGrass)
= ∝ < 0.5((0.1 * 0.8 * 0.01) + (0.1 * 0.2 * 0.1) + (0.9 * 0.8 * 0.1) + (0.9 * 0.2 * 1)),
0.5 ((0.5 * 0.2 * 0.01) + (0.5 * 0.8 * 0.1) + (0.5 * 0.2 * 0.1) + (0.5 * 0.8 * 1))
= 0.361, 0.639
'''
print(enumeration_ask('Cloudy', dict(WetGrass=F), climate).show_approx())




