from customtkinter import *
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import warnings
win = CTk()
win.title("Area Price Prediction")
win.geometry("343x455+500+80")
win.resizable(False, False)
win.config(bg="#333333")
# /////////////////////////////////////
def get_value():
    warnings.filterwarnings("ignore")
    area_x = eval(area_value.get())
    file = pd.read_csv("C:\\Users\\Rishikesh\\OneDrive\\Desktop\\Machine Models\\Area Price Prediction\\areaprice071.csv")
    area = file[["area"]]
    price = file["price"]
    train_x,test_x,train_y,test_y=train_test_split(area,price)
    model = LinearRegression()
    model.fit(train_x,train_y)
    prediction_price = model.predict([[area_x]])
    score_percent = model.score(test_x,test_y)
    price_value.configure(text=f"{round(prediction_price[0],2)} Rs.",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",18))
    if score_percent > 0:
        percentage_value.configure(text=f"{round(score_percent*100,)}.00%",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",20))
    else:
        percentage_value.configure(text="0.0%",text_color="#F5F5FA",font=("Franklin Gothic Demi Cond",20))
def clear():
    entry_label.delete(0,END)
    price_value.configure(text="000000000",font=("Franklin Gothic Demi Cond",22),text_color="#737373")
    percentage_value.configure(text="000%",font=("Franklin Gothic Demi Cond",22),text_color="#737373")
# /////////////////////////////////////////////////////////////////////////////////////////
message_label = CTkLabel(win,text="Enter  the  Area",font=("Franklin Gothic Demi Cond",22),
                        text_color="#EEEEEE",fg_color="#333333")
message_label.place(x=98,y=46)
message_label_1 = CTkLabel(win,text="⬇",font=("Franklin Gothic Demi Cond",20),
                        text_color="#EEEEEE",fg_color="#333333")
message_label_1.place(x=235,y=50)
area_value = StringVar()
entry_label = CTkEntry(win,text_color="#EEEEEE",font=("Franklin Gothic Demi Cond",18),bg_color="#333333",
                       height=35,width=246,border_width=1.50,border_color="#737373",
                       corner_radius=4,fg_color="#444444",textvariable=area_value)
entry_label.place(x=50,y=90)
generate_btn = CTkButton(win,text="Done",font=("Franklin Gothic Demi Cond",20),height=40,
                       width=120,text_color="#FFFFFF",fg_color="#009900",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#00cc00",
                       cursor="hand2",command=get_value)
generate_btn.place(x=50,y=145)
clear_btn = CTkButton(win,text="Clear",font=("Franklin Gothic Demi Cond",18),height=40,
                       width=120,text_color="#000000",fg_color="#EEEEEE",corner_radius=4,
                       border_color="#EEEEEE",border_width=1,hover_color="#ffffff",
                       cursor="hand2",command=clear)
clear_btn.place(x=176,y=145)
details_frame = CTkFrame(win,width=246,height=195,fg_color="#404040",border_width=2,border_color="#737373",bg_color="#333333")
price_tittle = CTkLabel(details_frame,text="______Price of Area______",font=("Franklin Gothic Demi Cond",17),width=242,text_color="#d9d9d9")
price_tittle.place(x=2,y=15)
price_value = CTkLabel(details_frame,text="000000000",font=("Franklin Gothic Demi Cond",22),width=242,text_color="#737373")
price_value.place(x=2,y=55)
percentage_tittle = CTkLabel(details_frame,text="______Accurate (%)______",font=("Franklin Gothic Demi Cond",17),width=242,text_color="#d9d9d9")
percentage_tittle.place(x=2,y=100)
percentage_value = CTkLabel(details_frame,text="000%",font=("Franklin Gothic Demi Cond",22),width=242,text_color="#737373")
percentage_value.place(x=2,y=140)
details_frame.place(x=50,y=210)
win.mainloop()