from flask import Flask, render_template, redirect, request, flash
from cycle import Cycle, Notice
from datetime import datetime
from waitress import serve
import re
import base64
app = Flask(__name__)


notices_fname = "notices"

cycles = ['upstairs_bathroom',
          'downstairs_bathroom',
          'kitchen'
          ]



@app.route('/')
def dashboard(name=None):
    cycle_insts = [Cycle.load(c) for c in cycles]
    notices = Notice.load_list(notices_fname)[::-1]
    today = datetime.today().weekday()
    chef = Cycle.load('cooking_schedule')[today]
    return render_template('dashboard.html', cycles=cycle_insts, notices=notices, chef=chef)


@app.route('/update_cycle/<iden>', methods=['POST'])
def update_cycle(iden):
    c = Cycle.load(iden)
    c.advance()
    c.save()
    return redirect('/')
    #return 'Success!'

@app.route('/add_notice', methods=['POST'])
def add_notice():
    body = request.form.get('body')
    author = request.form.get('author')
    n = Notice(body, author, ip=request.remote_addr)
    print(body)
    print(author)
    print(n.ip)
    print("-----")
    notices = Notice.load_list(notices_fname)
    notices.append(n)
    Notice.save_list(notices, notices_fname)
    return redirect('/')

@app.route('/delete_notice/<iden>', methods=['POST'])
def delete_notice(iden):
    notices = Notice.load_list(notices_fname)
    for n in notices:
        if str(n.identifier) == iden:
            notices.remove(n)
            Notice.save_list(notices, notices_fname)
    return "Deleted :)"

@app.route('/upload_whiteboard', methods=['POST'])
def upload_whiteboard():
    imgdata = request.form.get('imgBase64')
    image_data = re.sub('^data:image/.+;base64,', '', imgdata)
    print(image_data)
    with open("static/img/whiteboard.png", "wb") as fh:
        fh.write(base64.b64decode(image_data))
    return "Not working"


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(Exception)
def all_exception_handler(error):
   return render_template('500.html'), 500 

if __name__=="__main__":
    serve(app, host='0.0.0.0', port=5000)
