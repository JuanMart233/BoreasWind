import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

import flet as ft
from controllers.UserController import AuthController
from views.LoginView import LoginView

def start(page: ft.Page):
    try:
        auth_ctrl = AuthController()
    except Exception as e:
        page.add(ft.Text(f"Error BD: {e}", color=ft.Colors.RED))
        return

    def show_login():
        page.controls.clear()
        page.add(LoginView(page, auth_ctrl, on_login=lambda user: None))

    show_login()

ft.run(start)
