import java.util.ArrayList;
import java.util.List;

import family.KnowledgeBaseFactory;
import family.DomainFactory;

import aima.core.logic.fol.StandardizeApartIndexicalFactory;
import aima.core.logic.fol.inference.FOLFCAsk;
import aima.core.logic.fol.inference.InferenceProcedure;
import aima.core.logic.fol.inference.InferenceResult;
import aima.core.logic.fol.inference.InferenceResultPrinter;
import aima.core.logic.fol.inference.proof.Proof;
import aima.core.logic.fol.inference.proof.ProofPrinter;
import aima.core.logic.fol.kb.FOLKnowledgeBase;
import aima.core.logic.fol.parsing.ast.Predicate;
import aima.core.logic.fol.parsing.ast.Term;
import aima.core.logic.fol.parsing.ast.Variable;

public class FamilyRelations {
	public static void main(String[] args) {
		family(new FOLFCAsk());
	}


	private static void family(InferenceProcedure ip) {
		StandardizeApartIndexicalFactory.flush();

		FOLKnowledgeBase kb = KnowledgeBaseFactory
				.createFamilyKnowledgeBase(ip);

		String kbStr = kb.toString();

		List<Term> terms = new ArrayList<Term>();
		terms.add(new Variable("x"));
		terms.add(new Variable("y"));

		List<Predicate> queries = new ArrayList<Predicate>();

		queries.add(new Predicate("Mother", terms));
		queries.add(new Predicate("Father", terms));
		queries.add(new Predicate("Grandparent", terms));
		queries.add(new Predicate("Sister", terms));
		queries.add(new Predicate("Brother", terms));
		queries.add(new Predicate("Aunt", terms));
		queries.add(new Predicate("Uncle", terms));

		System.out.println("Family Knowledge Base:");
		System.out.println(kbStr);

		for (Predicate query:queries) {
			InferenceResult answer = kb.ask(query);
			System.out.println("Query: " + query);
			InferenceResultPrinter printer = new InferenceResultPrinter();
			for (Proof p : answer.getProofs()) {
				System.out.println(ProofPrinter.printProof(p));
			}
		}
	}
}
