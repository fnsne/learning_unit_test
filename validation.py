class Validation:
    def __init__(self, accountDao, hasher):
        self.dao = accountDao
        self.hash = hasher

    def check_authentication(self, user_id, password):
        dao = AccountDao()
        password_from_dao = dao.get_password(user_id)

        hasher = Hash()
        hash_result = hasher.get_hash_result(password)


        return hash_result == password_from_dao

class AccountDao:
    def get_password(self, user_id):
        raise NotImplementedError

class Hash:
    def get_hash_result(self, password):
        raise NotImplementedError
        