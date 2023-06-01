import pyttsx3
import webbrowser
import time
now=time.ctime()
import pywhatkit
from tkinter import*
root=Tk()



def send():
    send="You->" + e.get()
    engine=pyttsx3.init()
    txt.insert(END, "\n"+send)


    if(e.get()=="hello"):
        engine.say("hey,how can I help you?")
        txt.insert(END,"\n"+"Travelly->Hi")
        engine.runAndWait()
    elif(e.get()=="hi"):
        engine.say("hey,how can i help you?")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->hey,how can I help you?")
    elif(e.get()=="how are you"):
        engine.say("I am fine,how can I help you?")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->I am fine,how can I help you?")
    elif(e.get()=="how to have a good vacation"):
        engine.say("I have helped people have an amazing time,let's get started. What can i show you- activities,flights,hotels,cuisines?")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->I have helped people have an amazing time,let's get started. What can i show you- activities,flights,hotels,cuisines?")
    elif(e.get()=="what can you do"):
        engine.say("I can provide you with flight information, hotels, cuisine and activities. Have an exciting holiday.")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->I can provide you with flight information, hotels, cuisine and activities. Have an exciting holiday.")
    elif(e.get()=="what is your name"):
        engine.say("my name is Travelly")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->my name is Travelly")
    elif(e.get()=="what are the activities present"):
        engine.say("hiking, skydiving, scuba diving, camel rides, safari, rafting and kayaking, skiing")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->hiking,skydiving,scuba diving,camel rides,safari,rafting and kayaking,skiing")
    elif(e.get()=="what are the activities"):
        engine.say("hiking, skydiving, scuba diving, camel rides, safari, rafting and kayaking, skiing")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->hiking,skydiving,scuba diving,camel rides,safari,rafting and kayaking,skiing")
    elif(e.get()=="activities"):
        engine.say("hiking, skydiving, scuba diving, camel rides, safari, rafting and kayaking, skiing")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->hiking,skydiving,scuba diving,camel rides,safari, rafting and kayaking,skiing")
    elif(e.get()=="hiking"):
        engine.say("Manali, Garhwal, Mussoorie, Darjeeling, Ladakh, Araku Valley, Munnar, Ooty, Kodaikanal")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Manali,Garhwal,Mussoorie,Darjeeling,Ladakh,Araku Valley,Munnar,Ooty,Kodaikanal")
    elif(e.get()=="safari"):
        engine.say("Ranthambore-Rajasthan, Hemis-Ladakh, Jim Corbett-Uttarakhand, Bandhavgarh-Madhya Pradesh, Sasan Gir-Gujarat, Kaziranga-Assam, Periyar-Kerala, Sunderbans-West Bengal, Maharashtra")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Ranthambore-Rajasthan,Hemis-Ladakh,Jim Corbett-Uttarakhand,Bandhavgarh-Madhya Pradesh,Sasan Gir-Gujarat,Kaziranga-Assam,Periyar-Kerala,Sunderbans-West Bengal,Maharashtra")
    elif(e.get()=="skydiving"):
        engine.say("Goa,Deesa-Gujarat, Pondicherry-Tamil Nadu, Aamby Valley-Maharashtra, Bir Billing-Himachal Pradesh")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Goa,Deesa-Gujarat,Pondicherry-Tamil Nadu,Aamby Valley-Maharashtra,Bir Billing-Himachal Pradesh")
    elif(e.get()=="air activities"):
        engine.say("Goa,Deesa-Gujarat, Pondicherry-Tamil Nadu, Aamby Valley-Maharashtra, Bir Billing-Himachal Pradesh")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Goa,Deesa-Gujarat,Pondicherry-Tamil Nadu,Aamby Valley-Maharashtra,Bir Billing-Himachal Pradesh")
    elif(e.get()=="scuba diving"):
        engine.say("Pristine island-Pondicherry, Netrani island-Karnataka, Tarkali-Maharashtra, Kovalam-Kerala, Lakshwadeep, Andaman and Nicobar")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Pristine island-Pondicherry,Netrani island-Karnataka,Tarkali-Maharashtra,Kovalam-Kerala,Lakshwadeep,Andaman and Nicobar")
    elif(e.get()=="camel rides"):
        engine.say("Ladakh, Jammu and Kashmir, Jaisalmer, Bikaner, Mandawa, Pushkar, Udaipur, Mandawa")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Ladakh,Jammu and Kashmir,Jaisalmer,Bikaner,Mandawa,Pushkar,Udaipur,Mandawa")
    elif(e.get()=="rafting"):
        engine.say("Rishikesh, Kullu-Manali, Leh-Ladakh, Uttarakhand, Sikkim, Arunachal Pradesh, Coorg, Ooty, Maharashtra")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Rishikesh,Kullu-Manali,Leh-Ladakh,Uttarakhand,Sikkim,Arunachal Pradesh,Coorg,Ooty,Maharashtra")
    elif(e.get()=="water activities"):
        engine.say("Rishikesh, Kullu-Manali, Leh-Ladakh, Uttarakhand, Sikkim, Arunachal Pradesh, Coorg, Ooty, Maharashtra")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Rishikesh,Kullu-Manali,Leh-Ladakh,Uttarakhand,Sikkim,Arunachal Pradesh,Coorg,Ooty,Maharashtra")
    elif(e.get()=="kayaking"):
        engine.say("Rishikesh, Kullu-Manali, Leh-Ladakh, Uttarakhand, Sikkim, Arunachal Pradesh, Coorg, Ooty, Maharashtra")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Rishikesh,Kullu-Manali,Leh-Ladakh,Uttarakhand,Sikkim,Arunachal Pradesh,Coorg,Ooty,Maharashtra")
    elif(e.get()=="skiing"):
        engine.say("Auli, Kufri-Shimla, Solang Valley-Manali, Rohtang Pass, Sikkim, Narkanda-Himachal Pradesh, Gulmarg-Kashmir, Jharkhand, Jammu and Kashmir")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Auli,Kufri-Shimla,Solang Valley-Manali,Rohtang Pass,Sikkim,Narkanda-Himachal Pradesh,Gulmarg-Kashmir,Jharkhand,Jammu and Kashmir")
    elif(e.get()=="thank you"):
        engine.say("Welcome. Have a wonderful holiday")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Welcome.Have a wonderful holiday")
    elif(e.get()=="how are you"):
        engine.say("Welcome. Have a wonderful holiday")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Welcome.Have a wonderful holiday")
    elif(e.get()=="thanks"):
        engine.say("Welcome.Have a wonderful holiday")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Welcome.Have a wonderful holiday")
    elif(e.get()=="flights"):
        webbrowser.open("https://www.cleartrip.com/")
    elif(e.get()=="hotels" or e.get()=="resorts"):
         webbrowser.open("https://www.tripadvisor.in/")
    elif(e.get()=="trains" or e.get()=="train information"):
         webbrowser.open("https://www.makemytrip.com/railways/")
    elif(e.get()=="cuisines" or e.get()=="food"):
         webbrowser.open("https://www.tripadvisor.in/Restaurants")
    elif(e.get()=="fun things" or e.get()=="attractions"):
         webbrowser.open("https://www.tripadvisor.in/Attractions-g293860-Activities-India.html")
    elif(e.get()=="cruises" or e.get()=="cruise ships"):
         webbrowser.open("https://www.tripadvisor.in/Cruises")
    elif(e.get()=="vacation packages" or e.get()=="holiday packages"):
         webbrowser.open("https://www.tripadvisor.in/Vacation_Packages")
    elif(e.get()=="weather" or e.get()=="today’s weather"):
         webbrowser.open("https://www.accuweather.com/")
    elif(e.get()=="emergencies" or e.get()=="hospitals"):
          pywhatkit.search("hospitals near me")
    else:
        engine.say("Sorry, I didn't get you. Kindly check your input")
        engine.runAndWait()
        txt.insert(END,"\n"+"Travelly->Sorry I didn't get you. Kindly check your input")
        
    e.delete(0,END)
    

txt=Text(root,width=90,bg="lightblue")
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=107,bg="lavender")
send=Button(root,text="Send",command=send,bg='blue',fg='white',width="10", height=1)
send.grid(row=1,column=1)
e.grid(row=1,column=0)
scrollbar=Scrollbar(root, command=txt.yview())
scrollbar.place(x=910,y=0,height=480)
root.title("Travelly")
root.mainloop()
