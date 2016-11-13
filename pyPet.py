import pygame, random, sys
from pygame.locals import *

#Animations
IDLE_EGG = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x418200,0x418200,0x400200,0x700600,0x3c0c00,0x1e0800,0x3ffc00,0x0),(0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x7e000,0x87000,0x103800,0x300c00,0x700400,0x400200,0x418200,0x418200,0x700600,0x3c0c00,0xffff00,0x0))
IDLE_BABY = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x78000,0xb4000,0x1fe000), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x78000,0xcc000,0x84000,0xb4000,0x84000,0x78000,0x0))
IDLE_MATURE = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xfc00,0x10200,0x24900,0x20100,0x23100,0x20100,0x20100,0x10200,0xfc00,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xfc00,0x10200,0x28500,0x23100,0x23100,0x20100,0x10200,0xfc00,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
SLEEP_BABY = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x78000,0xfc000,0x1fe000), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x1fe000,0x3ff000))
SLEEP_MATURE = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x3fc00,0x40200,0x80100), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x1f800,0x20400,0x40200,0x40200))
OVERLAY_ZZZ = ((0x0,0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_EAT = ((0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7700000,0xff00000,0xfd00000,0xff00000,0x7f00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7700000,0xfe00000,0xfc00000,0xfe00000,0x7f00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7400000,0xf800000,0xf800000,0xf800000,0x7c00000,0x7e00000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x7000000,0xf000000,0xe000000,0xe000000,0x7000000,0x7800000,0x3c00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x4000000,0x2000000,0x1000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_STINK = ((0x0,0x0,0x0,0x0,0x10000000,0x8000008,0x10000004,0xa000028,0x11000044,0xa000028,0x1000044,0x12000020,0x21000040,0x10000000,0x20000000,0x10000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x10000000,0x8000008,0x10000004,0xa000028,0x11000044,0xa000028,0x1000044,0x12000020,0x21000040,0x10000000,0x20000000,0x10000000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_DEAD = ((0x0,0x0,0xfc00000,0x1fe00000,0x1b600000,0x1fe00000,0xfc00000,0xfc00000,0x5400000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x7e00000,0xff00000,0xdb00000,0xff00000,0x7e00000,0x7e00000,0x2a00000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_EXCLAIM = ((0x0,0x20,0x70,0x70,0x70,0x70,0x70,0x70,0x70,0x20,0x0,0x20,0x70,0x20,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0), (0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0))
OVERLAY_CLEAN = ((0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2,0x2),)

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
SECOND = 1000
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 520

def bitor(current_frame, overlay_frame):
    l = []
    for i in range(32):
        b = current_frame[i] | overlay_frame[i]
        l.append(b)
    return tuple(l)

def get_bits(number, num_bits):
    """Solution from http://stackoverflow.com/questions/16659944/iterate-between-bits-in-a-binary-number"""
    return [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

def render_display(image_data, fg_color, bg_color, off=0, percv=None):
    for y in range(32):
        for x in range(off, 32+off):
            pygame.draw.rect(screen, bg_color, ((x-off)*10+32, y*10+64, 8, 8))
        bits = get_bits(image_data[y], 32+off)
        bits.reverse()
        for x, bit in enumerate(bits):
            if percv is not None:
                if bit or percv > 0 and y > 11 and x > 2 and y < 17 and x < 3 + percv:
                    pygame.draw.rect(screen, fg_color, ((x-off)*10+32, y*10+64, 8, 8))       
            if x < 32 and x >= off:            
                if bit:
                    pygame.draw.rect(screen, fg_color, ((x-off)*10+32, y*10+64, 8, 8))       
            
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

def do_random_event(pet):
    num = random.randint(0, 31)
    if num == 12:
        pet['hunger'] += 1
    elif num == 16:
        pet['energy'] -= 1
    elif num == 18:
        pet['energy'] += 1
    elif num == 20:
        pet['waste'] += 1
    elif num == 7:
        pet['happiness'] += 1
    elif num == 4:
        pet['happiness'] -= 1

def do_cycle(pet):
    do_random_event(pet)
    pet['hunger'] += 1
    pet['waste'] += 1
    pet['energy'] -= 1
    pet['age'] += 2
    if pet['waste'] >= WASTE_EXPUNGE:
        pet['happiness'] -= 1

def get_offset():
    return random.randint(-3, 2)

def get_next_frame(animation_frames, current_frame):
    return (current_frame + 1) % len(animation_frames)

def trigger_death(stage):
    if stage == 1:
        current_anim = SLEEP_BABY
    elif stage == 2:
        current_anim = SLEEP_MATURE
    overlay_anim = OVERLAY_DEAD
    return current_anim, overlay_anim, True, True

def trigger_sleep(stage):
    if stage == 1:
        current_anim = SLEEP_BABY
    elif stage == 2:
        current_anim = SLEEP_MATURE
    overlay_anim = OVERLAY_ZZZ
    return current_anim, overlay_anim, True, True

def update_page(spid):
    if spid == 0:
        stats_page = DISPLAY_HUNGER
    elif spid == 1:
        stats_page = DISPLAY_AGE
    elif spid == 2:
        stats_page = DISPLAY_WASTE
    elif spid == 3:
        stats_page = DISPLAY_ENERGY
    elif spid == 4:
        stats_page = DISPLAY_BACK
    return stats_page

def get_button_at_pixel(x, y): 
    if y > 420 and y < 484:
        button = 0
        for i in range(0, 288, 96):
            if x > 64 + i and x < 128 + i:
                return button
            else:
                button += 1
    return None

def render_buttons(left, top):
    for i in range(0, 288, 96):
        pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (left + i, top, 64, 64))
        pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (left + i + 4, top + 4, 56, 56))
        pygame.draw.ellipse(screen, PIXEL_COLOR, (left + i, top, 64, 64), 1)

def main():
    global screen, clock
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    pygame.display.set_caption('Tamagotchi')
    font = pygame.font.Font('assets/DejaVuSans.ttf', 12)
    selector_img = pygame.Surface((32, 32)).convert_alpha()
    render_component(selector_img, SELECTOR, PIXEL_COLOR, TRANSPARENT_COLOR)
    pygame.time.set_timer(USEREVENT + 1, SECOND)

    # Tamagotchi
    pet = {'hunger':0, 'energy':256, 'waste':0, 'age':0, 'happiness':0} 

    # Counters
    off = 0
    selid = 0
    spid = 0
    stage = 0
    frame = 0
    ol_frame = 0

    # Flags
    stats = False
    has_overlay = False
    cleaning = False
    eating = False
    stats = False
    sleeping = False
    dead = False
    update_game = False

    current_anim = IDLE_EGG
    overlay_anim = OVERLAY_ZZZ
    stats_page = DISPLAY_HUNGER

    # Game loop
    while True:
        screen.fill(BG_COLOR)
        render_buttons(64, 420)
        mousex = 0
        mousey = 0        

        # Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos 
            elif event.type == USEREVENT + 1:
                if cleaning:
                    pygame.time.set_timer(USEREVENT + 1, SECOND / 10)
                update_game = True
        
        # Buttons logic
        button = get_button_at_pixel(mousex, mousey)
        if button == 0:
            if stats:
                spid -= 1
                if spid <= -1:
                    spid = 4
                stats_page = update_page(spid)
            else:
                selid -= 1
                if selid <= -1:
                    selid = 3
        elif button == 1:
            if stage > 0 or selid == 2:
                if selid == 0:
                    eating = True
                    overlay_anim = OVERLAY_EAT
                    ol_frame = 0
                    has_overlay = True
                elif selid == 1:
                    cleaning = True
                    overlay_anim = OVERLAY_CLEAN
                    ol_frame = 0
                    has_overlay = True
                elif selid == 2:
                    stats = not stats
                elif selid == 3:
                    if pet['energy'] <= ENERGY_CANSLEEP:
                        current_anim, overlay_anim, sleeping, has_overlay = trigger_sleep(stage)
        elif button == 2:
            if stats:
                spid += 1
                spid %= 5
                stats_page = update_page(spid)
            else:
                selid += 1
                selid %= 4

        # Game logic
        if update_game:
            if stage == 0 and pet['age'] > AGE_HATCH:
                stage += 1
                current_anim = IDLE_BABY
                has_overlay = False
            if stage == 1 and pet['age'] > AGE_MATURE:
                stage += 1
                current_anim = IDLE_MATURE
            if eating and ol_frame == len(overlay_anim) - 1:
                eating = False
                has_overlay = False
                ol_frame = 0
                pet['hunger'] = 0
            if sleeping:
                pet['energy'] += 8
                if pet['energy'] >= 256:
                    sleeping = False
                    has_overlay = False
                    if stage == 0:
                        current_anim = IDLE_EGG
                    elif stage == 1:
                        current_anim = IDLE_BABY
                    elif stage == 2:
                        current_anim = IDLE_MATURE
            if cleaning:
                off -= 1
                if off == -33:
                    off = 0
                    cleanincr = 0
                    cleaning = False
                    has_overlay = False
                    pet['waste'] = 0
                    pygame.time.set_timer(USEREVENT + 1, SECOND)
            else:
                if not dead:
                    frame = get_next_frame(current_anim, frame)
                    off = get_offset()
                if not sleeping and not dead:
                        do_cycle(pet)
                if pet['energy'] < ENERGY_PASSOUT:
                    if stage > 0:
                        pet['happiness'] -= 64                  
                    current_anim, overlay_anim, sleeping, has_overlay = trigger_sleep(stage)
                        
            if not sleeping and not cleaning and not eating and not dead:
                if pet['waste'] >= WASTE_EXPUNGE:
                    overlay_anim = OVERLAY_STINK
                    has_overlay = True
                elif pet['energy'] <= ENERGY_TIRED or pet['hunger'] >= HUNGER_NEEDSTOEAT \
                                                   or pet['waste'] >= WASTE_EXPUNGE - WASTE_EXPUNGE / 3:
                    overlay_anim = OVERLAY_EXCLAIM
                    has_overlay = True
                if not dead:
                    if pet['hunger'] >= HUNGER_DEADFROMNOTEATING or pet['age'] >= AGE_DEATHFROMNATURALCAUSES:
                        off = 3
                        current_anim, overlay_anim, dead, has_overlay = trigger_death(stage)
            if has_overlay:
                ol_frame = get_next_frame(overlay_anim, ol_frame)
            update_game = False

        # Render components
        z = zip([FEED, FLUSH, HEALTH, ZZZ], [i for i in range(64, 320, 64)])
        for i in range(len(z)):
            img = pygame.Surface((32, 32))
            render_component(img, z[i][0], PIXEL_COLOR, NONPIXEL_COLOR)
            screen.blit(pygame.transform.flip(img, True, False), (z[i][1], 16))

        # Render selector
        screen.blit(pygame.transform.flip(selector_img, True, False), (64+(selid*64), 16))

        # Render display
        if stats:
            if spid == 0:
                percv = pet['hunger'] * 27 / HUNGER_NEEDSTOEAT
            elif spid == 1:
                percv = pet['age'] * 27 / AGE_DEATHFROMNATURALCAUSES
            elif spid == 2:
                percv = (pet['waste'] % WASTE_EXPUNGE) * 27 / WASTE_EXPUNGE
            elif spid == 3:
                percv = pet['energy'] * 27 / 256
            elif spid == 4:
                percv = None
            if percv > 27:
                percv = 27
            render_display(stats_page, PIXEL_COLOR, NONPIXEL_COLOR, 0, percv)
        else:
            if has_overlay:
                animation = bitor(current_anim[frame], overlay_anim[ol_frame])
            else:
                animation = current_anim[frame]
            render_display(animation, PIXEL_COLOR, NONPIXEL_COLOR, off)

        # Render debug
        surf = font.render('DEBUG --', True, PIXEL_COLOR)
        screen.blit(surf, (360, 60))
        debug = (('AGE: %s', 'HUNGER: %s', 'ENERGY: %s', 'WASTE: %d', 'HAPPINESS: %s'), \
                 ('age', 'hunger', 'energy', 'waste', 'happiness'))
        for pos, y in enumerate(i for i in range(70, 120, 10)):
            surf = font.render(debug[0][pos] % pet[debug[1][pos]], True, PIXEL_COLOR)
            screen.blit(surf, (360, y))            

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
