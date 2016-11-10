import pygame, random, sys
from pygame.locals import *

#Animations
IDLE_EGG = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x418200,0x418200,0x400200,0x700600,0x3c0c00,0x1e0800,0x3ffc00,0x0),(0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x400200,0x418200,0x418200,0x700600,0x3c0c00,0xffff00,0x0))
IDLE_BABY = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x78000,0xb4000,0x1fe000), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x78000,0xcc000,0x84000,0xb4000,0x84000,0x78000,0x0))
IDLE_MATURE = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xfc00,0x10200,0x24900,0x20100,0x23100,0x20100,0x20100,0x10200,0xfc00,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xfc00,0x10200,0x28500,0x23100,0x23100,0x20100,0x10200,0xfc00,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_ZZZ = ((0x0,0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_EAT = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7700000,0xff00000,0xfd00000,0xff00000,0x7f00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7700000,0xfe00000,0xfc00000,0xfe00000,0x7f00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7400000,0xf800000,0xf800000,0xf800000,0x7c00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7000000,0xf000000,0xe000000,0xe000000,0x7000000,0x7800000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x1000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_STINK = ((0x0,0x0,0x0,0x0,0x10000000,0x8000008,0x10000004,0xa000028,0x11000044,0xa000028,0x1000044,0x12000020,0x21000040,0x10000000,0x20000000,0x10000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x10000000,0x8000008,0x10000004,0xa000028,0x11000044,0xa000028,0x1000044,0x12000020,0x21000040,0x10000000,0x20000000,0x10000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_DEAD = ((0x0,0x0,0xfc00000,0x1fe00000,0x1b600000,0x1fe00000,0xfc00000,0xfc00000,0x5400000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x7e00000,0xff00000,0xdb00000,0xff00000,0x7e00000,0x7e00000,0x2a00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_EXCLAIM = ((0x0,0x20,0x70,0x70,0x70,0x70,0x70,0x70,0x70,0x20,0x0,0x20,0x70,0x20,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_CLEAN = (0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2)

#Components
SELECTOR = (0x7800000f,0x60000003,0x40000001,0x40000001,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x40000001,0x40000001,0x60000003,0x7800000f)
FEED = (0x0,0x0,0x0,0x0,0x0,0x7805a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c05a0,0x7c07e0,0x7c07e0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x7803c0,0x300180,0x0,0x0,0x0)
FLUSH = (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x2000000,0x5000000,0x5000000,0x4800000,0x4800000,0x4400000,0x4400000,0x4400000,0x2200000,0x2200000,0x1200000,0xffff00,0x1200280,0x11ffd00,0x1000080,0x1000080,0x1000080,0x1000080,0x1000080,0x1000080,0x1000040,0xffff80,0x0,0x0,0x0)
HEALTH = (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x3ffffc0,0xc000030,0x10912488,0x10912488,0x10492908,0x8000010,0x8000010,0x8000410,0x4000820,0x4001020,0x4002020,0x201c040,0x201c040,0x1ffff80,0x0,0x0,0x0)
ZZZ = (0x0,0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)
DISPLAY_HUNGER = (0x0,0x0,0x3bcc94a4,0x4852b4a4,0x39c2d4bc,0x485a94a4,0x4bdc9324,0x0,0x0,0x0,0x0,0x1ffffff8,0x20000004,0x20000004,0x20000004,0x20000004,0x20000004,0x1ffffff8,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)
DISPLAY_ENERGY = (0x0,0x0,0x498ef4bc,0x4a521584,0x704e368c,0x43521484,0x3b92f4bc,0x0,0x0,0x0,0x0,0x1ffffff8,0x20000004,0x20000004,0x20000004,0x20000004,0x20000004,0x1ffffff8,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)
DISPLAY_WASTE = (0x0,0x0,0x7df38e44,0x4405144,0x1c439f44,0x4441154,0x7c439128,0x0,0x0,0x0,0x0,0x1ffffff8,0x20000004,0x20000004,0x20000004,0x20000004,0x20000004,0x1ffffff8,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)
DISPLAY_AGE = (0x0,0x0,0x7ce38,0x5144,0x1c17c,0x5944,0x7de44,0x0,0x0,0x0,0x0,0x1ffffff8,0x20000004,0x20000004,0x20000004,0x20000004,0x20000004,0x1ffffff8,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)
DISPLAY_BACK = (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x498c710,0x2a52918,0x185e77c,0x2a52918,0x4992710,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0)

AGE_HATCH = 128
AGE_MATURE = 796
AGE_DEATHFROMNATURALCAUSES = 8192
HUNGER_CANEAT = 32
HUNGER_NEEDSTOEAT = 128
HUNGER_SICKFROMNOTEATING = 256
HUNGER_DEADFROMNOTEATING = 512
ENERGY_CANSLEEP = 150
ENERGY_TIRED = 64
ENERGY_PASSOUT = 8
WASTE_EXPUNGE = 256

BG_COLOR = (160, 178, 129)
PIXEL_COLOR = (10, 12, 6)
NONPIXEL_COLOR = (156, 170, 125)
TRANSPARENT_COLOR = (0, 0, 0, 0)
BTN_BORDER_COLOR = (128, 12, 24)
BTN_CENTER_COLOR = (200, 33, 44)

FPS = 30
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 520

def get_bits(number, num_bits):
    """Solution from http://stackoverflow.com/questions/16659944/iterate-between-bits-in-a-binary-number"""
    return [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

def render_component(surface, image_data, fg_color, bg_color=(255, 255, 255)):
    pixels = pygame.PixelArray(surface)
    for y in range(surface.get_height()):
        bits = get_bits(image_data[y], surface.get_width())
        for x, bit in enumerate(bits):
            if (bit):
                pixels[x][y] = fg_color
            else:
                pixels[x][y] = bg_color
    del pixels

def render_display(image_data, fg_color, bg_color, off=0):
    for y in range(32):
        bits = get_bits(image_data[y], 32+off)
        bits.reverse()
        for x, bit in enumerate(bits):
            color = bg_color
            if x < abs(off) and off < 0:
                pygame.draw.rect(screen, color, (x*10+32, y*10+64, 8, 8))

            if x < 32 and x >= off:            
                if (bit):
                    color = fg_color
                pygame.draw.rect(screen, color, ((x-off)*10+32, y*10+64, 8, 8))

            elif x >= 32 and x < len(bits):
                pygame.draw.rect(screen, color, ((x-off)*10+32, y*10+64, 8, 8))        
            
def render_buttons(left, top):
    for i in range(0, 288, 96):
        pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (left + i, top, 64, 64))
        pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (left + i + 4, top + 4, 56, 56))
        pygame.draw.ellipse(screen, PIXEL_COLOR, (left + i, top, 64, 64), 1)

def get_button_at_pixel(x, y): 
    if y > 420 and y < 484:
        button = 0
        for i in range(0, 288, 96):
            if x > 64 + i and x < 128 + i:
                return button
            else:
                button += 1
    return None   

def main():
    global screen, clock
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('TamagotchiPy')
    screen.fill(BG_COLOR)
    pygame.key.set_repeat(100, 5)
    pygame.font.init()

    hunger = 0
    energy = 0
    waste = 0
    age = 0
    happiness = 0

    off = 0
    selid = 0
    spid = 0
    cleanincr = 0

    stats = False
    has_overlay_animation = False

    current_animation = IDLE_EGG
    overlay_animation = OVERLAY_ZZZ
    stats_page = DISPLAY_HUNGER

    render_display(current_animation[0], PIXEL_COLOR, NONPIXEL_COLOR, off)
    render_buttons(64, 420)

    while True:
        mousex = 0
        mousey = 0        

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos      

        button = get_button_at_pixel(mousex, mousey)

        if button == 0:
            if stats:
                pass
            else:
                selid -= 1
                if selid <= -1:
                    selid = 3
        elif button == 1:
            pass
        elif button == 2:
            if stats:
                pass
            else:
                selid += 1
                selid %= 4

        z = zip([FEED, FLUSH, HEALTH, ZZZ], [i for i in range(64, 320, 64)])
        for i in range(len(z)):
            img = pygame.Surface((32, 32))
            render_component(img, z[i][0], PIXEL_COLOR, NONPIXEL_COLOR)
            screen.blit(pygame.transform.flip(img, True, False), (z[i][1], 16))

        selector_img = pygame.Surface((32, 32)).convert_alpha()
        render_component(selector_img, SELECTOR, PIXEL_COLOR, TRANSPARENT_COLOR)
        screen.blit(pygame.transform.flip(selector_img, True, False), (64+(selid*64), 16))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
