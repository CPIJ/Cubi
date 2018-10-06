using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using WebSocketSharp;

namespace Cubi.Remote.Winforms
{
    public class SocketConfig
    {
        public string Url { get; set; }
        public WebSocket WebSocket { get; set; }
    }

    public static class WebSockets
    {
        private static readonly string[] Names = { "LED_SERVER", "IO_SERVER", "APP_SERVER", "LOGIC_SERVER" };
        private static readonly JObject Json = JsonConvert.DeserializeObject<JObject>(File.ReadAllText("../../../../config/server-config.json"));
        private const bool Testing = true;

        private static readonly Dictionary<string, SocketConfig> Sockets = Names
            .ToDictionary(name => name, value =>
            {
                var serverConfig = Json.GetValue(value);
                string host = serverConfig.SelectToken("host").ToObject<string>();
                int port = serverConfig.SelectToken("port").ToObject<int>();

                return new SocketConfig
                {
                    Url = $"ws://{host}:{port}",
                    WebSocket = null
                };
            });


        public static WebSocket LedClient => GetConnection("LED_SERVER", Testing);
        public static WebSocket IoClient => GetConnection("IO_SERVER", Testing);
        public static WebSocket AppClient => GetConnection("APP_SERVER", Testing);
        public static WebSocket LogicClient => GetConnection("LOGIC_SERVER", Testing);

        private static WebSocket GetConnection(string name, bool test = false)
        {
            if (Sockets[name].WebSocket == null)
            {
                string port = Sockets[name].Url.Split(':')[2];
                string url = test ? $"ws://127.0.0.1:{port}" : Sockets[name].Url;
                Sockets[name].WebSocket = new WebSocket(url);
                Sockets[name].WebSocket.Connect();
            }

            if (Sockets[name].WebSocket.ReadyState != WebSocketState.Open)
            {
                throw new Exception("Connection is closed!");
            }

            return Sockets[name].WebSocket;
        }

        public static void CloseAll()
        {
            foreach (var socket in Sockets.Values.Where(c => c.WebSocket != null && c.WebSocket.ReadyState == WebSocketState.Open).Select(c => c.WebSocket))
            {
                socket.Close(CloseStatusCode.Normal);
            }
        }
    }
}