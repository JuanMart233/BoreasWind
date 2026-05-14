import flet as ft

def RecuperarView(page: ft.Page, auth_controller, on_volver):
    email_input = ft.TextField(label="Correo electrónico", width=350, prefix_icon=ft.Icons.EMAIL, border_radius=10)
    codigo_input = ft.TextField(label="Código de 6 dígitos", width=350, prefix_icon=ft.Icons.KEY, border_radius=10)
    nueva_pass = ft.TextField(label="Nueva contraseña", width=350, password=True, prefix_icon=ft.Icons.LOCK, border_radius=10)
    confirmar_pass = ft.TextField(label="Confirmar contraseña", width=350, password=True, prefix_icon=ft.Icons.LOCK, border_radius=10)
    msg = ft.Text("", size=13)

    email_guardado = {"value": ""}

    paso1 = ft.Column(visible=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, controls=[
        ft.Text("Recuperar contraseña", size=22, weight=ft.FontWeight.BOLD),
        ft.Text("Ingresa tu correo y te enviaremos un código.", size=13, color=ft.Colors.GREY_400),
        email_input,
        msg,
        ft.ElevatedButton("Enviar código", width=200, bgcolor=ft.Colors.BLUE_400, color="white",
            on_click=lambda e: enviar(e)),
        ft.TextButton("Volver al inicio de sesión", on_click=lambda e: on_volver()),
    ])

    paso2 = ft.Column(visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, controls=[
        ft.Text("Verificar código", size=22, weight=ft.FontWeight.BOLD),
        ft.Text("Revisa tu correo e ingresa el código.", size=13, color=ft.Colors.GREY_400),
        codigo_input,
        msg,
        ft.ElevatedButton("Verificar", width=200, bgcolor=ft.Colors.BLUE_400, color="white",
            on_click=lambda e: verificar(e)),
    ])

    paso3 = ft.Column(visible=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15, controls=[
        ft.Text("Nueva contraseña", size=22, weight=ft.FontWeight.BOLD),
        nueva_pass,
        confirmar_pass,
        msg,
        ft.ElevatedButton("Guardar contraseña", width=200, bgcolor=ft.Colors.GREEN_400, color="white",
            on_click=lambda e: guardar(e)),
    ])

    def set_msg(texto, color=ft.Colors.RED_400):
        msg.value = texto
        msg.color = color
        page.update()

    def enviar(e):
        set_msg("")
        ok, texto = auth_controller.enviar_codigo(email_input.value.strip())
        if ok:
            email_guardado["value"] = email_input.value.strip()
            paso1.visible = False
            paso2.visible = True
            set_msg(texto, ft.Colors.GREEN_400)
        else:
            set_msg(texto)

    def verificar(e):
        set_msg("")
        ok, texto = auth_controller.verificar_codigo(email_guardado["value"], codigo_input.value.strip())
        if ok:
            paso2.visible = False
            paso3.visible = True
            set_msg(texto, ft.Colors.GREEN_400)
        else:
            set_msg(texto)

    def guardar(e):
        set_msg("")
        if nueva_pass.value != confirmar_pass.value:
            set_msg("Las contraseñas no coinciden.")
            return
        ok, texto = auth_controller.cambiar_password(email_guardado["value"], nueva_pass.value.strip())
        if ok:
            set_msg(texto, ft.Colors.GREEN_400)
            page.update()
            import time; time.sleep(1.5)
            on_volver()
        else:
            set_msg(texto)

    return ft.Container(
        content=ft.Column(
            controls=[paso1, paso2, paso3],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.Alignment(0, 0),
        expand=True,
    )
