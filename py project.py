import tkinter as tk
import mysql.connector as  sqlcon
import matplotlib.pyplot as plt
con1=sqlcon.connect(host="localhost",user="root",passwd="1234",database="project")
if con1.is_connected():
    print("connection established")
else:
    print("error")
cursor1=con1.cursor()
tablename=''
def list_tuple(s,l):
    global root
    #root.destroy()    #execute continuously
    first_tuple_elements = []
    second_elements=[]
    for a_tuple in l:
         first_tuple_elements.append(a_tuple[0])
         second_elements.append(a_tuple[1])
    plt.bar(first_tuple_elements,second_elements)
    plt.ylabel(s)
    plt.xlabel("commodities")
    plt.show()
def Newtable():
	global add
	global dele
	global read
	global newlbl
	global table_entry
	global sub_but
	
	try:
		add.pack_forget()
	except:
		pass
	try:
		dele.pack_forget()
	except:
		pass
	try:
		read.pack_forget()
	except:
		pass
	
	newlbl.pack(pady=20)
	
	table_entry.pack(pady=5)
	
	sub_but.pack(pady=5)
def onSub():
	global newlbl
	global table_entry
	global sub_but
	global add
	global tablename
	tablename=table_entry.get()
	newlbl.pack_forget()
	table_entry.pack_forget()
	sub_but.pack_forget()
	add.pack(pady=20)
def Deletetable():
	global add
	global dele
	global read
	try:
		add.pack_forget()
	except:
		pass
	try:
		dele.pack_forget()
	except:
		pass
	try:
		read.pack_forget()
	except:
		pass
	try:
		newlbl.pack_forget()
	except:
		pass
	try:
		table_entry.pack_forget()
	except:
		pass
	try:
		sub_but.pack_forget()
	except:
		pass
	dele.pack(pady=20)	
def Readtable():
	global add
	global dele
	global read
	try:
		add.pack_forget()
	except:
		pass
	try:
		dele.pack_forget()
	except:
		pass
	try:
		read.pack_forget()
	except:
		pass
	read.pack(pady=20)
class NewDialog:
    
    def __init__(self, parent):                #for input boxes
        top = self.top = tk.Toplevel(parent)
        self.mainframe=tk.Frame(top)      #frame like a list in tk
        self.mainframe.pack()
        self.myLabel1 = tk.Label(self.mainframe, text='Enter Object Code')
        self.o_entry = tk.Entry(self.mainframe)
        self.myLabel2 = tk.Label(self.mainframe, text='Enter  Commodity')
        self.c_entry = tk.Entry(self.mainframe)
        self.myLabel3 = tk.Label(self.mainframe, text='Enter Price')
        self.p_entry = tk.Entry(self.mainframe)
        self.myLabel4 = tk.Label(self.mainframe, text='Enter Quantity')
        self.q_entry = tk.Entry(self.mainframe)
        self.myLabel5 = tk.Label(self.mainframe, text='Enter Sales')
        self.s_entry = tk.Entry(self.mainframe)
        self.myLabel1.grid(row=0,column=1,padx=3,pady=5)
        self.o_entry.grid(row=0,column=2,padx=3,pady=5)
        self.myLabel2.grid(row=1,column=1,padx=3,pady=5)
        self.c_entry.grid(row=1,column=2,padx=3,pady=5)
        self.myLabel3.grid(row=2,column=1,padx=3,pady=5)
        self.p_entry.grid(row=2,column=2,padx=3,pady=5)
        self.myLabel4.grid(row=3,column=1,padx=3,pady=5)
        self.q_entry.grid(row=3,column=2,padx=3,pady=5)
        self.myLabel5.grid(row=4,column=1,padx=3,pady=5)
        self.s_entry.grid(row=4,column=2,padx=3,pady=5)
        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()
    def send(self):                        #uses text from input boxes 
        self.ocod = self.o_entry.get()        #stored in class
        self.comm=self.c_entry.get()
        self.pric=self.p_entry.get()
        self.quan=self.q_entry.get()
        self.sal=self.s_entry.get()
        self.top.destroy()                  #to close text box
