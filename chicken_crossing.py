import pygame
import random
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize Pygame
try:
    pygame.init()
except Exception as e:
    logging.error(f"Failed to initialize Pygame: {e}")
    sys.exit(1)

WIDTH, HEIGHT = 800, 600
try:
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chicken Crossing Chaos")
except Exception as e:
    logging.error(f"Failed to create display: {e}")
    sys.exit(1)

clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Game settings
DIFFICULTIES = {
    "Easy": {"car_speed": 3, "car_count": 3},
    "Medium": {"car_speed": 5, "car_count": 4},
    "Hard": {"car_speed": 7, "car_count": 6}
}
COLOR_SCHEMES = {
    "Classic": {"background": BLACK, "chicken": WHITE},
    "Night": {"background": (20, 20, 50), "chicken": (200, 200, 255)},
    "Sunset": {"background": (255, 100, 100), "chicken": (255, 255, 200)}
}

# Game objects
class Chicken:
    def __init__(self, color):
        self.width = 40
        self.height = 40
        self.x = WIDTH // 2
        self.y = HEIGHT - 60
        self.speed = 5
        self.score = 0
        self.lives = 3
        self.color = color

    def draw(self):
        try:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.circle(screen, BLACK, (self.x + 10, self.y + 10), 5)  # Left eye
            pygame.draw.circle(screen, BLACK, (self.x + 30, self.y + 10), 5)  # Right eye
            pygame.draw.polygon(screen, YELLOW, 
                               [(self.x + 20, self.y + 20), (self.x + 20, self.y + 30), (self.x + 30, self.y + 25)])
        except Exception as e:
            logging.error(f"Error drawing chicken: {e}")

    def move(self, keys):
        try:
            if keys[pygame.K_LEFT] and self.x > 0:
                self.x -= self.speed
                logging.info("Cluck! Moving left!")
            if keys[pygame.K_RIGHT] and self.x < WIDTH - self.width:
                self.x += self.speed
                logging.info("Cluck! Moving right!")
            if keys[pygame.K_UP] and self.y > 0:
                self.y -= self.speed
                logging.info("Bawk! Up we go!")
            if keys[pygame.K_DOWN] and self.y < HEIGHT - self.height:
                self.y += self.speed
                logging.info("Squawk! Down we go!")
        except Exception as e:
            logging.error(f"Error moving chicken: {e}")

class Car:
    def __init__(self, x, y, speed):
        self.width = 60
        self.height = 30
        self.x = x
        self.y = y
        self.speed = speed
        self.color = random.choice([RED, GREEN, YELLOW])

    def draw(self):
        try:
            pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
            pygame.draw.circle(screen, BLACK, (self.x + 10, self.y + 30), 5)
            pygame.draw.circle(screen, BLACK, (self.x + 50, self.y + 30), 5)
        except Exception as e:
            logging.error(f"Error drawing car: {e}")

    def move(self):
        try:
            self.x += self.speed
            if self.x > WIDTH:
                self.x = -self.width
                self.y = random.randint(50, HEIGHT - 100)
                self.color = random.choice([RED, GREEN, YELLOW])
                logging.info("Honk! New car zooming in!")
            elif self.x < -self.width:
                self.x = WIDTH
                self.y = random.randint(50, HEIGHT - 100)
                self.color = random.choice([RED, GREEN, YELLOW])
                logging.info("Beep! Car coming from the other side!")
        except Exception as e:
            logging.error(f"Error moving car: {e}")

class Corn:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.x = random.randint(0, WIDTH - self.width)
        self.y = random.randint(50, HEIGHT - 100)

    def draw(self):
        try:
            pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))
            pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.width, self.y + self.height), 2)
        except Exception as e:
            logging.error(f"Error drawing corn: {e}")

# Font
try:
    font = pygame.font.SysFont("Arial", 24)
    title_font = pygame.font.SysFont("Arial", 48)
except Exception as e:
    logging.error(f"Error initializing font: {e}")
    sys.exit(1)

# Game variables
funny_messages = [
    "Why did the chicken join a band? It had the drumsticks!",
    "Chicken says: I'm no coward, but these cars are fowl!",
    "Corn collected! Time for a corny celebration!"
]

def setup(difficulty, color_scheme):
    global chicken, cars, corns, game_over, background_color, paused
    try:
        chicken = Chicken(COLOR_SCHEMES[color_scheme]["chicken"])
        car_speed = DIFFICULTIES[difficulty]["car_speed"]
        car_count = DIFFICULTIES[difficulty]["car_count"]
        cars = [Car(random.randint(0, WIDTH), random.randint(50, HEIGHT - 100), random.choice([-car_speed, car_speed])) for _ in range(car_count)]
        corns = [Corn() for _ in range(3)]
        game_over = False
        paused = False
        background_color = COLOR_SCHEMES[color_scheme]["background"]
        logging.info("Game started! Why did the chicken cross the road? Let's find out!")
    except Exception as e:
        logging.error(f"Error in setup: {e}")

def check_collision(rect1, rect2):
    try:
        return (rect1.x < rect2.x + rect2.width and
                rect1.x + rect1.width > rect2.x and
                rect1.y < rect2.y + rect2.height and
                rect1.y + rect1.height > rect2.y)
    except Exception as e:
        logging.error(f"Error in collision check: {e}")
        return False

