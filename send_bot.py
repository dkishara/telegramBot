import requests
def telegram_bot_sendtext(message, User_chatID, bot_token):
    send_ = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + User_chatID + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_)
    return response.json()    
bot_token = 'add bot token here'
User_chatID = 'add user chat id here'
message_text = 'This is the message ...'
response = telegram_bot_sendtext(message_text,User_chatID,bot_token)
print(response)