using System;
using System.Globalization;
using System.Linq;
using System.Threading;
using System.Windows.Forms;
using Cubi.Remote.Winforms;
using CommandType = Cubi.Remote.Winforms.CommandType;

namespace Cubi.Remote
{
    public partial class TrainingModeForm : Form
    {
        public TrainingModeForm()
        {
            InitializeComponent();
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

        private void btnBack_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void btnStart_Click(object sender, EventArgs e)
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
                    .SendTo(WebSockets.IoClient);

                AutoClosingMessageBox.Show((seconds - i).ToString(), $"Emotion: {emotion}", delay);

                Command
                    .Create(CommandType.SetLed, black)
                    .SendTo(WebSockets.IoClient);

                Thread.Sleep(delay);
            }

            string resultColor = MessageBox.Show("Was the emotion correct?", "Result", MessageBoxButtons.YesNo) == DialogResult.Yes
                ? "green"
                : "red";

            Command
                .Create(CommandType.SetLed, Colors.Get(c => c.Name == resultColor))
                .SendTo(WebSockets.IoClient);
        }
    }
}
