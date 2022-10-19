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

        static double Sum(string message, params double[] parameters)
        {
            double result = 0;
            Console.Write(message);

            for (int i = 0; i < parameters.Length; i++) result += parameters[i];

            return result;
        }

        static void Main(string[] args)
        {
            Console.WriteLine(Sum("Hello, sum is: ", 1.1, 2.2, 3.0, 4.1));
        }
    }
}