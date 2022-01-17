from operator import truediv
import pygame
import random
import time


class Ball:
    def __init__(self, display):
        self.display = display
        self.color = pygame.Color('red')
        self.center_x = 100
        self.center_y = 100
        self.radius = 30

        self.vx = 2
        self.vy = 2

    def show(self):
        pygame.draw.circle(self.display, self.color,
                           (self.center_x, self.center_y), self.radius)

    def go(self):

        self.center_x += self.vx
        self.center_y += self.vy

    def clear(self):
        pygame.draw.circle(self.display, pygame.Color(
            'white'), (self.center_x, self.center_y), self.radius)

    def move(self):
        self.clear()
        self.go()
        self.show()

    def stop(self):
        self.vx = 0
        self.vy = 0

    def get_coords(self):
        x = self.center_x
        y = self.center_y
        radius = self.radius
        return x, y, radius

    def show_speed(self):
        return self.vx, self.vy


class RandomPointBall(Ball):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('Green')

        width, height = display.get_size()
        self.center_x = random.randint(self.radius, width - self.radius)
        self.center_y = random.randint(self.radius, height - self.radius)


class PointBall(Ball):
    def __init__(self, display, x, y):
        super().__init__(display)
        self.color = pygame.Color('yellow')
        self.center_x = x
        self.center_y = y


class RandomPointMovableBall(RandomPointBall):
    def __init__(self, display):
        super().__init__(display)
        speed_array = [-3, -2, -1, 1, 2, 3]
        self.vx = speed_array[random.randint(0, len(speed_array)-1)]
        self.vy = speed_array[random.randint(0, len(speed_array)-1)]


class BilliardBall(RandomPointMovableBall):
    def __init__(self, display):
        super().__init__(display)
        self.color = pygame.Color('red')

    def go(self):
        super().go()
        width, height = self.display.get_size()
        if self.center_x <= self.radius or self.center_x >= width - self.radius:
            self.vx = -self.vx
        if self.center_y <= self.radius or self.center_y >= height - self.radius:
            self.vy = -self.vy


def show_text(display, text, x, y):
    pygame.font.init()
    font = pygame.font.Font(None, 48)
    text = font.render(text, True,  (0, 128, 0))
    text_field = text.get_rect()
    text_field.center = (x, y)
    display.blit(text, text_field)


def is_in_circle(mouse_x, mouse_y, ball_x, ball_y, ball_radius):

    if (mouse_x - ball_x)**2 / ball_radius**2 + (mouse_y - ball_y)**2 / ball_radius**2 < 1:
        return True
    else:
        return False


def is_in_field(ball_coord_x, ball_coord_y, width, height):
    if ball_coord_x > width - 30 or ball_coord_x < 30 or ball_coord_y > height - 30 or ball_coord_y < 30:
        return False
    else:
        return True


def run_game():
    pygame.init()

    width = 1000
    height = 800
    display = pygame.display.set_mode((width, height))
    display.fill(pygame.Color('white'))
    balls_caught_counter = 0
    cnt_left_border = 0
    cnt_top_border = 0
    cnt_right_border = 0
    cnt_bottom_border = 0

    balls = []
    for i in range(10):
        ball = BilliardBall(display)
        ball.show()
        balls.append(ball)
    pygame.display.flip()

    time.sleep(1)
    run = True
    clock = pygame.time.Clock()
    while run:
        display.fill(pygame.Color('white'))
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                run = not run
            if event.type == pygame.MOUSEBUTTONDOWN:
                for ball in balls:
                    display.fill(pygame.Color('white'))
                    pygame.display.flip()
                    mouse_position = pygame.mouse.get_pos()
                    mouse_position_x = mouse_position[0]
                    mouse_position_y = mouse_position[1]
                    ball_coords = ball.get_coords()
                    ball_coord_x = ball_coords[0]
                    ball_coord_y = ball_coords[1]
                    if is_in_circle(mouse_position_x, mouse_position_y, ball_coord_x, ball_coord_y, 30) and is_in_field(ball_coord_x, ball_coord_y, width, height):
                        ball.stop()
                        # if ball_coord_x > width - 30 or ball_coord_x < 30 or ball_coord_y > height - 30 or ball_coord_y < 30:
                        balls_caught_counter += 1
            show_text(display, str(balls_caught_counter), 30, 30)
        for ball in balls:
            ball.move()
        for ball in balls:
            ball_coords = ball.get_coords()
            ball_coord_x = ball_coords[0]
            ball_coord_y = ball_coords[1]
            ball_radius = ball_coords[2]
            if ball_coord_x <= ball_radius:
                cnt_left_border += 1
            show_text(display, 'left: '+str(cnt_left_border), 100, 500)
            if ball_coord_x >= width - ball_radius:
                cnt_right_border += 1
            show_text(display, 'right: '+str(cnt_right_border), 900, 500)
            if ball_coord_y <= ball_radius:
                cnt_top_border += 1
            show_text(display, 'top: ' + str(cnt_top_border), 500, 100)
            if ball_coord_y >= height - ball_radius:
                cnt_bottom_border += 1
            show_text(display, 'bottom: ' + str(cnt_bottom_border), 500, 700)
        pygame.display.flip()
        clock.tick(60)


run_game()
