import os
from flask import Flask, render_template, flash
import flashcard_web
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired

app = Flask(__name__)
app.secret_key = 'n23f0arstbw4j'

class FileForm(FlaskForm):
    file_field = FileField(validators=[FileRequired()])
    

def valid_extension(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'txt'

@app.route('/', methods=['GET', 'POST'])
def upload():
    form = FileForm()
    result_str = ''
    if form.validate_on_submit():
        f = form.file_field.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(filename))
        if valid_extension(filename):
            result_str = flashcard_web.main(filename)
        else:
            flash('You must upload a .txt file.')
        
    return render_template('flashcard-view.html', template_form=form, result = result_str)



@app.route('/instructions.html', methods=['GET', 'POST'])
def instructions():
    
    return render_template('instructions.html')



@app.route('/about-contact.html', methods=['GET', 'POST'])
def about():
    
    return render_template('about-contact.html')

if __name__ == '__main__':
    app.run(debug = True)