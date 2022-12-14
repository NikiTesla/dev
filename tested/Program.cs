namespace tested
{
    enum Color
    {
        Red,
        Green,
        Blue,
        Black
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("testing");

            Point first = new Point(10, 10);
            Console.WriteLine(first.X);
            Point second = new Point(5, 5);
            Console.WriteLine(second.X);
            Point third = first.vector_sum(second);

            int x = third.X;
            Console.WriteLine(x);
            third.Print();

            DateTime time = DateTime.Now;
            DateTime previous = time;

            
            while (true){
                DateTime now = DateTime.Now;
                if ((now - time).Seconds > 1000) break;

                if((now - previous).Milliseconds >= 997) {
                    Console.WriteLine(now.ToLongTimeString());
                    previous = DateTime.Now;
                }
            }
        }
    }
}

namespace tested
{
    partial class Point
    {
        public void Print()
        {
            Console.WriteLine($"x : {x}");
            Console.WriteLine($"y : {y}");
            Console.WriteLine();
        }
    }
}