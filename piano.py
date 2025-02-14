import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the G4 note audio file
C = "Piano Notes/C.wav"  
C_note = pygame.mixer.Sound(C)

D = "Piano Notes/D.wav"
D_note = pygame.mixer.Sound(D)

E = "Piano Notes/E.wav"  
E_note = pygame.mixer.Sound(E)

F = "Piano Notes/F.wav"  
F_note = pygame.mixer.Sound(F)

G = "Piano Notes/G.mp3"  
G_note = pygame.mixer.Sound(G)

A5 = "Piano Notes/A.wav"  
A5_note = pygame.mixer.Sound(A5)

A = "Piano Notes/A4.wav"  
A_note = pygame.mixer.Sound(A)

# Initialize pygame for event handling
pygame.init()
window_width = 700
window_height = 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Piano Light!")

# Load and scale the background image
background_image = pygame.image.load("keys.jpg")  # Replace with the actual file path
background_image = pygame.transform.scale(background_image, (window_width, window_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # When 'S' key is pressed
                C_note.play()
            if event.key == pygame.K_d:  # When 'S' key is pressed
                D_note.play()
            if event.key == pygame.K_f:  # When 'S' key is pressed
                E_note.play()
            if event.key == pygame.K_g:  # When 'S' key is pressed
                F_note.play()
            if event.key == pygame.K_h:  # When 'S' key is pressed
                G_note.play()
            if event.key == pygame.K_a:  # When 'S' key is pressed
                A5_note.play()
            if event.key == pygame.K_j:  # When 'S' key is pressed
                A_note.play()

    # Draw the background image
    screen.blit(background_image, (0, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
