import tkinter as tk

def run_math(event):
    x1 = entry_point1_x.get()
    y1 = entry_point1_y.get()
    coordinates ={'point1':{'x':entry_point1_x.get(),'y':entry_point1_y.get()}}
    coordinates['point2'] = {'x':entry_point2_x.get(),'y':entry_point2_y.get()}
    coordinates['point3'] = {'x':entry_point3_x.get(),'y':entry_point3_y.get()}
    coordinates['point4'] = {'x':entry_point4_x.get(),'y':entry_point4_y.get()}
    coordinates['point5'] = {'x':entry_point5_x.get(),'y':entry_point5_y.get()}
    coordinates['point6'] = {'x':entry_point6_x.get(),'y':entry_point6_y.get()}
    out_text = ''
    i=0
    for point in coordinates:
        i+=1
        out_text +='x'+str(i)+' = '+coordinates['point'+str(i)]['x']+', y'+str(i)+' = '+ coordinates['point'+str(i)]['y'] + '\n'

    label_test.config(text = out_text)

root = tk.Tk()
root.geometry("800x600+100+50")
root.title('Поперечный срез №5')

# frame = tk.Frame(root,borderwidth=2,relief="solid")
# frame.pack()
label_form_name = tk.Label(root,text="Координаты точек")
label_form_name.grid(row=0,column=0,columnspan=4,padx=0,pady=5)

label_point1 = tk.Label(root,text="Точка 1")
label_point1.grid(row=2,column=0,columnspan=4,padx=5,pady=5)
label_point1_x = tk.Label(root,text="x")
label_point1_x.grid(row=3,column=0, padx=5,pady=5)
entry_point1_x = tk.Entry(root,width=4)
entry_point1_x.grid(row=3,column=1,padx=5,pady=5)
label_point1_y = tk.Label(root,text="y")
label_point1_y.grid(row=3,column=2, padx=5,pady=5)
entry_point1_y = tk.Entry(root,width=4)
entry_point1_y.grid(row=3,column=3,padx=5,pady=5)

label_point2 = tk.Label(root,text="Точка 2")
label_point2.grid(row=4,column=0,columnspan=4,padx=5,pady=5)
label_point2_x = tk.Label(root,text="x")
label_point2_x.grid(row=5,column=0, padx=5,pady=5)
entry_point2_x = tk.Entry(root,width=4)
entry_point2_x.grid(row=5,column=1,padx=5,pady=5)
label_point2_y = tk.Label(root,text="y")
label_point2_y.grid(row=5,column=2, padx=5,pady=5)
entry_point2_y = tk.Entry(root,width=4)
entry_point2_y.grid(row=5,column=3,padx=5,pady=5)

label_point3 = tk.Label(root,text="Точка 3")
label_point3.grid(row=6,column=0,columnspan=4,padx=5,pady=5)
label_point3_x = tk.Label(root,text="x")
label_point3_x.grid(row=7,column=0, padx=5,pady=5)
entry_point3_x = tk.Entry(root,width=4)
entry_point3_x.grid(row=7,column=1,padx=5,pady=5)
label_point3_y = tk.Label(root,text="y")
label_point3_y.grid(row=7,column=2, padx=5,pady=5)
entry_point3_y = tk.Entry(root,width=4)
entry_point3_y.grid(row=7,column=3,padx=5,pady=5)

label_point4 = tk.Label(root,text="Точка 4")
label_point4.grid(row=8,column=0,columnspan=4,padx=5,pady=5)
label_point4_x = tk.Label(root,text="x")
label_point4_x.grid(row=9,column=0, padx=5,pady=5)
entry_point4_x = tk.Entry(root,width=4)
entry_point4_x.grid(row=9,column=1,padx=5,pady=5)
label_point4_y = tk.Label(root,text="y")
label_point4_y.grid(row=9,column=2, padx=5,pady=5)
entry_point4_y = tk.Entry(root,width=4)
entry_point4_y.grid(row=9,column=3,padx=5,pady=5)

label_point5 = tk.Label(root,text="Точка 5")
label_point5.grid(row=10,column=0,columnspan=4,padx=5,pady=5)
label_point5_x = tk.Label(root,text="x")
label_point5_x.grid(row=11,column=0, padx=5,pady=5)
entry_point5_x = tk.Entry(root,width=4)
entry_point5_x.grid(row=11,column=1,padx=5,pady=5)
label_point5_y = tk.Label(root,text="y")
label_point5_y.grid(row=11,column=2, padx=5,pady=5)
entry_point5_y = tk.Entry(root,width=4)
entry_point5_y.grid(row=11,column=3,padx=5,pady=5)

label_point6 = tk.Label(root,text="Точка 6")
label_point6.grid(row=12,column=0,columnspan=4,padx=5,pady=5)
label_point6_x = tk.Label(root,text="x")
label_point6_x.grid(row=13,column=0, padx=5,pady=5)
entry_point6_x = tk.Entry(root,width=4)
entry_point6_x.grid(row=13,column=1,padx=5,pady=5)
label_point6_y = tk.Label(root,text="y")
label_point6_y.grid(row=13,column=2, padx=5,pady=5)
entry_point6_y = tk.Entry(root,width=4)
entry_point6_y.grid(row=13,column=3,padx=5,pady=5)

frame = tk.Frame(root, borderwidth=0, relief="sunken")
frame.place(x=200,y=10,width=300,height=500)

label_test = tk.Label(frame)
label_test.grid(row=0,column=6,padx=5,pady=5)

button = tk.Button(root,text="Рассчитать")
button.bind('<Return>',run_math)
button.bind('<Button-1>',run_math)
button.grid(row=15, column=0, columnspan=4, pady=10)

root.mainloop()