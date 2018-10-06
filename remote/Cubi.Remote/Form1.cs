using System.Windows.Forms;
using WebSocketSharp;

namespace Cubi.Remote
{
    public partial class Form1 : Form
    {
        private readonly WebSocket ioClient;

        public Form1()
        {
            ioClient = new WebSocket("ws://localhost:8002");
            ioClient.Connect();

            InitializeComponent();
        }

        private void setColorBtn_Click(object sender, System.EventArgs e)
        {
            if (!(sender is Button button)) return;
            if (!(button.Tag is string colorName)) return;

            var command = Command.Create(CommandType.SetLed, Colors.Get(colorName));
            command.SendTo(ioClient);
        }
    }
}
