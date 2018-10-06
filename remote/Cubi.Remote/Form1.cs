using System.Globalization;
using System.Linq;
using System.Threading;
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
            cbxEmotionList.Items.AddRange(
                Colors.RgbColors
                    .Select(c => CultureInfo.CurrentCulture.TextInfo.ToTitleCase(c.Emotion.ToLower()))
                    .ToArray()
            );

            cbxEmotionList.SelectedIndex = 0;
        }

        private void CreateColorButtons()
        {
            var buttons = Colors.RgbColors.Select((color, index) => new Button
            {
                BackColor = System.Drawing.Color.FromArgb(color.Value.Red, color.Value.Green, color.Value.Blue),
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

            var command = Command.Create(CommandType.SetLed, Colors.Get(c => c.Name == colorName));
            command.SendTo(ioClient);
        }

        private void btnStart_Click(object sender, System.EventArgs e)
        {
            if (!(cbxEmotionList.SelectedItem is string emotion)) return;

            string color = Colors.Get(c => c.Emotion == emotion.ToLower());
            const string black = "(0,0,0)";
            const int seconds = 3;
            const int delay = 1000;

            for (int i = 0; i < seconds; i++)
            {
                Command
                    .Create(CommandType.SetLed, color)
                    .SendTo(ioClient);

                AutoClosingMessageBox.Show((seconds - i).ToString(), $"Emotion: {emotion}", delay);

                Command
                    .Create(CommandType.SetLed, black)
                    .SendTo(ioClient);

                Thread.Sleep(delay);
            }

            string resultColor = MessageBox.Show("Was the emotion correct?", "Result", MessageBoxButtons.YesNo) == DialogResult.Yes 
                ? "green" 
                : "red";

            Command
                .Create(CommandType.SetLed, Colors.Get(c => c.Name == resultColor))
                .SendTo(ioClient);
        }
    }
}

