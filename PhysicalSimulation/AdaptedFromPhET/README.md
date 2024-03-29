# Adapted from PhET
Contained in this directory is an adaptation of a [PhET][1] simulation.

## [Vector Addition](./VectorAddition_AdaptedFromPhET.html)
The file [VectorAddition_AdaptedFromPhET.html](./VectorAddition_AdaptedFromPhET.html) is the compiled and published version of a customized simulation for exploring the properties of vector addition. Hosted preview of the file coming soon. [vector-addition](./vector-addition) contains my edited version of the JavaScript source code. The original source code is available at [this][2] PhET GitHub repository and relies on many other repositories under the [phetsims][3] GitHub account.

One modification is made to unlock the restriction located in the [Vector class](./vector-addition/js/common/model/Vector.js) which causes vectors to snap to integer values on the grid. Another modification is made to [VectorAdditionConstants](./vector-addition/js/common/VectorAdditionConstants.js) which increases the precision for all displayed values to two decimal places. Both edits allow for greater accuracy when drawing vectors and improves the ability of the simulation to model real-world scenarios.

This modification increases the viability of the simulation as an online replacement for in-person physics lab experiments due to remote/hybrid course offerings at The University of Georgia during the COVID-19 pandemic. 


[1]: https://phet.colorado.edu/
[2]: https://github.com/phetsims/vector-addition
[3]: https://github.com/phetsims
