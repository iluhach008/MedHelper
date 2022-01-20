from flask import jsonify
from . import routes
from service import levelService
from flask_cors import cross_origin


@routes.route('/level', methods=['GET'])
@cross_origin()
def get_levels():
    return jsonify(levelService.getAll())