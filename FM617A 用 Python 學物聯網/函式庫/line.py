import urequests
import json

api_url = 'https://api.line.me/v2/bot/message/push'

headers = {
    'Content-type': 'application/json',
    'Authorization': ''
}

data = {"to": '', "messages":[]}

def line_token(token):
    headers['Authorization'] = 'Bearer ' + token
    
def line_notify(to, t=None, pid=None, sid=None, img=None):
    data['to'] = to
    
    if t:
        data['messages'].append({
            'type': 'text',
            'text': t})

    if pid and sid:
        data['messages'].append({
            'type': 'sticker',
            "packageId": pid,
            "stickerId": sid})
    
    if img:
        data['messages'].append({
            "type": "image",
            "originalContentUrl": img,
            "previewImageUrl": img})
    
    if not data['messages']:
        return 400
    
    res = urequests.post(
        api_url,
        headers=headers,
        data=json.dumps(data).encode('utf8')
    )
    status_code = res.status_code
    res.close()
    return status_code