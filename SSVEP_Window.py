import time
import pygame_gui
import pygame

# Design Parameters
MIN_FREQ = 5
MAX_FREQ = 50
DEFAULT_FREQ = 5

def create_blinking_window():
    pygame.init()

    # Set the Dimensions of the Window
    Width = 800
    Height = 600

    # Create the Window and a UIManager for the GUI
    Window = pygame.display.set_mode((Width, Height))
    Manager = pygame_gui.UIManager((Width, Height))

    # Create an Input Field and a Label for Frequency
    FreqInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((Width - 100, 0), (100, 50)), manager=Manager)
    FreqLabel = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((0, 0), (100, 50)), text=f"Freq: {DEFAULT_FREQ:0.0f} Hz", manager=Manager)

    # Initialize Freq and Duration
    Freq = DEFAULT_FREQ
    Duration = 1.0 / (2 * Freq)

    # Main Loop
    Running = True
    clock = pygame.time.Clock()

    while Running:
        DeltaTime = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Running = False
                
                elif event.key == pygame.K_RETURN:
                    try:
                        # Get the Frequency Input from the Text Input
                        Freq = float(FreqInput.get_text())
                        
                        # Constrain Frequency to Between 5 and 50 Hz
                        Freq = min(max(Freq, MIN_FREQ), MAX_FREQ)
                        Duration = 1.0 / (2 * Freq)
                        
                        # Update Label Text
                        FreqLabel.set_text(f"Freq: {Freq:0.0f} Hz")  
                    
                    except ValueError:
                        pass

            Manager.process_events(event)

        Manager.update(DeltaTime)

        # Set the Window to White
        Window.fill((255, 255, 255))
        Manager.draw_ui(Window)
        pygame.display.flip()
        time.sleep(Duration)

        # Set the Window to Black
        Window.fill((0, 0, 0))
        Manager.draw_ui(Window)
        pygame.display.flip()
        time.sleep(Duration)

    pygame.quit()


# Call the Func
create_blinking_window()
