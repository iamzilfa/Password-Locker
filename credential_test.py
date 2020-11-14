#!/usr/bin/env python3.6
import pyperclip
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

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
        
    def test_save_multiple_credential(self): 
        
            '''
            test_save_multiple_contact to check if we can save multiple credential
            objects to our credential_list
            '''

            self.new_credential.save_credential()
            test_credential = Credential("Gmail","zilcyam","a1b2c3d4")
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            """
            test_delete_credential to test if we can remove an account credentials from our credential list
            """
            self.new_credential.save_credential()
            test_credential = Credential("Gmail","zilcyam","a1b2c3d4")
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1)


    def test_find_credential_by_username(self):
        '''
        test to check if we can find an account by username and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Gmail","zilcyam","a1b2c3d4")
        test_credential.save_credential()

        found_credential = Credential.find_by_username("zilcyam")
        self.assertEqual(found_credential.password,test_credential.password)

    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Gmail","zilcyam","a1b2c3d4")
        test_credential.save_credential()

        credentail_exists = Credential.credential_exist("zilcyam")
        self.assertTrue(credentail_exists)

    def test_display_all_credential(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credential.display_credential(),Credential.credential_list)














if __name__ == '__main__':
    unittest.main()