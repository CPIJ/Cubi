namespace Cubi.Remote.Winforms
{
    partial class ConversationModeForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblSetColor = new System.Windows.Forms.Label();
            this.pnlColors = new System.Windows.Forms.Panel();
            this.button1 = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // lblSetColor
            // 
            this.lblSetColor.AutoSize = true;
            this.lblSetColor.Dock = System.Windows.Forms.DockStyle.Top;
            this.lblSetColor.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblSetColor.Location = new System.Drawing.Point(0, 0);
            this.lblSetColor.Name = "lblSetColor";
            this.lblSetColor.Padding = new System.Windows.Forms.Padding(5);
            this.lblSetColor.Size = new System.Drawing.Size(90, 29);
            this.lblSetColor.TabIndex = 0;
            this.lblSetColor.Text = "Set Color";
            // 
            // pnlColors
            // 
            this.pnlColors.AutoSize = true;
            this.pnlColors.Dock = System.Windows.Forms.DockStyle.Top;
            this.pnlColors.Location = new System.Drawing.Point(0, 29);
            this.pnlColors.Name = "pnlColors";
            this.pnlColors.Padding = new System.Windows.Forms.Padding(5);
            this.pnlColors.Size = new System.Drawing.Size(311, 10);
            this.pnlColors.TabIndex = 1;
            // 
            // button1
            // 
            this.button1.Dock = System.Windows.Forms.DockStyle.Top;
            this.button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.button1.Location = new System.Drawing.Point(0, 39);
            this.button1.Name = "button1";
            this.button1.Padding = new System.Windows.Forms.Padding(5);
            this.button1.Size = new System.Drawing.Size(311, 45);
            this.button1.TabIndex = 2;
            this.button1.Text = "Reset";
            this.button1.UseVisualStyleBackColor = true;
            // 
            // ConversationModeForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(311, 554);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.pnlColors);
            this.Controls.Add(this.lblSetColor);
            this.Font = new System.Drawing.Font("Arial", 9.75F);
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "ConversationModeForm";
            this.Text = "ConversationModeForm";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label lblSetColor;
        private System.Windows.Forms.Panel pnlColors;
        private System.Windows.Forms.Button button1;
    }
}