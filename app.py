###integrate HTML with flask



from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'saidmwacharo8@gmail.com'
app.config['MAIL_PASSWORD'] = 'nikupera14'
app.config['MAIL_DEFAULT_SENDER'] = 'saidmwacharo8@gmail.com'

mail = Mail(app)

@app.route('/')
def index():
    return render_template('portfolio.html',)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Validate form inputs
        if not name or not email:
            return 'Please fill in all required fields', 400

        # Send email notification
        send_email_notification(name, email)

        return 'Form submitted successfully!'

def send_email_notification(name, email):
    msg = Message(subject='New Contact Form Submission',
                  recipients=['saidmwacharo8@gmail.com'])
    msg.body = f'Name: {name}\nEmail: {email}'
    mail.send(msg)

if __name__ == '__main__':
    app.run(debug=True)

