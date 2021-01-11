/**
 * Ryan McArdle
 * 9/2/19
 **/

import java.util.*;
import java.lang.String;

class JavaBasics {

  public static void main (String[] args) {

    //Demonstrates my_intersection
    ArrayList<Character> my_intersection_list1 = new ArrayList<Character>(Arrays.asList('e','d','d','f','g','g'));
    ArrayList<Character> my_intersection_list2 = new ArrayList<Character>(Arrays.asList('d','d','g','j'));

    System.out.println("\nmy_intersection\n");
    System.out.println("list1: "+my_intersection_list1);
    System.out.println("list2: "+my_intersection_list2);

    System.out.println("\nIntersection: "+my_intersection(my_intersection_list1,my_intersection_list2));


    //Demonstrates my_union
    ArrayList<Object> my_union_list1 = new ArrayList<Object>(Arrays.asList("e","d","d","f","g","g"));
    ArrayList<Object> my_union_list2 = new ArrayList<Object>(Arrays.asList("d","d","g","j"));

    System.out.println("\n\n\nmy_union\n");
    System.out.println("list1: "+my_union_list1);
    System.out.println("list2: "+my_union_list2);

    System.out.println("\nUnion: "+my_union(my_union_list1,my_union_list2));


    //Demonstrates addvec
    ArrayList<Integer> addvec_list = new ArrayList<Integer>(Arrays.asList(2,3,4));

    System.out.println("\n\n\naddvec\n");
    System.out.println("list: "+addvec_list);

    System.out.println("\nSum: "+addvec(addvec_list));


    //Demonstrates vecmul
    ArrayList<Integer> vecmul_list1 = new ArrayList<Integer>(Arrays.asList(2,3,4,5));
    ArrayList<Integer> vecmul_list2 = new ArrayList<Integer>(Arrays.asList(1,4,5,2,14));

    System.out.println("\n\n\nvecmul\n");
    System.out.println("list1: "+vecmul_list1);
    System.out.println("list2: "+vecmul_list2);

    System.out.println("\nProduct: "+vecmul(vecmul_list1,vecmul_list2));


    //Demonstrates innprod
    ArrayList<Integer> innprod_list1 = new ArrayList<Integer>(Arrays.asList(1,2,3,4));
    ArrayList<Integer> innprod_list2 = new ArrayList<Integer>(Arrays.asList(7,8,9));

    System.out.println("\n\n\ninnprod\n");
    System.out.println("list1 = "+innprod_list1);
    System.out.println("list2 = "+innprod_list2);

    System.out.println("\nInner Product = "+innprod(innprod_list1,innprod_list2));


    //Demonstrates occurences
    ArrayList<Object> occurences_list_1 = new ArrayList<Object>(Arrays.asList('a','a','b','a','c','c','d','d'));
    ArrayList<Object> occurences_list_2 = new ArrayList<Object>(Arrays.asList('a','a',Arrays.asList('b'),'a','c','c','d',Arrays.asList('c',Arrays.asList('d')),Arrays.asList('b'),'b','d'));

    System.out.println("\n\n\noccurences\n");
    System.out.println("list1 = "+occurences_list_1);
    System.out.println("Occurences = "+occurences(occurences_list_1));

    System.out.println("\nlist2 = "+occurences_list_2);
    System.out.println("Occurences = "+occurences(occurences_list_2));


    //Demonstrates my_trianglenos
    ArrayList<Integer> my_trianglenos_list1 = new ArrayList<Integer>(Arrays.asList(1,3,6,10,15,21));
    ArrayList<Integer> my_trianglenos_list2 = new ArrayList<Integer>(Arrays.asList(66,36,190));
    ArrayList<Integer> my_trianglenos_list3 = new ArrayList<Integer>(Arrays.asList(1,2,3));

    System.out.println("\n\n\nmy_trinanglenos\n");
    System.out.println("list1 = "+my_trianglenos_list1);
    System.out.println(my_trianglenos(my_trianglenos_list1));

    System.out.println("\nlist2 = "+my_trianglenos_list2);
    System.out.println(my_trianglenos(my_trianglenos_list2));

    System.out.println("\nlist3 = "+my_trianglenos_list3);
    System.out.println(my_trianglenos(my_trianglenos_list3));


    //Demonstrates number_embed
    ArrayList<Object> number_embed_list1 = new ArrayList<Object>(Arrays.asList('a','b','c'));

    ArrayList<Character> list21 = new ArrayList<Character>(Arrays.asList('2'));
    ArrayList<Character> list22 = new ArrayList<Character>(Arrays.asList('a','b','c'));
    ArrayList<Object> number_embed_list2 = new ArrayList<Object>(Arrays.asList('1',list21,'3',list22));

    ArrayList<Character> list31 = new ArrayList<Character>(Arrays.asList('2'));
    ArrayList<Character> list321 = new ArrayList<Character>(Arrays.asList('5','6'));
    ArrayList<Object> list32 = new ArrayList<Object>(Arrays.asList('4',list321));
    ArrayList<Object> number_embed_list3 = new ArrayList<Object>(Arrays.asList('1',list31,'3',list32));


    System.out.println("\n\n\nnumber_embed\n");
    System.out.println("list1 = "+number_embed_list1);
    System.out.println(number_embed(number_embed_list1));

    System.out.println("\nlist2 = "+number_embed_list2);
    System.out.println(number_embed(number_embed_list2));

    System.out.println("\nlist3 = "+number_embed_list3);
    System.out.println(number_embed(number_embed_list3));

    //Demonstrates powerset
    ArrayList<Character> powerset_list1 = new ArrayList<Character>();
    powerset_list1.add('a');
    powerset_list1.add('b');
    powerset_list1.add('c');

    ArrayList<Character> powerset_list2 = new ArrayList<Character>();
    powerset_list2.add('a');
    powerset_list2.add('b');
    powerset_list2.add('b');


    System.out.println("\n\n\npowerset\n");
    System.out.println("list1 = "+powerset_list1);
    System.out.println(powerset(powerset_list1));

    System.out.println("\nlist2 = "+powerset_list2);
    System.out.println(powerset(powerset_list2));
  }


