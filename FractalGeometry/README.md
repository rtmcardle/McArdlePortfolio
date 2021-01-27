# Fractal Geometry
This directory showcases the drawing of a number of recursively defined and self-similar structures. The [TurtleFractal](Fractals.py) class excutes the various drawings to a given recursive depth depending on the method called and can save the image to a .png file. Copies of these .png images for each of the methods are stored in [Images](Images/). The bulk of these algorithms are derived from Gerald Edgar's [Measure, Topology, and Fractal Geometry][1]. Some methods serve as support methods for those that execute the actual drawing of the objects. 

Each of the images and their relevant methods are discussed below.

## [Barnsley Fern](Images/BarnsFern.png)
This iterated function system begins at a point near the bottom-middle of the screen, then chooses with random weight a transformation to translate the location of the point. At each location, the turtle 'stamps' the canvas beneath it and leaving a dot, imitating a stipling technique. The transformations are defined such that the resulting collection of points as the number of transformations goes to infinity is a fern-shaped area known as the [Barnsley Fern][7]. 

## [Barnsley Leaf](Images/BarnsleyLeaf.png)
This method defines a straight-line drawing implementation of the Barnsley Leaf. This method is interesting to watch with the turtle visible, as it often retraces its steps and rotates quite a lot to achieve this image.

## [Eisenstein Boundary](Images/EisensteinBoundary.png)
This boundary encloses the limit of the Eisenstein Fractions. These fractions alongside the Eisenstein Integers (the algebraic integers of the quadratice number field Q(sqrt(3), i.e., 'the rationals adjoined root 3') allow a method for [representing any complex number in the plane][2]. 

## [Fibonacci Spiral](Images/FibonacciSpiral.png)
This method approximates the Golden Spiral by calculating Fibonacci numbers, drawing adjoined squares with side lengths equal to the successive Fibonacci numbers, and drawing a quarter-circle within the square. This process continues until the computer can no long distinguish the difference between the ratio of the Fibonacci numbers and the limit of that ratio, (1+sqrt(5))/2.

## [Heighway Pinwheel](Images/HeighwayPinwheel.png)
This object is constructed via four [Heighway Dragons][3] which radiate outwards from the origin at right angles. From this image, one can see that in the limit that the length of the dragon curve goes to infinity (and the recursive depth of the drawing program also goes to infinity), this curve will fill or tile the plane. 

## [Koch Snowflake](Images/KochSnowFlake.png)
[The Koch Snowflake][4] can be defined as the result of the iterative process in which one begins with a triangle, then for each straight line in the object, replace the middle third of that line with two sides of an equilateral triangle. The result is a curve which has an infinite perimeter yet contains a finite area. 

## [Pentadendrite](Images/Pentadendrite.png)
This shape is defined in Edgar's work by modifying and repeating [McWorter's Pentigree][5] in order to create a radially symmetric 'dendrite.' 

## [Sierpinski Gasket](Images/SierpinskiGasket.png)
This curve approximates the [Sierpinski Gasket][6], which can be derived by beginning with a filled equilateral triangle, removing a center triangle from the original, and repeating this process on the three remaining triangular areas. The resulting object has a defined shape with infinite perimeter yet containing zero area.






[1]: https://www.springer.com/gp/book/9780387747484
[2]: https://link.springer.com/article/10.1007/s00283-014-9504-y
[3]: https://en.wikipedia.org/wiki/Dragon_curve
[4]: https://en.wikipedia.org/wiki/Koch_snowflake
[5]: https://larryriddle.agnesscott.org/ifs/pentigre/pentigre2.htm
[6]: https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle
[7]: https://en.wikipedia.org/wiki/Barnsley_fern
