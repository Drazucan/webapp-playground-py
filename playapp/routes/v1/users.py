from fastapi import APIRouter
from fastapi.params import Depends

from playapp import PlayAppLogger
from playapp.services.dbservice import PostgresClient, PostgresClientProvider
from playapp.datamodels.v1.users import PlayAppUser

users_v1 = APIRouter(prefix='/users',
                   tags=['users'])

logger = PlayAppLogger()
@users_v1.get('/')
def get_all_users(db_client: PostgresClient = Depends(PostgresClientProvider.get_client)):

    logger.info("A request was made to get all users")
    users = db_client.get_session().query(PlayAppUser).all()
    return users
    # """
    # Get all the users  in the system. As the system grows, this endpoint may need to return a limited amount of users
    # but for now can just return all.
    # :return: a JSON response of all the users in the system
    # """
    # # @TODO: Get user information from the database
    # return {"users": [{
    #     "user-id": "abc123",
    #     "user-display-name": "BagRaider",
    #     "user-email": "big.raider@gmail.com",
    #     "user-phone": "555-222-5027"
    # }]}