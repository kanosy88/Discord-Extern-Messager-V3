import requests
import PySimpleGUI as sg
import pickle as storage

Token = ('')
channel = []
victim = {}

def sendMessage(message):
    
    if values['channels'] in str(list(victim)):
        i = victim[values['channels']]

    payload = {
        'content': (message)
    }

    header = {
        'authorization': Token
    }

    r = requests.post(i, data=payload, headers=header)
    
    return r

def addNewChannel(victime, channelURL):
    channel.append(victime)
    victim[victime] = channelURL
    
def saveData():
    storage.dump(channel, open('channelSave.s', "wb"))
    storage.dump(victim, open('victimeSave.s', "wb"))

def loadData(choisirUneData):
    channelDat = storage.load(open('channelSave.s', "rb"))
    victimeDat = storage.load(open('victimeSave.s', "rb"))

    if choisirUneData == 'channel':
        return channelDat
    elif choisirUneData == 'victime':
        return victimeDat

sg.theme('DarkAmber')   

layout = [  [sg.Text('Discord Messager')],
            [sg.Text('Your Token'), sg.InputText(),sg.Button('Save Token')],
            [sg.Text('Message as send'), sg.InputText()],
            [sg.Text('The channel'), sg.Combo(values=channel, key='channels')],
            [sg.Button('Ok'), sg.Button('Cancel')],
            [sg.Text('Username'), sg.InputText()],
            [sg.Text('Url of channel'), sg.InputText()],
            [sg.Button('Save'), sg.Button('Load')]
         ]


window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': 
        break
    if event in (sg.Button, 'Ok'):
        sendMessage(values[1])
    else:
        continue
    if event in (sg.Button, 'Save'):
        print('save')
        addNewChannel(values[2], values[3])
        saveData()
    if event in (sg.Button, 'Load'):
        print('load')
        channel = loadData('channel')
        victim = loadData('victime')
        window.Element('channels').Update(values=channel)
    if event in (sg.Button, 'Save Token'):
        Token = values[0]

window.close()
