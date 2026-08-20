import tkinter as tk
from tkinter import messagebox
import random

class RandomDeathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Death Game")
        self.root.geometry("500x300")
        self.root.config(bg="#2c3e50")
        
        # Death scenarios
        self.deaths = [
            "You were struck by lightning! ⚡",
            "A meteor fell on you! 🌍",
            "You were eaten by a giant rubber duck! 🦆",
            "You spontaneously combusted! 🔥",
            "You were hit by a flying piano! 🎹",
            "An angry swarm of bees attacked you! 🐝",
            "You were crushed by a giant marshmallow! 🍡",
            "You slipped on a banana peel and died! 🍌",
            "A ninja star flew into your face! 🌟",
            "You were attacked by a rogue toaster! 🍞",
            "A giant squid dragged you underwater! 🦑",
            "You were hit by a runaway shopping cart! 🛒",
            "An anvil fell on your head! 🔨",
            "You were defeated in a dance battle! 💃",
            "A sentient spaghetti noodle strangled you! 🍝",
            "You were pecked to death by angry penguins! 🐧",
            "A rogue golf ball hit a hole-in-one... in your face! ⛳",
            "You were crushed by falling books! 📚",
            "A swarm of angry squirrels attacked you! 🐿️",
            "You were defeated by a sentient couch! 🛋️",
            "You tripped over nothing and died! 👟",
            "A giant yoyo decapitated you! 🪀",
            "You were hit by a comet made of cheese! 🌙🧀",
            "A flock of angry flamingos stampeded you! 🦩",
            "You were sat on by an invisible giant! 👻",
            "A rogue confetti cannon exploded in your face! 🎉",
            "You were attacked by sentient socks! 🧦",
            "A giant rubber chicken fell on you! 🐔",
            "You were defeated in a staring contest with a cat! 😾",
            "A pizza slice fell on you from space! 🍕",
            "You were whipped by a sentient noodle! 🍜",
            "A rogue vacuum cleaner consumed you! 🌪️",
            "You were hit by an airborne waffle! 🧇",
            "A sentient shadow ate your soul! 🌑",
            "You were defeated by aggressive pillows! 🛏️",
            "A flying fish hit you in the face! 🐟",
            "You were crushed by a giant jello cube! 🟧",
            "A rogue watermelon exploded near you! 🍉",
            "You were attacked by angry butterflies! 🦋",
            "A sentient pudding consumed you! 🍮",
            "You were defeated by a gang of hamsters! 🐹",
            "A rogue cloud of glitter suffocated you! ✨",
            "You were hit by a stray bowling ball! 🎳",
            "A giant rubber band catapulted you into space! 🚀",
        ]
        
        # Title
        title = tk.Label(
            self.root,
            text="💀 RANDOM DEATH GAME 💀",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="#e74c3c"
        )
        title.pack(pady=20)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Press the button below...\nif you dare!",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        instructions.pack(pady=10)
        
        # Main button
        self.button = tk.Button(
            self.root,
            text="PRESS ME",
            font=("Arial", 16, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=40,
            pady=15,
            command=self.die
        )
        self.button.pack(pady=20)
        
        # Death counter
        self.death_count = 0
        self.counter_label = tk.Label(
            self.root,
            text="Deaths: 0",
            font=("Arial", 12),
            bg="#2c3e50",
            fg="#3498db"
        )
        self.counter_label.pack()
    
    def die(self):
        """Random death function"""
        death = random.choice(self.deaths)
        self.death_count += 1
        
        messagebox.showinfo("💀 YOU DIED! 💀", f"{death}\n\nDeaths: {self.death_count}")
        self.counter_label.config(text=f"Deaths: {self.death_count}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RandomDeathGame(root)
    root.mainloop()
