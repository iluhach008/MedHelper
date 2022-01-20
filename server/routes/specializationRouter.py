from flask import jsonify
from . import routes
from service import specializationService
from flask_cors import cross_origin


@routes.route('/specialization', methods=['GET'])
@cross_origin()
def get_specialization():
    return jsonify(specializationService.getAll())