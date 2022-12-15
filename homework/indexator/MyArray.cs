namespace homework {
    [MyClass("It's my array with indexator")]
    class MyArray {
        string[,] arr;
        private int lengthFirstDimension, lengthSecondDimension;
        public MyArray(){
            System.Console.WriteLine("Created");
        }
        public MyArray(string[,] inArray) {
            arr = inArray;
            lengthFirstDimension = inArray.GetLength(0);
            lengthSecondDimension = inArray.GetLength(1);
            System.Console.WriteLine("Created");
        }

        public string this[int index1, int index2] {
            get {
                if (index1 >= 0 && index2 >= 0 && index1 < arr.Length && index2 < arr.Length){
                    return arr[index1, index2];
                } else {
                    throw new ArgumentOutOfRangeException();
                }
            }
            set {
                if (index1 >= 0 && index2 >= 0 && index1 < arr.Length && index2 < arr.Length) {
                    arr[index1, index2] = value;
                }
            }

        }
        
        [FirstMethod()]
        public int LengthFirstDimension(){
            return lengthFirstDimension; 
        }

        [SecondMethod(12, 24, "name")]
        public int LengthSecondDimension(){
            return lengthSecondDimension;
        }
    }
}