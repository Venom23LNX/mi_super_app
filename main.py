import flet as ft

def main(page: ft.Page):
    # Configuración de la página (Tu estilo original)
    page.title = "Mi App Multiplataforma Fusionada"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    # --- Variables ---
    contador = 0

    # --- Elementos Visuales ---
    # Empezamos con tu texto original
    texto = ft.Text("¡Bienvenido a mi App!", size=30, weight="bold")
    
    # Campo para escribir (Nueva función)
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre", 
        width=300, 
        border_radius=10,
        hint_text="Ej: Juan"
    )

    # Texto secundario para el contador
    texto_contador = ft.Text("Clics realizados: 0", size=16, color="grey")

    # --- Función de Lógica (Tu función original evolucionada) ---
    def al_hacer_clic(e):
        nonlocal contador
        contador += 1
        
        # 1. Mantiene tu mensaje original al hacer clic
        texto.value = "¡Funciona en Ubuntu y Móvil! 🚀"
        texto.color = "blue"
        
        # 2. Si hay un nombre, personaliza el saludo
        if entrada_nombre.value:
            texto.value = f"¡Hola {entrada_nombre.value}! Funciona en Móvil 🚀"
        
        # 3. Actualiza el contador
        texto_contador.value = f"Clics realizados: {contador}"
        
        page.update()

    # Botón (Tu botón original con la nueva lógica)
    boton = ft.ElevatedButton("Haz clic aquí", on_click=al_hacer_clic)

    # --- Añadir elementos (Tu estructura de filas, pero organizada) ---
    page.add(
        ft.Column(
            [
                ft.Row([texto], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([entrada_nombre], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([boton], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([texto_contador], alignment=ft.MainAxisAlignment.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

# Ejecución
ft.app(target=main)
