from flask import Blueprint , render_template ,redirect , url_for , request
from todoapp.extentions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('./index.html')

#from waitress import serves
#serve(main, host="0.0.0.0", port=8080)
# http_server = WSGIServer(("127.0.0.1", 8080), main)
# http_server.serve_forever()

@main.route('/add_todo' , methods=["POST"])
def add_todo():
    todo_collection = mongo.db.todos
    todo_item = request.form.get('add-todo')
    todo_collection.insert_one({'text':todo_item, 'complete': False})
    print(todo_item)
    return redirect(url_for("main.index"))