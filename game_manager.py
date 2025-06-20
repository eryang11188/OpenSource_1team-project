# 앞으로 다른 팀원들이 만들 파일들을 불러옵니다.
import dungeon  # D팀원이 만들 dungeon.py
import shop     # B팀원이 만들 shop.py

def main_loop(player):
    """
    플레이어가 살아있는 동안 게임의 메인 루프를 계속 실행합니다.
    """
    print("\n" + "=" * 30)
    print("로그라이크 TRPG에 오신 것을 환영합니다!")
    print("=" * 30)

    while player.is_alive(): # B팀원이 만든 player 객체의 is_alive() 메서드를 사용합니다.
        # 현재 플레이어 상태를 보여줍니다.
        player.show_status()

        # 사용자에게 행동을 선택하라고 요청합니다.
        print("1. 사냥터로 가기")
        print("2. 상점 방문하기")
        print("3. 게임 종료")
        
        choice = input(">> 행동 입력 ")

        if choice == '1':
            dungeon.enter_dungeon(player) # D팀원의 기능
        elif choice == '2':
            shop.open_shop(player)        # B팀원의 기능
        elif choice == '3':
            print("게임을 종료합니다.")
            break # while 루프를 탈출하여 게임을 끝냅니다.
        else:
            print("잘못된 입력입니다.")
        
    print("\nGAME OVER")