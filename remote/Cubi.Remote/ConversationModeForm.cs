using System;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace Cubi.Remote.Winforms
{
    public partial class ConversationModeForm : Form
    {
        public ConversationModeForm()
        {
            InitializeComponent();
            CreateColorButtons();
        }

        private void CreateColorButtons()
        {
            var colorButtons = Colors.RgbColors.Select((color, index) => new Button
            {
                BackColor = System.Drawing.Color.FromArgb(color.Value.Red, color.Value.Green, color.Value.Blue),
                FlatStyle = FlatStyle.Flat,
                ForeColor = System.Drawing.Color.Black,
                Location = new Point(10, 41),
                Dock = DockStyle.Top,
                Size = new Size(30, 30),
                TabIndex = index + 1,
                Tag = color.Name,
                UseVisualStyleBackColor = false,
                AutoSize = true,
                AutoSizeMode = AutoSizeMode.GrowOnly,
                Text = color.Emotion
            });

            foreach (var button in colorButtons)
            {
                button.Click += setColorBtn_Click;
                pnlColors.Controls.Add(button);
            }
        }

        private void setColorBtn_Click(object sender, EventArgs e)
        {
            if (!(sender is Button button)) return;

            string color = (string) button.Tag;

            Command
                .Create(CommandType.SetLed, Colors.Get(c => c.Name == color))
                .SendTo(WebSockets.IoClient);
        }

        private void btnBack_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
