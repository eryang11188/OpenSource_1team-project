# 다른 팀원들이 만든 파일들을 불러옵니다.
import dungeon
import shop     
from player import Player # player 객체의 타입을 명확히 하기 위해 import

def main_loop(player: Player): 
    """플레이어가 살아있는 동안 메인 루프를 실행."""
    print("\n" + "=" * 30)
    print("로그라이크 TRPG에 오신 것을 환영합니다!")
    print("=" * 30)

    while player.is_alive(): 
        player.print_status() 

        print("1. 사냥터로 가기")
        print("2. 상점 방문하기")
        print("3. 게임 종료")
        
        choice = input(">> 행동 입력: ")

        if choice == '1':
            dungeon.enter_dungeon(player) 
        elif choice == '2':
            shop.enter_shop(player)      
        elif choice == '3':
            print("게임을 종료합니다.")
            break 
        else:
            print("잘못된 입력입니다.")
        
    print("\nGAME OVER")