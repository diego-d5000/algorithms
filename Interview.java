/**
 * Created by Diego on 18/05/2015.
 */

// Rename methods, original class no contained bugs


public class Interview {

    // this method receive an sequence (array) of numbers and reorder from low to high
    public static void OrderSequenceLowToHigh(int[] sequence){
        // for each number in sequence, check order, find index to swap according order, and swap that
        for(int i = 0; i < sequence.length; ++i){
            int j = findCorrectIndexAccordingOrderOfNumbersInSequence(0, i-1, sequence, sequence[i]);
            if (i != j)
              swapItemsInSequenceAndReorder(sequence, i, j);
        }
    }

    /* this method receive 2 numbers, a sequence and item in this sequence,
    and find the correct index according order of number (from low to high) */
    public static int findCorrectIndexAccordingOrderOfNumbersInSequence(int beg, int end, int[] sequence, int item) {
        // uncommented if causes a error because in first index received in OrderSequenceLowToHigh is -1 and that is illegal
        //if (item > sequence[end])
         //return end + 1;


        while (beg < end) {
            /* middle is a middle index given a begin index and end of search, */
            int middle = beg + (end - beg) / 2;

            // search a middle range in sequence, and trims that depending order
            if (item <= sequence[middle])
                end = middle;
            else
                beg = middle + 1;
        }
        return beg;
    }

    // this method receive a sequence and two numbers (two index in sequence) and swap thath
    public static void swapItemsInSequenceAndReorder(int[] sequence, int i, int j){
        int item = sequence[i];
        for (int k = i; k > j; --k)
            sequence[k] = sequence[k-1];
        sequence[j] = item;
    }

    public static void printSequence(int[] sequence){
        for(int item : sequence)
            System.out.println(item);
        System.out.println();
    }

    // this method print origin sequence, reorder that and print
    public static void run(int[] sequence){
        printSequence(sequence);
        OrderSequenceLowToHigh(sequence);
        printSequence(sequence);
    }

    public static void main(String[] args){
        int[] items1 = {0, -1, 2, -3, 4, 6, 0, -2, -2, 3, 4};
        run(items1);
    }
}
