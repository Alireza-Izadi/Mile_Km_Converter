import tkinter

window = tkinter.Tk()
window.minsize(width=300, height=200)
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)
#Get Input from the user
input = tkinter.Entry()
input.grid(column=1, row=0)

#Mile Label
mile_label = tkinter.Label(text="Miles")
mile_label.config(padx=10)
mile_label.grid(column=2, row=0)
#is equal to label
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.config(pady=20)
equal_to_label.grid(column=0, row=1)
#Converted number label(km)
converted_label =tkinter.Label(text= "0")
converted_label.grid(column=1, row=1)
#km label
km_label  = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)


#calculate button
def calculate():
    converted_label.config(text=str(int(input.get())*1.6093))

calculate_button = tkinter.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)




window.mainloop()