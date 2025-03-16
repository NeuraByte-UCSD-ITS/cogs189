# +
import pygame
import random
import time

#initialize pygame
pygame.init()

#setting display dimensions
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("OpenVEP-SSVEP Data Collection & FBTRCA Model Application Visualization")

#defining colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

#defining position of squares (cross layout)
square_size = 100
square_positions = {
    0: (WIDTH//2 - square_size//2, HEIGHT//2 - 150),  #top (8 Hz)
    1: (WIDTH//2 - square_size//2, HEIGHT//2 + 50),   #bottom (10 Hz)
    2: (WIDTH//2 - 150, HEIGHT//2 - square_size//2),  #left (12 Hz)
    3: (WIDTH//2 + 50, HEIGHT//2 - square_size//2)    #right (15 Hz)
}

#defining frequencies
frequencies = {0: "8 Hz", 1: "10 Hz", 2: "12 Hz", 3: "15 Hz"}

def draw_squares(highlighted=None, phase="SSVEP Data Collection", round_num=1):
    """drawing squares & highlighting active one"""
    screen.fill(WHITE)
    
    for idx, pos in square_positions.items():
        color = GREEN if idx == highlighted else BLACK
        pygame.draw.rect(screen, color, (*pos, square_size, square_size), 5)
    
    #displaying phase text (w/ dynamic centering)
    font = pygame.font.Font(None, 36)
    phase_text = f"{phase} - Round {round_num}"
    text_surface = font.render(phase_text, True, BLACK)

    #calculating x-position dynamically based on text width
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 30))
    screen.blit(text_surface, text_rect)
    
    pygame.display.flip()
    

def data_collection_phase():
    """simulating 3 full rounds of data collection before moving to FBTRCA model application"""
    print("\n### Starting SSVEP Data Collection Phase ###")
    
    for round_num in range(1, 4):  #3 rounds
        print(f"Starting Data Collection Round {round_num}")
        for _ in range(10):  #simulating 10 trials per round
            chosen = random.choice([0, 1, 2, 3])
            draw_squares(highlighted=chosen, phase="SSVEP Data Collection", round_num=round_num)
            time.sleep(0.5)
            draw_squares(phase="SSVEP Data Collection", round_num=round_num)  #clearing highlight
            time.sleep(0.5)
    
    print("### SSVEP Data Collection Completed ###\n")
    time.sleep(3)  #pausing before moving to FBTRCAmodel application

def model_application_phase():
    """simulating 3 full rounds of FBTRCA model application after all SSVEP data collection is done"""
    print("### Starting FBTRCA Model Application Phase ###")

    for round_num in range(1, 4):  #3 rounds
        print(f"Starting FBTRCA Model Application Round {round_num}")
        
        user_target = random.choice([0, 1, 2, 3])  #user fixating on one
        #flashing simulation (all squares flicker, as in real model use)
        for _ in range(5):
            draw_squares(highlighted=random.choice([0, 1, 2, 3]), phase="FBTRCA Model Application", round_num=round_num)
            time.sleep(1)
        
        #model prediction (correctly selecting the user’s intended square)
        draw_squares(highlighted=user_target, phase=f"FBTRCA Model Prediction: {frequencies[user_target]}", round_num=round_num)
        time.sleep(2)

    print("### FBTRCA Model Application Completed ###")
    time.sleep(2)

def main():
    """running full visualization with complete SSVEP data collection first & FBTRCA model application phases second"""
    screen.fill(WHITE)
    pygame.display.flip()
    
    data_collection_phase()
    model_application_phase()

    print("Simulation complete")
    pygame.quit()

if __name__ == "__main__": 
    main()

