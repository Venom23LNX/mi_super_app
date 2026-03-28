import flet as ft

def main(page: ft.Page):
    # 1. Configuración de la página
    page.title = "App Final Corregida"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = "light"
    page.bgcolor = "#F0F2F5"
    
    # Estado de la aplicación
    estado = {"contador": 0}

    # 2. Creación de componentes
    texto_bienvenida = ft.Text(value="¡Bienvenido!", size=30, weight="bold", color="blue")
    
    entrada_nombre = ft.TextField(
        label="Escribe tu nombre",
        width=280,
        border_radius=10,
        text_align="center",
        bgcolor="white"
    )

    texto_stats = ft.Text(value="Interacciones: 0", size=16, color="grey")

    # 3. Lógica de funcionamiento
    def al_clic(e):
        estado["contador"] += 1
        
        if entrada_nombre.value:
            texto_bienvenida.value = f"Hola, {entrada_nombre.value}"
            texto_bienvenida.color = "green"
        else:
            texto_bienvenida.value = "¡Hola de nuevo!"
            texto_bienvenida.color = "blue"
            
        texto_stats.value = f"Interacciones: {estado['contador']}"
        page.update()

    # --- SOLUCIÓN AL ERROR DEL BOTÓN ---
    # Creamos el botón y luego asignamos sus propiedades por separado 
    # para evitar cualquier error de "keyword argument"
    boton_accion = ft.ElevatedButton()
    boton_accion.text = "Actualizar App"
    boton_accion.icon = "play_arrow"
    boton_accion.on_click = al_clic

    # 4. Montaje de la interfaz
    # Usamos un contenedor para darle un aspecto de "tarjeta"
    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    texto_bienvenida,
                    ft.Divider(height=10, color="transparent"),
                    entrada_nombre,
                    boton_accion,
                    ft.Divider(height=10, color="transparent"),
                    texto_stats,
                ],
                horizontal_alignment="center",
                spacing=10
            ),
            padding=40,
            bgcolor="white",
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=15, color="grey")
        )
    )

# Ejecución
if __name__ == "__main__":
    ft.app(target=main)
