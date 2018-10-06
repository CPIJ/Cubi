using System.Linq;
using System.Windows.Forms;
using System.Windows.Forms.VisualStyles;
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
            CreateColorButtons();
            InitEmotionList();
        }

        private void InitEmotionList()
        {
            cbxEmotionList.Items.AddRange(Colors.RgbColors.Select(c => c.Emotion).ToArray());
        }

        private void CreateColorButtons()
        {
            var buttons = Colors.RgbColors.Select((color, index) => new Button
            {
                BackColor = System.Drawing.Color.FromArgb(color.Rgb[0], color.Rgb[1], color.Rgb[2]),
                FlatStyle = FlatStyle.Flat,
                ForeColor = System.Drawing.Color.Black,
                Location = new System.Drawing.Point(10, 41),
                Dock = DockStyle.Top,
                Size = new System.Drawing.Size(30, 30),
                TabIndex = index + 1,
                Tag = color.Name,
                UseVisualStyleBackColor = false,
                AutoSize = true,
                AutoSizeMode = AutoSizeMode.GrowOnly
            });

            foreach (var button in buttons)
            {
                button.Click += setColorBtn_Click;
                colorBox.Controls.Add(button);
            }
        }

        private void setColorBtn_Click(object sender, System.EventArgs e)
        {
            if (!(sender is Button button)) return;
            if (!(button.Tag is string colorName)) return;

            var command = Command.Create(CommandType.SetLed, Colors.Get(colorName));
            command.SendTo(ioClient);
        }

        private void btnStart_Click(object sender, System.EventArgs e)
        {

        }
    }
}

