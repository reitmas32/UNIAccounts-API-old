# External Packages
from flask import Blueprint, request

from tools.functions_authentication import valid_credentials

from ..views.users import signup_route_POST

views_users = Blueprint("users", __name__)


@views_users.route("/api/v1/signup", methods=["POST"])
def signup():
    """SignUp EndPoint

    Returns:
        dict: JSON response
        int: status code of the request
    """

    response_credentials = valid_credentials(request)

    if not response_credentials.get("Success"):
        return response_credentials

    if request.method == "POST":
        response = signup_route_POST(parameters_json=request.get_json())
        return response


# @views_users.route('/api/v1/signin', methods=['PUT', 'GET'])
# def signin():
#     """SignIn EndPoint

#     Returns:
#         dict: JSON response
#         int: status code of the request
#     """
#     response_credentials = valid_credentials(request, f'signin_route_{request.method}')
#     service_name = response_credentials.get('service_name')

#     if response_credentials.get('status') == False:
#         return response_credentials, response_credentials.get('status_code')

#     if not request.is_json and request.method != 'GET':
#         return {'message': 'No content Type'}, 401

#     if request.method == 'PUT':
#         response = signin_route_PUT(request.json, data_base_service, service_name)
#         status_code = response.get('status_code')

#     if request.method == 'GET':
#         response = signin_route_GET(request.headers['Authorization'].split(" ")[1], data_base_service, service_name)
#         status_code = response.get('status_code')

#     return response, status_code

# @views_users.route('/api/v1/signout', methods=['PUT'])
# def signout():
#     """SignOut EndPoint

#     Returns:
#         dict: JSON response
#         int: status code of the request
#     """
#     response_credentials = valid_credentials(request, f'signout_route_{request.method}')
#     service_name = response_credentials.get('service_name')

#     if response_credentials.get('status') == False:
#         return response_credentials, response_credentials.get('status_code')

#     if request.method == 'PUT':
#         response = signout_route_PUT(request.headers['Authorization'].split(" ")[1], data_base_service, service_name)
#         status_code = response.get('status_code')

#     return response, status_code

# @views_users.route('/signup', methods=['GET', 'POST'])
# def signup_users():
#     """SignUp Form

#     Returns:
#         str: Form by SignUp
#         -------------------
#         dict: JSON response
#     """
#     if request.method == 'POST':
#         # Obtener los datos del formulario de registro
#         nick_name  = request.form['nick_name']
#         password  = request.form['password']
#         email  = request.form['email']
#         name   = request.form['name']
#         last_name_fathers   = request.form['last_name_fathers']
#         last_name_mothers  = request.form['last_name_mothers']
#         account_number  = request.form['account_number']
#         careers  = request.form['careers']
#         role   = request.form['role']
#         role_key  = request.form['role_key']
#         half_year = request.form['half_year']

#         query = {
#             'nick_name'         : nick_name,
#             'password'          : password,
#             'email'             : email,
#             'name'              : name,
#             'last_name_fathers' : last_name_fathers,
#             'last_name_mothers' : last_name_mothers,
#             'account_number'    : account_number,
#             'careers'           : careers,
#             'half_year'         : half_year,
#             'role'              : role,
#             'role_key'          : role_key,
#         }

#         response = requests.post('http://127.0.0.1:4000/api/v1/signup',json=query, headers={'API_KEY': CONFIG.API_KEYS.get('UNICA_MANAGER_ACCOUNTS_API')} )

#         # Retornar la respuesta adecuada
#         return response.text
#     else:
#         # Mostrar el formulario de registro
#         return render_template('signup.html')
