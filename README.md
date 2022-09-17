# retail-management-system
WORKING DESCRIPTION
I designed this project for the purpose of handling the sales of commodities in businesses. For this I used various libraries in the following ways:

1)Mysql.connector
My python program is designed in a way to connect to a database in mysql and fetch data from tables or create or delete tables. I used the library mysql.connector
for this purpose. I pre-stored data for some months  in different tables in mysql. I fetch data from the tables using parameterized queries. And then I used the data for providing bar graphs in my project. I also used parameterized queries to create and delete tables.


2)Matplotlib 
After fetching data from mysql database I decided to plot them on a bar graph using matplotlib.pyplot. the retrieved data in the form of tuples is stored in two lists that I later plot on x and y axis of the bar graph . The x axis has commodities while y has a choice between sale quantity and prices of goods.

 

3)tkinter 

I used tkinter to give an interface to my program and to create a window like structure for taking input . in the window I created 3 options for the user between new table ,delete table and read table. These are in the form of buttons that when pressed take required inputs


i)New table
Clicking on the button takes you to a new window where you are required to enter the name of the table .then it gives you an option to add as many rows as you want in the new table you have created . all the buttons use the commands written as functions.

ii)Read table 
This button takes you to a window where you have to enter the name of the month that you want to fetch the data from and then you select the data from a drop down list consisting of sale quantity and quality .


iii)delete table 
this button executes the drop table command .clicking on this button takes you to another window where it asks you for the name of the table that you need to delete and deletes it .


iv) submit button 
 a frame is like a list in tkinter .the data (input taken ) is stored in a frame in tkinter .the submit button uses text from the input boxes and stores it in a class for the  matplotlib /my sql part to function



v) root.mainloop()
it is used to initiate tkinter .without this tkinter will not work .








Along with this I used tkinter to give shape and structure to the window that asks for input from the user .
The data is stored in a frame in tkinter that is then used in a class for execution in matplotlib and mysql part
