import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

import json 

API_TOKEN = '530315801:AAEwhkd6z1c2s7CCSo6w3g2fJUFzLIcbdtw'
WEBHOOK_URL = 'https://4b2913c0.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state4',
        'state5',
        'state6',
        'state7',
        'state8',
        'state9',
        'state10',
        'state11',
        'state12',
        'state13',
        'state14',
        'state15',
        'state16',
        'state17',
        'state18',
        'state19',
        'state20',
        'state21',
        'state22',
        'state23'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state4',
            'conditions': 'is_going_to_state4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state7',
            'conditions': 'is_going_to_state7'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state8',
            'conditions': 'is_going_to_state8'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state9',
            'conditions': 'is_going_to_state9'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state10',
            'conditions': 'is_going_to_state10'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state11',
            'conditions': 'is_going_to_state11'
        },
        {
            'trigger': 'advance',
            'source': 'state1',
            'dest': 'state12',
            'conditions': 'is_going_to_state12'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state13',
            'conditions': 'is_going_to_state13'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state14',
            'conditions': 'is_going_to_state14'
        },
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state15',
            'conditions': 'is_going_to_state15'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state16',
            'conditions': 'is_going_to_state16'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state17',
            'conditions': 'is_going_to_state17'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state18',
            'conditions': 'is_going_to_state18'
        },
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state19',
            'conditions': 'is_going_to_state19'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state20',
            'conditions': 'is_going_to_state20'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state21',
            'conditions': 'is_going_to_state21'
        },
        {
            'trigger': 'advance',
            'source': 'state4',
            'dest': 'state22',
            'conditions': 'is_going_to_state22'
        },  
        {
            'trigger': 'advance',
            'source': 'state6',
            'dest': 'state23',
            'conditions': 'is_going_to_state23'
        }, 
        {
            'trigger': 'go_back_tomenu',
            'source': [
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state6',
                'state7',
                'state8',
                'state9',
                'state10',
                'state11',
                'state12',
                'state13',
                'state14',
                'state15',
                'state16',
                'state17',
                'state18',
                'state19',
                'state20',
                'state21',
                'state22',
                'state23'
            ],
            'dest': 'user'
        },
		{
            'trigger': 'go_back_toN',
            'source': [
                'state8',
                'state9',
                'state10',
                'state11',
                'state12'
            ],
            'dest': 'state1'
		},
		{
            'trigger': 'go_back_toW',
            'source': [
                'state13',
                'state14',
                'state15'
            ],
            'dest': 'state2'
		},
		{
            'trigger': 'go_back_toS',
            'source': [
                'state16',
                'state17',
                'state18',
                'state19'
            ],
            'dest': 'state3'
		},
		{
            'trigger': 'go_back_toE',
            'source': [
                'state20',
                'state21',
                'state22',
            ],
            'dest': 'state4'
		},
        {
            'trigger': 'go_to_favorite',
            'source': [
                'user',
                'state1',
                'state2',
                'state3',
                'state4',
                'state5',
                'state7',
                'state8',
                'state9',
                'state10',
                'state11',
                'state12',
                'state13',
                'state14',
                'state15',
                'state16',
                'state17',
                'state18',
                'state19',
                'state20',
                'state21',
                'state22'
            ],
            'dest': 'state6'

        }

    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))
    
favorite=[]    
@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True),bot)
    message = update.message
    if '/start' in message.text :
        update.message.reply_text("輸入: \n/北部\n/中部\n/南部\n/東部\n/外島 ->搜尋各地區飯店\n輸入: /我的最愛 ->查看收藏\n輸入: /推薦 ->觀看推薦行程!\n輸入: /menu 回到目錄")       

    elif '/menu' in message.text:
        machine.go_back_tomenu(update)
        update.message.reply_text("輸入: \n/北部\n/中部\n/南部\n/東部\n/外島 ->搜尋各地區飯店\n輸入: /我的最愛 ->查看收藏\n輸入: /推薦 ->觀看推薦行程!\n輸入: /menu 回到目錄")  

    elif '/back' in message.text:
        if machine.state=="state8" or machine.state=="state9" or machine.state=="state10" or machine.state=="state11" or machine.state=="state12":
            machine.go_back_toN(update)
        if machine.state=="state13" or machine.state=="state14" or machine.state=="state15":
            machine.go_back_toW(update)
        if machine.state=="state16" or machine.state=="state17" or machine.state=="state18" or machine.state=="state19":
            machine.go_back_toS(update)
        if machine.state=="state20" or machine.state=="state21" or machine.state=="state22":
            machine.go_back_toE(update)
    
    elif '/add' in message.text:
        save_text=message.text
        savedata(favorite,save_text,update)
        update.message.reply_text("輸入: /我的最愛 查看收藏\n 輸入: /menu 回到目錄")

    elif '/我的最愛' in message.text:
        showdata(favorite)
        update.message.reply_text("輸入: /menu 回到目錄")

    else:
        machine.advance(update)

    return 'ok'

@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')

def savedata(favorite,save_text,update):
    favorite.append(save_text[5:]) 
    return

def showdata(favorite):
    for data in favorite:
        update.message.reply_text(data)
    return

if __name__ == "__main__":
    _set_webhook()
    app.run()
