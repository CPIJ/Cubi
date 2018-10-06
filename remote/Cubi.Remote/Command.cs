using System;
using WebSocketSharp;

namespace Cubi.Remote
{
    public enum CommandType { SetLed }

    public class Command
    {
        public string Action { get; private set; }
        public string Parameter { get; private set; }

        private Command(string action, string parameter)
        {
            Action = action;
            Parameter = parameter;
        }

        public static Command Create(CommandType type, string parameter)
        {
            string action;

            switch (type)
            {
                case CommandType.SetLed:
                    action = "SET_LED";
                    break;
                default:
                    throw new ArgumentOutOfRangeException(nameof(type), type, null);
            }

            return new Command(action, parameter);
        }

        public void SendTo(WebSocket socket)
        {
            socket.Send($"{Action}:{Parameter}");
        }
    }
}