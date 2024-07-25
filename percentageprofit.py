from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your own secret key

PORT = 9001  # Define the port number as a constant

@app.route('/', methods=['GET', 'POST'])
def home():
    target_margin = session.get('target_margin', 30)
    return render_template('index.html', target_margin=target_margin)

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        target_margin = float(request.form['target_margin'])
        session['target_margin'] = target_margin
        return render_template('settings.html', target_margin=target_margin)
    target_margin = session.get('target_margin', 30)
    return render_template('settings.html', target_margin=target_margin)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
