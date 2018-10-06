using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;

namespace Cubi.Remote
{
    public class Colors
    {
        private static readonly Dictionary<string, Tuple<int, int, int>> RgbColors = JsonConvert
            .DeserializeObject<IEnumerable<Color>>(File.ReadAllText("../../../../config/colors.json"))
            .ToDictionary(k => k.Name, v => Tuple.Create(v.Rgb[0], v.Rgb[1], v.Rgb[2]));

        public static string Get(string name)
        {
            var color = RgbColors[name];

            return color.ToString();
        }
    }

    public class Color
    {
        public string Name { get; set; }
        public int[] Rgb { get; set; }
    }

}