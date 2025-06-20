# 팀원들이 만들 파일을 불러옵니다.
import game_manager
from player import Player 

def start_game():
    """
    게임을 시작하기 위한 준비를 하고, 게임 매니저를 호출합니다.
    """
    player_character = Player()
    
    # 생성한 플레이어 정보를 가지고 game_manager의 메인 루프를 시작시킵니다.
    game_manager.main_loop(player_character)

if __name__ == "__main__":
    start_game()