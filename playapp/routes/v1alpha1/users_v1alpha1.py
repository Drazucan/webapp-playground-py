from fastapi import APIRouter

router = APIRouter(prefix='/users',
                   tags=['users'])

@router.get('/')
def getAllUsers():
    """
    Get all the users  in the system. As the system grows, this endpoint may need to return a limited amount of users
    but for now can just return all.
    :return: a JSON response of all the users in the system
    """
    # @TODO: Get user information from the database
    return {"users": [{
        "user-id": "abc123",
        "user-display-name": "BagRaider",
        "user-email": "big.raider@gmail.com",
        "user-phone": "555-222-5027"
    }]}