using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Cubi.Remote.Winforms
{
    public partial class ModeSelectionForm : Form
    {
        public ModeSelectionForm()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            var frm = new ConversationModeForm
            {
                Location = this.Location,
                StartPosition = FormStartPosition.Manual,
            };

            frm.FormClosing += delegate { Show(); };
            frm.Show();

            Hide();
        }

        private void btnTraining_Click(object sender, EventArgs e)
        {
            var frm = new TrainingModeForm
            {
                Location = this.Location,
                StartPosition = FormStartPosition.Manual,
            };

            frm.FormClosing += delegate { Show(); };
            frm.Show();

            Hide();
        }
    }
}
