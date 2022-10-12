using System;
using dev.another;

namespace dev.ConsoleApp
{
    public class Program
    {
        /* 
        Class program created to work with structures, showing syntax and main ideas of C#
        firstly, main function starts with capital M, get it.
        secondly, read comments to understand what to learn next
        */

        // разобраться со статическими методами
        static void Main(string[] args)
        {
            mystruct s1 = new(1, 1);
            mystruct s2 = new(10, 10);

            Console.WriteLine(Class1.Sum(s1.x, s2.x));

            Console.WriteLine(String.Format("s1.x : {0}\ts2.x : {1}", s1.x, s2.x));
            Console.WriteLine(String.Format("s1.y : {0}\ts2.y : {1}", s1.y, s2.y));
        }

        // разобраться с доступом и в целом структурой программы на C#
        struct mystruct
        {
            public int x = 0; public int y = 0; 
            public mystruct (int x, int y)
            {
                this.x = x; this.y = y;
            }
        }
    }
}