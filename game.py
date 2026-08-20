import tkinter as tk
from tkinter import ttk
import random
from PIL import Image, ImageDraw
import io

class RandomDeathGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Death Game")
        self.root.geometry("800x600")
        self.root.config(bg="#1a1a1a")
        
        # Death scenarios with ASCII art
        self.deaths = [
            {
                "text": "You were struck by lightning! ⚡",
                "art": self.draw_lightning_death
            },
            {
                "text": "A meteor fell on you! 🌍",
                "art": self.draw_meteor_death
            },
            {
                "text": "You were eaten by a giant rubber duck! 🦆",
                "art": self.draw_duck_death
            },
            {
                "text": "You spontaneously combusted! 🔥",
                "art": self.draw_fire_death
            },
            {
                "text": "You were hit by a flying piano! 🎹",
                "art": self.draw_piano_death
            },
            {
                "text": "An angry swarm of bees attacked you! 🐝",
                "art": self.draw_bees_death
            },
            {
                "text": "You were crushed by a giant marshmallow! 🍡",
                "art": self.draw_marshmallow_death
            },
            {
                "text": "You slipped on a banana peel and died! 🍌",
                "art": self.draw_banana_death
            },
            {
                "text": "A ninja star flew into your face! 🌟",
                "art": self.draw_ninja_death
            },
            {
                "text": "You were attacked by a rogue toaster! 🍞",
                "art": self.draw_toaster_death
            },
            {
                "text": "A giant squid dragged you underwater! 🦑",
                "art": self.draw_squid_death
            },
            {
                "text": "You were hit by a runaway shopping cart! 🛒",
                "art": self.draw_cart_death
            },
            {
                "text": "An anvil fell on your head! 🔨",
                "art": self.draw_anvil_death
            },
            {
                "text": "You were defeated in a dance battle! 💃",
                "art": self.draw_dance_death
            },
            {
                "text": "A sentient spaghetti noodle strangled you! 🍝",
                "art": self.draw_spaghetti_death
            },
            {
                "text": "You were pecked to death by angry penguins! 🐧",
                "art": self.draw_penguin_death
            },
            {
                "text": "A rogue golf ball hit a hole-in-one... in your face! ⛳",
                "art": self.draw_golf_death
            },
            {
                "text": "You were crushed by falling books! 📚",
                "art": self.draw_books_death
            },
            {
                "text": "A swarm of angry squirrels attacked you! 🐿️",
                "art": self.draw_squirrel_death
            },
            {
                "text": "You were defeated by a sentient couch! 🛋️",
                "art": self.draw_couch_death
            },
            {
                "text": "You tripped over nothing and died! 👟",
                "art": self.draw_trip_death
            },
            {
                "text": "A giant yoyo decapitated you! 🪀",
                "art": self.draw_yoyo_death
            },
            {
                "text": "You were hit by a comet made of cheese! 🌙🧀",
                "art": self.draw_cheese_death
            },
            {
                "text": "A flock of angry flamingos stampeded you! 🦩",
                "art": self.draw_flamingo_death
            },
            {
                "text": "You were sat on by an invisible giant! 👻",
                "art": self.draw_invisible_death
            },
        ]
        
        self.death_count = 0
        self.current_screen = "menu"
        
        self.create_menu_screen()
    
    def create_menu_screen(self):
        """Create the main menu screen"""
        self.clear_screen()
        self.current_screen = "menu"
        
        # Title
        title = tk.Label(
            self.root,
            text="💀 RANDOM DEATH GAME 💀",
            font=("Arial", 32, "bold"),
            bg="#1a1a1a",
            fg="#e74c3c"
        )
        title.pack(pady=40)
        
        # Instructions
        instructions = tk.Label(
            self.root,
            text="Press the button below...\nif you dare!",
            font=("Arial", 18),
            bg="#1a1a1a",
            fg="#ecf0f1"
        )
        instructions.pack(pady=20)
        
        # Main button
        self.button = tk.Button(
            self.root,
            text="PRESS ME",
            font=("Arial", 20, "bold"),
            bg="#e74c3c",
            fg="white",
            padx=60,
            pady=20,
            command=self.die,
            cursor="hand2"
        )
        self.button.pack(pady=40)
        
        # Death counter
        self.counter_label = tk.Label(
            self.root,
            text=f"Deaths: {self.death_count}",
            font=("Arial", 16, "bold"),
            bg="#1a1a1a",
            fg="#3498db"
        )
        self.counter_label.pack(pady=20)
    
    def die(self):
        """Trigger a random death"""
        death = random.choice(self.deaths)
        self.death_count += 1
        self.show_death_screen(death)
    
    def show_death_screen(self, death):
        """Show the death screen with illustration"""
        self.clear_screen()
        self.current_screen = "death"
        
        # Title
        title = tk.Label(
            self.root,
            text="💀 YOU DIED! 💀",
            font=("Arial", 28, "bold"),
            bg="#1a1a1a",
            fg="#e74c3c"
        )
        title.pack(pady=10)
        
        # Canvas for ASCII art
        canvas_frame = tk.Frame(self.root, bg="#1a1a1a")
        canvas_frame.pack(pady=15)
        
        text_display = tk.Text(
            canvas_frame,
            width=70,
            height=20,
            bg="#0d0d0d",
            fg="#00ff00",
            font=("Courier", 10),
            border=0,
            state='normal'
        )
        text_display.pack()
        
        # Get ASCII art
        ascii_art = death["art"]()
        text_display.insert('1.0', ascii_art)
        text_display.config(state='disabled')
        
        # Death description
        desc = tk.Label(
            self.root,
            text=death["text"],
            font=("Arial", 14, "bold"),
            bg="#1a1a1a",
            fg="#f39c12"
        )
        desc.pack(pady=10)
        
        # Death counter
        counter = tk.Label(
            self.root,
            text=f"Deaths: {self.death_count}",
            font=("Arial", 12),
            bg="#1a1a1a",
            fg="#3498db"
        )
        counter.pack()
        
        # Back to menu button
        back_button = tk.Button(
            self.root,
            text="Try Again",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            command=self.create_menu_screen,
            cursor="hand2"
        )
        back_button.pack(pady=10)
    
    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    # ASCII Art Methods
    def draw_lightning_death(self):
        return """
        
                    ⚡
                    |
                    |
                 ⚡ | ⚡
                    |
                    |
                  \(o)/
                   |=|
                  /| |\\
                   | |
                  /   \\
                 
        Lightning Strike!
        """
    
    def draw_meteor_death(self):
        return """
        
                    💫
                   /
                  /
               🌍
              ███
             █████
            ███X███
             █████
              ███
              
             \(o_o)/
              |███|
             /|   |\\
        
        Meteor Impact!
        """
    
    def draw_duck_death(self):
        return """
        
              🦆 🦆 🦆
             🦆 👤 🦆
              🦆 🦆 🦆
              
              (o_o)
              |###|
             /|   |\\
               | |
              / \\
              
        Devoured by Ducks!
        """
    
    def draw_fire_death(self):
        return """
        
            🔥    🔥
           🔥🔥  🔥🔥
          🔥  (o)  🔥
          🔥  ###  🔥
           🔥  |  🔥
            🔥 | 🔥
        
        Spontaneous Combustion!
        """
    
    def draw_piano_death(self):
        return """
        
               ▄▄▄▄▄▄▄
              ║█ ░ █░║
              ║░ █ █░║
              ║█ ░ █░║
              ║█████░║
              ║░░░░░ ║  ⬇️
              ▀▀▀▀▀▀▀
              
              (o o)
              |═══|
             /|   |\\
        
        Crushed by a Piano!
        """
    
    def draw_bees_death(self):
        return """
        
              🐝    🐝
           🐝  🐝 🐝  🐝
              (o_o)
              |XXX|
             /|XXX|\\
              |XXX|
           🐝    🐝
        
        Swarmed by Bees!
        """
    
    def draw_marshmallow_death(self):
        return """
        
           ████████████
           █  ████  █
           █ ████████ █
           █ █      █ █
           █ █ (o) █ █
           █ █ |=| █ █
           █ █/| |\\█ █
           ████████████
        
        Crushed by Marshmallow!
        """
    
    def draw_banana_death(self):
        return """
        
                  🍌
                  🍌
                  🍌
                  
                 /o\\
                 |#|
                /| |\\  WHOOOOSH!
                 | |
                / \\
                
        Slipped on Banana!
        """
    
    def draw_ninja_death(self):
        return """
        
                   ★
                   |\\ ★
                   | \\
                   |  ★
                   |
                  (o✦o)
                  |###|
                 /|   |\\
                  | |
        
        Ninja Star Strike!
        """
    
    def draw_toaster_death(self):
        return """
        
               [TOASTER]
               ┌─────┐
               │  ▂▂  │
               │ |🍞| │ ⚡
               │ |🍞| │
               └─────┘
               
              (o_o)★
              |███|
             /|   |\\
        
        Rogue Toaster!
        """
    
    def draw_squid_death(self):
        return """
        
             ~~~~~~~~
            ~~~~🦑~~~~
           ~~~🦑 🦑~~~
            ~~~🦑~~~
             ~~~~○~~~~
             ~~~(o)~~~
             ~~~###~~~
             ~~/ | \\~~
        
        Dragged Underwater!
        """
    
    def draw_cart_death(self):
        return """
        
               🛒🛒🛒
              🛒 (o) 🛒
              🛒 ### 🛒
              🛒|   |🛒
              🛒 / \\ 🛒
               🛒🛒🛒
        
        Hit by Shopping Cart!
        """
    
    def draw_anvil_death(self):
        return """
        
                ▲▲▲▲▲
                █▀▀▀█
                █▄▄▄█
                  |||  ⬇️
                  |||
                 (o_o)
                 |███|
                /|   |\\
        
        Anvil Drop!
        """
    
    def draw_dance_death(self):
        return """
        
              💃  🕺
              🎵 🎵 🎵
              
              (o_o)
              ╱ # ╲
              ╲   ╱
               |   |
              / \\
        
        Lost Dance Battle!
        """
    
    def draw_spaghetti_death(self):
        return """
        
             ~~~~🍝~~~
            ~~🍝 🍝 🍝~
           ~🍝 (o) 🍝~
           ~🍝 |#| 🍝~
           ~🍝/| |\\🍝~
            ~~🍝 🍝 🍝~
             ~~~~🍝~~~
        
        Strangled by Spaghetti!
        """
    
    def draw_penguin_death(self):
        return """
        
              🐧 🐧 🐧
             🐧 🐧 🐧 🐧
            🐧  (o)  🐧
            🐧  ###  🐧
            🐧 /   \\ 🐧
             🐧 🐧 🐧 🐧
              🐧 🐧 🐧
        
        Penguin Stampede!
        """
    
    def draw_golf_death(self):
        return """
        
                   ⛳
                   ◎  ⬇️
                   |
                   |
                  (o✦)
                  |###|
                 /|   |\\
                  | |
        
        Hole-in-One!
        """
    
    def draw_books_death(self):
        return """
        
             ╔════╗╔════╗
             ║📚📚║║📚📚║
             ║📚📚║║📚📚║ ⬇️
             ╚════╝╚════╝
                (o_o)
                |███|
               /|   |\\
        
        Crushed by Books!
        """
    
    def draw_squirrel_death(self):
        return """
        
              🐿️  🐿️
           🐿️  🐿️ 🐿️  🐿️
              (o_o)
              |XXX|
             /|XXX|\\
              |XXX|
           🐿️  🐿️  🐿️
        
        Squirrel Attack!
        """
    
    def draw_couch_death(self):
        return """
        
            ╔═════════╗
            ║ 🛋️🛋️🛋️ ║
            ║ 🛋️(o)🛋️ ║  ⬇️
            ║ 🛋️###🛋️ ║
            ║ 🛋️🛋️🛋️ ║
            ╚═════════╝
        
        Crushed by Couch!
        """
    
    def draw_trip_death(self):
        return """
        
                  ✋
                
                (o_o)
                |===|
               /|   |\\  ⬇️
                | |
               / \\
               
        Tripped and Died!
        """
    
    def draw_yoyo_death(self):
        return """
        
                 ◎
                /|\\
                 |
                 |  WHOOSH!
                (o✦
                |###
               /|   \\
        
        Yoyo Decapitation!
        """
    
    def draw_cheese_death(self):
        return """
        
                🌙🧀
                  ⬇️
                  |
                  |
                 (o_o)
                 |###|
                /|   |\\
                  | |
        
        Cheese Comet!
        """
    
    def draw_flamingo_death(self):
        return """
        
              🦩 🦩 🦩
             🦩  🦩  🦩 🦩
            🦩  (o)  🦩
            🦩  ###  🦩
            🦩 /   \\ 🦩
             🦩 🦩 🦩 🦩
              🦩 🦩 🦩
        
        Flamingo Stampede!
        """
    
    def draw_invisible_death(self):
        return """
        
             👻 👻 👻
            👻 👻 👻 👻
           👻  (o)  👻
           👻  ###  👻
           👻 /   \\ 👻
            👻 👻 👻 👻
             👻 👻 👻
        
        Sat on by Invisible!
        """

if __name__ == "__main__":
    root = tk.Tk()
    game = RandomDeathGame(root)
    root.mainloop()
