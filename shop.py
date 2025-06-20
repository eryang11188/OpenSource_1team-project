# 상점 완료

from player import Player

def enter_shop(player: Player):
    print("\n🛒 상점에 오신 것을 환영합니다!")
    while True:
        print("\n[상점 메뉴]")
        print("1. 체력 회복 (+30 HP) - 10골드")
        print("2. 공격력 증가 (+2 ATK) - 20골드")
        print("3. 방어력 증가 (+2 DEF) - 20골드")
        print("4. 아이템 구매 (치유물약) - 15골드")
        print("5. 상점 나가기")

        choice = input("원하는 항목을 선택하세요: ")

        if choice == '1':
            if player.spend_gold(10):
                player.heal(30)
        elif choice == '2':
            if player.spend_gold(20):
                player.attack += 2
                print(f"{player.name}의 공격력이 2만큼 증가했습니다! (현재 ATK: {player.attack})")
        elif choice == '3':
            if player.spend_gold(20):
                player.defense += 2
                print(f"{player.name}의 방어력이 2만큼 증가했습니다! (현재 DEF: {player.defense})")
        elif choice == '4':
            if player.spend_gold(15):
                player.inventory.append("치유물약")
                print("치유물약이 인벤토리에 추가되었습니다.")
        elif choice == '5':
            print("상점을 나갑니다.")
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    # 테스트용 실행 코드
    p = Player("용사")
    p.print_status()
    enter_shop(p)
    p.print_status()
