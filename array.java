public class array {
    public static void main(String args[]){

int arr[]={1,2,5,4,3,6};

        int firstLargest = Integer.MIN_VALUE;

       
        int secondLargest = Integer.MIN_VALUE;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > firstLargest) {
                secondLargest = firstLargest;
                firstLargest = arr[i];
            } else 
            if (arr[i] > secondLargest && arr[i] != firstLargest) {
                secondLargest = arr[i];
            }
      }
      System.out.println("SL: "+secondLargest);
    }
      }

