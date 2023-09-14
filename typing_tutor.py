import tkinter
from tkinter import *
from tkinter import messagebox
import datetime
from tkinter import ttk
from paragraph import Paragraph


class Application(Paragraph):
	paragraph = Paragraph.para2

	def key_bindings(self):
		def accuracy_checker(key):
			right = 0
			wrong = 0
			length = 0
			inp_text = self.paragraph_box1.get(1.0,'end')
			inp_text_len = len(inp_text)
			inp_text = inp_text.split()
			para = self.paragraph.split()
			for i in range(len(inp_text)):
				if inp_text[i] == para[i]:
					right +=1
					length = length + len(para[i]) + 1 
				elif inp_text[i] != para[i]:
					wrong +=1
					self.paragraph_box.config(state=NORMAL)
					self.paragraph_box.tag_add("start", f"1.{length}",f"1.{length + len(para[i])}")
					self.paragraph_box.tag_config("start", background= "red", foreground= "black")
					self.paragraph_box.config(state=DISABLED)
					length = length + len(para[i]) + 1 
	
			Total_word = len(inp_text)
			time= int(self.time_combo_box.get()) * 60 - (self.time_choosen - 671400)
			time = time / 60
			self.grs_speed = round(Total_word / time)
			self.avg_speed = round(right / time)
			self.grs_display.config(state=NORMAL)
			self.grs_display.delete(0,'end')
			self.grs_display.insert(0,self.grs_speed)
			self.grs_display.config(state=DISABLED)
			self.avg_display.config(state=NORMAL)
			self.avg_display.delete(0,'end')
			self.avg_display.insert(0,self.avg_speed)
			self.avg_display.config(state=DISABLED)
			self.accuracy=  f'{(right / Total_word) * 100:.2f}%'
			self.acc_display.config(state=NORMAL)
			self.acc_display.delete(0,'end')
			self.acc_display.insert(0,self.accuracy)
			self.acc_display.config(state=DISABLED)

		self.paragraph_box1.bind('<space>', accuracy_checker)

		def timer_activator(key):
			if key.char:	
				if self.paragraph_box1.get(1.0).isalpha() == False:
					self.time_choosen = 671400 + int(self.time_combo_box.get()) * 60
				def timer():
					tt = datetime.datetime.fromtimestamp(self.time_choosen)
					self.string = tt.strftime("%M:%S")
					self.clock_label.config(text= self.string)
					if self.string == '00:00':
						messagebox.showinfo('Result',f"Gross Speed: {self.grs_speed}\nAvg. Speed: {self.avg_speed}\nAccuracy: {self.accuracy}")
					else:
						self.clock_label.after(1000,timer)
						self.time_choosen -=1

				if self.paragraph_box1.get(1.0).isalpha() == False:
					timer()

		self.paragraph_box1.bind('<Key>',timer_activator)

	def display(self):
		self.app = tkinter.Tk()
		self.app.title('Instant - Typing Tutor')
		self.app.geometry('800x610')
		self.app.resizable(False,False)

	def buttons(self):
		def restart():
			self.paragraph_box1.delete(1.0,'end')
			self.paragraph_box.tag_remove("start",1.0,'end')
			self.time_choosen = 671400
			self.grs_display.config(state=NORMAL)
			self.grs_display.delete(0,'end')
			self.grs_display.insert(0,'00')
			self.grs_display.config(state=DISABLED)
			self.avg_display.config(state=NORMAL)
			self.avg_display.delete(0,'end')
			self.avg_display.insert(0,'00')
			self.avg_display.config(state=DISABLED)
			self.acc_display.config(state=NORMAL)
			self.acc_display.delete(0,'end')
			self.acc_display.insert(0,'00.00%')
			self.acc_display.config(state=DISABLED)

		self.restart_button = tkinter.Button(self.frame2,text='RESTART',command=restart)
		self.restart_button.grid(row=3,column=0,sticky='news',pady=5)

		clock_frame = tkinter.LabelFrame(self.frame2,text='# Time')
		clock_frame.grid(row=2,column=0,sticky='news',pady=5)
		self.clock_label = tkinter.Label(clock_frame,text='00:00')
		self.clock_label.grid(row=0,column=0)
		time_label= tkinter.Label(self.frame2,text='Select the typing time')
		time_label.grid(row=0,column=0,pady=5)
		self.time_combo_box = ttk.Combobox(self.frame2,values=['5','10','15','20','30'])
		self.time_combo_box.current(0)
		self.time_combo_box.grid(row=1,column=0)
		accuracy_frame= tkinter.LabelFrame(self.frame2)
		accuracy_frame.grid(row=4,column=0,pady=5,sticky='news')
		label_avg_speed= tkinter.Label(accuracy_frame,text='Avg. Speed')
		label_avg_speed.grid(row=0,column=0)
		self.avg_display= tkinter.Entry(accuracy_frame)
		self.avg_display.insert(0, '00')
		self.avg_display.config(state=DISABLED)
		self.avg_display.grid(row=1,column=0,pady=5)
		label_grs_speed= tkinter.Label(accuracy_frame,text='Gross Speed')
		label_grs_speed.grid(row=2,column=0)
		self.grs_display= tkinter.Entry(accuracy_frame)
		self.grs_display.insert(0, '00')
		self.grs_display.config(state=DISABLED)
		self.grs_display.grid(row=3,column=0,pady=5)
		label_accuracy= tkinter.Label(accuracy_frame,text='Avg. Accuracy')
		label_accuracy.grid(row=4,column=0)
		self.acc_display= tkinter.Entry(accuracy_frame)
		self.acc_display.insert(0, '00:00%')
		self.acc_display.config(state=DISABLED)
		self.acc_display.grid(row=5,column=0,pady=5)

	def copyright(self):
		copyright_label = tkinter.Label(self.app,text='Copyright: © Surendar Singh')
		copyright_label.pack(side='bottom')

	def label_frame(self):
		self.frame1 = tkinter.Frame(self.app,width=600,height=600)
		self.frame1.pack(side='left')
		self.frame2 = tkinter.Frame(self.app,width=200,height=600)
		self.frame2.pack(side='right')

	def paragraph_read(self):
		paragraph = tkinter.Label(self.frame1, text='PARAGRAPH', font=('TIMES NEW ROMAN', 15, 'bold'))
		paragraph.grid(row=0,column=0)
		self.paragraph_box = tkinter.Text(self.frame1,width=80,height=16,wrap=WORD)
		self.paragraph_box.tag_configure("center", justify='center')
		self.paragraph_box.insert('1.0',self.paragraph)
		self.paragraph_box.config(state=DISABLED)
		self.paragraph_box.grid(row=1,column=0)

	def paragraph_write(self):
		paragraph = tkinter.Label(self.frame1, text='START TYPING BELOW', font=('TIMES NEW ROMAN', 15, 'bold'))
		paragraph.grid(row=2,column=0)
		self.paragraph_box1 = tkinter.Text(self.frame1,width=80,height=16,wrap=WORD)
		self.paragraph_box1.tag_configure("center", justify='center')
		self.paragraph_box1.grid(row=3,column=0)

	def scrollbar(self):
		self.sb = tkinter.Scrollbar(self.frame1,orient='vertical',command=self.paragraph_box.yview)
		self.sb.grid(row=1,column=1,sticky='ns')
		self.paragraph_box.configure(yscrollcommand=self.sb.set)
		self.sb1 = tkinter.Scrollbar(self.frame1,orient='vertical',command=self.paragraph_box1.yview)
		self.sb1.grid(row=3,column=1,sticky='ns')
		self.paragraph_box1.configure(yscrollcommand=self.sb1.set)

	def loop(self):
		self.app.mainloop()


if __name__ == '__main__':
	tt= Application()
	tt.display()
	tt.copyright()
	tt.label_frame()
	tt.paragraph_read()
	tt.paragraph_write()
	tt.scrollbar()
	tt.buttons()
	tt.key_bindings()
	tt.loop()
