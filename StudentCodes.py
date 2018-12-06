import re
import PySimpleGUI as sg

# Variable definitions
emails = set()
codes = set()
output = ""
OK = True
semiMail = ""
commaMail = ""


# pySimpleGUI syntax has you enter a layout where it loops through a list of the lists, each one f which has comma seperated objects
# that are displayed in order
layout = [  [sg.Txt('Enter Roster')],      
            [sg.Multiline(size=(100,20), key='emails')], 
            [sg.Txt('Enter Codes')],      
            [sg.Multiline(size=(100,20), key='Codes')],    
         
            [sg.Button('Submit', bind_return_key=True), sg.Button('Cancel', bind_return_key=False)] ]

# Actually launches the window
window = sg.Window('StudentCodes').Layout(layout)

# Main loop, polls for new events in window:
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

        aemails = sorted(emails)
        i=1
        for email in emails:
            code = codes.pop()
            semiMail += email + "; "
            commaMail += email + ", "

            if len(emails) < 100:
                pad = 2
            else:
                pad = 3
            myString = "{0}. {1}           {2}\n".format(str(i).zfill(pad), email, code)
            i += 1
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