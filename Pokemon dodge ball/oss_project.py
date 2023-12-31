import pygame
import random


class Character:

    def __init__(self):
        self.image_path = ''
        self.character_image = \
            pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5
        self.score = 0

    def set_speed(self):
        pass

    def stop_ball(self):
        pass

    def reset_game(self):
        pass

    def increase_score(self):
        self.score += 1


class Pikachu(Character):
    def __init__(self):
        self.score = 0
        self.image_path = 'pikachu.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5

    def set_speed(self):
        self.speed = 10


class Pyree(Character):
    def __init__(self):
        self.score = 0
        self.image_path = 'pyree.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5

    def stop_ball(self, screen, ball_image, size, skill_count):
        balls = []
        font = pygame.font.Font('NanumGothic.ttf', 30)
        text = font.render("!공이 일시적으로 사라집니다!", True, (255, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 4 * text.get_height()))
        text = font.render(f"* 남은 스킬 사용 횟수는 {skill_count}번 입니다 *", True, (255, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 2 * text.get_height()))
        pygame.display.flip()
        pygame.time.delay(1000)
        balls = balls_init(ball_image, size)
        balls = gen_balls(balls, ball_image, size)
        return balls


class Kkobugi(Character):
    def __init__(self):
        self.score = 0
        self.image_path = 'kkobugi.png'
        self.character_image = pygame.transform.scale(pygame.image.load(self.image_path), (120, 120))
        self.speed = 5

    def reset_game(self, screen, ball_image, size, count):
        balls = []
        font = pygame.font.Font('NanumGothic.ttf', 30)
        text = font.render(f"!목숨이 {count}번 남았습니다!", True, (255, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 3 * text.get_height()))
        pygame.display.flip()
        pygame.time.delay(1000)
        balls = balls_init(ball_image, size)
        balls = gen_balls(balls, ball_image, size)
        return balls


def balls_init(ball_image, size):
    random.seed()
    balls = []
    for _ in range(5):
        if len(balls) >= 6:
            break
        rect = pygame.Rect(ball_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(3, 9)
        balls.append({'rect': rect, 'dy': dy})
    return balls


def gen_balls(balls, ball_image, size):
    for ball in balls:
        ball['rect'].top += ball['dy']
        if ball['rect'].top > size[1]:
            balls.remove(ball)
            rect = pygame.Rect(ball_image.get_rect())
            rect.left = random.randint(0, size[0])
            rect.top = -100
            dy = random.randint(3, 9)
            balls.append({'rect': rect, 'dy': dy})
    return balls


def coins_init(coin_image, size):
    random.seed()
    coins = []
    for _ in range(5):
        if len(coins) >= 6:
            break
        rect = pygame.Rect(coin_image.get_rect())
        rect.left = random.randint(0, size[0])
        rect.top = -100
        dy = random.randint(2, 6)
        coins.append({'rect': rect, 'dy': dy})
    return coins


def gen_coins(coins, coin_image, size):
    for coin in coins:
        coin['rect'].top += coin['dy']
        if coin['rect'].top > size[1]:
            coins.remove(coin)
            rect = pygame.Rect(coin_image.get_rect())
            rect.left = random.randint(0, size[0])
            rect.top = -100
            dy = random.randint(2, 6)
            coins.append({'rect': rect, 'dy': dy})
    return coins

def game_lose(balls, screen, background_image, size):
    balls = []
    screen.blit(background_image, (0, 0))
    font = pygame.font.Font('NanumGothic.ttf', 50)
    text = font.render("!Game Over!", True, (255, 0, 0))
    screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 3 * text.get_height()))
    pygame.display.flip()
    pygame.time.delay(1000)
    done = True
    return balls, done

