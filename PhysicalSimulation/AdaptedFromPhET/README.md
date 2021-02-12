# Adapted from PhET
Contained in this directory is an adaptation of a [PhET][1] simulation published into a single .html document.

## [Vector Addition](./VectorAddition_AdaptedFromPhET.html)
This file is the compiled and published version of a customized simulation for exploring the properties of vector addition. GitHub Pages hosting of the file coming soon. The original JavaScript is available at [this][2] PhET GitHub repository and relies on many other repositories under the [phetsims][3] GitHub account.

The modifications made unlock the restriction located in the [Vector](./vector-addition/js/common/model/Vector.js) class which causes vectors to snap to interger values on the grid and increase the precision for all displayed values to two decimal places. This allows for greater accuracy when drawing vectors and improves the ability of the simulation to model real-world scenarios.

This modification increases the viability of the simulation as an online replacement for in-person physics lab experiments due to remote/hybrid course offerings at The University of Georgia during the COVID-19 pandemic. 


[1]: https://phet.colorado.edu/
[2]: https://github.com/phetsims/vector-addition
[3]: https://github.com/phetsims