  /** Problem 1
   *  Part (a) **/

  public static ArrayList<Character> my_intersection(ArrayList<Character> list1, ArrayList<Character> list2) {

    //Declares list to be returned
    ArrayList<Character> matches = new ArrayList<Character>();

    //Checks for and adds matches (ignoring duplicates)
    for (Character element : list1) {
      if ((list2.contains(element)) && !matches.contains(element)) {
        matches.add(element);
      }
    }
    //Returns matches as ArrayList
    return matches;
  }


  /** Problem 1
   *  Part (b) **/

  public static ArrayList<?> my_union(ArrayList<?> list1, ArrayList<?> list2) {

    //Defines inputs and output as lists
    ArrayList<ArrayList<?>> inputs = new ArrayList<ArrayList<?>>(Arrays.asList(list1,list2));
    ArrayList<Object> union = new ArrayList<>();

    //Add each element from the input
    //that has not been added to the union (output)
    for (ArrayList<?> list : inputs){
      for (Object element : list) {
        if (!union.contains(element)) {
          union.add(element);
        }
      }
    }
    //Returns the union ArrayList
    return union;
  }


  // Custom Function: no_duplicates
  //Returns a copy of the list with no duplicates
  //Uses a union with the empty set to produce

  public static ArrayList<?> no_duplicates(ArrayList<?> list) {

    //Defines empty set
    ArrayList<?> null_set = new ArrayList<>();

    //Defines union of input set and empty set
    ArrayList<?> no_dup = my_union(list,null_set);

    //Returns the set with duplicates removed
    return no_dup;
  }

  /** Problem 2
   *  Part (a) **/

  public static int addvec (ArrayList<Integer> list) {

    //Checks if empty list; throws exception
    if (list.size() == 0) {
      throw new IllegalArgumentException("addvec() requires non-empty input list.");
    }

    //Defines the running sum of elements
    int sum = 0;

    //Adds each element in list to the sum
    for (Integer element : list){
      sum += element;
    }

    //Returns the total sum
    return sum;
  }

  /** Problem 2
   *  Part (b) **/

  public static ArrayList<Integer> vecmul (ArrayList<Integer> list1, ArrayList<Integer> list2) {

    //Collects inputs
    ArrayList<ArrayList<Integer>> inputs = new ArrayList<ArrayList<Integer>>(Arrays.asList(list1,list2));

    //Checks for empty lists; throws exception
    for (ArrayList<Integer> list : inputs) {
      if (list.size() == 0) {
        throw new IllegalArgumentException("vecmul() requires non-empty input lists.");
      }
    }

    //Creates output vector
    ArrayList<Integer> productVec = new ArrayList<Integer>();

    //Find longest vector length
    int maxLength = 0;
    for (ArrayList<Integer> list : inputs) {
      if (list.size()>maxLength) {
        maxLength = list.size();
      }
    }

    //Pads shorter lists with 1s
    for (ArrayList<Integer> list : inputs) {
      while (list.size() < maxLength) {
        list.add(1);
      }
    }

    //Multiplies coordinate-wise; adds to productVec for output
    for (int i = 0; i<list1.size(); i++) {
      productVec.add(list1.get(i)*list2.get(i));
    }

    //Returns product vector
    return productVec;
  }


  /** Problem 2
  * Part (c) **/

  public static int innprod (ArrayList<Integer> list1, ArrayList<Integer> list2) {

    //Collects inputs
    ArrayList<ArrayList<Integer>> inputs = new ArrayList<ArrayList<Integer>>(Arrays.asList(list1,list2));

    //Checks for empty lists; throws exception
    for (ArrayList<Integer> list : inputs) {
      if (list.size() == 0) {
        throw new IllegalArgumentException("innprod() requires non-empty input lists.");
      }
    }

    //Multiplies the vectors coordinate-wise then sums the products
    int innprod = addvec(vecmul(list1,list2));

    //Returns the inner product
    return innprod;
  }


