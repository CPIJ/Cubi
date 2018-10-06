using System;
using System.Collections.Generic;
using WebSocketSharp;

namespace Cubi.Remote.Winforms
{
    public class Command
    {
        private string Action { get; set; }
        private string Parameter { get; set; }
        private static readonly Dictionary<CommandType, string> ActionNames = new Dictionary<CommandType, string>
        {
            { CommandType.SetLed, "SET_LED" },
            { CommandType.SetMode, "SET_MODE" }
        };

        private Command(string action, string parameter)
        {
            Action = action;
            Parameter = parameter;
        }

        public static Command Create(CommandType type, string parameter)
        {
            return new Command(ActionNames[type], parameter);
        }

        public void SendTo(WebSocket socket)
        {
            socket.Send($"{Action}:{Parameter}");
        }
    }
}