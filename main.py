import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Mi App Profesional"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    
    # Color principal de la app (Usando string directo para evitar errores)
    page.theme = ft.Theme(color_scheme_seed="blue")

    # --- Elementos de la interfaz ---
    texto_principal = ft.Text("¡Bienvenido!", size=35, weight="bold", color="blue700")
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre",
        width=300,
        border_radius=15,
        text_align=ft.TextAlign.CENTER,
    )

    texto_contador = ft.Text("Has interactuado 0 veces", size=14, color="grey600")
    
    # Variable para el contador
    page.session.set("contador", 0)

    # --- Lógica ---
    def al_pulsar(e):
        # Obtener y actualizar el contador de la sesión
        count = page.session.get("contador") + 1
        page.session.set("contador", count)
        
        if entrada_nombre.value:
            texto_principal.value = f"Hola, {entrada_nombre.value}"
            texto_principal.color = "green700"
        else:
            texto_principal.value = "¡Hola de nuevo!"
            texto_principal.color = "blue700"
            
        texto_contador.value = f"Has interactuado {count} veces"
        page.update()

    # Botón más moderno
    boton = ft.FilledButton(
        "Actualizar",
        icon=ft.icons.CHEVRON_RIGHT,
        on_click=al_pulsar,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10))
    )

    # --- Diseño Final ---
    page.add(
        ft.Column(
            [
                texto_principal,
                ft.Divider(height=20, color="transparent"), 
                entrada_nombre,
                boton,
                ft.Divider(height=10, color="transparent"),
                texto_contador,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )
    )

ft.app(target=main)
