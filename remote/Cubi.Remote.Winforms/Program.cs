using System;
using System.Windows.Forms;
using Cubi.Remote.Logic;

namespace Cubi.Remote
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);

            var form = new ModeSelectionForm();
            form.Closing += (sender, args) =>
            {
                WebSockets.CloseAll();
            };

            Application.Run(form);
        }
    }
}
