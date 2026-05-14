import flet as ft

def DashboardView(page, tarea_controller, user, on_logout):
    lista_tareas = ft.Column(scroll=ft.ScrollMode.ALWAYS, expand=True)

    def refresh():
        lista_tareas.controls.clear()
        for t in tarea_controller.obtener_lista(user["id_usuario"]):
            lista_tareas.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.ListTile(
                            title=ft.Text(t["titulo"], weight="bold"),
                            subtitle=ft.Text(f"{t['descripcion']}\nPrioridad: {t['prioridad']}"),
                            trailing=ft.Container(
                                content=ft.Text(t["estado"], size=12, color="white"),
                                bgcolor=ft.Colors.ORANGE_300,
                                padding=ft.padding.symmetric(horizontal=8, vertical=4),
                                border_radius=10,
                            ),
                        ),
                        padding=10,
                    )
                )
            )
        page.update()

    txt_titulo = ft.TextField(
        label="Nueva Tarea",
        expand=True,
        border_color=ft.Colors.RED_800,
        focused_border_color=ft.Colors.RED_400,
        label_style=ft.TextStyle(color=ft.Colors.RED_300),
        cursor_color=ft.Colors.RED_300,
        border_radius=10,
    )

    def add_task(e):
        success, msg = tarea_controller.guardar_nueva(
            user["id_usuario"], txt_titulo.value, "", "media", "trabajo"
        )
        if success:
            txt_titulo.value = ""
            refresh()

    refresh()

    return ft.Column(
        controls=[
            ft.AppBar(
                title=ft.Text(f"Bienvenido a tu gestor de tareas: {user['nombre']}"),
                bgcolor=ft.Colors.BLUE_400,
                color="white",
                actions=[ft.IconButton(ft.Icons.EXIT_TO_APP, on_click=lambda _: on_logout())],
            ),
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Text(
                            "Nueva Tarea",
                            size=16,
                            weight=ft.FontWeight.BOLD,
                            color=ft.Colors.RED_200,
                        ),
                        ft.Row(
                            controls=[
                                txt_titulo,
                                ft.ElevatedButton(
                                    "Guardar",
                                    icon=ft.Icons.SAVE,
                                    on_click=add_task,
                                    bgcolor=ft.Colors.RED_800,
                                    color="white",
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                    ),
                                ),
                            ],
                        ),
                    ],
                    spacing=8,
                ),
                bgcolor=ft.Colors.RED_900,
                padding=ft.padding.all(16),
                border_radius=12,
                border=ft.border.all(1, ft.Colors.RED_700),
                margin=ft.margin.symmetric(horizontal=10),
            ),
            ft.Divider(color=ft.Colors.RED_800),
            ft.Text("Mis Pendientes", size=20, weight="bold", color=ft.Colors.RED_300),
            lista_tareas,
        ],
        expand=True,
        spacing=10,
    )
