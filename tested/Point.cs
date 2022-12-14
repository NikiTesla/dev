using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tested
{
    partial class Point
    {
        private int x; private int y; private int z;
        private Color color;

        public int X { get {return x;} set {x = value;}}
        public int Y { get {return y;} set {y = value;}}
        public int Z { get {return z;} set {z = value;}}

        public Point()
        {
            x = 0; y = 0; z = 0; color = Color.Black;
        }

        public Point(int x, int y, Color color = Color.Black)
        {
            this.x = x;
            this.y = y;
            this.color = color;
        }

        public Point(int x, int y, int z, Color color = Color.Black) : this(x, y, color)
        {
            this.z = z;
        }

        
        public Point vector_sum(Point second)
        {
            return new Point(x + second.x, y + second.y);
        }
        

        public double radius_vector()
        {
            return Math.Sqrt(x * x + y * y);
        }
    }
}