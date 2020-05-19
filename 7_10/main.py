import os
from flask import Flask, request, render_template, send_from_directory
from wtforms import Form, validators, StringField, TextAreaField, SubmitField

from flake8.api import legacy as flake8

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


class Flake8Form(Form):
    text_str = TextAreaField('Python Text', validators=[validators.required()])
    submit_btn = SubmitField('Flake8')


source_dir='tmp'
source_file='tmp.py'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')


@app.route('/', methods=['GET', 'POST'])
def action_index():
    form = Flake8Form(request.form)
    result = None
    if form.submit_btn.data:
        if form.validate():
            if not os.path.isdir(os.path.join(app.root_path, source_dir)):
                os.mkdir(os.path.join(app.root_path, source_dir))
            f_name = os.path.join(app.root_path, source_dir, source_file)
            f = open(f_name, 'w')
            f.write(form.text_str.data)
            f.close()
            #http://flake8.pycqa.org/en/latest/user/python-api.html
            style_guide = flake8.get_style_guide()
            check_report = style_guide.check_files([f_name])
            result = check_report.get_statistics("")
            os.remove(f_name)

    return render_template('test.html', form=form, result=result)

if __name__ == '__main__':
    app.run(debug=True)
