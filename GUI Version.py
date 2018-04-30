from tkinter import *
import pandas as pd
import quandl
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

root=Tk()
root.title('Stock Market Predictor')
var=IntVar()

def stock_name():
    global stock
    stock=int(var.get())
    
def submit():
    if stock==1:
        stock1='Bombay Stock Exchange'
        L5.config(text=stock1)
    elif stock==2:
        stock2='National Stock Exchange of India Ltd.'
        L5.config(text=stock2)
    if stock==2:
        name='NSE'
    else:
        name='BOM'    
    company_name=str(E1.get())
    quandl.ApiConfig.api_key = "bSsk6gidxG91jv-wcrWy"
    if(name=="NSE"):
        df=quandl.get('NSE/'+company_name)
    elif(name=="BOM"):
        df=quandl.get('BSE/'+name+company_name)
    df=df[['Open','High','Low','Close']]
    df=df.dropna()
    x=df[['Open','High','Low']]
    y=df['Close']
    x_train,x_test,y_train,y_test=train_test_split(x,y)
    reg=LinearRegression()
    reg.fit(x_train,y_train)
    
    uclient=req("https://finance.google.com/finance?q="+name+"%3A"+company_name+"&ei=I1HcWZKjOJCQuQTKl6OADA")
    page_html=uclient.read()
    uclient.close()
    page_soup=soup(page_html,"html.parser")
    current=page_soup.findAll("table",{"class":"snap-data"})
    x1=current[0]
    x2=x1.tr
    x3=x2.findAll("td",{"class":"val"})
    x4=x3[0].text
    x5=x4.strip()
    x6=x5.split("-")
    x7=x6[0]
    x8=x7.split(" ")
    low=x8[0]

    x10=x6[1]
    x11=x10.split(" ")
    x12=x11[1]
    high=x12

    y1=page_soup.body
    y2=y1.findAll("table",{"class":"snap-data"})
    y3=y2[0]
    y4=y3.findAll("td",{"class":"val"})
    opn=y4[2].text.strip()

    name1=page_soup.title.text
    name2=name1.split(":")
    stock_name=name2[0]
    
    L7.config(text=stock_name)
    L9.config(text=opn)
    L11.config(text=high)
    L13.config(text=low)

    p={'Open':[opn],
   'High':[high],
   'Low':[low]
   }
    df1=pd.DataFrame(p)
    x1231=reg.predict(df1)
    x1232=x1231[0]
    x123=format(x1232,'.2f')
    L15.config(text=x123)

def clear():
    E1.delete(0,END)
    var.set(0)
    L5.config(text="")
    L7.config(text="")
    L9.config(text="")
    L11.config(text="")
    L13.config(text="")
    L15.config(text="")

def close():
    root.destroy()

def refresh():
    L5.config(text="")
    L7.config(text="")
    L9.config(text="")
    L11.config(text="")
    L13.config(text="")
    L15.config(text="")
    submit()
        
#####
F1=Frame(root)
F1.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L1=Label(F1,text='Stock Exchange :',bg='light green')
L1.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

R1=Radiobutton(F1,text='BSE',variable=var,value=1,command=stock_name)
R1.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT,anchor=W)

R2=Radiobutton(F1,text='NSE',variable=var,value=2,command=stock_name)
R2.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT,anchor=W)

#####
F2=Frame(root)
F2.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L2=Label(F2,text='Company Code :',bg='light green')
L2.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

E1=Entry(F2)
E1.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

B1=Button(F2,text='Enter',bg='sky blue',command=submit)
B1.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

#####
F3=Frame(root)
F3.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L3=Label(F3,text='DATA',bg='red')
L3.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

#####
F4=Frame(root)
F4.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L4=Label(F4,text='Stock Exchange Name :',bg='gold')
L4.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L5=Label(F4)
L5.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F5=Frame(root)
F5.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L6=Label(F5,text='Company Name :',bg='gold')
L6.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L7=Label(F5)
L7.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F6=Frame(root)
F6.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L8=Label(F6,text='Opening Price :',bg='gold')
L8.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L9=Label(F6)
L9.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F7=Frame(root)
F7.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L10=Label(F7,text='Todays High :',bg='gold')
L10.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L11=Label(F7)
L11.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F8=Frame(root)
F8.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L12=Label(F8,text='Todays Low :',bg='gold')
L12.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L13=Label(F8)
L13.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F9=Frame(root)
F9.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L14=Label(F9,text='Expected Closing Price :',bg='gold')
L14.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L15=Label(F9)
L15.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=RIGHT)

#####
F10=Frame(root)
F10.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

B2=Button(F10,text='Refresh',bg='sky blue',command=refresh)
B2.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

B3=Button(F10,text='Clear',bg='sky blue',command=clear)
B3.pack(side=LEFT,fill=BOTH,expand=YES,padx=5,pady=5)

B4=Button(F10,text='Close',bg='sky blue',command=close)
B4.pack(side=RIGHT,fill=BOTH,expand=YES,padx=5,pady=5)

#####
F11=Frame(root)
F11.pack(side=TOP,padx=5,pady=5,fill=BOTH,expand=YES)

L16=Label(F11,text='Data Courtesy : Quandl & Google Finance')
L16.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)

L17=Label(F11,text='(Prices in INR)')
L17.pack(fill=BOTH,expand=YES,padx=5,pady=5,side=LEFT)













