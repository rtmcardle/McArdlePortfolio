package family;

import family.DomainFactory;

import aima.core.logic.fol.kb.FOLKnowledgeBase;
import aima.core.logic.fol.inference.InferenceProcedure;

public class KnowledgeBaseFactory {

  public static FOLKnowledgeBase createFamilyKnowledgeBase(
      InferenceProcedure infp) {
    FOLKnowledgeBase kb = new FOLKnowledgeBase(DomainFactory.familyDomain(),
        infp);

    //Symmetry of Different()
    kb.tell("FORALL x (FORALL y (Different(x,y) => Different(y,x)))");

    //Parental Relations
    kb.tell("FORALL x (FORALL y ((Parent(x,y) AND Female(x)) => Mother(x,y)))");
    kb.tell("FORALL x (FORALL y ((Parent(x,y) AND Male(x)) => Father(x,y)))");
    kb.tell("FORALL x (FORALL z (FORALL y (Parent(x,y) AND Parent(y,z) => Grandparent(x,z))))");

    //Sibling Relations
    kb.tell("FORALL z (FORALL y (FORALL x (FORALL w ((((Parent(w,y) AND Parent(w,z)) AND (Parent(x,y) AND Parent(x,z))) AND ((Different(y,z) AND Different(w,x)) AND Male(y)) => Brother(y,z))))))");
    kb.tell("FORALL z (FORALL y (FORALL x (FORALL w ((((Parent(w,y) AND Parent(w,z)) AND (Parent(x,y) AND Parent(x,z))) AND ((Different(y,z) AND Different(w,x)) AND Female(y)) => Sister(y,z))))))");

    //Parental Sibling Relations
    kb.tell("FORALL x (FORALL y (FORALL z ((Parent(x,y) AND Sister(z,x)) => Aunt(z,y))))");
    kb.tell("FORALL x (FORALL y (FORALL z ((Parent(x,y) AND Brother(z,x)) => Uncle(z,y))))");

    //KB Givens
    kb.tell("Female(Virginia)");
    kb.tell("Female(Barbara)");
    kb.tell("Female(Linda)");
    kb.tell("Female(Lisa)");
    kb.tell("Female(Danielle)");

    kb.tell("Male(Adam)");
    kb.tell("Male(Richard)");
    kb.tell("Male(Thomas)");
    kb.tell("Male(Jim)");
    kb.tell("Male(Ryan)");

    kb.tell("Parent(Virginia,Linda)");
    kb.tell("Parent(Virginia,Lisa)");
    kb.tell("Parent(Adam,Linda)");
    kb.tell("Parent(Adam,Lisa)");

    kb.tell("Parent(Barbara,Thomas)");
    kb.tell("Parent(Barbara,Jim)");
    kb.tell("Parent(Richard,Thomas)");
    kb.tell("Parent(Richard,Jim)");
    
    kb.tell("Parent(Linda,Danielle)");
    kb.tell("Parent(Linda,Ryan)");
    kb.tell("Parent(Thomas,Danielle)");
    kb.tell("Parent(Thomas,Ryan)");

    kb.tell("Different(Virginia,Barbara)");
    kb.tell("Different(Virginia,Linda)");
    kb.tell("Different(Virginia,Lisa)");
    kb.tell("Different(Virginia,Danielle)");
    kb.tell("Different(Virginia,Adam)");
    kb.tell("Different(Virginia,Richard)");
    kb.tell("Different(Virginia,Thomas)");
    kb.tell("Different(Virginia,Jim)");
    kb.tell("Different(Virginia,Ryan)");

    kb.tell("Different(Barbara,Linda)");
    kb.tell("Different(Barbara,Lisa)");
    kb.tell("Different(Barbara,Danielle)");
    kb.tell("Different(Barbara,Adam)");
    kb.tell("Different(Barbara,Richard)");
    kb.tell("Different(Barbara,Thomas)");
    kb.tell("Different(Barbara,Jim)");
    kb.tell("Different(Barbara,Ryan)");

    kb.tell("Different(Linda,Lisa)");
    kb.tell("Different(Linda,Danielle)");
    kb.tell("Different(Linda,Adam)");
    kb.tell("Different(Linda,Richard)");
    kb.tell("Different(Linda,Thomas)");
    kb.tell("Different(Linda,Jim)");
    kb.tell("Different(Linda,Ryan)");

    kb.tell("Different(Lisa,Danielle)");
    kb.tell("Different(Lisa,Adam)");
    kb.tell("Different(Lisa,Richard)");
    kb.tell("Different(Lisa,Thomas)");
    kb.tell("Different(Lisa,Jim)");
    kb.tell("Different(Lisa,Ryan)");

    kb.tell("Different(Danielle,Adam)");
    kb.tell("Different(Danielle,Richard)");
    kb.tell("Different(Danielle,Thomas)");
    kb.tell("Different(Danielle,Jim)");
    kb.tell("Different(Danielle,Ryan)");

    kb.tell("Different(Adam,Richard)");
    kb.tell("Different(Adam,Thomas)");
    kb.tell("Different(Adam,Jim)");
    kb.tell("Different(Adam,Ryan)");

    kb.tell("Different(Richard,Thomas)");
    kb.tell("Different(Richard,Jim)");
    kb.tell("Different(Richard,Ryan)");

    kb.tell("Different(Thomas,Jim)");
    kb.tell("Different(Thomas,Ryan)");

    kb.tell("Different(Jim,Ryan)");


    return kb;
  }
}
