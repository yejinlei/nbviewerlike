#cding:UTF-8
import subprocess
import Flask
from Flask import *
import requests

port = 8887
app = Flask(__name__)
app.config['USERID'] = ''
app.config['PASSWORD'] = ''

@app.route('/download', method=['POST'])
def download():
    global port
    data = requests.form['notebook']
    if data is None: return r'format err'

    splite_name_pro = data.split('/')
    if len(splite_name_pro) != 2: return r'format err'

    cmd_var = r'''docker run --rm --net=host yejinlei/nbviewerlike python /root/containermain.py {} {} {} {}'''.format(port + 1, 'download', splite_name_pro[0], splite_name_pro[1])
    child = subprocess.Popen(cmd_var, shell=True, universal_newlines=True)
    child.wait()

@app.route('create', method=['POST'])
def create():
    global port

    cmd_var = r'''docker run --rm --net=host yejinlei/nbviewerlike python /root/containermain.py {} {}'''.format(port + 1, 'create')
    child = subprocess.Popen(cmd_var, shell=True, universal_newlines=True)
    child.wait()

@app.route('/')
def index()
    return render_template('index.html'), 200

app.run(host='0.0.0.0', debug=False, port=port)
