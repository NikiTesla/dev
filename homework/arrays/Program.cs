namespace homework {
    class Program {
        static void Main(string[] args) {
            int[,] myArray = new int[10, 10];

            for (int i = 0; i < 10; i++){
                for (int j = 0; j < 10; j++){
                    // System.Console.WriteLine(i + " " + j);
                    myArray[i, j] = i + j;
                }
            }

            System.Console.WriteLine(getElement1(6, 3, myArray));

            // создаю массив из 100 элементов для заполнение его с getElement2
            int[] outArray = new int[100];
            getElement2(ref outArray, 3, 2, myArray);
            System.Console.WriteLine(outArray[3 + 2]);

            int[,] mySecondArray = new int[20, 20];

            for (int i = 0; i < 20; i++){
                for (int j = 0; j < 20; j++){
                    // System.Console.WriteLine(i + " " + j);
                    mySecondArray[i, j] = i + j;
                }
            }

            var myList = new List<int>();
            getElement3(ref myList, 4, mySecondArray);
        }

        static int getElement1(int index1, int index2, int[,] myArray) {
            return myArray[index1, index2];
        }

        static void getElement2(ref int[] outArray, int index1, int index2, int[,] inArray){
            outArray[index1+index2] = inArray[index1, index2];
        }

        // TODO ПОИСК В ДВУМЕРНОМ МАССИВЕ
        static void getElement3(ref List<int> outList, int el, int[,] inArray){
            var outEl = from elem in inArray select new int[,];
        }
    }
}