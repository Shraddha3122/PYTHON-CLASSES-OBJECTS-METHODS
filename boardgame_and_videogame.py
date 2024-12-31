# Create a Game class with a BoardGame and VideoGame subclass. 
#Include methods to display rules specific to each subclass.

class Game:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def display_info(self):
        return f"Game Title: {self.title}, Genre: {self.genre}"


class BoardGame(Game):
    def __init__(self, title, genre, player_count, play_time):
        super().__init__(title, genre)
        self.player_count = player_count
        self.play_time = play_time

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Player Count: {self.player_count}, Play Time: {self.play_time} minutes"

    def display_rules(self):
        return f"Rules for '{self.title}':\n1. Set up the board.\n2. Players take turns.\n3. Follow the instructions on the cards.\n4. The first player to reach the goal wins."


class VideoGame(Game):
    def __init__(self, title, genre, platform, multiplayer):
        super().__init__(title, genre)
        self.platform = platform
        self.multiplayer = multiplayer

    def display_info(self):
        base_info = super().display_info()
        multiplayer_info = "Multiplayer: Yes" if self.multiplayer else "Multiplayer: No"
        return f"{base_info}, Platform: {self.platform}, {multiplayer_info}"

    def display_rules(self):
        return f"Rules for '{self.title}':\n1. Use the controller to navigate.\n2. Complete missions to progress.\n3. Follow the on-screen prompts.\n4. Have fun and enjoy the game!"



if __name__ == "__main__":
    board_game = BoardGame("Catan", "Strategy", 3, 90)
    video_game = VideoGame("The Legend of Zelda: Breath of the Wild", "Action-Adventure", "Nintendo Switch", True)

    print(board_game.display_info())
    print(board_game.display_rules())

    print(video_game.display_info())
    print(video_game.display_rules())