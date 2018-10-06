namespace Cubi.Remote.Winforms
{
    partial class Form1
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
            this.panel1 = new System.Windows.Forms.Panel();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.colorBox = new System.Windows.Forms.GroupBox();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.btnStart = new System.Windows.Forms.Button();
            this.cbxEmotionList = new System.Windows.Forms.ComboBox();
            this.groupBox3 = new System.Windows.Forms.GroupBox();
            this.rbTraining = new System.Windows.Forms.RadioButton();
            this.rbConversation = new System.Windows.Forms.RadioButton();
            this.panel2 = new System.Windows.Forms.Panel();
            this.panel3 = new System.Windows.Forms.Panel();
            this.rbStandby = new System.Windows.Forms.RadioButton();
            this.panel1.SuspendLayout();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.groupBox3.SuspendLayout();
            this.panel2.SuspendLayout();
            this.panel3.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.groupBox1);
            this.panel1.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel1.Location = new System.Drawing.Point(0, 0);
            this.panel1.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(177, 210);
            this.panel1.TabIndex = 0;
            // 
            // groupBox1
            // 
            this.groupBox1.AutoSize = true;
            this.groupBox1.Controls.Add(this.colorBox);
            this.groupBox1.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox1.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox1.Location = new System.Drawing.Point(0, 0);
            this.groupBox1.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBox1.Size = new System.Drawing.Size(177, 30);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Conversation mode";
            // 
            // colorBox
            // 
            this.colorBox.AutoSize = true;
            this.colorBox.Dock = System.Windows.Forms.DockStyle.Top;
            this.colorBox.Font = new System.Drawing.Font("Arial Narrow", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.colorBox.Location = new System.Drawing.Point(2, 22);
            this.colorBox.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.colorBox.Name = "colorBox";
            this.colorBox.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.colorBox.Size = new System.Drawing.Size(173, 5);
            this.colorBox.TabIndex = 1;
            this.colorBox.TabStop = false;
            this.colorBox.Text = "Set Color";
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.btnStart);
            this.groupBox2.Controls.Add(this.cbxEmotionList);
            this.groupBox2.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox2.Font = new System.Drawing.Font("Arial", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox2.Location = new System.Drawing.Point(0, 0);
            this.groupBox2.Margin = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Padding = new System.Windows.Forms.Padding(2, 3, 2, 3);
            this.groupBox2.Size = new System.Drawing.Size(200, 78);
            this.groupBox2.TabIndex = 2;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Training mode";
            // 
            // btnStart
            // 
            this.btnStart.Dock = System.Windows.Forms.DockStyle.Top;
            this.btnStart.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStart.Location = new System.Drawing.Point(2, 48);
            this.btnStart.Name = "btnStart";
            this.btnStart.Size = new System.Drawing.Size(196, 30);
            this.btnStart.TabIndex = 1;
            this.btnStart.Text = "Start";
            this.btnStart.UseVisualStyleBackColor = true;
            this.btnStart.Click += new System.EventHandler(this.btnStart_Click);
            // 
            // cbxEmotionList
            // 
            this.cbxEmotionList.Dock = System.Windows.Forms.DockStyle.Top;
            this.cbxEmotionList.FormattingEnabled = true;
            this.cbxEmotionList.Location = new System.Drawing.Point(2, 22);
            this.cbxEmotionList.Name = "cbxEmotionList";
            this.cbxEmotionList.Size = new System.Drawing.Size(196, 26);
            this.cbxEmotionList.TabIndex = 1;
            // 
            // groupBox3
            // 
            this.groupBox3.AutoSize = true;
            this.groupBox3.Controls.Add(this.rbStandby);
            this.groupBox3.Controls.Add(this.rbTraining);
            this.groupBox3.Controls.Add(this.rbConversation);
            this.groupBox3.Dock = System.Windows.Forms.DockStyle.Top;
            this.groupBox3.Location = new System.Drawing.Point(0, 0);
            this.groupBox3.Name = "groupBox3";
            this.groupBox3.Size = new System.Drawing.Size(200, 87);
            this.groupBox3.TabIndex = 1;
            this.groupBox3.TabStop = false;
            this.groupBox3.Text = "Mode switch";
            // 
            // rbTraining
            // 
            this.rbTraining.AutoSize = true;
            this.rbTraining.Dock = System.Windows.Forms.DockStyle.Top;
            this.rbTraining.Location = new System.Drawing.Point(3, 42);
            this.rbTraining.Name = "rbTraining";
            this.rbTraining.Size = new System.Drawing.Size(194, 21);
            this.rbTraining.TabIndex = 2;
            this.rbTraining.TabStop = true;
            this.rbTraining.Text = "Training";
            this.rbTraining.UseVisualStyleBackColor = true;
            this.rbTraining.CheckedChanged += new System.EventHandler(this.rbTraining_CheckedChanged);
            // 
            // rbConversation
            // 
            this.rbConversation.AutoSize = true;
            this.rbConversation.Dock = System.Windows.Forms.DockStyle.Top;
            this.rbConversation.Location = new System.Drawing.Point(3, 21);
            this.rbConversation.Name = "rbConversation";
            this.rbConversation.Size = new System.Drawing.Size(194, 21);
            this.rbConversation.TabIndex = 1;
            this.rbConversation.TabStop = true;
            this.rbConversation.Text = "Conversation";
            this.rbConversation.UseVisualStyleBackColor = true;
            this.rbConversation.CheckedChanged += new System.EventHandler(this.rbConversation_CheckedChanged);
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.groupBox2);
            this.panel2.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel2.Location = new System.Drawing.Point(177, 0);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(200, 210);
            this.panel2.TabIndex = 1;
            // 
            // panel3
            // 
            this.panel3.Controls.Add(this.groupBox3);
            this.panel3.Dock = System.Windows.Forms.DockStyle.Left;
            this.panel3.Location = new System.Drawing.Point(377, 0);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(200, 210);
            this.panel3.TabIndex = 2;
            // 
            // rbStandby
            // 
            this.rbStandby.AutoSize = true;
            this.rbStandby.Dock = System.Windows.Forms.DockStyle.Top;
            this.rbStandby.Location = new System.Drawing.Point(3, 63);
            this.rbStandby.Name = "rbStandby";
            this.rbStandby.Size = new System.Drawing.Size(194, 21);
            this.rbStandby.TabIndex = 3;
            this.rbStandby.TabStop = true;
            this.rbStandby.Text = "Standby";
            this.rbStandby.UseVisualStyleBackColor = true;
            this.rbStandby.CheckedChanged += new System.EventHandler(this.rbStandby_CheckedChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 17F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoSize = true;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(568, 210);
            this.Controls.Add(this.panel3);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Font = new System.Drawing.Font("Arial", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Margin = new System.Windows.Forms.Padding(3, 4, 3, 4);
            this.Name = "Form1";
            this.Text = "Cubi Remote";
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox3.ResumeLayout(false);
            this.groupBox3.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.GroupBox colorBox;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button btnStart;
        private System.Windows.Forms.ComboBox cbxEmotionList;
        private System.Windows.Forms.GroupBox groupBox3;
        private System.Windows.Forms.RadioButton rbTraining;
        private System.Windows.Forms.RadioButton rbConversation;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.RadioButton rbStandby;
    }
}

