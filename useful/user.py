import re
from piece import Piece

class User:

    def __init__(self):
        self._privacy = True
        self._username = None
        self._email = None
        self._password = None
        self.createdPieces = []
        self.likedPieces = []
        self.followers = []
        self.following = []

    @property
    def username(self):
        return self._username
  
    @username.setter
    def username(self, username):
        users_list = []                # lista criada só para testar o código
        if username not in users_list: # users_list: lista com todos os nomes de usuário do banco de dados
            self._username = username
            users_list.append(username)
        else:
            raise ValueError('Nome de usuário já existe.')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            self._email = email
        else:
            raise ValueError('Informe um email válido.')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        pattern = re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,12}')
        if pattern.match(password):
            self._password = password
        else:
            raise ValueError('A senha deve conter de 8 a 12 caracteres, um número, uma letra maiúscula e uma letra minúscula.')

    def createPiece(self, text_prompt, width, height, model, seed, iterations):
        aaa = Piece(text_prompt, width, height, model, seed, iterations)
        aaa._image = aaa.runModel()
        self.createdPieces.append(aaa)
       
    def deletePiece(self, index):
        self.createdPieces.pop(index)

    def follow(self, user):
        user._followers.append(self._username)
        self._following.append(user._username)

    def changeUsername(self, current_username, new_username):
        if self._username == current_username:
            users_list = []                    # lista criada só para testar o código
            if new_username not in users_list: # users_list: lista com todos os nomes de usuário do banco de dados
                users_list.remove(self._username)
                self._username = new_username
                users_list.append(new_username)
            else:
                raise ValueError('Nome de usuário já existe.')
        else:
            raise ValueError('Os nomes não correspondem.')

    def changeEmail(self, current_email, new_email):
        if self._email == current_email:
            regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
            if re.search(regex, new_email):
                self._email = new_email
            else:
                raise ValueError('Informe um email válido.')
        else:
            raise ValueError('Os emails não correspondem.')

    def changePassword(self, current_password, new_password):
        if self._password == current_password:
            pattern = re.compile('(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,12}')
            if pattern.match(new_password):
                self._password = new_password
            else:
                raise ValueError('A senha deve conter de 8 a 12 caracteres, um número, uma letra maiúscula e uma letra minúscula.')
        else:
            raise ValueError('As senhas não correspondem.')

    def changePrivacy(self):
        self._privacy = not self._privacy

    def likePiece(self, piece): ## como que eu garanto que piece é do tipo Piece?
        piece.likes.append(self._username)
        self.likedPieces.append(piece)

    def deleteUser():
        pass 