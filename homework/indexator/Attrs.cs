namespace homework {
    
    [AttributeUsage(AttributeTargets.Class)]
    class MyClassAttribute : System.Attribute {
        public string message;
        public MyClassAttribute(string message) {this.message = message;}
        public string GetMessage() {return message;}
    }

    [AttributeUsage(AttributeTargets.Method)]
    class FirstMethodAttribute : System.Attribute {
        public string message;
        public FirstMethodAttribute(){this.message = "I'm first-method attribute";}
    }

    [AttributeUsage(AttributeTargets.Method)]
    class SecondMethodAttribute : System.Attribute {
        public string result, message;
        public float a, b;

        public SecondMethodAttribute(float a, float b, string result) {
            this.message = "I'm second-method attribute";
            this.result = result;
            this.a = a; this.b = b;
        }
    }
}