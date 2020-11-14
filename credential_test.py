import unittest
from credential import Credential

class TestCredential(unittest.TestCase):

    """ 
    Test class that defines test cases for the credential class behaviours
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """

        self.new_credential = Credential("Hotmail","zilfeur","kigali123!")

    def test_init(self):

        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.account,"Hotmail")
        self.assertEqual(self.new_credential.username,"zilfeur")
        self.assertEqual(self.new_credential.password,"kigali123!")

    def test_save_credential(self):
        """
          Test case to test if the contact object is saved into
         the credential list
         """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)


if __name__ == '__main__':
    unittest.main()