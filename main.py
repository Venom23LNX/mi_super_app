import flet as ft

def main(page: ft.Page):
    # Configuración de la página
    page.title = "Mi App Profesional"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 30
    
    # Color principal de la app
    page.theme = ft.Theme(color_scheme_seed=ft.colors.BLUE)

    # --- Elementos de la interfaz ---
    # Ya no hay "¡Funciona en!", solo un saludo elegante
    texto_principal = ft.Text("¡Bienvenido!", size=35, weight="bold", color="blue_700")
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre",
        width=300,
        border_radius=15,
        text_align=ft.TextAlign.CENTER,
        on_submit=lambda _: al_pulsar(None) # Permite dar al 'Enter' en el teclado
    )

    texto_contador = ft.Text("Has interactuado 0 veces", size=14, color="grey_600")
    
    contador = 0

    # --- Lógica ---
    def al_pulsar(e):
        nonlocal contador
        contador += 1
        
        if entrada_nombre.value:
            texto_principal.value = f"Hola, {entrada_nombre.value}"
            texto_principal.color = "green_700"
        else:
            texto_principal.value = "¡Hola de nuevo!"
            texto_principal.color = "blue_700"
            
        texto_contador.value = f"Has interactuado {contador} veces"
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
                ft.Divider(height=20, color="transparent"), # Espacio invisible
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
