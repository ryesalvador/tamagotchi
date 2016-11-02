import pygame

pygame.init()
screen = pygame.display.set_mode((100, 100), 0, 32)
pygame.display.set_caption('Stippling')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen.fill(WHITE)


NUM_BITS = 32

def get_bits(number, num_bits):
    return [(number >> bit) & 1 for bit in range(num_bits - 1, -1, -1)]

zzz_img = pygame.Surface((32, 32))

ZZZ = [0x0,0x0,0x0,0x0,0xf800000,0x4000000,0x2000000,0x1000000,0xf800000,0x0,0x0,0x3c00000,0x1000000,0x800000,0x3c00000,0x0,0x700000,0x200000,0x700000,0x0,0x80000,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0]


pixels = pygame.PixelArray(zzz_img)
for y in range(32):
    bits = get_bits(ZZZ[y], NUM_BITS)
    for x, bit in enumerate(bits):
        if (bit):
            pixels[x][y] = BLACK
        else:
            pixels[x][y] = GREEN
del pixels

screen.blit(zzz_img, (10, 10))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    
