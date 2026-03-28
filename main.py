import flet as ft

def main(page: ft.Page):
    # --- Configuración Visual de la App ---
    page.title = "Mi App Interactiva"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.padding = 30
    page.bgcolor = "#F5F5F5" # Sustituido ft.colors.GREY_50

    # --- Variables de "Estado" ---
    estado = {"contador": 0}

    # --- Elementos de la Interfaz ---
    # Eliminado el texto de "¡Funciona en!" y usado color como texto
    texto_titulo = ft.Text("¡Bienvenido!", size=32, weight="bold", color="blue")
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre aquí",
        width=300,
        border_radius=15,
        prefix_icon="person", # Usado nombre del icono como texto
        text_align="center"
    )
    
    texto_clicks = ft.Text("Interacciones: 0", size=14, weight="w500")

    # --- Lógica de la App ---
    def ejecutar_accion(e):
        estado["contador"] += 1
        
        if entrada_nombre.value:
            texto_titulo.value = f"¡Hola, {entrada_nombre.value}!"
            texto_titulo.color = "green"
            entrada_nombre.error_text = None
        else:
            texto_titulo.value = "¡Bienvenido de nuevo!"
            texto_titulo.color = "blue"
            entrada_nombre.error_text = "Escribe un nombre"
        
        texto_clicks.value = f"Interacciones: {estado['contador']}"
        page.update()

    # --- Botón con estilo (Corregido para evitar errores) ---
    boton_principal = ft.ElevatedButton(
        text="Actualizar App",
        icon="play_circle_fill",
        on_click=ejecutar_accion,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="blue700",
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
            horizontal_alignment="center",
            spacing=10
        )
    )

# Lanzamiento de la app
if __name__ == "__main__":
    ft.app(target=main)
