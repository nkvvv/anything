import random
import time

class ColorHack:
    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        self.colors = ['🟥','🟦','🟨','🟩','🟧','🟪','🟫']
        self.secret_code = self.create_code()
        self.attemps = 0
        self.history = []
        self.right_key = {}

    def create_code(self):
        secret_code = []
        for i in range(self.difficulty):
            secret_code.append(random.choice(self.colors))
        return secret_code

    def generate_key(self):
        pick_list = []
        for i in range(self.difficulty):
            if i in self.right_key:
                pick_list.append(self.right_key[i])
            else:
                pick_list.append(random.choice(self.colors))
        return pick_list

    def auto_pick_key(self):
        self.attemps += 1
        this_key = self.generate_key()
        while this_key in self.history:
            this_key = self.generate_key()
        self.history.append(this_key)
        return this_key
    
    def try_hack(self):
        key = self.auto_pick_key()
        key_string = ""
        for k in key:
            key_string = f"{key_string}{k} "
        print(f"{key_string}\x1b[1;34m< \x1b[0m \x1b[1;33m{self.attemps}\x1b[0m")
        if key == self.secret_code:
            print("\x1b[1;32mКлюч подобран!\x1b[0m")
            return True
        else:
            index = 0
            for k in key:
                if k == self.secret_code[index]:
                    self.right_key[index] = k
                index+=1
        return False

def play_test():
    game = ColorHack(32)
    while True:
        if game.try_hack():
            break
        time.sleep(0.1)
    return game.attemps
    
print(f"\x1b[1;36mУспех с {play_test()} попытки!\x1b[0m")