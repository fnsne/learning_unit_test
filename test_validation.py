import unittest
from validation import Validation, AccountDao, Hash

class ValidationTestCase(unittest.TestCase):
    def setUp(self):
        dao = AccountDao
        hasher = Hash
        dao.get_password = lambda self,user_id: "1111"
        hasher.get_hash_result = lambda self, password: "1111"

        self.to_test = Validation(dao, hasher)
    def test_validation(self):
        expected = True
        actual = self.to_test.check_authentication("aaaa", "123123")
        self.assertEqual(expected, actual)
    
if __name__ == "__main__":
    unittest.main(verbosity=2)