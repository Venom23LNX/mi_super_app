import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Mi App Multiplataforma"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # Texto y Botón
    texto = ft.Text("¡Bienvenido a mi App!", size=30, weight="bold")
    
    def cambiar_color(e):
        texto.value = "¡Funciona en Ubuntu y Móvil! 🚀"
        texto.color = "blue"
        page.update()

    boton = ft.ElevatedButton("Haz clic aquí", on_click=cambiar_color)

    # Añadir elementos a la pantalla
    page.add(
        ft.Row(
            [texto],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [boton],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Importante: view=ft.AppView.WEB_BROWSER sirve para probarlo como si fuera una web
ft.app(target=main)