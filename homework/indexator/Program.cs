namespace homework {
    class Program {
        static void Main(string[] args) {
            string[,] inArr = new string[4, 3];

            for (int i = 0; i < 4; i++){
                for (int j = 0; j < 3; j++) {
                    inArr[i, j] = $"i-{i} j-{j}: {i+j}";
                }
            }

            var myArr = new MyArray(inArr);
            System.Console.WriteLine(myArr[1, 2]);
            System.Console.WriteLine();
            
            var attrs = System.Attribute.GetCustomAttributes(typeof(MyArray));
            foreach (System.Attribute attr in attrs) {
                if (attr is MyClassAttribute) {
                    MyClassAttribute a = (MyClassAttribute)attr;
                    System.Console.WriteLine(a.GetMessage());
                }
            }


            var method1 = typeof(MyArray).GetMethod("LengthFirstDimension");
            var method2 = typeof(MyArray).GetMethod("LengthSecondDimension");

            var attr1 = (FirstMethodAttribute)System.Attribute.GetCustomAttribute(method1, typeof(FirstMethodAttribute));
            var attr2 = (SecondMethodAttribute)System.Attribute.GetCustomAttribute(method2, typeof(SecondMethodAttribute));

            System.Console.WriteLine(
                $"attr1 is {attr1.message}\nattr2 is {{a:{attr2.a} b:{attr2.b} message:'{attr2.message}'}}"
            );
        }
    }
}