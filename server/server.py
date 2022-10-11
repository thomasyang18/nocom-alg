from flask import Flask, request, jsonify
from typing import List
from Agent import Agent

AgentList: List[Agent]

AgentList = []
app = Flask(__name__)

@app.route("/query_chunk", methods=['GET'])
def query_chunk():
    args = request.args 
    if not ('x' in args and 'y' in args):
        return "Please query with an x and y coordinate", 400

    works = any(max(abs(int(args['x']) - o.x), abs(int(args['y']) - o.y)) <= 2 for o in AgentList)

    return jsonify({'loaded': works})

@app.route("/actual_location", methods=['GET'])
def actual_location():
    dict = {}
    for agent in AgentList:
        dict[agent.name] = (agent.x, agent.y)
    return jsonify(dict)

if __name__ == "__main__":
    app.run()