def main_menu():
    selected_difficulty = "Medium"
    selected_color_scheme = "Classic"
    while True:
        screen.fill(BLACK)
        title_text = title_font.render("Chicken Crossing Chaos", True, WHITE)
        start_text = font.render("Press S to Start", True, WHITE)
        difficulty_text = font.render(f"Difficulty: {selected_difficulty} (D to change)", True, WHITE)
        color_text = font.render(f"Color Scheme: {selected_color_scheme} (C to change)", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 100))
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(difficulty_text, (WIDTH // 2 - difficulty_text.get_width() // 2, 350))
        screen.blit(color_text, (WIDTH // 2 - color_text.get_width() // 2, 400))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    return selected_difficulty, selected_color_scheme
                if event.key == pygame.K_d:
                    difficulties = list(DIFFICULTIES.keys())
                    current_idx = difficulties.index(selected_difficulty)
                    selected_difficulty = difficulties[(current_idx + 1) % len(difficulties)]
                if event.key == pygame.K_c:
                    color_schemes = list(COLOR_SCHEMES.keys())
                    current_idx = color_schemes.index(selected_color_scheme)
                    selected_color_scheme = color_schemes[(current_idx + 1) % len(color_schemes)]

def game_loop(difficulty, color_scheme):
    global game_over, background_color, paused
    setup(difficulty, color_scheme)
    running = True
    while running:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    logging.info("Quit event detected")
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p and not game_over:
                        paused = not paused
                        logging.info("Game paused" if paused else "Game resumed")

            keys = pygame.key.get_pressed()
            if not game_over and not paused:
                chicken.move(keys)

                # Move cars
                for car in cars:
                    car.move()

                # Check for collisions with cars
                chicken_rect = pygame.Rect(chicken.x, chicken.y, chicken.width, chicken.height)
                for car in cars:
                    car_rect = pygame.Rect(car.x, car.y, car.width, car.height)
                    if check_collision(chicken_rect, car_rect):
                        chicken.lives -= 1
                        chicken.x, chicken.y = WIDTH // 2, HEIGHT - 60
                        logging.info(f"Ouch! Chicken got flattened! Lives left: {chicken.lives}")
                        if chicken.lives <= 0:
                            game_over = True
                            logging.info("Game Over! The chicken's road trip is over!")

                # Check for corn collection
                for corn in corns:
                    corn_rect = pygame.Rect(corn.x, corn.y, corn.width, corn.height)
                    if check_collision(chicken_rect, corn_rect):
                        chicken.score += 10
                        if chicken.score == 1000:
                            logging.info("Cluck yeah! You've reached 1000 pints!")
                        corn.x, corn.y = random.randint(0, WIDTH - corn.width), random.randint(50, HEIGHT - 100)
                        logging.info(random.choice(funny_messages))

                # Random funny event
                if random.random() < 0.01:  # 1% chance per frame
                    logging.info("Surprise! A random pigeon flies by and steals a corn!")
                    corns.pop(0)
                    corns.append(Corn())
                    
                # check if chicken succesfully crossed the road
                if chicken.y <= 5:
                    chicken.score += 50
                    chicken.x, chicken.y = WIDTH // 2, HEIGHT - 60
                    logging.info("hooray! The chicken made it across! Bonus Points!!!")

            # Draw everything
            screen.fill(background_color)
            for car in cars:
                car.draw()
            for corn in corns:
                corn.draw()
            chicken.draw()

            # Draw HUD
            score_text = font.render(f"Score: {chicken.score}", True, WHITE)
            lives_text = font.render(f"Lives: {chicken.lives}", True, WHITE)
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (10, 40))
            if chicken.score >= 1000:
                text_1000 = font.render("1000 Points!", True, YELLOW)
                screen.blit(text_1000, (10,70))
            controls_text = font.render("Arrows: Move | P: Pause", True, WHITE)
            screen.blit(controls_text, (10, HEIGHT - 30))

            if paused:
                pause_text = title_font.render("Paused", True, WHITE)
                continue_text = font.render("Press C to Continue", True, WHITE)
                menu_text = font.render("Press M to Return to Menu", True, WHITE)
                screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2 - 100))
                screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2))
                screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 + 50))

                if keys[pygame.K_c]:
                    paused = False
                    logging.info("Game resumed")
                if keys[pygame.K_m]:
                    return True  # Return to menu

            if game_over:
                game_over_text = title_font.render("Game Over!", True, WHITE)
                restart_text = font.render("Press R to Restart", True, WHITE)
                menu_text = font.render("Press M to Return to Menu", True, WHITE)
                final_score_text = font.render(f"Final Score: {chicken.score}", True, WHITE)
                screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - 100))
                screen.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width() // 2, HEIGHT // 2 - 50))
                screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
                screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 + 50))

                if keys[pygame.K_r]:
                    setup(difficulty, color_scheme)
                if keys[pygame.K_m]:
                    return True  # Return to menu

            pygame.display.flip()
            clock.tick(FPS)

        except Exception as e:
            logging.error(f"Error in game loop: {e}")
            running = False

    return False

def main():
    while True:
        difficulty, color_scheme = main_menu()
        return_to_menu = game_loop(difficulty, color_scheme)
        if not return_to_menu:
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"Critical error in main: {e}")
        pygame.quit()
        sys.exit(1)