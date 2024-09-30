from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, send, emit
from openai_query import get_response
from db import insertQuery

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Route to serve the HTML page
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# Route to serve the HTML page
@app.route('/about')
def about():
    return render_template('about.html')

# Route to serve the HTML page
@app.route('/education')
def education():
    return render_template('education.html')

# Route to serve the HTML page
@app.route('/research')
def research():
    return render_template('research.html')

# Route to serve the HTML page
@app.route('/work')
def work():
    return render_template('work.html')

# Route to serve the HTML page
@app.route('/publications')
def publications():
    return render_template('publications.html')

# Route to serve the HTML page
@app.route('/awards')
def awards():
    return render_template('awards.html')

# Route to serve the HTML page
@app.route('/mentoring')
def mentoring():
    return render_template('mentoring.html')

# Route to serve the HTML page
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# Route to serve the HTML page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print('Received:', name, email, message)
        insertQuery(name, email, message)        
        # Process the form data (e.g., save to database, send an email, etc.)
        flash(f"Thank you {name}, your message has been received!", 'success')
        
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Route to serve the HTML page
@app.route('/chat')
def chat():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Received message: {msg}')
    # Get response from OpenAI
    response = get_response(msg)
    # Emit the response back to the client who sent the message
    emit('response', response)

if __name__ == '__main__':
    socketio.run(app, debug=True)
