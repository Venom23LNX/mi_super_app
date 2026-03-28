import flet as ft

def main(page: ft.Page):
    # --- Configuración Visual de la App ---
    page.title = "Mi App Interactiva"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    page.bgcolor = ft.colors.GREY_50

    # --- Variables de "Estado" ---
    # Usamos una lista para el contador para evitar problemas de "nonlocal"
    estado = {"contador": 0}

    # --- Elementos de la Interfaz ---
    # Eliminado el texto de "¡Funciona en!" y dejado solo el saludo
    texto_titulo = ft.Text("¡Bienvenido!", size=32, weight="bold", color=ft.colors.BLUE)
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre aquí",
        width=300,
        border_radius=15,
        prefix_icon=ft.icons.PERSON,
        text_align=ft.TextAlign.CENTER
    )
    
    texto_clicks = ft.Text("Interacciones: 0", size=14, weight="w500")

    # --- Lógica de la App ---
    def ejecutar_accion(e):
        estado["contador"] += 1
        
        if entrada_nombre.value:
            texto_titulo.value = f"¡Hola, {entrada_nombre.value}!"
            texto_titulo.color = ft.colors.GREEN
            entrada_nombre.error_text = None
        else:
            texto_titulo.value = "¡Bienvenido de nuevo!"
            texto_titulo.color = ft.colors.BLUE
            entrada_nombre.error_text = "Escribe un nombre"
        
        texto_clicks.value = f"Interacciones: {estado['contador']}"
        page.update()

    # --- Botón con estilo ---
    boton_principal = ft.ElevatedButton(
        text="Actualizar App",
        icon=ft.icons.PLAY_CIRCLE_FILL,
        on_click=ejecutar_accion,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
        )
    )

    # --- Montar la App ---
    page.add(
        ft.Column(
            [
                texto_titulo,
                ft.Divider(height=20, color="transparent"),
                entrada_nombre,
                boton_principal,
                ft.Divider(height=20, color="transparent"),
                texto_clicks,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

# Lanzamiento de la app
if __name__ == "__main__":
    ft.app(target=main)
