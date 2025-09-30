from flask import Flask,jsonify,request

app=Flask(__name__)

items = {
    1:{"title": "Finish Flask assignment", "status": "pending", "priority": "high"},
    2:{"title": "Read SQL notes", "status": "completed", "priority": "medium"},
    3:{"title": "Practice Python logging", "status": "pending", "priority": "high"},
    4:{"title": "Workout for 30 mins", "status": "pending", "priority": "low"},
    5:{"title": "Review data science project", "status": "in progress", "priority": "high"}
}

@app.route('/')
def home():
    return "Welcome to home page"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# get Retrive a specific item by id

@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    try:
        result=items[item_id]
    except KeyError:
        result="Invalid item id"
    return jsonify(result)

## post

@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'title' in request.json or not 'priority' in request.json or not 'status' in request.json:
        return jsonify({"error":"items not found"})
    
    key=list(items.keys())[-1]
    items[key+1]=request.json
    return jsonify(request.json)

#put
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    try:
        result=items[item_id]
        items[item_id]=request.json
        return jsonify(request.json)
    except KeyError:
        return jsonify({"error":"Item not found"})

#delete

@app.route('/items/<int:item_id>',methods=['DELETE'])
def delete_items(item_id):
    global items
    if item_id in items.keys():
        del items[item_id]
        return jsonify({'Deleted Successfully key':item_id})
    else:
        return jsonify({'Not Found Key':item_id})

if __name__=="__main__":
    app.run(debug=True)