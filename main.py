import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página
    page.title = "Mi App Profesional"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.padding = 30
    
    # Color de fondo suave para que se vea mejor
    page.bgcolor = "#f0f2f5"
    
    # Variables de la app (Estado)
    estado = {"contador": 0}

    # 2. Elementos de la interfaz
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
        bgcolor="white"
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

    # --- BOTÓN CORREGIDO ---
    # Usamos Elevated Button con "text" en minúsculas
    boton_accion = ft.ElevatedButton(
        text="Actualizar",
        icon="play_arrow",
        on_click=al_pulsar_boton
    )

    # 4. Montar la interfaz
    # Usamos un Column para organizar todo verticalmente
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

# Lanzamiento oficial
if __name__ == "__main__":
    ft.app(target=main)
