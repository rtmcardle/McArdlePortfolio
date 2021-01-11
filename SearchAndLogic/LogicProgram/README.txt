Ryan McArdle
12 Nov. 2019


The main class is defined in 'FamilyRelations.java'. Enter commands 'javac FamilyRelations.java' and 'java FamilyRelations' to run the code and get outputs for each of the requested predicates.

The folder '\family\' contains Domain and Knowledge Base Factory files. Domain lists all constants and used predicates. Knowledge Base lists given statements and relations, and the relations which can be used to infer more compex predicates (i.e. grandparent, aunt, uncle, etc.). 

The folder '\aima\' contains file for the AIMA code, for the purpose of avoiding complications and issues that could arise from CLASSPATH definitions. 

A predicate named Different() is used to explicitly differentiate between all of the defined constants and prevent undue self-relations, such that Sister(x,y) would not be satisfied by the substitution {x=Linda, y=Linda}.