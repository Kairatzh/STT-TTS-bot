import pygame
import sys
import os
from data import emotion_paths


class EmotionViewer:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("Emotion Viewer")

        self.width, self.height = self.screen.get_size()
        self.clock = pygame.time.Clock()

        self.current_image = None
        self.running = True

    def set_emotion(self, emotion: str):
        emotion = emotion.lower()

        if emotion not in emotion_paths:
            print(f"[ERROR] Unknown emotion: {emotion}")
            return

        path = emotion_paths[emotion]

        if not os.path.exists(path):
            print(f"[ERROR] Image not found: {path}")
            return

        image = pygame.image.load(path)
        self.current_image = pygame.transform.scale(
            image, (self.width, self.height)
        )

    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            if self.current_image:
                self.screen.blit(self.current_image, (0, 0))

            pygame.display.flip()

        pygame.quit()
        sys.exit()


viewer = EmotionViewer()

