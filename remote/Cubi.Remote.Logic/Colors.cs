using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

namespace Cubi.Remote
{
    public class Colors
    {
        public static readonly IEnumerable<Color> RgbColors = JsonConvert
            .DeserializeObject<IEnumerable<JObject>>(File.ReadAllText("../../../../config/colors.json"))
            .Select(obj => new Color
            {
                Name = obj.GetValue("name").ToString(),
                Value = GetValue(obj.GetValue("value")),
                Emotion = obj.GetValue("emotion").ToString()
            });

        public static string Get(Func<Color, bool> predicate)
        {
            var color = RgbColors.FirstOrDefault(predicate);

            if (color == null)
            {
                throw new IndexOutOfRangeException();
            }

            return $"({color.Value.Red},{color.Value.Green},{color.Value.Blue})";
        }

        private static (int, int, int) GetValue(JToken token)
        {
            var a = token.ToString().Replace("(", "");
            var b = a.Replace(")", "");
            var c = b.Split(',').Select(v => v.Trim());
            var d = c.Select(v => Convert.ToInt32(v)).ToArray();
            var e = (d[0], d[1], d[2]);

            return e;
        }
    }
}