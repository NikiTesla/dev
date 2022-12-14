namespace homework
{
    class Program {
        static void Main(string[] args){
            MyDate myDate1 = new MyDate();
            MyDate myDate2 = new MyDate(new DateOnly(2022, 2, 8));
            MyDate myDate3 = new MyDate(new DateOnly(2002, 5, 8), new TimeOnly(18, 10, 40));

            System.Console.WriteLine(myDate1.date);
            System.Console.WriteLine(myDate2.date);

            new ChangingMain(ref myDate3);

            System.Console.WriteLine(myDate3.date);
        }

        // класс, имеющий три конструктора для задания даты
        class MyDate {
            public DateTime date;
            public MyDate(){
                this.date = DateTime.Now;
            }

            public MyDate(DateOnly date){
                this.date = new DateTime(date.Year, date.Month, date.Day,
                        DateTime.Now.Hour, DateTime.Now.Minute, DateTime.Now.Second);
            }

            public MyDate(DateOnly date, TimeOnly time){
                this.date = new DateTime(date.Year, date.Month, date.Day, time.Hour, time.Minute, time.Second);
            }
        }

        // при вызове конструктора с ссылкой на MyDate, меняет значение на текущее время и дату 
            class ChangingMain{
            public ChangingMain(){
                System.Console.WriteLine("Nothing to change");
            }
            public ChangingMain(ref MyDate someVariable){
                someVariable = new MyDate();
            }
        }
    }
}