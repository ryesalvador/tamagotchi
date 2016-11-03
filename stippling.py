import pygame, sys

pygame.init()
screen = pygame.display.set_mode((500, 520), 0, 32)
pygame.display.set_caption('Stippling')

BG_COLOR = (160, 178, 129)
PIXEL_COLOR = (10, 12, 6)
NONPIXEL_COLOR = (156, 170, 125)
TRANSPARENT_COLOR = (0, 0, 0, 0)
BTN_BORDER_COLOR = (128, 12, 24)
BTN_CENTER_COLOR = (200, 33, 44)

screen.fill(BG_COLOR)

def get_bits(number, num_bits):
    return [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

def renderPixels(surface, image_data, fg_color, bg_color=(255, 255, 255)):
    """Returns none"""
    pixels = pygame.PixelArray(surface)
    for y in range(surface.get_height()):
        bits = get_bits(image_data[y], surface.get_width())
        for x, bit in enumerate(bits):
            if (bit):
                pixels[x][y] = fg_color
            else:
                pixels[x][y] = bg_color
    del pixels

selector_img = pygame.Surface((32, 32)).convert_alpha()
feed_img = pygame.Surface((32, 32))
flush_img = pygame.Surface((32, 32))
health_img = pygame.Surface((32, 32))
zzz_img = pygame.Surface((32, 32))

IDLE_EGG = ([0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x418200,0x418200,0x400200,0x700600,0x3c0c00,0x1e0800,0x3ffc00,0x0],[0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x400200,0x418200,0x418200,0x700600,0x3c0c00,0xffff00,0x0])
SELECTOR = [0x7800000f,0x60000003,0x40000001,0x40000001,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x40000001,0x40000001,0x60000003,0x7800000f]
FEED = [0x0,0x0,0x0,0x0,0x0,0x7805a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c07e0,0x7c07e0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x300180,0x0,0x0,0x0]
FLUSH = [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x2000000,0x5000000,0x5000000,0x4800000,0x4800000,0x4400000,0x4400000,0x4400000,0x2200000,0x2200000,0x1200000,0xffff00,0x1200280,0x11ffd00,0x1000080,0x1000080,0x1000080,0x1000080,0x1000080,0x1000080,0x1000040,0xffff80,0x0,0x0,0x0]
HEALTH = [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x3ffffc0,0xc000030,0x10912488,0x10912488,0x10492908,0x8000010,0x8000010,0x8000410,0x4000820,0x4001020,0x4002020,0x201c040,0x201c040,0x1ffff80,0x0,0x0,0x0]
ZZZ = [0x0,0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]

renderPixels(selector_img, SELECTOR, PIXEL_COLOR, TRANSPARENT_COLOR)
renderPixels(feed_img, FEED, PIXEL_COLOR, NONPIXEL_COLOR)
renderPixels(flush_img, FLUSH, PIXEL_COLOR, NONPIXEL_COLOR)
renderPixels(health_img, HEALTH, PIXEL_COLOR, NONPIXEL_COLOR)
renderPixels(zzz_img, ZZZ, PIXEL_COLOR, NONPIXEL_COLOR)

screen.blit(pygame.transform.flip(feed_img, True, False), (64, 16))
screen.blit(pygame.transform.flip(selector_img, True, False), (64, 16))
screen.blit(pygame.transform.flip(flush_img, True, False), (128, 16))
screen.blit(pygame.transform.flip(health_img, True, False), (192, 16))
screen.blit(pygame.transform.flip(zzz_img, True, False), (256, 16))

pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (64,420, 64, 64))
pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (68,424, 56, 56))
pygame.draw.ellipse(screen, PIXEL_COLOR, (64,420, 64, 64), 1)

pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (64+96,420, 64, 64))
pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (68+96,424, 56, 56))
pygame.draw.ellipse(screen, PIXEL_COLOR, (64+96,420, 64, 64), 1)

pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (64+192,420, 64, 64))
pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (68+192,424, 56, 56))
pygame.draw.ellipse(screen, PIXEL_COLOR, (64+192,420, 64, 64), 1)

for x in range(32):
    bits = get_bits(IDLE_EGG[0][x], 32)
    for y, bit in enumerate(bits):
        if (bit):
            pygame.draw.rect(screen, PIXEL_COLOR, (y*10+32, x*10+64, 8, 8))
        else:
            pygame.draw.rect(screen, NONPIXEL_COLOR, (y*10+32, x*10+64, 8, 8))
#for x in range(32):
#    for y in range(32):
        #bits = get_bits(IDLE_EGG[1][y], 32)
        #for r, bit in enumerate(bits):

pygame.display.flip()
pygame.time.wait(1000)

for x in range(32):
    bits = get_bits(IDLE_EGG[1][x], 32)
    for y, bit in enumerate(bits):
        if (bit):
            pygame.draw.rect(screen, PIXEL_COLOR, (y*10+32, x*10+64, 8, 8))
        else:
            pygame.draw.rect(screen, NONPIXEL_COLOR, (y*10+32, x*10+64, 8, 8))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    
