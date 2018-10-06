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
        public static readonly IEnumerable<Color> RgbColors = JsonConvert
            .DeserializeObject<IEnumerable<Color>>(File.ReadAllText("../../../../config/colors.json"));

        public static string Get(string name)
        {
            var color = RgbColors.FirstOrDefault(c => c.Name == name);

            if (color == null)
            {
                throw new IndexOutOfRangeException();
            }

            return $"{color.Rgb[0]}:{color.Rgb[1]}:{color.Rgb[2]}";
        }
    }

    public class Color
    {
        public string Name { get; set; }
        public int[] Rgb { get; set; }
        public string Emotion { get; set; }
    }
}