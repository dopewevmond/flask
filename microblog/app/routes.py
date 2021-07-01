from app import app

@app.route('/')
@app.route('/index5')
def index():
    return "Hello world"