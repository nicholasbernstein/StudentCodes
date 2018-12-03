import re
import PySimpleGUI as sg




layout = [  [sg.Txt('Enter Roster')],      
            [sg.Multiline(size=(100,20), key='emails')], 
            [sg.Txt('Enter Codes')],      
            [sg.Multiline(size=(100,20), key='Codes')],    
         
            [sg.Button('Submit', bind_return_key=True), sg.Button('Cancel', bind_return_key=False)] ]

window = sg.Window('Math').Layout(layout)

emails = set()
codes = set()
output = ""
OK = True
semiMail = ""
commaMail = ""

while True:      
    event, values = window.Read()

    if event is not None:      
        
        try:
            ew_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", values['emails'], re.I))
            emails.update(ew_emails) 
        except:
            OK = False
            
        try:
            ew_codes = set(re.findall(r"\d{9}", values['Codes'], re.I))
            codes.update(ew_codes) 
        except:
            OK = False

    
        for email in emails:
            code = codes.pop()
            semiMail += email + "; "
            commaMail += email + ", "
           # print(email, code)
            myString = (email + ":\t\t" + code + "\n")
            #output.append(myString)
            output += myString
    if OK is True: 
        commaMail.rstrip()
        semiMail.rstrip()
        layout2 = [ [sg.Txt('Emails & Codes')],
                    [ sg.Multiline(output, size=(100,20), autoscroll=True)],
                    [sg.Txt('Emails & Codes')],
                    [ sg.Multiline(commaMail.rstrip(","), size=(100,2), autoscroll=True)],
                    [sg.Txt('Emails & Codes')],
                    [ sg.Multiline(semiMail.rstrip(";"), size=(100,2), autoscroll=True)],
                    [sg.Button('OK', bind_return_key=True)]]
        window = sg.Window("Output").Layout(layout2)
        window.Read()
    else:
        window = sg.PopupError("Invalid input").Layout

    if event == 'Cancel'  or event is None:      
        break 

    else:      
        break