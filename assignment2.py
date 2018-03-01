from flask import Flask, jsonify, request, json
app = Flask(__name__)

players = [{'codeName' : 'BloodySweet', 'rank' : 'Platinum I'}, {'codeName' : 'jinjavu', 'rank': 'Gold III'}, {'codeName' : 'babySwarm', 'rank':'Platinum II'}]

@app.route('/',methods =['GET'])
def test():
	return jsonify({'message' : 'Success! Please use the python shell or postman for commands. For python shell you can return the json by typing <var_name in request>.json(). \n Commands: for get is requests.get("http://127.0.0.1:5000/rosplayer") or when specifying a player requests.get("http://127.0.0.1:5000/rosplayer=<codeName>"). For post is requests.post("http://127.0.0.1:5000/rosplayer", json = {"<attributes>"}). Put is requests.put("http://127.0.0.1:5000/rosplayer=<codeName of player to update>", json = {"<attributes>"}) and finally delete is requests.delete("http://127.0.0.1:5000/rosplayer=<codeName of player to delete>")'})

@app.route('/rosplayer', methods=['GET'])
def playerAll():
	return jsonify({'players' : players})

@app.route('/rosplayer=<string:codeName>', methods=['GET'])
def player(codeName):
	play = [player for player in players if player['codeName']==codeName]

	return jsonify({'player' : play[0]})

@app.route('/rosplayer',methods= ['POST'])
def addPlayer():
	play = {'codeName' : request.json['codeName'], 'rank': request.json['rank']}
	players.append(play)
	return jsonify({'players' : players})

@app.route('/rosplayer=<string:codeName>', methods = ['PUT'])
def changeInfo(codeName):
	play = [player for player in players if player['codeName'] == codeName]
	play[0]['codeName'] = request.json['codeName']
	play[0]['rank'] = request.json['rank']
	return jsonify({'players' : play[0]})

@app.route('/rosplayer=<string:codeName>', methods = ['DELETE'])
def removeOne(codeName):
	play = [player for player in players if player['codeName'] == codeName]
	players.remove(play[0])
	return jsonify({'players' : players})

if __name__ == '__main__':
	app.run(debug = True)
