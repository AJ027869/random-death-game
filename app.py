from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Death scenarios
DEATHS = [
    {
        "text": "You were struck by lightning! ⚡",
        "art": """
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
    },
    {
        "text": "A meteor fell on you! 🌍",
        "art": """
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
    },
    {
        "text": "You were eaten by a giant rubber duck! 🦆",
        "art": """
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
    },
    {
        "text": "You spontaneously combusted! 🔥",
        "art": """
            🔥    🔥
           🔥🔥  🔥🔥
          🔥  (o)  🔥
          🔥  ###  🔥
           🔥  |  🔥
            🔥 | 🔥
        
        Spontaneous Combustion!
        """
    },
    {
        "text": "You were hit by a flying piano! 🎹",
        "art": """
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
    },
    {
        "text": "An angry swarm of bees attacked you! 🐝",
        "art": """
              🐝    🐝
           🐝  🐝 🐝  🐝
              (o_o)
              |XXX|
             /|XXX|\\
              |XXX|
           🐝    🐝
        
        Swarmed by Bees!
        """
    },
    {
        "text": "You were crushed by a giant marshmallow! 🍡",
        "art": """
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
    },
    {
        "text": "You slipped on a banana peel and died! 🍌",
        "art": """
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
    },
    {
        "text": "A ninja star flew into your face! 🌟",
        "art": """
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
    },
    {
        "text": "You were attacked by a rogue toaster! 🍞",
        "art": """
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
    },
    {
        "text": "A giant squid dragged you underwater! 🦑",
        "art": """
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
    },
    {
        "text": "You were hit by a runaway shopping cart! 🛒",
        "art": """
               🛒🛒🛒
              🛒 (o) 🛒
              🛒 ### 🛒
              🛒|   |🛒
              🛒 / \\ 🛒
               🛒🛒🛒
        
        Hit by Shopping Cart!
        """
    },
    {
        "text": "An anvil fell on your head! 🔨",
        "art": """
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
    },
    {
        "text": "You were defeated in a dance battle! 💃",
        "art": """
              💃  🕺
              🎵 🎵 🎵
              
              (o_o)
              ╱ # ╲
              ╲   ╱
               |   |
              / \\
        
        Lost Dance Battle!
        """
    },
    {
        "text": "A sentient spaghetti noodle strangled you! 🍝",
        "art": """
             ~~~~🍝~~~
            ~~🍝 🍝 🍝~
           ~🍝 (o) 🍝~
           ~🍝 |#| 🍝~
           ~🍝/| |\\🍝~
            ~~🍝 🍝 🍝~
             ~~~~🍝~~~
        
        Strangled by Spaghetti!
        """
    },
    {
        "text": "You were pecked to death by angry penguins! 🐧",
        "art": """
              🐧 🐧 🐧
             🐧 🐧 🐧 🐧
            🐧  (o)  🐧
            🐧  ###  🐧
            🐧 /   \\ 🐧
             🐧 🐧 🐧 🐧
              🐧 🐧 🐧
        
        Penguin Stampede!
        """
    },
    {
        "text": "A rogue golf ball hit a hole-in-one... in your face! ⛳",
        "art": """
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
    },
    {
        "text": "You were crushed by falling books! 📚",
        "art": """
             ╔════╗╔════╗
             ║📚📚║║📚📚║
             ║📚📚║║📚📚║ ⬇️
             ╚════╝╚════╝
                (o_o)
                |███|
               /|   |\\
        
        Crushed by Books!
        """
    },
    {
        "text": "A swarm of angry squirrels attacked you! 🐿️",
        "art": """
              🐿️  🐿️
           🐿️  🐿️ 🐿️  🐿️
              (o_o)
              |XXX|
             /|XXX|\\
              |XXX|
           🐿️  🐿️  🐿️
        
        Squirrel Attack!
        """
    },
    {
        "text": "You were defeated by a sentient couch! 🛋️",
        "art": """
            ╔═════════╗
            ║ 🛋️🛋️🛋️ ║
            ║ 🛋️(o)🛋️ ║  ⬇️
            ║ 🛋️###🛋️ ║
            ║ 🛋️🛋️🛋️ ║
            ╚═════════╝
        
        Crushed by Couch!
        """
    },
    {
        "text": "You tripped over nothing and died! 👟",
        "art": """
                  ✋
                
                (o_o)
                |===|
               /|   |\\  ⬇️
                | |
               / \\
               
        Tripped and Died!
        """
    },
    {
        "text": "A giant yoyo decapitated you! 🪀",
        "art": """
                 ◎
                /|\\
                 |
                 |  WHOOSH!
                (o✦
                |###
               /|   \\
        
        Yoyo Decapitation!
        """
    },
    {
        "text": "You were hit by a comet made of cheese! 🌙🧀",
        "art": """
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
    },
    {
        "text": "A flock of angry flamingos stampeded you! 🦩",
        "art": """
              🦩 🦩 🦩
             🦩  🦩  🦩 🦩
            🦩  (o)  🦩
            🦩  ###  🦩
            🦩 /   \\ 🦩
             🦩 🦩 🦩 🦩
              🦩 🦩 🦩
        
        Flamingo Stampede!
        """
    },
    {
        "text": "You were sat on by an invisible giant! 👻",
        "art": """
             👻 👻 👻
            👻 👻 👻 👻
           👻  (o)  👻
           👻  ###  👻
           👻 /   \\ 👻
            👻 👻 👻 👻
             👻 👻 👻
        
        Sat on by Invisible!
        """
    },
]

death_count = 0

@app.route('/')
def index():
    """Render the main game page"""
    return render_template('index.html')

@app.route('/api/die', methods=['GET'])
def die():
    """API endpoint to get a random death"""
    global death_count
    death_count += 1
    death = random.choice(DEATHS)
    return jsonify({
        'text': death['text'],
        'art': death['art'],
        'death_count': death_count
    })

@app.route('/api/reset', methods=['GET'])
def reset():
    """API endpoint to reset death count"""
    global death_count
    death_count = 0
    return jsonify({'death_count': death_count})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
