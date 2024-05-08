from flask import Flask, Response, jsonify, request
import xml.etree.ElementTree as Et

app = Flask(__name__)

players = [
    {
        'id':1,
        'name':'Player 1',
        'score':100,
    }, 
    {
        'id':2,
        'name':'Player 2',
        'score':200
    }
]

@app.route('/player', methods=['GET'])
def get_all_players():
    root = Et.Element('players')
    for player in players:
        xml_player = Et.SubElement(root, 'player')
        xml_player.set('id', str(player['id']))
        name = Et.SubElement(xml_player, 'name')
        name.text = player['name']
        score = Et.SubElement(xml_player, 'score')
        score.text = str(player['score'])
    xml_string = Et.tostring(root, encoding='utf-8')
    return Response(xml_string, mimetype="text/xml")

@app.route('/player/<int:player_id>', methods=['GET'])
def get_one_player(player_id):
    player = next((p for p in players if p['id']==player_id))
    if player:
        return jsonify(player)
    else:
        return jsonify({"Message": "Player not Found"},404)   

@app.route('/player/add', methods=['POST'])
def add_a_player():
    new_player = {
        'id':len(players)+1,
        'name': request.json['name'],
        'score': request.json['score'],
    }
    players.append(new_player)
    print(players)
    return jsonify(new_player)

@app.route("/player/edit/<int:player_id>",methods=["PUT"])
def update_player(player_id):
    request_data = request.get_json()
    player = next((p for p in players if p['id']==player_id))
    if player:
        player.update(request_data)
        return jsonify(player)
    else:
        return jsonify({"Message":"No Player Found"}), 404

@app.route("/player/remove/<int:player_id>", methods=["DELETE"])
def remove_player(player_id):
    player = next((pi for pi in players if pi['id'] == player_id))
    if player is None:
        return jsonify({"error":"Player Not Found!"})
    players.remove(player)
    print(players)
    return jsonify({"message":"Successfully removed the player."})

if __name__ == "__main__":
    app.run(debug= True, port=4430)