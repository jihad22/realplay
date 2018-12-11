from flask import jsonify, request, url_for
from app import db
from app.models import Player
from app.player import bp



@bp.route('/register', methods = ['POST'])
def create_player():
    data = request.get_json()
    add_user = Player(
        nama        = data['nama'],
        jk          = data['jk'],
        tgllahir    = data['tgllahir'],
        email       = data['email'],
        latitude    = data['latitude'],
        longitude   = data['longitude'],
        username    = data['username']
        )
    add_user.hash_password(data['password'])
    
    db.session.add(add_user)
    db.session.commit()

    return jsonify({'message':'Congratulation You Has Been Registered, Check Your Email'})

@bp.route('/all', methods = ['GET'])
def show_all_player():
    player = Player.query.all()
    pl = []
    for p in player:
        player_data = {}
        player_data['id_user']  = p.id_user
        player_data['nama']     = p.nama
        player_data['jk']       = p.jk 
        player_data['tgllahir'] = p.tgllahir
        player_data['email']    = p.email
        player_data['latitude'] = p.latitude
        player_data['longitude']= p.longitude
        player_data['username'] = p.username
        player_data['password'] = p.password
        pl.append(player_data)

    return jsonify({'player':pl})

@bp.route('/person/<int:id_user>', methods = ['GET'])
def my_profile(id_user):

    player = Player.query.filter_by(id_user = id_user).first()

    if not player:
        return jsonify({'message':'No User Found'})
    
    player_data = {}
    player_data['id_user']  = player.id_user
    player_data['nama']     = player.nama
    player_data['jk']       = player.jk 
    player_data['tgllahir'] = player.tgllahir
    player_data['email']    = player.email
    player_data['latitude'] = player.latitude
    player_data['longitude']= player.longitude
    player_data['username'] = player.username
    player_data['password'] = player.password
    
    return jsonify({'player':player_data})

@bp.route('/update/<int:id_user>', methods = ['PUT'])
def edit_player(id_user):

    plyrs = Player.query.filter_by(id_user = id_user).first()

    if plyrs is None:
        return jsonify({'message':'Player Not Found' })

    data = request.get_json()

    player = Player.query.filter_by(id_user = id_user).update(
        dict(
            nama        = data['nama'],
            jk          = data['jk'],
            tgllahir    = data['tgllahir'],
            email       = data['email'],
            latitude    = data['latitude'],
            longitude   = data['longitude'],
        )
    )
    db.session.commit()
    return jsonify({'message':'Your Profile Has Been Update'})

@bp.route('/delete/<int:id_user>', methods = ['DELETE'])
def delete_player(id_user):

    player = Player.query.filter_by(id_user = id_user).first()

    if player is None:
        return jsonify({'message':'Player Not Found'})
    
    db.session.delete(player)
    db.session.commit()
    return jsonify({'message':'You Has Been Deleted'})
    
    
