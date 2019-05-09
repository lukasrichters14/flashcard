from flask import Flask, render_template, request, flash
from FlashcardProgramV2 import *  # This just a placeholder. Need a web-compatible version to import.
from wtforms import Form, FileField, validators
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'n23f0arstbw4j'

class InputForm(Form):
    text_field = TextField([validators.InputRequired()])

@app.route('/', methods=['GET', 'POST'])
def index():
    result_str = None
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        pass
        


if __name__ == '__main__':
    app.run(debug = True)