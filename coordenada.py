import pyautogui
import time

# Aguarde 4 segundos antes de obter a posição do cursor do mouse
time.sleep(4)

# Obtenha a posição atual do cursor do mouse
posicao_mouse = pyautogui.position()

# Exiba a coordenada x e y do cursor do mouse
print(f"A posição atual do cursor do mouse é: x = {posicao_mouse.x}, y = {posicao_mouse.y}")
