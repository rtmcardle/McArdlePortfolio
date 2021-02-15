## !!!CAUTION!!!
The images produced by the Automandala class and the .gif recordings contained in the ./automatagifs/ directory may cause adverse reactions in photosensitive viewers. Please excercise caution before viewing. 

# Automandala
The class defined in [Automandala.py](./Automandala.py) creates a cellular automata using a square grid of binary cells which are initialized to their 'off' value. The cells near the center of the grid are initialized using a seed chosen from the [Seeds.py](./Seeds.py) file, and then a rule represented by a three-tuple defining critical values is given to the Automandala update() method to defines the activation and deactivation of cells upon their neighboring cells for each iteration of the simulation.

The result is a dynamic image which often seems to produce imitations of a naturally growing [mandala][1]. A sample of these images are available as .gif files in [automatagifs](./automatagifs/). This exploration of cellular automata was inspired by the exploration of complexity originating from simple rules in Stephen Wolfram's [A New Kind of Science][2].


[1]: https://en.wikipedia.org/wiki/Mandala
[2]: https://store.wolfram.com/view/book/ISBN1579550088.str
