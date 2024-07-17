import pygame
import sys
import threading
import tkinter as tk
from tkinter import ttk

class AudioPlayer:
    def __init__(self, file_path):
        pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
        self.file_path = file_path
        self.is_playing = False
        self.play_thread = None
        self.volume = 0.5  # Default volume (0.0 to 1.0)

    def play_audio(self):
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        self.is_playing = True

        while self.is_playing:
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
            pygame.time.wait(30000)  # Check more frequently

    def start(self):
        self.play_thread = threading.Thread(target=self.play_audio)
        self.play_thread.start()

    def stop(self):
        self.is_playing = False
        pygame.mixer.music.stop()
        if self.play_thread:
            self.play_thread.join()

    def set_volume(self, volume):
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

class PlayerGUI:
    def __init__(self, master, file_path):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("300x150")

        self.player = AudioPlayer(file_path)

        self.status_label = tk.Label(master, text=f"Status: Playing {self.player.file_path}")
        self.status_label.pack(pady=10)

        self.toggle_button = tk.Button(master, text="Stop", command=self.toggle_playback)
        self.toggle_button.pack(pady=5)

        self.volume_label = tk.Label(master, text="Volume:")
        self.volume_label.pack()

        self.volume_slider = ttk.Scale(master, from_=0, to=100, orient="horizontal", command=self.update_volume)
        self.volume_slider.set(100)  # Default volume
        self.volume_slider.pack(pady=5)

        self.player.start()

        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def toggle_playback(self):
        if not self.player.is_playing:
            self.player.start()
            self.status_label.config(text=f"Status: Playing {self.player.file_path}")
            self.toggle_button.config(text="Stop")
        else:
            self.player.stop()
            self.status_label.config(text="Status: Not Playing")
            self.toggle_button.config(text="Start")

    def update_volume(self, value):
        volume = float(value) / 100
        self.player.set_volume(volume)

    def on_closing(self):
        if self.player.is_playing:
            self.player.stop()
        self.master.destroy()

def main():
    if len(sys.argv) < 2:
        print("Usage: python mp3_player.py <path_to_mp3_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    root = tk.Tk()
    PlayerGUI(root, file_path)
    root.mainloop()

if __name__ == "__main__":
    main()