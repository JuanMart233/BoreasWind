import flet as ft

def main(page: ft.Page):
    page.title = "Imagenes :3"
    page.bgcolor = ft.Colors.PURPLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    mensaje = ft.Text(size=18, color=ft.Colors.WHITE)

    def cambiar_mensaje(e):
        valor = slider.value

        if valor < 25:
            mensaje.value = "COMO QUE MENOS DE 25 HDP"
        elif 25 <= valor <= 60:
            mensaje.value = "Bueno podria ser peor"
        elif 60 < valor <= 90:
            mensaje.value = "Pero si que te gusta :3"
        else:
            mensaje.value = "Eres un fan como yo yei"

        page.update()

    slider = ft.Slider(
        min=0,
        max=100,
        divisions=100,
        value=15,
        label="{value}%",
        on_change=cambiar_mensaje

    )

    cambiar_mensaje(None)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Hola gente",
                    size=24,
                    color=ft.Colors.BLUE,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Image(
                    src="https://imgs.search.brave.com/UhsZ9-jNQWI3gZKMYBGM4-PWsQxP2LuenhKIocudJj0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzQ2L2M0/LzhlLzQ2YzQ4ZWE0/MWNiMmUxZTk3YzE1/ZTE1OWRiNzc4OTk4/LmpwZw",
                    width=250,
                    height=250,
                    border_radius=125,
                ),

                ft.Text("Que tanto te gusta ado?", size=18, color=ft.Colors.WHITE),

                slider,

                mensaje,

                ft.Divider(height=10, thickness=2, color=ft.Colors.BLACK),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.add(
        ft.Column(
            ft.Text("iniciar sesion", color=ft.Colors.DEEP_PURPLE_ACCENT_100,
                    width=320,
                    size=25,
                    text_align=ft.TextAlign.CENTER,
                    weight="w900",
            ),
        ),
        ft.Column(
            ft.TextField(
                hint_text="Correo electronico",
                border="underline",
                color=ft.Colors.BLACK,
                border_color=ft.Colors.RED,
                focused_border_color=ft.Colors.BLUE,
                filled=True,
                bgcolor=ft.Colors.RED_400,
                prefix=ft.Icon(ft.icons.Icons.EMAIL, color=ft.Colors.BLACK),
            ),
        ),
        ft.Column(
            ft.TextField(
                label="Contraseña",
                hint_text="Agrega tu Contraseña",
                value="",
                prefix=ft.Icon(ft.icons.Icons.LOCK, color=ft.Colors.BLACK),
                suffix=ft.Text(".com"),
                password=True,
                can_reveal_password=True,
                multiline=False,
                max_length=50,
                keyboard_type=ft.KeyboardType.TEXT,
                border=ft.InputBorder.OUTLINE,
                border_color=ft.Colors.RED,
                focused_border_color=ft.Colors.BLUE,
                filled=True,
                bgcolor=ft.Colors.RED_400,
                on_change=lambda e: print(e.control.value),
                on_submit=lambda e: print("Enter presionado")
            ),
        ),
        ft.Column(
            ft.Checkbox(
                label="Recordar contraseña",
                check_color=ft.Colors.BLACK,
                align= "CENTER",
                )
        )
        )
ft.run(main)