  /** Problem 3 **/

  public static ArrayList<ArrayList<?>> occurences (ArrayList<?> list) {

    //Checks if empty list; throws exception
    if (list.size() == 0) {
      throw new IllegalArgumentException("occurences() requires non-empty input list.");
    }

    //Defines output ArrayList
    ArrayList<ArrayList<?>> occurences_list = new ArrayList<ArrayList<?>>();

    //Removes duplicates from original list
    ArrayList<?> no_dup = (ArrayList<?>) no_duplicates(list);

    //Counts occurences of each unique element
    for (Object element : no_dup) { //unique elements loop
      int occurences_count = 0;
      for (Object occurence : list) { //original occurences loop
        if (element.equals(occurence)) {
          occurences_count++;
        }
      }

      //Adds pair indicating occurences to list
      ArrayList<Object> counts_pair = new ArrayList<Object>(Arrays.asList(element,occurences_count));
      occurences_list.add(counts_pair);
    }

    /* //Sorts the list of occurence lists by number of occurences
    class SortOccurences implements Comparator<ArrayList<?>> {
      public int compare(ArrayList<?> list1, ArrayList<?> list2) {
        //Sets whether ascending or descending order
        boolean descending = true;
        int direction = 0;
        if (descending) {
          direction = -1;
        } else {
          direction = 1;
        }
        //Sorts list by number of occurences
        return ((int)list1.get(1)-(int)list2.get(1))*direction;
      }
    } */

    Collections.sort(occurences_list, new SortOccurences());

    //Returns occurence list
    return occurences_list;
  }


  /** Problem 4 **/

  public static boolean my_trianglenos (ArrayList<Integer> list) {

    //Checks if empty list; throws exception
    if (list.size() == 0) {
      throw new IllegalArgumentException("my_trianglenos() requires non-empty input list.");
    }

    list_iteration :

    //Loops through input numbers
    for (int element : list) {

      //Counts upwards (only takes on triangular number values)
      int triang_num = 0;

      //Checks element against triangular numbers;
      //If triang_num gets above element, then element is not a triangular number
      for (int i = 0; triang_num <= element; i++) {
        triang_num += i; //sets triang_num to the next triangular number
        if (triang_num == element) {
          continue list_iteration; //goes to next input element if current element is triangular
        }
      }
      return false; //returns false if any element is not triangular
    }
    return true; //returns true if all elements pass as triangular
  }


  /** Problem 5 **/

  public static int number_embed (ArrayList<?> list) {

    //Checks if empty list; throws exception
    if (list.size() == 0) {
      throw new IllegalArgumentException("number_embed() requires non-empty input list.");
    }

    //Declares number of embedded lists
    int number = 0;

    //Loops through input list, looking for lists
    for (Object element : list) {
      if (element instanceof List) {
        //If element is a list, counts that list
        ArrayList<?> embed_list = (ArrayList<?>) element;
        number += 1 + number_embed(embed_list); //recursively counts its embedded lists
      }
    }

    //Returns total number of embedded lists
    return number;
  }


  /** Problem 6 **/

  public static ArrayList<ArrayList<?>> powerset (ArrayList<?> list) {

    //removes duplicate elements
    ArrayList<?> no_dupl = (ArrayList<?>) no_duplicates(list);

    //Declares output ArrayList
    ArrayList<ArrayList<?>> subsets = new ArrayList<ArrayList<?>>();

    //checks that list is non-empty
    if (no_dupl.size() != 0) {

      //finds largest proper subsets
      for (int i = 0; i < no_dupl.size(); i++) {
        ArrayList<?> prop_subset = (ArrayList<?>) no_dupl.clone();
        prop_subset.remove(prop_subset.size()-1-i); //Removes 1 element at a time to create largest prop. subsets

        // Recursively adds all subsets of proper subset to output list
        subsets.addAll(powerset(prop_subset));
      }
    }

    //adds self to list of subsets
    subsets.add(no_dupl);

    //removes duplicate subsets
    subsets = (ArrayList<ArrayList<?>>) no_duplicates(subsets);

    //sorts lists by size
    subsets.sort(Comparator.comparing(ArrayList::size));

    //returns all subsets
    return subsets;
  }
}

//Sorts the list of occurence lists by number of occurences
class SortOccurences implements Comparator<ArrayList<?>> {
  public int compare(ArrayList<?> list1, ArrayList<?> list2) {
    //Sets whether ascending or descending order
    boolean descending = true;
    int direction = 0;
    if (descending) {
      direction = -1;
    } else {
      direction = 1;
    }
    //Sorts list by number of occurences
    return ((int)list1.get(1)-(int)list2.get(1))*direction;
  }
}