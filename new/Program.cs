using System;
using System.Linq;
using System.Globalization;

namespace devdotnet.New
{
    public class Program
    {
        struct Point
        {
            public double x;
            public double y;
            public double z;
            public Point(double x, double y, double z)
            {
                this.x = x; this.y = y; this.z = z;
            }
        }

        static void Print(params object[] attributes)
        {
            for (int i = 0; i < attributes.Length; i++) Console.Write(attributes[i] + " ");
            Console.WriteLine();
        }

        static string Input()
        {
            Console.Write("Input: ");
            return Console.ReadLine();
        }

        static void Foo(int i, int n = 10)
        {
            Print(i);
            if (i >= n) return;
            i++;
            Foo(i, n);
        }

        static int Int(string str)
        {
            return int.Parse(str);
        }

        static void Main(string[] args)
        {
            int n = Int(Input());
            Foo(0, n);
            
            Print("parsing: ", 1, 2, 3, 4);
        }
    }
}