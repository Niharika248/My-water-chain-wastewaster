import hashlib
import os

class EnforceSecurity:
    #0= Encrypt a password and return
    #1= Decrypt a password and verify
    def __init__(self,details):
        self.details = details
    def EncodePassword(self): 
        self.salt = os.urandom(32)
        self.password = str(self.details["password"])
        self.key = hashlib.pbkdf2_hmac('sha256',
                                       self.password.encode('utf-8'),
                                       self.salt,100000)
        self.storage = self.salt+self.key
        return(self.storage)
    def DecodePassword(self):
        self.storage = self.details["storage"]
        self.password = self.details["password"]
        self.salt = self.storage[:32]
        self.key = self.storage[32:]
        self.generated_key = hashlib.pbkdf2_hmac('sha256',
                                self.password.encode('utf-8'),
                                self.salt, 100000)
        if(self.generated_key==self.key):
            return True
        else:
            return False

