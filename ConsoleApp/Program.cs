using System;
using System.Globalization;
using devdotnet.another;

namespace devdotnet.ConsoleApp
{
    public class Program
    {
        /* 
        Class program created to work with structures, showing syntax and main ideas of C#
        firstly, main function starts with capital M, get it.
        secondly, read comments to understand what to learn next
        */
        public static bool GetFirst()
        {
            Console.WriteLine("Getting first...");
            return false;
        }

        public static bool GetSecond()
        {
            Console.WriteLine("Getting second...");
            return true;
        }
        
        static void Main(string[] args)
        {   
            // создание экземпляра класса, отвечающего за формат чисел
            // распознавание точки как разделителя дробной части
            NumberFormatInfo numberFormatInfo = new NumberFormatInfo()
            {
                NumberDecimalSeparator = ".",
            };
            // создадим список для дальнейшей записи чисел
            double[] arr = {0, 0, 0, 0};
            
            // преобразование строк, введеных в консоль в число с плавающей точкой
            // arr[0] = Convert.ToDouble(Console.ReadLine(), numberFormatInfo);
            // arr[1] = Convert.ToDouble(Console.ReadLine(), numberFormatInfo);
            

            // double.TryParse(Console.ReadLine(), out arr[2]);
            // bool bb = double.TryParse(Console.ReadLine(), out arr[3]);
            
            // создание экземпляров структуры с двумя дробными числами
            mystruct s1 = new(arr[0], arr[1]);
            mystruct s2 = new(arr[2], arr[3]);

            Console.WriteLine(String.Format("s1.x : {0}\ts2.x : {1}", s1.x, s2.x));
            Console.WriteLine(String.Format("s1.y : {0}\ts2.y : {1}", s1.y, s2.y));


            if(GetFirst() && GetSecond()) Console.WriteLine("Infected or hot");
            else Console.WriteLine("Not infected and not hot");

            while (true)
            {
                ConsoleKey consoleKey = Console.ReadKey().Key;
                switch (consoleKey)
                {
                    case ConsoleKey.W:
                        Console.WriteLine("Идём вперёд");
                        break;
                    case ConsoleKey.S:
                        Console.WriteLine("Идём назад");
                        break;
                    case ConsoleKey.A:
                        Console.WriteLine("Идём налево");
                        break;
                    case ConsoleKey.D:
                        Console.WriteLine("Идём направо");
                        break;
                    case ConsoleKey.Spacebar:
                        Console.WriteLine("JUMP");
                        break;
                }
            }
        }

        // создание структуры в теле основного класса программы
        // структура хранит два числа с плавающей точкой
        struct mystruct
        {
            public double x = 0; public double y = 0; 
            public mystruct (double x, double y)
            {
                this.x = x; this.y = y;
            }
        }
    }
}