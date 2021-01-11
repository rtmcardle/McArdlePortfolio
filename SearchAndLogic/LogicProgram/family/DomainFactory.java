package family;

import aima.core.logic.fol.domain.FOLDomain;

public class DomainFactory {

  public static FOLDomain familyDomain() {
    FOLDomain domain = new FOLDomain();
    domain.addConstant("Virginia");
    domain.addConstant("Barbara");
    domain.addConstant("Linda");
    domain.addConstant("Lisa");
    domain.addConstant("Danielle");

    domain.addConstant("Adam");
    domain.addConstant("Richard");
    domain.addConstant("Thomas");
    domain.addConstant("Jim");
    domain.addConstant("Ryan");

    domain.addPredicate("Parent");
    domain.addPredicate("Male");
    domain.addPredicate("Female");

    domain.addPredicate("Father");
    domain.addPredicate("Mother");
    domain.addPredicate("Grandparent");

    domain.addPredicate("Brother");
    domain.addPredicate("Sister");

    domain.addPredicate("Aunt");
    domain.addPredicate("Uncle");

    domain.addPredicate("Different");
    return domain;
  }
}
