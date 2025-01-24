import pygame

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.snake_position = [(100, 50), (90, 50), (80, 50)]
        self.snake_direction = 'RIGHT'
        self.food_position = (200, 50)
        self.score = 0
        self.game_over = False

    def change_direction(self, direction):
        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            self.snake_direction = direction

    def move_snake(self):
        head_x, head_y = self.snake_position[0]
        if self.snake_direction == 'UP':
            head_y -= 10
        elif self.snake_direction == 'DOWN':
            head_y += 10
        elif self.snake_direction == 'LEFT':
            head_x -= 10
        elif self.snake_direction == 'RIGHT':
            head_x += 10

        new_head = (head_x, head_y)
        self.snake_position.insert(0, new_head)

        if new_head == self.food_position:
            self.score += 1
            self.place_food()
        else:
            self.snake_position.pop()

        self.check_collision()

    def place_food(self):
        import random
        self.food_position = (random.randint(0, 39) * 10, random.randint(0, 29) * 10)

    def check_collision(self):
        head = self.snake_position[0]
        if head in self.snake_position[1:] or not (0 <= head[0] < 400 and 0 <= head[1] < 300):
            self.game_over = True

    def get_state(self):
        return {
            'snake_position': self.snake_position,
            'food_position': self.food_position,
            'score': self.score,
            'game_over': self.game_over
        }

    def update(self):
        self.move_snake()

    def render(self):
        self.screen.fill((0, 0, 0))
        for pos in self.snake_position:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))