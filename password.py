class Password:
    """
    Class that generates new instances of password
    """
    password_list =  [] #used to store our created password objects 

    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)
        

    