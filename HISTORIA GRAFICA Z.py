import pygame
import sys

pygame.init()

width, height = 1800, 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Aventureros en Antigua Guatemala")

background_color = (0, 0, 0)
font_color = (255, 255, 255)

font = pygame.font.Font(None, 40)

estado = "menu"

imagenes = {
    "menu": pygame.transform.scale(pygame.image.load("imagen_menu.jpg"), (width, height)),
    "inicio": pygame.transform.scale(pygame.image.load("imagen_inicio.jpg"), (width, height)),
    "visitar_ruinas": pygame.transform.scale(pygame.image.load("imagen_visitar_ruinas.jpg"), (width, height)),
    "ir_al_mercado": pygame.transform.scale(pygame.image.load("imagen_ir_al_mercado.jpg"), (width, height)),
    "explorar_tuneles": pygame.transform.scale(pygame.image.load("imagen_explorar_tuneles.jpg"), (width, height)),
    "comprar_jade": pygame.transform.scale(pygame.image.load("imagen_comprar_jade.jpg"), (width, height)),
    "preguntar_historias": pygame.transform.scale(pygame.image.load("imagen_preguntar_historias.jpg"), (width, height)),
    "historia_1": pygame.transform.scale(pygame.image.load("imagen_historia_1.jpg"), (width, height)),
    "historia_2": pygame.transform.scale(pygame.image.load("imagen_historia_2.jpg"), (width, height)),
    "explorar_cuenta": pygame.transform.scale(pygame.image.load("imagen_explorar_cuenta.jpg"), (width, height)),
    "explorar_oculto": pygame.transform.scale(pygame.image.load("imagen_explorar_oculto.jpg"), (width, height)),
    "seguir_tuneles": pygame.transform.scale(pygame.image.load("imagen_seguir_tuneles.jpg"), (width, height)),
    "tomar_objeto": pygame.transform.scale(pygame.image.load("imagen_tomar_objeto.jpg.webp"), (width, height)),
    "no_tocar": pygame.transform.scale(pygame.image.load("imagen_no_tocar.jpg"), (width, height)),
    "final_1": pygame.transform.scale(pygame.image.load("imagen_final_1.jpg"), (width, height)),
    "final_2": pygame.transform.scale(pygame.image.load("imagen_final_2.jpg.png"), (width, height)),
    "final_3": pygame.transform.scale(pygame.image.load("imagen_final_3.jpg"), (width, height)),
    "final_4": pygame.transform.scale(pygame.image.load("imagen_final_4.jpg"), (width, height)),
    "final_5": pygame.transform.scale(pygame.image.load("imagen_final_5.jpg"), (width, height)),
    "final_6": pygame.transform.scale(pygame.image.load("imagen_final_6.jpg"), (width, height)),
    "final_7": pygame.transform.scale(pygame.image.load("imagen_final_7.jpg"), (width, height)),
    "volver_parque": pygame.transform.scale(pygame.image.load("imagen_volver_parque.jpg"), (width, height))
}

