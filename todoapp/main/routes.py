from flask import Blueprint , render_template ,redirect , url_for , request
# from gevent.pywsgi import WSGIServer

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('./index.html')

#from waitress import serve
#serve(main, host="0.0.0.0", port=8080)
# http_server = WSGIServer(("127.0.0.1", 8080), main)
# http_server.serve_forever()

@main.route('/add_todo' , methods=["POST"])
def add_todo():
    return redirect(url_for("main.index"))