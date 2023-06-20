# Basic tkinter template

from tkinter import *Tk
root = Tk()

root.title("Driver's License")
root.geometry("300x400")

root.configure(bg="white")
canvas=Canvas(root,width=400,height=250)
canvas.create_image(0,0,anchor=NW)
canvas.create_rectangle(0, 0, 400, 45, fill="#F6091E")


label_heading = canvas.create_text(200,20, font=('Times', '24', 'bold italic') ,text="Driving License", fill = "white")
label_id_tag = canvas.create_text(25,60, font=('Times', '14', 'bold') ,text="ID :")
label_name_tag = canvas.create_text(30,100, font=('Times', '12', 'bold') ,text="Name :")
label_dob_tag = canvas.create_text(52,120, font=('Times', '12', 'bold') ,text="Date of birth :")
label_pin_tag = canvas.create_text(32,140, font=('Times', '12', 'bold') ,text="Pin no. :")
label_address_tag = canvas.create_text(36,160, font=('Times', '12', 'bold') ,text="Address :")
label_vehicle_type_tag = canvas.create_text(155,180, font=('Times', '12', 'bold') ,text="Authorisation to drive the following vehicles :")

label_id_tag = Label(root)
label_name_tag = Label(root)
label_dob_tag = Label(root)
label_pin_tag = Label(root)
label_address_tag = Label(root)
label_vehicle_type_tag = Label(root)
 
def myCardDetails():
    idtag = 19827198349
    print(type(idtag))   
    nametag = "Winnie the Pooh"
    print(type(nametag))
    dobtag = "August 21, 1921"
    print(type(dobtag))
    pintag = 451478
    print(type(pintag))
    addresstag = "Disney Land, Hong Kong"
    print(type(addresstag))
    vehicletag = "Two Four"
    print(type(vehicletag))
    
    label_id_tag['text'] = idtag
    label_name_tag['text'] = nametag
    label_dob_tag['text'] = dobtag
    label_pin_tag['text'] = pintag
    label_address_tag['text'] = addresstag
    label_vehicle_type_tag['text'] = vehicletag
    
    
button1 = Button(root, text = "Show my Driving License", command=myCardDetails)

button1.configure(width = 20 , activebackground = "#9EC6EE", relief= FLAT)
button1_window = canvas.create_window(200, 235, anchor=CENTER, window=button1)
label_id_window = canvas.create_window(80, 60, anchor=CENTER, window=label_id)
label_name_window = canvas.create_window(100, 100, anchor=CENTER, window=label_name)
label_dob_window = canvas.create_window(140, 120, anchor=CENTER, window=label_dob)
label_pin_window = canvas.create_window(85, 140, anchor=CENTER, window=label_pin)
label_address_window = canvas.create_window(130, 160, anchor=CENTER, window=label_address)
label_vehicle_no_window = canvas.create_window(335, 180, anchor=CENTER, window=label_vehicle_type)
canvas.pack()

root.mainloop()
# tkinter basic template end statement
