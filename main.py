import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página
    page.title = "Mi App Profesional"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.padding = 30
    
    # Variables de la app (Estado)
    # Usamos un diccionario para que Python lo maneje de forma estable
    estado = {"contador": 0}

    # 2. Elementos de la interfaz (Usamos nombres de colores como texto)
    texto_bienvenida = ft.Text(
        value="¡Bienvenido!", 
        size=35, 
        weight="bold", 
        color="blue"
    )
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre",
        width=300,
        border_radius=15,
        text_align="center",
    )

    texto_stats = ft.Text(
        value="Interacciones: 0", 
        size=14, 
        color="grey"
    )

    # 3. Lógica de la aplicación
    def al_pulsar_boton(e):
        # Aumentar contador
        estado["contador"] += 1
        
        # Lógica de saludo
        if entrada_nombre.value:
            texto_bienvenida.value = f"Hola, {entrada_nombre.value}"
            texto_bienvenida.color = "green"
        else:
            texto_bienvenida.value = "¡Hola de nuevo!"
            texto_bienvenida.color = "blue"
            
        # Actualizar texto de contador
        texto_stats.value = f"Interacciones: {estado['contador']}"
        
        # Refrescar la pantalla
        page.update()

    # Botón principal
    boton_accion = ft.ElevatedButton(
        text="Actualizar",
        icon="play_arrow",
        on_click=al_pulsar_boton,
    )

    # 4. Montar la interfaz
    page.add(
        ft.Column(
            [
                texto_bienvenida,
                ft.Container(height=10), # Espaciador
                entrada_nombre,
                boton_accion,
                ft.Container(height=10), # Espaciador
                texto_stats,
            ],
            horizontal_alignment="center",
            spacing=15
        )
    )

# Ejecutar la aplicación
if __name__ == "__main__":
    ft.app(target=main)
