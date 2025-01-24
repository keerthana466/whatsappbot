import webbrowser as wb
from keyboard import press
import time
import datetime

def whatsapp(to,message):
    time.sleep(wait)
    wb.open_new_tab("https://web.whatsapp.com/send?phone="+to+'&text='+message)
    time.sleep(20)
    press('enter')

def Time():
    Time= datetime.datetime.now().strftime("%H:%M:%S")



if __name__ == "__main__":
    Time()
    while True:

        to = input("Whom should i contact?")
        message= input("What should I say?")

        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        second = datetime.datetime.now().second
        c_hour = int(hour*60*60)
        c_minute = int(minute*60)
        c_second = int(second)
        c_Time = int(c_hour + c_minute + c_second)



        send_hour = input("When should I send it?(hour)")
        send_minute = input("Tell me about the minutes?")
        send_second = input("when about the seconds?")

        send_time = str(send_hour+':'+send_minute+':'+send_second)
        print(send_time)

        #wait time
        n_hour = int(int(send_hour)*60*60)
        n_minute = int(int(send_minute)*60)
        n_second = int(send_second)

        n_time = int(n_hour+n_minute+n_second) 

        wait = int(n_time-c_Time) #no.of seconds to wait
        print("Your message will be sent after "+str(wait)+"seconds")
        whatsapp(to,message)