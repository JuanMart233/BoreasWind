import re
from models.UserModel import UsuarioModel

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def login(self, email, password):
        if not email or not password:
            return None, "Completa todos los campos."
        user = self.model.validar_login(email, password)
        if user:
            return user, "OK"
        return None, "Correo o contraseña incorrectos."

    def registrar(self, nombre, email, password):
        if not nombre or not email or not password:
            return False, "Completa todos los campos."
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email):
            return False, "Correo inválido."
        class UserData:
            pass
        data = UserData()
        data.nombre = nombre
        data.email = email
        data.password = password
        ok = self.model.registrar(data)
        if ok:
            return True, "Cuenta creada exitosamente."
        return False, "Error al crear la cuenta. El correo ya existe."
