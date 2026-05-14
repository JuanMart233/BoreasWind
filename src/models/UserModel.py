from .database import Database

class UsuarioModel:
    def __init__(self):
        self.db = Database()

    def registrar(self, usuario_data):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO usuario (nombre, email, password) VALUES (%s, %s, %s)",
                (usuario_data.nombre, usuario_data.email, usuario_data.password)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
        finally:
            conn.close()

    def validar_login(self, email, password):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s AND password=%s", (email, password))
        user = cursor.fetchone()
        conn.close()
        return user

    def buscar_por_email(self, email):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuario WHERE email=%s", (email,))
        user = cursor.fetchone()
        conn.close()
        return user

    def actualizar_password(self, email, nueva_password):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE usuario SET password=%s WHERE email=%s", (nueva_password, email))
        conn.commit()
        conn.close()