def onClick():                    #parent   #passes all sql commands
    id = NewDialog(root) #to open new window within a window id
    root.wait_window(id.top)            #waits till window is closed
    try:
        cursor1.execute("create table {}(o_code int primary key,commodity varchar(20),quantity int,price int,sale int)".format(tablename))
    except:
        pass
    try:
    	query="insert into {} values({},'{}',{},{},{})".format(tablename,id.ocod,id.comm,id.pric,id.quan,id.sal)   #id is dialogue box
    	cursor1.execute(query)
    	con.commit()
    except:
    	pass
class DelDialog:
	def __init__(self,parent):
		top=self.top=tk.Toplevel(parent)
		self.mainframe=tk.Frame(top)
		self.mainframe.pack()
		self.myLabel1=tk.Label(self.mainframe,text="Enter Table Name")
		self.t_entry=tk.Entry(self.mainframe)
		self.myLabel1.grid(row=0,column=1,padx=3,pady=5)
		self.t_entry.grid(row=0,column=2,padx=3,pady=5)
		self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
		self.mySubmitButton.pack()
	def send(self):
		self.table=self.t_entry.get()
		self.top.destroy()
def onClick2():
	deleteDialog=DelDialog(root)
	root.wait_window(deleteDialog.top)
	try:
		cursor1.execute("drop table {}".format(deleteDialog.table))
		con.commit()
	except:
		pass
class ReadDialog:
	list=['Sale','Quantity','Price']
	def __init__(self,parent):
		top=self.top=tk.Toplevel(parent)  #new window on top  of parent 
		self.mainframe=tk.Frame(top)
		self.mainframe.pack()
		self.myLabel1=tk.Label(self.mainframe,text="Enter Table Name")
		self.t_entry=tk.Entry(self.mainframe)
		self.myLabel2=tk.Label(self.mainframe,text="Plot against")
		self.variable=tk.StringVar(self.mainframe)
		self.variable.set(self.list[0])
		self.menu=tk.OptionMenu(self.mainframe,self.variable,*self.list)
		self.myLabel1.grid(row=0,column=1,padx=3,pady=5)
		self.t_entry.grid(row=0,column=2,padx=3,pady=5)
		self.myLabel2.grid(row=1,column=1,padx=3,pady=5)
		self.menu.grid(row=1,column=2,padx=3,pady=5)
		self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
		self.mySubmitButton.pack()
	def send(self):
		self.table=self.t_entry.get()
		self.choice=self.variable.get()
		self.top.destroy()
def onClick3():
	readDialog=ReadDialog(root)
	root.wait_window(readDialog.top)
	try:
		query="select commodity,{} from {}".format(readDialog.choice,readDialog.table)
		cursor1.execute(query)
		list_tuple(readDialog.choice,cursor1.fetchall())
	except:
		pass
	#print(readDialog.choice)
root=tk.Tk()
root.title("Arya's Project")
##mainwin=tk.Canvas(root,width = 400, height = 450)
##mainwin.pack()
Label1=tk.Label(root,text="What do you wanna do?")
#mainwin.create_window(window=label1)
Label1.pack()
buttons=tk.Frame(root)
buttons.pack()
newlbl=tk.Label(root,text="Enter Table Name Below")  #label for window
table_entry=tk.Entry(root)
sub_but=tk.Button(root,text="Submit",command=onSub)
add=tk.Button(root,text='Add row',command=onClick)
dele=tk.Button(root,text='Delete by Name',command=onClick2)
read=tk.Button(root,text='Read Data by Name',command=onClick3)
New=tk.Button(buttons,text='New Table',command=Newtable)
Del=tk.Button(buttons,text='Delete Table',command=Deletetable)
Rea=tk.Button(buttons,text='Read Table',command=Readtable)
New.grid(row=0, column=1,padx=5,pady=15)
Del.grid(row=0, column=2,padx=5,pady=15)
Rea.grid(row=0, column=3,padx=5,pady=15)
buttons.grid_columnconfigure(0, weight=1) #for neatness
buttons.grid_columnconfigure(4, weight=1)

root.mainloop()     #to initiate tkinter
