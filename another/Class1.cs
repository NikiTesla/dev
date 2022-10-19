namespace devdotnet.another
{
    public static class Class1
    {
        public static double Sum(double x, double y)
        {
            return x + y;
        }

        public static int[,] GetArray()
        {
            int n = 3;
            int[,] myArray = new int[n, n];

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    Console.Write($"{i}.{j}: ");
                    myArray[i,j] = int.Parse(Console.ReadLine());
                }
                Console.WriteLine();
            }

            return myArray;
        }
    }

}