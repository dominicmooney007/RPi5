#!/usr/bin/env python3
"""
Game Sound Effects with PWMOutputDevice
Collection of classic game sounds and effects
"""

from gpiozero import PWMOutputDevice
from time import sleep

class GameSounds:
    """Collection of game sound effects"""
    
    def __init__(self, pin=22):
        self.buzzer = PWMOutputDevice(pin)
    
    def coin_collect(self):
        """Mario-style coin sound"""
        print("Playing: Coin collect")
        notes = [(988, 0.1), (1319, 0.3)]
        for freq, duration in notes:
            self.buzzer.frequency = freq
            self.buzzer.value = 0.5
            sleep(duration)
        self.buzzer.off()
    
    def power_up(self):
        """Power-up sound effect"""
        print("Playing: Power up")
        for freq in range(200, 800, 50):
            self.buzzer.frequency = freq
            self.buzzer.value = 0.5
            sleep(0.02)
        self.buzzer.off()
    
    def game_over(self):
        """Sad game over sound"""
        print("Playing: Game over")
        notes = [(392, 0.3), (349, 0.3), (330, 0.3), (294, 0.5)]
        for freq, duration in notes:
            self.buzzer.frequency = freq
            self.buzzer.value = 0.3
            sleep(duration)
        self.buzzer.off()
    
    def level_complete(self):
        """Victory fanfare"""
        print("Playing: Level complete")
        notes = [
            (523, 0.1), (659, 0.1), (784, 0.1), (1047, 0.3),
            (784, 0.1), (1047, 0.4)
        ]
        for freq, duration in notes:
            self.buzzer.frequency = freq
            self.buzzer.value = 0.7
            sleep(duration)
        self.buzzer.off()
    
    def jump(self):
        """Character jump sound"""
        print("Playing: Jump")
        for freq in range(300, 600, 50):
            self.buzzer.frequency = freq
            self.buzzer.value = 0.4
            sleep(0.02)
        self.buzzer.off()
    
    def shoot(self):
        """Shooting/laser sound"""
        print("Playing: Shoot")
        self.buzzer.value = 0.5
        for freq in range(1500, 500, -100):
            self.buzzer.frequency = freq
            sleep(0.02)
        self.buzzer.off()
    
    def hit(self):
        """Hit/damage sound"""
        print("Playing: Hit")
        self.buzzer.frequency = 150
        self.buzzer.value = 0.6
        sleep(0.1)
        self.buzzer.frequency = 100
        sleep(0.1)
        self.buzzer.off()
    
    def menu_select(self):
        """Menu selection sound"""
        print("Playing: Menu select")
        self.buzzer.frequency = 800
        self.buzzer.value = 0.3
        sleep(0.05)
        self.buzzer.frequency = 1000
        sleep(0.05)
        self.buzzer.off()
    
    def menu_move(self):
        """Menu navigation sound"""
        print("Playing: Menu move")
        self.buzzer.frequency = 600
        self.buzzer.value = 0.2
        sleep(0.03)
        self.buzzer.off()
    
    def bonus(self):
        """Bonus/achievement sound"""
        print("Playing: Bonus")
        notes = [
            (523, 0.1), (587, 0.1), (659, 0.1),
            (698, 0.1), (784, 0.1), (880, 0.2)
        ]
        for freq, duration in notes:
            self.buzzer.frequency = freq
            self.buzzer.value = 0.5
            sleep(duration)
        self.buzzer.off()
    
    def countdown(self, seconds=3):
        """Countdown timer sound"""
        print(f"Playing: Countdown ({seconds} seconds)")
        for i in range(seconds, 0, -1):
            print(f"  {i}...")
            self.buzzer.frequency = 500
            self.buzzer.value = 0.4
            sleep(0.1)
            self.buzzer.off()
            sleep(0.9)
        # Final beep
        self.buzzer.frequency = 1000
        self.buzzer.value = 0.6
        sleep(0.5)
        self.buzzer.off()
        print("  GO!")
    
    def error(self):
        """Error/wrong answer sound"""
        print("Playing: Error")
        for _ in range(2):
            self.buzzer.frequency = 200
            self.buzzer.value = 0.5
            sleep(0.1)
            self.buzzer.off()
            sleep(0.05)
    
    def cleanup(self):
        """Ensure buzzer is off"""
        self.buzzer.off()

# Demonstration
if __name__ == "__main__":
    print("Game Sound Effects Demonstration")
    print("=" * 40)
    
    # Create game sounds object
    game = GameSounds(22)
    
    # List of all sound effects
    effects = [
        ("Coin Collect", game.coin_collect),
        ("Power Up", game.power_up),
        ("Jump", game.jump),
        ("Shoot", game.shoot),
        ("Hit", game.hit),
        ("Menu Move", game.menu_move),
        ("Menu Select", game.menu_select),
        ("Bonus", game.bonus),
        ("Error", game.error),
        ("Countdown", lambda: game.countdown(3)),
        ("Level Complete", game.level_complete),
        ("Game Over", game.game_over)
    ]
    
    # Play all effects
    for name, effect in effects:
        print(f"\n{name}:")
        effect()
        sleep(1)
    
    print("\n" + "=" * 40)
    print("Game sounds demonstration complete!")
    game.cleanup()
