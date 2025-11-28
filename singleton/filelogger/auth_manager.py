from file_logger import FileLogger

class AuthManager:

    
    def __init__(self):
        
        self.logger = FileLogger()
        self.current_user = None

    def login(self, username, password):
   
        if username == "admin" and password == "secret":
            self.current_user = username
            self.logger.info(f"Usuário '{username}' logado com sucesso.")
            return True
        else:
            self.logger.warning(f"Tentativa de login falhou para o usuário '{username}'.")
            return False

    def get_current_user(self):
        if self.current_user:
            self.logger.info(f"Usuário atual consultado: '{self.current_user}'.")
            return self.current_user
        else:
            self.logger.warning("Tentativa de consultar usuário sem estar logado.")
            return None

    def logout(self):
        if self.current_user:
            self.logger.info(f"Usuário '{self.current_user}' deslogado.")
            self.current_user = None
            return True
        return False