import pygame
from sys import exit
import os

win_x = 720
win_y = 720

def draw():
    win.fill((135, 206, 235))
    win.blit(tanah, (tanahX, tanahY))
    win.blit(player.image, player)

#tanah
tanah = pygame.image.load(r"D:\Belajar\BelajarPython\pygame\img game 1\objek\tanah.jpeg")
tanah = pygame.transform.scale(tanah, (720, 300))
tanahX= 0
tanahY= 420

player_kanan = pygame.image.load(r"D:\Belajar\BelajarPython\pygame\img game 1\player\09_karakter_biru_1_kanan.png")
player_kiri = pygame.image.load(r"D:\Belajar\BelajarPython\pygame\img game 1\player\09_karakter_biru_1_kiri.png")
p_width = 24
p_height = 29
px = win_x/2
py = tanahY - 10
bottom = tanahY- 10

lompatY = 0
lompat = -10
gravitasi = 0.5

gerak= 5

class player(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, px, py, p_width, p_height)
        self.image_kanan = player_kanan
        self.image_kiri = player_kiri
        self.image = self.image_kanan

player =  player()
pygame.init()
win = pygame.display.set_mode((win_x, win_y))
pygame.display.set_caption("Si Biji Biru")
fps = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tombol = pygame.key.get_pressed()
    if tombol[pygame.K_LEFT] or tombol[pygame.K_a]:
        player.x -= gerak
        player.image = player_kiri
    if tombol[pygame.K_RIGHT] or tombol[pygame.K_d]:
        player.x += gerak
        player.image = player_kanan
    if tombol[pygame.K_SPACE] or tombol[pygame.K_w]:
        lompatY = lompat

    #lompat
    lompatY += gravitasi
    player.y += lompatY
    if player.bottom >= tanahY:
        player.bottom = tanahY
        kecepatan_y = 0

    draw()
    pygame.display.update()
    fps.tick(60)