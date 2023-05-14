# # Local Packages
# from services.db.idata_base import IDataBase
# from models.user import User
# from services.db.users import UserService
# from schemas import UserSchema
# from pydantic import ValidationError


# def signup_route_POST(parameters_json: dict):
#     """EndPoint /signup with method HTTP POST, Create new User in DataBase

#     Args:
#         parameters_json (dict): User data
#     Returns:
#         dict: response of the operation in the DataBase
#     """
#     try:
#         user = UserSchema(**parameters_json)
#     except ValidationError as e:
#         errors = []
#         for error in e.errors():
#             errors.append({
#                 'field': error['loc'][0],
#                 'message': error['msg']
#             })
#         response = {
#             'errors': errors
#         }
#         status_code = 400
#         return response,status_code

#     user_service = UserService()
#     try:
#         user_service.create_user(user_data=user)
#         status_code = 200
#         response={
#             'message': 'Succesfull signUp'
#             }
#     except Exception as e:
#         status_code = 400
#         response={
#             'errors': str(e)
#         }
#     return response,status_code
