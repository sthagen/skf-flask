from flask import request
from flask_restplus import Resource
from skf.api.security import security_headers, val_alpha_num_special
from skf.api.labs.business import get_labs_code
from skf.api.labs.serializers import lab_items_code, message
from skf.api.restplus import api

ns = api.namespace('interactive_labs', description='Operations related to the labs')

@ns.route('/code/items/type/<string:code_type>')
@api.doc(params={'code_type': 'The code type items based on name for example: php, asp, java'})
@api.response(404, 'Validation error', message)
class LabCollectionCode(Resource):
    @api.marshal_with(lab_items_code)
    @api.response(400, 'No results found', message)
    def get(self, code_type):
        """
        Returns list of code review labs.
        * Privileges required: **none**
        """
        val_alpha_num_special(code_type)
        result = get_labs_code(code_type)
        return result, 200, security_headers()
 