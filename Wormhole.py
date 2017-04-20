from flask import Flask
from flask import request
import requests

app = Flask(__name__)

DINGTALK_HOST = 'https://oapi.dingtalk.com/robot/send'
SENTRY_IMAGE = 'http://7xjlg5.com1.z0.glb.clouddn.com/sentry.png'


@app.route('/robot/send', methods=['GET', 'POST'])
def sentry_msg():
    access_token = request.args.get('access_token')
    msg = request.get_json(silent=True)
    print(msg)
    dingtalk_data = {
        'msgtype': 'link',
        'link': {
            'text': msg['message'] + '\n' + msg['culprit'],
            'title': msg['project_name'],
            'picUrl': SENTRY_IMAGE,
            'messageUrl': msg['url']
        }
    }
    if msg['tags']['url'] is not None:
        requests.post('%s?access_token=%s' % (DINGTALK_HOST, access_token),
                      json=dingtalk_data)
    return 'Success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
