from tkinter import *


win=Tk()

Rate_11b={0:"1M",1:"2M",2:"5.5M",3:"11M"}
Rate_11g={0:"6M",1:"9M",2:"12M",3:"18M",4:"24M",5:"36M",6:"48M",7:"54M"}
Rate_11n={0:"MCS0",1:"MCS1",2:"1MCS2",3:"MCS3",4:"MCS4",5:"3MCS5",6:"MCS6",7:"MCS7"}
Rate_11n40={0:"MCS0",1:"MCS1",2:"1MCS2",3:"MCS3",4:"MCS4",5:"3MCS5",6:"MCS6",7:"MCS7"}

#for i in range(len(Rate_11n)):
#    Rate_11n[i]=StringVar()
#    Rate_11n40[i]=StringVar()
    
def SetstriVar(tuple_n={}):
    for i in range(len(tuple_n)):
        tuple_n[i]=StringVar()
        

SetstriVar(Rate_11b)
SetstriVar(Rate_11g)
SetstriVar(Rate_11n)
SetstriVar(Rate_11n40)


