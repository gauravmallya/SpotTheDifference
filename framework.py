import pygame

def grid(window, size, rows):
    distanceBtwRows = size // rows
    x = 0
    y = 0
    for _ in range(rows):
        x+=distanceBtwRows
        y+=distanceBtwRows

        pygame.draw.line(window, (0,0,0), (x,0), (x,size))
        pygame.draw.line(window, (0,0,0), (0,y), (size, y))

def redraw(window):
    global size, rows
    window.fill((255, 255, 255))
    grid(window, size, rows)
    pygame.display.update()

def main():
    global size, rows
    size = 500
    rows = 4
    window = pygame.display.set_mode((size,size))

    play = True

    while play: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        redraw(window)

main()