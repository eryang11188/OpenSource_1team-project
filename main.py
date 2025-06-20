import game_manager
from player import Player 

def start_game():
    # Player 클래스는 이름을 인자로 받으므로, 이름을 지정해줍니다.
    player_character = Player("용사")
    
    # 생성한 플레이어 정보를 가지고 game_manager의 메인 루프를 시작시킵니다.
    game_manager.main_loop(player_character)

if __name__ == "__main__":
    start_game()