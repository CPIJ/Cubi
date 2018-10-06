namespace Cubi.Remote.Winforms
{
    partial class ModeSelectionForm
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
            this.btnConversation = new System.Windows.Forms.Button();
            this.btnTraining = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnConversation
            // 
            this.btnConversation.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnConversation.Location = new System.Drawing.Point(13, 13);
            this.btnConversation.Name = "btnConversation";
            this.btnConversation.Size = new System.Drawing.Size(101, 37);
            this.btnConversation.TabIndex = 0;
            this.btnConversation.Text = "Conversation";
            this.btnConversation.UseVisualStyleBackColor = true;
            this.btnConversation.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnTraining
            // 
            this.btnTraining.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnTraining.Location = new System.Drawing.Point(13, 56);
            this.btnTraining.Name = "btnTraining";
            this.btnTraining.Size = new System.Drawing.Size(101, 37);
            this.btnTraining.TabIndex = 1;
            this.btnTraining.Text = "Training";
            this.btnTraining.UseVisualStyleBackColor = true;
            this.btnTraining.Click += new System.EventHandler(this.btnTraining_Click);
            // 
            // ModeSelectionForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(136, 105);
            this.Controls.Add(this.btnTraining);
            this.Controls.Add(this.btnConversation);
            this.Font = new System.Drawing.Font("Arial", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "ModeSelectionForm";
            this.Text = "Select a mode";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnConversation;
        private System.Windows.Forms.Button btnTraining;
    }
}