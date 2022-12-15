using System.Collections;
using System.Numerics;

namespace homework {
    class Program {
        static void Main(string[] args) {
            Hashtable myTable = new Hashtable();

            myTable.Add("first", 11231);
            myTable.Add("second", 21234234231);
            myTable.Add("third", 312312311);

            foreach (DictionaryEntry el in myTable) {
                System.Console.WriteLine($"key={el.Key} value={el.Value}");
            }

            printColl(myTable);
            setElement("first", "hello", ref myTable);

            var myVector = new Vector<Vector<char>>();

            ArrayList arrList = new ArrayList(3){'\x006A', '\x005A', '\x002A'};

            foreach (char el in arrList) {
                System.Console.WriteLine(el);
            }

            for (int i = 0; i < 5; i++)
            {
                arrList = new ArrayList(){'\x006A', '\x005A', '\x002A'};
                addToVector(i, arrList, ref myVector);
            }
        }

        static void printColl(Hashtable inTable) {
            foreach (string key in inTable.Keys) {
                System.Console.WriteLine($"key:{key} value:{inTable[key]}");
            }
        }

        static void setElement(string key, string value, ref Hashtable inTable) {
            try {
                inTable[key] = value;
            } catch {
                System.Console.WriteLine("No elemets with such key");
            }

            System.Console.WriteLine($"new value with key {key} and value {inTable[key]}");
        }

        static void addToVector(int pos, ArrayList inArray, ref Vector<Vector<char>> outVector) {
            char[] charList = new char[3];
            for (int i = 0; i < 3; i++) {
                charList[i] = (char)inArray[i];
            }

            Vector<char>[] vectorList = new Vector<char>[5];
            outVector.CopyTo(vectorList);
            vectorList[pos] = new Vector<char>(charList);

            outVector = new Vector<Vector<char>>(vectorList);
            System.Console.WriteLine($"pos:{pos} value:{inArray}");
        }
    }
}