def draw_text(text, x, y):
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, font_color)
        screen.blit(text_surface, (x, y + i * 50))

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
            elif estado == "visitar_ruinas":
                if event.key == pygame.K_1:
                    estado = "explorar_tuneles"
                elif event.key == pygame.K_2:
                    estado = "final_1"  
            elif estado == "ir_al_mercado":
                if event.key == pygame.K_1:
                    estado = "comprar_jade"
                elif event.key == pygame.K_2:
                    estado = "preguntar_historias"
            elif estado == "preguntar_historias":
                if event.key == pygame.K_1:
                    estado = "historia_1"
                elif event.key == pygame.K_2:
                    estado = "historia_2"
            elif estado == "historia_1":
                if event.key == pygame.K_1:
                    estado = "final_2"
            elif estado == "historia_2":
                if event.key == pygame.K_1:
                    estado = "final_3"
            elif estado == "explorar_tuneles":
                if event.key == pygame.K_a:
                    estado = "seguir_tuneles"
                elif event.key == pygame.K_b:
                    estado = "final_4" 
            elif estado == "comprar_jade":
                if event.key == pygame.K_a:
                    estado = "final_5"  
                elif event.key == pygame.K_b:
                    estado = "explorar_cuenta"
            elif estado == "explorar_cuenta":
                if event.key == pygame.K_a:
                    estado = "explorar_oculto"
                elif event.key == pygame.K_b:
                    estado = "final_6"
            elif estado == "explorar_oculto":
                if event.key == pygame.K_a:
                    estado = "tomar_objeto"
                elif event.key == pygame.K_b:
                    estado = "final_7"  
            elif estado == "seguir_tuneles":
                if event.key == pygame.K_a:
                    estado = "final_1"
                elif event.key == pygame.K_b:
                    estado = "final_2"
                elif event.key == pygame.K_c:
                    estado = "final_3"
            elif estado == "tomar_objeto":
                if event.key == pygame.K_a:
                    estado = "final_4"
                elif event.key == pygame.K_b:
                    estado = "final_5"
            elif estado == "no_tocar":
                if event.key == pygame.K_a:
                    estado = "final_6"
                elif event.key == pygame.K_b:
                    estado = "final_7"

    if estado in imagenes:
        screen.blit(imagenes[estado], (0, 0))

    if estado == "menu":
        draw_text("Menu Principal:\n1. Jugar\n2. Salir", 100, height // 2)
    elif estado == "inicio":
        draw_text("Te encuentras en el cruce de caminos del parque central.\nElige tu destino:\n1. Visitar las ruinas\n2. Ir al mercado", 100, height // 2)
    elif estado == "visitar_ruinas":
        draw_text("Caminas hacia las antiguas ruinas, llenas de misterios y secretos.\n1. Explorar túneles oscuros\n2. Volver al parque", 100, height // 2)
    elif estado == "ir_al_mercado":
        draw_text("Llegas al bullicioso mercado lleno de vida y colores.\n1. Comprar una pieza de jade\n2. Preguntar a los vendedores sobre historias locales", 100, height // 2)
    elif estado == "explorar_tuneles":
        draw_text("Te adentras en los túneles oscuros bajo las ruinas. Escuchas un eco misterioso.\nA. Seguir explorando los túneles\nB. Salir y volver al parque", 100, height // 2)
    elif estado == "comprar_jade":
        draw_text("Compras una hermosa pieza de jade. El vendedor te ofrece un guía.\nA. Unirte al guía\nB. Explorar por tu cuenta", 100, height // 2)
    elif estado == "explorar_cuenta":
        draw_text("Decides explorar el mercado por tu cuenta y encuentras un pasadizo oculto.\nA. Entrar al pasadizo oculto\nB. Continuar explorando el mercado", 100, height // 2)
    elif estado == "explorar_oculto":
        draw_text("El pasadizo te lleva a una cámara secreta donde ves un objeto brillante.\nA. Tomar el objeto\nB. No tocar el objeto", 100, height // 2)
    elif estado == "seguir_tuneles":
        draw_text("Sigues los túneles y encuentras una salida secreta al otro lado de las ruinas. Estás a salvo.\nA. Encuentra un tesoro\nB. La reliquia antigua\nC. Salida segura", 100, height // 2)
    elif estado == "tomar_objeto":
        draw_text("Tomas el objeto y una puerta secreta se abre.\nA. Seguir por la puerta\nB. Dejar el objeto y volver al parque", 100, height // 2)
    elif estado == "no_tocar":
        draw_text("Decides no tocar el objeto y buscas una salida.\nA. Salir por donde entraste\nB. Buscar otra salida", 100, height // 2)
    elif estado == "preguntar_historias":
        draw_text("Preguntas a los vendedores sobre historias locales.\n1. Escuchar la primera historia\n2. Escuchar la segunda historia", 100, height // 2)
    elif estado == "historia_1":
        draw_text("Primera historia: Un antiguo guerrero que protegía estas tierras...\n1. Volver al parque", 100, height // 2)
    elif estado == "historia_2":
        draw_text("Segunda historia: Una leyenda de amor prohibido entre dos aldeanos...\n1. Volver al parque", 100, height // 2)
    elif estado == "volver_parque":
        draw_text("Decides volver al parque central para decidir tu próximo destino.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_1":
        draw_text("Final 1: Encuentras un tesoro en la salida. Tu aventura ha sido recompensada con riquezas.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_2":
        draw_text("Final 2: El objeto es una reliquia antigua que te otorga sabiduría y poder.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_3":
        draw_text("Final 3: Evitas posibles peligros y encuentras una salida segura. La aventura continúa...\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_4":
        draw_text("Final 4: Sigues por la puerta y descubres un bar para pasarlo bien.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_5":
        draw_text("Final 5: Dejas el objeto y te vas a tu hotel, sintiendo que has hecho lo correcto.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_6":
        draw_text("Final 6: Sales por donde entraste y mejor vas a las iglesias, decidido a no arriesgarte más.\n1. Volver al menú principal", 100, height // 2)
    elif estado == "final_7":
        draw_text("Final 7: Encuentras otra salida que te lleva a un hermoso jardín secreto.\n1. Volver al menú principal", 100, height // 2)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
