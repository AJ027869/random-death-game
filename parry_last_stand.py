import math
import random
import tkinter as tk


class ParryLastStandGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Parry Last Stand")
        self.root.geometry("900x650")
        self.root.configure(bg="#0b1020")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=900,
            height=600,
            bg="#0b1020",
            highlightthickness=0,
            cursor="crosshair",
        )
        self.canvas.pack(fill="both", expand=True, padx=12, pady=12)

        self.state = "menu"
        self.keys = {"w": False, "a": False, "s": False, "d": False}
        self.mouse_x = 450
        self.mouse_y = 300
        self.message = ""

        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        self.root.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.reset_game()
        self.draw_menu()
        self.game_loop()

    def reset_game(self):
        self.player = {
            "x": 450,
            "y": 300,
            "radius": 20,
            "speed": 4.0,
            "health": 100,
            "max_health": 100,
            "face_x": 1,
            "face_y": 0,
            "dash_cooldown": 0,
            "dash_time": 0,
            "attack_cooldown": 0,
            "parry_time": 0,
            "parry_cooldown": 0,
            "hit_flash": 0,
        }
        self.enemies = []
        self.wave = 1
        self.max_waves = 10
        self.game_over = False
        self.victory = False
        self.message = ""

    def start_game(self):
        self.reset_game()
        self.state = "playing"
        self.spawn_wave()

    def on_canvas_click(self, event):
        if self.state == "menu":
            if 330 <= event.x <= 570 and 220 <= event.y <= 290:
                self.start_game()
            return
        if self.state in {"game_over", "victory"}:
            self.state = "menu"
            self.draw_menu()
            return
        self.melee_attack()

    def on_key_press(self, event):
        key = event.keysym.lower()
        if key in self.keys:
            self.keys[key] = True
        if key == "space":
            self.trigger_parry()
        if key == "q":
            self.dash()

    def on_key_release(self, event):
        key = event.keysym.lower()
        if key in self.keys:
            self.keys[key] = False

    def on_mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def draw_menu(self):
        self.state = "menu"
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 900, 600, fill="#0b1020")

        self.canvas.create_text(
            450,
            120,
            text="PARRY LAST STAND",
            font=("Arial", 34, "bold"),
            fill="#f8fafc",
        )
        self.canvas.create_text(
            450,
            170,
            text="Survive 10 waves and beat the final boss.",
            font=("Arial", 14),
            fill="#94a3b8",
        )

        play_button = self.canvas.create_rectangle(330, 220, 570, 290, fill="#22c55e", outline="#16a34a", width=4)
        self.canvas.create_text(450, 255, text="PLAY", font=("Arial", 24, "bold"), fill="white")
        self.canvas.itemconfig(play_button, tags=("play_button",))
        self.canvas.tag_bind("play_button", "<Button-1>", lambda event: self.start_game())

        instruction_lines = [
            "How to play:",
            "• Move with W A S D",
            "• Left-click to melee attack",
            "• Press Q to dash",
            "• Press Space to use Parry",
            "• Parry deflects all enemy attacks",
            "• Survive each wave and defeat the last boss",
        ]
        y_pos = 340
        for line in instruction_lines:
            self.canvas.create_text(450, y_pos, text=line, font=("Arial", 16), fill="#e2e8f0")
            y_pos += 30

    def melee_attack(self):
        if self.state != "playing":
            return
        if self.player["attack_cooldown"] > 0:
            return
        self.player["attack_cooldown"] = 0.35

        px = self.player["x"]
        py = self.player["y"]
        dx = self.mouse_x - px
        dy = self.mouse_y - py
        dist = math.hypot(dx, dy) or 1
        self.player["face_x"] = dx / dist
        self.player["face_y"] = dy / dist

        for enemy in list(self.enemies):
            ex = enemy["x"]
            ey = enemy["y"]
            to_enemy_x = ex - px
            to_enemy_y = ey - py
            enemy_dist = math.hypot(to_enemy_x, to_enemy_y)
            if enemy_dist > 95:
                continue

            facing_angle = math.atan2(self.player["face_y"], self.player["face_x"])
            target_angle = math.atan2(to_enemy_y, to_enemy_x)
            angle_diff = abs((target_angle - facing_angle + math.pi) % (2 * math.pi) - math.pi)
            if angle_diff <= math.radians(100):
                enemy["hp"] -= 22
                enemy["hit_flash"] = 0.15
                enemy["stun"] = 0.18
                if enemy["hp"] <= 0:
                    self.enemies.remove(enemy)

    def trigger_parry(self):
        if self.state != "playing":
            return
        if self.player["parry_cooldown"] > 0:
            return
        self.player["parry_time"] = 0.6
        self.player["parry_cooldown"] = 2.5
        self.message = "PARRY!"

    def dash(self):
        if self.state != "playing":
            return
        if self.player["dash_cooldown"] > 0:
            return
        dx = self.mouse_x - self.player["x"]
        dy = self.mouse_y - self.player["y"]
        dist = math.hypot(dx, dy)
        if dist > 0:
            self.player["face_x"] = dx / dist
            self.player["face_y"] = dy / dist
        self.player["dash_cooldown"] = 1.6
        self.player["dash_time"] = 0.18

    def spawn_wave(self):
        self.enemies = []
        if self.wave == 10:
            boss = {
                "x": random.randint(150, 750),
                "y": random.randint(150, 450),
                "radius": 32,
                "hp": 260 + self.wave * 24,
                "max_hp": 260 + self.wave * 24,
                "speed": 1.7,
                "color": "#f43f5e",
                "attack_cooldown": 0,
                "stun": 0,
                "boss": True,
                "hit_flash": 0,
            }
            self.enemies.append(boss)
            for _ in range(8):
                self.enemies.append(self.create_enemy())
        else:
            count = 4 + self.wave * 2
            for _ in range(count):
                self.enemies.append(self.create_enemy())

    def create_enemy(self):
        side = random.choice(["top", "bottom", "left", "right"])
        if side == "top":
            x = random.randint(50, 850)
            y = -20
        elif side == "bottom":
            x = random.randint(50, 850)
            y = 620
        elif side == "left":
            x = -20
            y = random.randint(50, 550)
        else:
            x = 920
            y = random.randint(50, 550)

        radius = random.randint(12, 18)
        hp = 28 + self.wave * 6
        if self.wave >= 7:
            hp += 12
        return {
            "x": x,
            "y": y,
            "radius": radius,
            "hp": hp,
            "max_hp": hp,
            "speed": 1.3 + self.wave * 0.12,
            "color": random.choice(["#ef4444", "#f97316", "#facc15", "#a78bfa", "#22d3ee"]),
            "attack_cooldown": random.uniform(0.6, 1.2),
            "stun": 0,
            "boss": False,
            "hit_flash": 0,
        }

    def update_player(self, dt):
        player = self.player
        move_x = 0
        move_y = 0

        if self.keys["w"]:
            move_y -= 1
        if self.keys["s"]:
            move_y += 1
        if self.keys["a"]:
            move_x -= 1
        if self.keys["d"]:
            move_x += 1

        if move_x != 0 or move_y != 0:
            length = math.hypot(move_x, move_y)
            move_x /= length
            move_y /= length
            player["x"] += move_x * player["speed"] * dt * 60
            player["y"] += move_y * player["speed"] * dt * 60

        if player["dash_time"] > 0:
            player["dash_time"] -= dt
            player["x"] += player["face_x"] * 18 * dt * 60
            player["y"] += player["face_y"] * 18 * dt * 60

        player["x"] = max(30, min(870, player["x"]))
        player["y"] = max(30, min(570, player["y"]))
        player["dash_cooldown"] = max(0, player["dash_cooldown"] - dt)
        player["attack_cooldown"] = max(0, player["attack_cooldown"] - dt)
        player["parry_cooldown"] = max(0, player["parry_cooldown"] - dt)
        player["parry_time"] = max(0, player["parry_time"] - dt)
        player["hit_flash"] = max(0, player["hit_flash"] - dt)

    def update_enemies(self, dt):
        player = self.player
        for enemy in list(self.enemies):
            enemy["hit_flash"] = max(0, enemy["hit_flash"] - dt)
            enemy["stun"] = max(0, enemy["stun"] - dt)
            enemy["attack_cooldown"] -= dt

            if enemy["stun"] > 0:
                continue

            dx = player["x"] - enemy["x"]
            dy = player["y"] - enemy["y"]
            dist = math.hypot(dx, dy)
            if dist > 0:
                dx /= dist
                dy /= dist
                enemy["x"] += dx * enemy["speed"] * dt * 60
                enemy["y"] += dy * enemy["speed"] * dt * 60

            if dist <= player["radius"] + enemy["radius"] + 4:
                if player["parry_time"] > 0:
                    enemy["hp"] -= 35 + self.wave * 4
                    enemy["stun"] = 0.6
                    enemy["x"] += -dx * 18
                    enemy["y"] += -dy * 18
                    if enemy["hp"] <= 0:
                        self.enemies.remove(enemy)
                    continue
                if enemy["attack_cooldown"] <= 0:
                    damage = 8 if not enemy["boss"] else 16
                    player["health"] -= damage
                    player["hit_flash"] = 0.3
                    enemy["attack_cooldown"] = 0.8 if not enemy["boss"] else 1.2

            if player["parry_time"] > 0 and dist <= player["radius"] + enemy["radius"] + 28:
                enemy["hp"] -= 15 + self.wave * 2
                enemy["stun"] = 0.35
                enemy["x"] += -dx * 12
                enemy["y"] += -dy * 12
                if enemy["hp"] <= 0:
                    self.enemies.remove(enemy)

        if player["health"] <= 0:
            self.state = "game_over"
            self.message = "YOU WERE OVERWHELMED"

        if not self.enemies and self.state == "playing":
            if self.wave >= self.max_waves:
                self.state = "victory"
                self.message = "VICTORY! THE FINAL BOSS IS DOWN"
            else:
                self.wave += 1
                self.message = f"WAVE {self.wave} CLEAR"
                self.root.after(1200, self.spawn_wave)

    def draw_game(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 900, 600, fill="#0b1020")

        if self.state == "playing":
            self.draw_arena()
            self.draw_player()
            self.draw_enemies()
            self.draw_ui()
        elif self.state == "menu":
            self.draw_menu()
        elif self.state in {"game_over", "victory"}:
            self.canvas.create_rectangle(0, 0, 900, 600, fill="#111827")
            self.canvas.create_text(450, 170, text=self.message, font=("Arial", 32, "bold"), fill="#f8fafc")
            self.canvas.create_text(450, 230, text="Click anywhere to return to menu", font=("Arial", 16), fill="#cbd5e1")
            self.canvas.create_text(450, 320, text=f"Final wave: {self.wave}", font=("Arial", 18), fill="#93c5fd")
            self.canvas.create_text(450, 380, text=f"Health remaining: {max(0, int(self.player['health']))}", font=("Arial", 18), fill="#86efac")

    def draw_arena(self):
        self.canvas.create_rectangle(30, 30, 870, 570, outline="#1f2937", width=3)
        self.canvas.create_text(120, 42, text=f"Wave {self.wave}/{self.max_waves}", font=("Arial", 16, "bold"), fill="#f8fafc", anchor="w")

    def draw_player(self):
        player = self.player
        glow = "#fca5a5" if player["hit_flash"] > 0 else "#38bdf8"
        px = player["x"]
        py = player["y"]
        self.canvas.create_oval(px - player["radius"], py - player["radius"], px + player["radius"], py + player["radius"], fill=glow, outline="#e0f2fe", width=2)
        facing_x = px + player["face_x"] * 26
        facing_y = py + player["face_y"] * 26
        self.canvas.create_line(px, py, facing_x, facing_y, fill="#e0f2fe", width=3)
        if player["parry_time"] > 0:
            self.canvas.create_oval(px - 34, py - 34, px + 34, py + 34, outline="#facc15", width=3, dash=(6, 6))

    def draw_enemies(self):
        for enemy in self.enemies:
            x = enemy["x"]
            y = enemy["y"]
            radius = enemy["radius"]
            fill = "#f87171" if enemy["boss"] else enemy["color"]
            outline = "#fef2f2" if enemy["hit_flash"] > 0 else "#111827"
            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=fill, outline=outline, width=3)
            if enemy["boss"]:
                self.canvas.create_text(x, y - radius - 12, text="BOSS", font=("Arial", 10, "bold"), fill="white")

            bar_width = max(25, radius * 2)
            hp_ratio = max(0, enemy["hp"] / enemy["max_hp"])
            self.canvas.create_rectangle(x - radius, y + radius + 8, x + radius, y + radius + 14, fill="#374151")
            self.canvas.create_rectangle(x - radius, y + radius + 8, x - radius + bar_width * hp_ratio, y + radius + 14, fill="#4ade80")

    def draw_ui(self):
        self.canvas.create_rectangle(670, 20, 860, 100, fill="#111827", outline="#334155", width=2)
        self.canvas.create_text(705, 42, text="Health", font=("Arial", 12, "bold"), fill="#e2e8f0", anchor="w")
        self.canvas.create_rectangle(705, 52, 840, 70, fill="#374151")
        health_ratio = max(0, self.player["health"] / self.player["max_health"])
        self.canvas.create_rectangle(705, 52, 705 + 135 * health_ratio, 70, fill="#22c55e")
        self.canvas.create_text(705, 82, text=f"{int(self.player['health'])}/{int(self.player['max_health'])}", font=("Arial", 11), fill="#f8fafc", anchor="w")

        if self.message:
            self.canvas.create_text(450, 38, text=self.message, font=("Arial", 18, "bold"), fill="#facc15")

    def game_loop(self):
        dt = 1 / 60
        if self.state == "playing":
            self.update_player(dt)
            self.update_enemies(dt)
            self.draw_game()
        else:
            self.draw_game()
        self.root.after(16, self.game_loop)


if __name__ == "__main__":
    root = tk.Tk()
    ParryLastStandGame(root)
    root.mainloop()
