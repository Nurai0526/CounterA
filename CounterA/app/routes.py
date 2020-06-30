from app import app
from flask import render_template, url_for
from app.forms import Upload
from config import Config
from werkzeug.utils import secure_filename
import os
from myLib1 import count_letters_RU, detect_encoding
from chardet.universaldetector import UniversalDetector
import plotly as py
import plotly.graph_objects as go

@app.route('/')
@app.route('/index')
def index():
    data ='Welcome username'
    dictionary= {'Россия':'Москва','Казахстан':'Астана','Италия':'Рим'}
    return render_template('index.html', dictionary = dictionary, title = data)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = Upload()
    if form.validate_on_submit():
        f = form.file.data
        data = {}
        data['name'] = form.name.data
        data['surname'] = form.surname.data
        data['email'] = form.email.data
        filename = secure_filename(f.filename)
        files_dir = os.path.join(os.getcwd(),'files')
        html_dir = os.path.join(files_fir, filename)
        filename = os.path.join(files_dir, filename)
        if not os.path.exists(files_dir):
            os.mkdir(files_dir)
        if not os.path.exists(html_dir):
            os.mkdir(html_dir)
        
        f.save(filename)
        f=open(filename,'r',encoding=detect_encoding(filename)['encoding'])
        text=f.read()
        f.close()
        result=count_letters_RU(text) 
        fig = go.Figure([go.Bar(x=list(result.keys()), y=list(result.values()))])
        py.offline.plot(fig,filename=os.path.join(html_dir,filename+'_'+'counter.html'),auto_open=True)
        #title = form.title
        return render_template('result.html', data=data)

    return render_template('upload.html', form=form)
