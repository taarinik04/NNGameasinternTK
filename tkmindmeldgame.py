import random

# Character class
class Character:
    def __init__(self, name):
        self.name = name
        self.intelligence = 50
        self.strength = 50
        self.inventory = []

# Game class
class Game:
    def __init__(self):
        self.words = {
            "brunch": {"hint": "Breakfast and lunch combined." },
            "smog": {"hint": "Smoke and fog combined." },
            "motel": {"hint": "Motor hotel." },
            "staycation": {"hint": "Stay-at-home vacation."},
            "meme": {"hint": "Viral internet idea or image."},
            "shopaholic": {"hint": "Someone addicted to shopping."},
            "bromance": {"hint": "Close friendship between men."},
            "sitcom": {"hint": "Situation Comedy"},
            "frenemy": {"hint": "Friend who is also a rival." },
            "smize": {"hint": "Smiling with your eyes." },
            "mocktail": {"hint": "Non-alcoholic cocktail." },
            "brainstorm": {"hint": "A spontaneous group discussion to produce ideas and ways of solving problems."},
            "lethargic": {"hint": "Lacking in energy; feeling sluggish or lazy."},
            "oxymoron": {"hint": "A figure of speech in which contradictory terms are combined." },
            "paradox": {"hint": "A statement or proposition that seems self-contradictory or absurd but, in reality, expresses a possible truth." },
            "palindrome": {"hint": "A word, phrase, number, or other sequence of characters that reads the same forward and backward." },
            # Add more words here
        }
        self.quests = {
            "quest1 - The Enigmatic Artifact": {
                "title":"Quest Title - The Enigmatic Artifact",
                "description": "You've stumbled upon an ancient artifact in the ruins of Tenebris. It emits a faint glow and hums with mysterious energy.",
                "objective": "Investigate the artifact and uncover its purpose by deciphering its inscriptions.",
                "reward": 20,
                "puzzle": "What ancient civilization is credited with building the Great Pyramids of Giza?",
                "answer": "egyptian"
            },
            "quest2 - The Lost Treasure of Avalon": {
                "title":"Quest Title - The Lost Treasure of Avalon",
                "description": "Legends speak of a hidden treasure buried deep within the mystical forest of Avalon. Can you uncover its secrets?",
                "objective": "Navigate through the enchanted forest, solving riddles left by the forest guardians, to reach the treasure's location.",
                "reward": 20,
                "puzzle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
                "answer": "echo"
            },
            "quest3 - The Pirate's Plunder": {
                "title":"Quest Title - The Pirate's Plunder",
                "description": "Captain Blackbeard's legendary treasure is said to be hidden on the Isle of Skulls. Will you brave the treacherous waters to find it?",
                "objective": "Follow the clues left in Blackbeard's journal to locate the buried treasure chest.",
                "reward": 20,
                "puzzle": "What has a face and two hands but no arms or legs?",
                "answer": "clock"
            },
            "quest4 - The Time Traveler's Dilemma": {
                "title":"Quest Title - The Time Traveler's Dilemma",
                "description": " You've discovered a malfunctioning time machine in Professor Quantum's laboratory. It holds the key to unraveling the mysteries of time travel.",
                "objective": "Repair the time machine by arranging the temporal circuits in the correct sequence.",
                "reward": 20,
                "puzzle": "What comes once in a minute, twice in a moment, but never in a thousand years?(hint - single character answer)",
                "answer": "m"
            },
            "quest5 - The Haunted Manor": {
                "title":"Quest Title - The Haunted Manor",
                "description": "Explore the eerie halls of Ravenwood Manor, where whispers of ghostly apparitions and lost souls abound.",
                "objective": "Find the key to the locked study on the third floor and uncover the truth behind the haunting.",
                "reward": 20,
                "puzzle": "What has keys but can't open locks?",
                "answer": "piano"
            },
            "quest6 - The Crystal Caverns": {
                "title":"Quest Title - The Crystal Caverns",
                "description": "Deep within the Crystal Caverns lies a legendary crystal of immense power, guarded by ancient elemental spirits.",
                "objective": "Navigate through the caverns, overcoming elemental challenges, to reach the heart of the crystal chamber.",
                "reward": 20,
                "puzzle": "I am taken from a mine, and shut up in a wooden case, from which I am never released, and yet I am used by almost every person. What am I?",
                "answer": "pencil"
            },
            "quest7 - The Lost City of Atlantis": {
                "title":"Quest Title - The Lost City of Atlantis",
                "description": "Dive deep into the ocean's depths to uncover the secrets of the fabled Lost City of Atlantis, hidden for millennia beneath the waves.",
                "objective": "Decode the Atlantean glyphs to locate the entrance to the submerged city and retrieve its legendary artifact.",
                "reward": 20,
                "puzzle": "What has a head, a tail, is brown, and has no legs??",
                "answer": "coin"
            },
            "quest8 - The Astral Observatory": {
                "title":"Quest Title - The Astral Observatory",
                "description": "Ascend to the Astral Observatory atop Mount Celestia, where the celestial bodies hold the key to ancient prophecies.",
                "objective": "Align the telescopes to reveal the constellation that foretells the location of the lost star shard.",
                "reward": 20,
                "puzzle": "What has cities, but no houses; forests, but no trees; and rivers, but no water?",
                "answer": "map"
            },
            # Add more quests here
        }

    def create_character(self,name):
        #name = input("Enter your character's name: ")
        return Character(name)

    def play_single_player(self):
        character = self.create_character(input("Enter your character's name: "))
        print(f"Welcome, {character.name}! You are playing a puzzle-solving game.")
        print(f"Your current intelligence is {character.intelligence}.")

        while True:
            print("\nWhat do you want to do?")
            print("1. Solve a puzzle(3 rounds) ")
            print("2. Take a quest")
            print("3. Check inventory")
            print("4. Quit")

            action = input("Enter your choice: ")

            if action == "1":
                for i in range(3):
                    self.solve_puzzle(character)
            elif action == "2":
                self.take_quest(character)
            elif action == "3":
                self.check_inventory(character)
            elif action == "4":
                print(f"Your Intelligence : {character.intelligence}")
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")
    def play_double_player(self):
        character1 = self.create_character(input("Enter player 1's name: "))
        character2 = self.create_character(input("Enter player 2's name: "))

        print(f"Welcome, {character1.name} and {character2.name}! You are playing a puzzle-solving game.")
        print(f"{character1.name}'s current intelligence is {character1.intelligence}.")
        print(f"{character2.name}'s current intelligence is {character2.intelligence}.")
        while True:
            print("\nWhat do you want to do?")
            print("1. Solve a puzzle (Player 1- 3 rounds)")
            print("2. Solve a puzzle (Player 2- 3 rounds)")
            print("3. Take a quest (Player 1)")
            print("4. Take a quest (Player 2)")
            print("5. Check inventory (Player 1)")
            print("6. Check inventory (Player 2)")
            print("7. Quit")

            action = input("Enter your choice: ")

            if action == "1":
                for i in range(3):
                    self.solve_puzzle(character1)
            elif action == "2":
                for i in range(3):
                    self.solve_puzzle(character2)
            elif action == "3":
                self.take_quest(character1)
            elif action == "4":
                self.take_quest(character2)
            elif action == "5":
                self.check_inventory(character1)
            elif action == "6":
                self.check_inventory(character2)
            elif action == "7":
                print("RESULTS ARE:")
                if character1.intelligence > character2.intelligence :
                    print(f"Congratulations, {character1.name} has won the game!")
                    break
                elif character2.intelligence > character1.intelligence:
                    print(f"Congratulations, {character2.name} has won the game!")
                    break
                else :
                    print ("It's a Draw!")            
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

        

    def solve_puzzle(self, character):
        puzzle_id = random.choice(list(self.words.keys()))
        puzzle = self.words[puzzle_id]
        print(f"\n{puzzle['hint']}")
        answer = input("Enter your answer: ")

        if answer.lower() == puzzle_id:
            print()
            print("Congratulations! You solved the puzzle.")
            character.intelligence += 10
            print(f"Your intelligence has increased to {character.intelligence}.")
        else:
            print()
            print("Sorry, that's incorrect. Try again.")

    def take_quest(self, character):
        quest_id = random.choice(list(self.quests.keys()))
        quest = self.quests[quest_id]
        print(f"\n{quest['title']}")
        print(f"\n{quest['description']}")
        print(f"{quest['objective']}")
        print()
        print("Do you want to accept the quest? (yes/no)")

        response = input("Enter your response: ")

        if response.lower() == "yes":
            print("You accepted the quest!")
            print()
            print(f"Solve the puzzle: {quest['puzzle']}")
            answer = input("Enter your answer: ")

            if answer.lower() == quest["answer"]:
                print()
                print("Congratulations! You solved the puzzle.")
                character.intelligence += quest["reward"]
                print()
                print(f"Your intelligence has increased to {character.intelligence}.")
                character.inventory.append(quest_id)
                print(f"Your current inventory: {character.inventory}")
            else:
                print()
                print("Sorry, that's incorrect. Try again.")
        else:
            print("You declined the quest.")

    def check_inventory(self, character):
        print(f"\nYour current inventory: {character.inventory}")
        for item in character.inventory:
            quest = self.quests[item]
            print(f"  - {quest['description']} (Reward: {quest['reward']})")
if __name__ == "__main__":
    game = Game()
    print("Welcome to the Puzzle-Solving Game!")
    print("Do you want to play single player or double player?")
    print("1. Single Player")
    print("2. Double Player")

    choice = input("Enter your choice: ")

    if choice == "1":
        game.play_single_player()
    elif choice == "2":
        game.play_double_player()
    else:
        print("Invalid choice. Goodbye!")

    


   
   
