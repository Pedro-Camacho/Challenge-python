import random
pilotos = ['Nick Cassidy', 'Pascal Wehrlein', 
           'Mitch Evans', 'Oliver Rowland', 
           'Jake Dennis', 'Jean-Éric Vergne', 
           'António Félix da Costa','Maximilian Gunther', 
           'Stoffel Vandoorne', 'Jake Highes',
           'Norman Nato', 'Sam Bird',
           'Sacha Fenestraz', 'Sébastien Buemi',
           'Robin Frijns', ' Nico Muller',
           'Dan ticktum', 'Sérgio Sette Câmara',
           'Jeahan Daruvala', 'Edoardo Mortara',
           'Nyck De Vries', ' Joel, Eriksson',
           'Lucas di Grassi', 'Kelvin Van Der Linde',
           'Jordan King', 'Paul Aron' ]

def sortear_carta():
    num= random.random(0, 22)
    print(num)
    
for i in range(10):
    sortear_carta()