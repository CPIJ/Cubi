using System;
using System.Collections.Generic;

namespace Cubi.Remote
{
    public class Colors
    {
        private static readonly Dictionary<string, Tuple<int, int, int>> RgbColors = new Dictionary<string, Tuple<int, int, int>>
        {
            { "white", Tuple.Create(255, 255, 255) }
        };

        public static string Get(string name)
        {
            var color = RgbColors[name];

            return color.ToString();
        }
    }
}