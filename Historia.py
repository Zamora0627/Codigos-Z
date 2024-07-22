import pygame
import sys

pygame.init()

# Configuración de la pantalla
width, height = 1800, 920
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Historia Interactiva")

# Colores
background_color = (0, 0, 0)
font_color = (255, 255, 255)

# Fuente
font = pygame.font.Font(None, 80)

# Estado inicial
estado = "inicio"

# Bucle principal
running = True
while running:
    screen.fill(background_color)  # Rellenar el fondo de la pantalla

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if estado == "inicio":
                    estado = "visitar_ruinas"
                elif estado == "ir_al_mercado":
                    estado = "comprar_jade"
            elif event.key == pygame.K_2:
                if estado == "inicio":
                    estado = "ir_al_mercado"
                elif estado == "visitar_ruinas":
                    estado = "volver_al_parque"
                elif estado == "ir_al_mercado":
                    estado = "preguntar_historias"
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

    # Lógica de estados y visualización
    if estado == "inicio":
        texto = font.render("Elige tu destino: 1. Visitar las ruinas (A1), 2. Ir al mercado (A2)", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "visitar_ruinas":
        texto = font.render("Visitas las ruinas. 1. Explorar túneles, 2. Volver al parque", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "ir_al_mercado":
        texto = font.render("Estás en el mercado. 1. Comprar jade, 2. Preguntar historias", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "explorar_tuneles":
        texto = font.render("Exploras los túneles. A. Seguir túneles, B. Salir y volver", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "comprar_jade":
        texto = font.render("Compras jade. A. Unirse al guía, B. Explorar por tu cuenta", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "explorar_cuenta":
        texto = font.render("Exploras por tu cuenta. A. Explorar oculto, B. Continuar", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "explorar_oculto":
        texto = font.render("Encuentras un objeto. A. Tomar, B. No tocar", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "seguir_tuneles":
        texto = font.render("Sigues los túneles y encuentras una salida. Final 1", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "tomar_objeto":
        texto = font.render("Tomas el objeto y encuentras algo valioso. Final 2", True, font_color)
        screen.blit(texto, (100, height // 2))
    elif estado == "no_tocar":
        texto = font.render("No tocas el objeto y sigues tu camino. Final 3", True, font_color)
        screen.blit(texto, (100, height // 2))

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
