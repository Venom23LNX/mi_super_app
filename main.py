import flet as ft

def main(page: ft.Page):
    # 1. CONFIGURACIÓN DE LA PÁGINA
    page.title = "Mi App Estable"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.bgcolor = "#F0F2F5" # Un gris muy claro de fondo
    page.padding = 40

    # 2. VARIABLES DE ESTADO
    # Usamos un diccionario para que sea fácil de actualizar
    estado = {"contador": 0}

    # 3. ELEMENTOS VISUALES (CONTROLES)
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
        size=16, 
        color="grey"
    )

    # 4. LÓGICA DE LA APP (FUNCIONES)
    def al_pulsar_boton(e):
        # Aumentamos el contador en el diccionario
        estado["contador"] += 1
        
        # Cambiamos el saludo según el nombre
        if entrada_nombre.value:
            texto_bienvenida.value = f"Hola, {entrada_nombre.value}"
            texto_bienvenida.color = "green"
        else:
            texto_bienvenida.value = "¡Hola de nuevo!"
            texto_bienvenida.color = "blue"
            
        # Actualizamos el texto del contador
        texto_stats.value = f"Interacciones: {estado['contador']}"
        
        # ¡IMPORTANTE! Refrescamos la página para ver los cambios
        page.update()

    # 5. EL BOTÓN (CORREGIDO)
    # Definimos texto e icono desde el inicio para evitar errores de Flet
    boton_accion = ft.ElevatedButton(
        text="Actualizar App",
        icon="play_arrow",
        on_click=al_pulsar_boton
    )

    # 6. MONTAJE FINAL EN LA PANTALLA
    # Metemos todo en una columna centrada
    page.add(
        ft.Column(
            controls=[
                texto_bienvenida,
                ft.Container(height=10), # Espacio
                entrada_nombre,
                boton_accion,
                ft.Container(height=10), # Espacio
                texto_stats,
            ],
            horizontal_alignment="center",
            spacing=15
        )
    )

# 7. ARRANCAR LA APLICACIÓN
if __name__ == "__main__":
    ft.app(target=main)
