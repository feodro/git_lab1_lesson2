def main():
    import pygame
    try:
        size = [int(i) for i in input().split()]
        if len(size) != 2:
            raise Exception
    except Exception:
        print('Неправильный формат ввода')
        return
    pygame.init()
    pygame.display.set_caption('Крест')
    screen = pygame.display.set_mode(size)
    screen.fill((95, 127, 122))
    pygame.draw.line(screen, (255, 255, 255), (0, 0), size, width=5)
    pygame.draw.line(screen, (255, 255, 255), (size[0], 0), (0, size[1]), width=5)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()