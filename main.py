import flet as ft

def main(page: ft.Page):
    # --- Configuración Visual ---
    page.title = "Mi App Interactiva"
    page.vertical_alignment = "center" # Eliminado ft.MainAxisAlignment
    page.horizontal_alignment = "center" # Eliminado ft.CrossAxisAlignment
    page.theme_mode = "light"
    page.padding = 30
    page.bgcolor = "#F5F5F5" # Color gris claro en formato hex

    # --- Variables de Estado ---
    estado = {"contador": 0}

    # --- Elementos de la Interfaz ---
    texto_titulo = ft.Text(
        value="¡Bienvenido!", 
        size=32, 
        weight="bold", 
        color="blue" # Color como texto directo
    )
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre aquí",
        width=300,
        border_radius=15,
        prefix_icon="person", # Icono como texto directo
        text_align="center"
    )
    
    texto_clicks = ft.Text(
        value="Interacciones: 0", 
        size=14, 
        weight="w500"
    )

    # --- Lógica ---
    def ejecutar_accion(e):
        estado["contador"] += 1
        
        if entrada_nombre.value:
            texto_titulo.value = f"¡Hola, {entrada_nombre.value}!"
            texto_titulo.color = "green" # Color como texto directo
            entrada_nombre.error_text = None
        else:
            texto_titulo.value = "¡Bienvenido de nuevo!"
            texto_titulo.color = "blue"
            entrada_nombre.error_text = "Escribe un nombre"
        
        texto_clicks.value = f"Interacciones: {estado['contador']}"
        page.update()

    # --- Botón con estilo ---
    boton_principal = ft.ElevatedButton(
        text="Actualizar App",
        icon="play_circle_fill", # Icono como texto directo
        on_click=ejecutar_accion,
        style=ft.ButtonStyle(
            color="white",
            bgcolor="blue700", # Color como texto directo
        )
    )

    # --- Montar la App ---
    page.add(
        ft.Column(
            controls=[
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

# Lanzamiento
if __name__ == "__main__":
    ft.app(target=main)
