import pygame
import sys

pygame.init()


width, height = 1800, 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Historia Interactiva")

background_color = (0, 0, 0)
font_color = (255, 255, 255)

font = pygame.font.Font(None, 80)

estado = "menu"

imagenes = {
    "menu": pygame.transform.scale(pygame.image.load("ruta/a/imagen_menu.jpg"), (width, height)),  
    "inicio": pygame.transform.scale(pygame.image.load("ruta/a/imagen_inicio.jpg"), (width, height)),  
    "visitar_ruinas": pygame.transform.scale(pygame.image.load("ruta/a/imagen_visitar_ruinas.jpg"), (width, height)),  
    "ir_al_mercado": pygame.transform.scale(pygame.image.load("ruta/a/imagen_ir_al_mercado.jpg"), (width, height)),  
    "explorar_tuneles": pygame.transform.scale(pygame.image.load("ruta/a/imagen_explorar_tuneles.jpg"), (width, height)),  
    "comprar_jade": pygame.transform.scale(pygame.image.load("ruta/a/imagen_comprar_jade.jpg"), (width, height)),  
    "explorar_cuenta": pygame.transform.scale(pygame.image.load("ruta/a/imagen_explorar_cuenta.jpg"), (width, height)),  
    "explorar_oculto": pygame.transform.scale(pygame.image.load("ruta/a/imagen_explorar_oculto.jpg"), (width, height)),  
    "seguir_tuneles": pygame.transform.scale(pygame.image.load("ruta/a/imagen_seguir_tuneles.jpg"), (width, height)),  
    "tomar_objeto": pygame.transform.scale(pygame.image.load("ruta/a/imagen_tomar_objeto.jpg"), (width, height)),  
    "no_tocar": pygame.transform.scale(pygame.image.load("ruta/a/imagen_no_tocar.jpg"), (width, height)),  
    "final_1": pygame.transform.scale(pygame.image.load("ruta/a/imagen_final_1.jpg"), (width, height)),  
    "final_2": pygame.transform.scale(pygame.image.load("ruta/a/imagen_final_2.jpg"), (width, height)),  
    "final_3": pygame.transform.scale(pygame.image.load("ruta/a/imagen_final_3.jpg"), (width, height)),  
    "final_4": pygame.transform.scale(pygame.image.load("ruta/a/imagen_final_4.jpg"), (width, height)),  
    "final_5": pygame.transform.scale(pygame.image.load("ruta/a/imagen_final_5.jpg"), (width, height)),  
}

def draw_text(text, x, y):
    text_surface = font.render(text, True, font_color)
    screen.blit(text_surface, (x, y))

running = True
while running:
    screen.fill(background_color) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if estado == "menu":
                if event.key == pygame.K_1:
                    estado = "inicio"
                elif event.key == pygame.K_2:
                    running = False
            elif estado == "inicio":
                if event.key == pygame.K_1:
                    estado = "visitar_ruinas"
                elif event.key == pygame.K_2:
                    estado = "ir_al_mercado"
            elif estado == "ir_al_mercado":
                if event.key == pygame.K_1:
                    estado = "comprar_jade"
                elif event.key == pygame.K_2:
                    estado = "preguntar_historias"
            elif estado == "visitar_ruinas":
                if event.key == pygame.K_1:
                    estado = "explorar_tuneles"
                elif event.key == pygame.K_2:
                    estado = "volver_al_parque"
            elif event.key == pygame.K_a:
                if estado == "explorar_tuneles":
                    estado = "seguir_tuneles"
                elif estado == "comprar_jade":
                    estado = "unirse_guia"
                elif estado == "explorar_cuenta":
                    estado = "explorar_oculto"
                elif estado == "explorar_oculto":
                    estado = "tomar_objeto"
            elif event.key == pygame.K_b:
                if estado == "explorar_tuneles":
                    estado = "volver_parque"
                elif estado == "comprar_jade":
                    estado = "explorar_cuenta"
                elif estado == "explorar_oculto":
                    estado = "no_tocar"
                elif estado == "seguir_tuneles":
                    estado = "final_1"
                elif estado == "tomar_objeto":
                    estado = "final_2"
                elif estado == "no_tocar":
                    estado = "final_3"
            elif event.key == pygame.K_c:
                if estado == "seguir_tuneles":
                    estado = "final_4"
                elif estado == "tomar_objeto":
                    estado = "final_5"

    if estado in imagenes:
        screen.blit(imagenes[estado], (0, 0))

    if estado == "menu":
        draw_text("Menu Principal: 1. Jugar  2. Salir", 100, height // 2)
    elif estado == "inicio":
        draw_text("Elige tu destino: 1. Visitar las ruinas (A1), 2. Ir al mercado (A2)", 100, height // 2)
    elif estado == "visitar_ruinas":
        draw_text("Visitas las ruinas. 1. Explorar túneles, 2. Volver al parque", 100, height // 2)
    elif estado == "ir_al_mercado":
        draw_text("Estás en el mercado. 1. Comprar jade, 2. Preguntar historias", 100, height // 2)
    elif estado == "explorar_tuneles":
        draw_text("Exploras los túneles. A. Seguir túneles, B. Salir y volver", 100, height // 2)
    elif estado == "comprar_jade":
        draw_text("Compras jade. A. Unirse al guía, B. Explorar por tu cuenta", 100, height // 2)
    elif estado == "explorar_cuenta":
        draw_text("Exploras por tu cuenta. A. Explorar oculto, B. Continuar", 100, height // 2)
    elif estado == "explorar_oculto":
        draw_text("Encuentras un objeto. A. Tomar, B. No tocar", 100, height // 2)
    elif estado == "seguir_tuneles":
        draw_text("Sigues los túneles y encuentras una salida. Final 1", 100, height // 2)
    elif estado == "tomar_objeto":
        draw_text("Tomas el objeto y encuentras algo valioso. Final 2", 100, height // 2)
    elif estado == "no_tocar":
        draw_text("No tocas el objeto y sigues tu camino. Final 3", 100, height // 2)
    elif estado == "final_1":
        draw_text("Final 1: Encuentras un tesoro en la salida.", 100, height // 2)
    elif estado == "final_2":
        draw_text("Final 2: El objeto es una reliquia antigua.", 100, height // 2)
    elif estado == "final_3":
        draw_text("Final 3: Decides no tocar el objeto y seguir tu camino.", 100, height // 2)
    elif estado == "final_4":
        draw_text("Final 4: Encuentras una salida secreta y escapas.", 100, height // 2)
    elif estado == "final_5":
        draw_text("Final 5: El objeto resulta ser una llave mágica.", 100, height // 2)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
