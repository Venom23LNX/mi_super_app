import flet as ft

def main(page: ft.Page):
    # --- Configuración Visual de la App ---
    page.title = "Mi App Interactiva Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400  # Tamaño ideal para probar en PC
    page.bgcolor = ft.colors.GREY_50

    # --- Variables de "Estado" (Datos que cambian) ---
    contador = 0

    # --- Elementos de la Interfaz ---
    texto_titulo = ft.Text("¡Bienvenido!", size=32, weight="bold", color="blue")
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre aquí",
        width=300,
        border_radius=15,
        prefix_icon=ft.icons.PERSON
    )
    
    texto_info = ft.Text("Haz clic en el botón para interactuar", size=16, italic=True)
    texto_clicks = ft.Text("Clics totales: 0", size=14, weight="w500")

    # --- Lógica de la App (Qué pasa al pulsar) ---
    def ejecutar_accion(e):
        nonlocal contador
        contador += 1
        
        # Si el usuario escribió algo, lo saludamos por su nombre
        if entrada_nombre.value:
            texto_titulo.value = f"¡Hola, {entrada_nombre.value}!"
            texto_titulo.color = "green"
            entrada_nombre.error_text = None
        else:
            # Si está vacío, mostramos un error
            texto_titulo.value = "¡Escribe algo!"
            texto_titulo.color = "red"
            entrada_nombre.error_text = "Campo obligatorio"
        
        texto_clicks.value = f"Clics totales: {contador}"
        
        # ¡Muy importante! Actualizar la pantalla para que el móvil lo vea
        page.update()

    # --- Botón con estilo ---
    boton_principal = ft.ElevatedButton(
        text="Actualizar App",
        icon=ft.icons.PLAY_CIRCLE_FILL,
        on_click=ejecutar_accion,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_700,
            padding=20
        )
    )

    # --- Montar la App (Columnas y Filas) ---
    page.add(
        ft.Container(
            content=ft.Column(
                [
                    texto_titulo,
                    ft.Divider(height=20, color="transparent"),
                    entrada_nombre,
                    boton_principal,
                    ft.Divider(height=20, color="transparent"),
                    texto_info,
                    texto_clicks,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=30,
            alignment=ft.alignment.center
        )
    )

# Lanzamiento de la app
ft.app(target=main)
