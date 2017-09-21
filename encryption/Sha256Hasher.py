import uuid
import hashlib

class Sha256Hasher:
    """
    This class is used in order to hash password before persisting it into database.
    
    """

    def hash_password(self, password):
        """
        hashes password 
        
        :param password: string  
        :return: string hash 
        """
        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


    def check_password(self, hashed_password, user_password):
        """
        checks whether hashed_password was generated from user_password 
        
        :param hashed_password: string hash  
        :param user_password: string 
        :return: boolean 
        """
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()





# password = "foobar"
# hasher = Sha256Hasher()
# hashed_password = hasher.hash_password(password)
# print("password = ", password)
# print("hashed_password = ", hashed_password)
#
# print(hasher.check_password(hashed_password, "foobar"))
