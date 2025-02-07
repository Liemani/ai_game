import pygame

class Game:
    """
    Snake 게임의 로직과 상태를 관리하는 클래스입니다.
    """

    def __init__(self, screen):
        """
        Game 클래스의 생성자입니다.
        
        매개변수:
            screen (pygame.Surface): 게임이 렌더링될 화면 객체
        """
        self.screen = screen
        self.snake_position = [(100, 50), (90, 50), (80, 50)]
        self.snake_direction = 'RIGHT'
        self.food_position = (200, 50)
        self.score = 0
        self.game_over = False

    def change_direction(self, direction):
        """
        뱀의 이동 방향을 변경합니다.
        
        매개변수:
            direction (str): 변경할 방향 ('UP', 'DOWN', 'LEFT', 'RIGHT')
        """
        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            self.snake_direction = direction

    def move_snake(self):
        """
        뱀을 현재 방향으로 이동시킵니다.
        음식과 충돌하면 점수를 증가시키고, 그렇지 않으면 꼬리를 제거합니다.
        충돌 여부를 확인합니다.
        """
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
        """
        화면 내의 임의의 위치에 음식을 배치합니다.
        """
        import random
        self.food_position = (random.randint(0, 39) * 10, random.randint(0, 29) * 10)

    def check_collision(self):
        """
        뱀의 머리가 몸통이나 화면 경계와 충돌했는지 확인합니다.
        충돌 시 게임 오버 상태로 설정합니다.
        """
        head = self.snake_position[0]
        if head in self.snake_position[1:] or not (0 <= head[0] < 400 and 0 <= head[1] < 300):
            self.game_over = True

    def get_state(self):
        """
        게임의 현재 상태를 반환합니다.
        
        반환값:
            dict: 뱀의 위치, 음식의 위치, 점수, 게임 오버 상태를 포함하는 딕셔너리
        """
        return {
            'snake_position': self.snake_position,
            'food_position': self.food_position,
            'score': self.score,
            'game_over': self.game_over
        }

    def update(self):
        """
        게임 상태를 업데이트합니다.
        """
        self.move_snake()

    def render(self):
        """
        현재 게임 상태를 화면에 렌더링합니다.
        """
        self.screen.fill((0, 0, 0))
        for pos in self.snake_position:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.food_position[0], self.food_position[1], 10, 10))