def game_win(screen, size):
    font = pygame.font.Font('NanumGothic.ttf', 50)
    win_text = font.render("!Win!", True, (255, 0, 0))
    screen.blit(win_text, (size[0] // 2 - win_text.get_width() // 2, size[1] // 2 - win_text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(1000)
    return True

def runGame():
    pygame.init()

    size = [600, 700]
    screen = pygame.display.set_mode(size)

    done = False
    clock = pygame.time.Clock()

    background_image = pygame.image.load('background.png')
    background_image = pygame.transform.scale(background_image, (size[0], size[1]))
    screen.blit(background_image, (0, 0))

    ball_image = pygame.image.load('ball.png')
    ball_image = pygame.transform.scale(ball_image, (50, 50))
    balls = balls_init(ball_image, size)
    life_count = 3
    skill_count = 5

    coin_image = pygame.image.load('coin.png')
    coin_image = pygame.transform.scale(coin_image, (50, 50))
    coins = coins_init(coin_image, size)

    selected_character = None
    while selected_character is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_character = "pikachu"
                    pikachu = Pikachu()
                    pikachu.set_speed()
                    speed = pikachu.speed
                    character = pygame.Rect(pikachu.character_image.get_rect())
                elif event.key == pygame.K_2:
                    selected_character = "pyree"
                    pyree = Pyree()
                    speed = pyree.speed
                    character = pygame.Rect(pyree.character_image.get_rect())
                elif event.key == pygame.K_3:
                    selected_character = "kkobugi"
                    kkobugi = Kkobugi()
                    speed = kkobugi.speed
                    character = pygame.Rect(kkobugi.character_image.get_rect())

        font = pygame.font.Font('NanumGothic.ttf', 30)
        text = font.render("!번호를 입력하여 캐릭터를 선택하세요!", True, (255, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 7 * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 25)
        text = font.render("1. 피카츄 \t   2. 파이리 \t   3. 꼬부기", True, (0, 0, 255))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 6 * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 20)
        text = font.render("--------------  캐릭터 설명  ---------------", True, (0, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 5 * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 20)
        text = font.render("피카츄:\t\t공을 피하는 속도가 2배 빠릅니다.", True, (0, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 3 * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 20)
        text = font.render("파이리:\t\t엔터키를 누르면 공이 일시적으로 사라집니다. (5번 가능)", True, (0, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 -1  * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 20)
        text = font.render("꼬부기:\t\t공을 3번 맞아야 게임이 종료됩니다. (목숨 3개)", True, (0, 0, 0))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 + 1 * text.get_height()))
        font = pygame.font.Font('NanumGothic.ttf', 25)
        text = font.render("* 포켓볼을 피하며 15개의 코인을 모으면 승리 *", True, (255, 201, 57))
        screen.blit(text, (size[0] // 2 - text.get_width() // 2, size[1] // 2 + 3 * text.get_height()))

        pygame.display.flip()
        clock.tick(30)

    character_dx = 0
    character.left = size[0] // 2 - character.width // 2
    character.top = size[1] - character.height
    
    IGNORE_KEY_EVENTS = pygame.USEREVENT + 1  # 사용자 지정 이벤트 생성
    ignore_key_events = False
    
    while not done:
        clock.tick(30)
        screen.blit(background_image, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                break
            elif event.type == IGNORE_KEY_EVENTS:
                ignore_key_events = False
            elif event.type == pygame.KEYDOWN:
                if ignore_key_events:
                    continue
                if event.key == pygame.K_LEFT:
                    character_dx = -speed
                elif event.key == pygame.K_RIGHT:
                    character_dx = speed
            elif event.type == pygame.KEYUP:
                if ignore_key_events:
                    continue
                if event.key == pygame.K_LEFT:
                    character_dx = 0
                elif event.key == pygame.K_RIGHT:
                    character_dx = 0

        balls = gen_balls(balls, ball_image, size)
        coins = gen_coins(coins, coin_image, size)

        character.left = character.left + character_dx
        if character.left < 0:
            character.left = 0
        elif character.left > size[0] - character.width:
            character.left = size[0] - character.width

        if selected_character == "pikachu":
            screen.blit(pikachu.character_image, character)
        elif selected_character == "pyree":
            screen.blit(pyree.character_image, character)
        elif selected_character == "kkobugi":
            screen.blit(kkobugi.character_image, character)

        font = pygame.font.Font('NanumGothic.ttf', 30)
        if selected_character == "pikachu":
            score_text = font.render(f"Score: {pikachu.score}", True, (255, 0, 0))
        elif selected_character == "pyree":
            score_text = font.render(f"Score: {pyree.score}", True, (255, 0, 0))
        elif selected_character == "kkobugi":
            score_text = font.render(f"Score: {kkobugi.score}", True, (255, 0, 0))

        screen.blit(score_text, (10, 10))

        for ball in balls:
            if selected_character == "pyree":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if skill_count >= 1:
                            pygame.time.set_timer(IGNORE_KEY_EVENTS, 1000)  # 1초동안 모든 키 입력 무시
                            ignore_key_events = True
                            skill_count -= 1
                            balls = pyree.stop_ball(screen, ball_image, size, skill_count)
                            break
                        else:
                            font = pygame.font.Font('NanumGothic.ttf', 50)
                            text = font.render("!사용 초과!", True, (255, 0, 0))
                            screen.blit(text,
                                        (size[0] // 2 - text.get_width() // 2, size[1] // 2 - 3 * text.get_height()))
                            pygame.display.flip()
                            pygame.time.delay(100)
                            break
            if ball['rect'].colliderect(character):
                if (selected_character == "kkobugi") and (life_count >= 2):
                    screen.blit(background_image, (0, 0))
                    life_count -= 1
                    balls = kkobugi.reset_game(screen, ball_image, size, life_count)
                    break
                else:
                    balls, done = game_lose(balls, screen, background_image, size)
                    break
            screen.blit(ball_image, ball['rect'])

        for coin in coins:
            coin['rect'].top += coin['dy']
            if coin['rect'].top > size[1] or coin['rect'].colliderect(character):
                if coin['rect'].colliderect(character):
                    coins.remove(coin)
                    if selected_character == "pikachu":
                        pikachu.increase_score()
                        if pikachu.score >= 15:
                            done = game_win(screen, size)
                    elif selected_character == "pyree":
                        pyree.increase_score()
                        if pyree.score >= 15:
                            done = game_win(screen, size)
                    elif selected_character == "kkobugi":
                        kkobugi.increase_score()
                        if kkobugi.score >= 15:
                            done = game_win(screen, size)

                rect = pygame.Rect(coin_image.get_rect())
                rect.top = -100
                dy = random.randint(3, 9)
                
                while True:
                    rect.left = random.randint(0, size[0])
                    if not rect.colliderect(character):
                        break
                coins.append({'rect': rect, 'dy': dy})

            screen.blit(coin_image, coin['rect'])

        pygame.display.update()

runGame()
pygame.quit()