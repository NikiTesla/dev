namespace homework {
    struct struct1 {
        public static void WhatIsType (string s) {
            Type tp = Type.GetType(s);

            if (tp != null) {
                System.Console.WriteLine($"type is {tp}");
                System.Console.WriteLine($"is class? {tp.IsClass}");
                System.Console.WriteLine($"\t{tp.IsNested}");
            } else {
                System.Console.WriteLine($"No such type {s}");
            }
        }
    }
   
}