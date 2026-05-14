import re
import random
import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from models.UserModel import UsuarioModel

_search_dirs = [
    os.path.dirname(__file__),
    os.path.join(os.path.dirname(__file__), ".."),
    os.path.join(os.path.dirname(__file__), "..", ".."),
    os.path.join(os.path.dirname(__file__), "..", "..", "base"),
]
for _d in _search_dirs:
    _env = os.path.join(os.path.abspath(_d), ".env")
    if os.path.exists(_env):
        load_dotenv(_env)
        break

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()
        self._codigos = {}

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

    def enviar_codigo(self, email):
        if not self.model.buscar_por_email(email):
            return False, "No existe una cuenta con ese correo."
        codigo = str(random.randint(100000, 999999))
        self._codigos[email] = codigo
        try:
            msg = MIMEText(f"Hola, tu código de recuperación es: {codigo}")
            msg["Subject"] = "Recuperación de contraseña - BoreasWind"
            msg["From"] = os.getenv("MAIL_USER")
            msg["To"] = email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(os.getenv("MAIL_USER"), os.getenv("MAIL_PASSWORD"))
                server.sendmail(os.getenv("MAIL_USER"), email, msg.as_string())
            return True, "Código enviado a tu correo."
        except Exception as e:
            return False, f"Error al enviar correo: {e}"

    def verificar_codigo(self, email, codigo):
        if self._codigos.get(email) == codigo:
            return True, "Código correcto."
        return False, "Código incorrecto."

    def cambiar_password(self, email, nueva_password):
        if not nueva_password or len(nueva_password) < 8:
            return False, "La contraseña debe tener al menos 8 caracteres."
        self.model.actualizar_password(email, nueva_password)
        self._codigos.pop(email, None)
        return True, "Contraseña actualizada correctamente."
