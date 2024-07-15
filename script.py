import pygame
import sys
import time
import threading


class AudioPlayer:
    def __init__(self, file_path):
        pygame.mixer.init()
        self.file_path = file_path
        self.is_playing = False
        self.play_thread = None

    def play_audio(self):
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        self.is_playing = True

        while self.is_playing:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
            time.sleep(1)

    def start(self):
        self.play_thread = threading.Thread(target=self.play_audio)
        self.play_thread.start()

    def stop(self):
        self.is_playing = False
        pygame.mixer.music.stop()
        if self.play_thread:
            self.play_thread.join()


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <path_to_mp3_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    player = AudioPlayer(file_path)
    player.start()

    print(f"Now playing: {file_path}")
    print("Press Enter to stop playback and exit.")

    input()  # Wait for user to press Enter
    player.stop()
    print("Playback stopped. Exiting.")


if __name__ == "__main__":
    main()