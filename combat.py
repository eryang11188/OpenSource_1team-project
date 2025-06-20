import time
from player import Player

def start_combat(player: Player, monster: dict):
    """
    플레이어 객체와 몬스터 딕셔너리를 받아 전투를 진행합니다.
    이제 플레이어는 매 턴마다 행동을 선택할 수 있습니다.
    """
    print("\n--- 전투 시작 ---")
    while player.is_alive() and monster['hp'] > 0:

        # --- 플레이어 턴 ---
        # 플레이어가 올바른 행동을 선택할 때까지 반복합니다.
        while True:
            print("\n어떤 행동을 하시겠습니까?")
            print("1. 공격")
            print("2. 물약 사용 (치유물약)")
            print("3. 도망가기")
            choice = input(">> 행동 선택: ")

            if choice == '1':
                # --- 1. 공격 ---
                print(f"\n{player.name}의 공격!")
                damage_to_monster = max(1, player.attack - monster['defense'])
                monster['hp'] -= damage_to_monster
                print(f"{monster['name']}에게 {damage_to_monster}의 피해를 입혔습니다. (몬스터 HP: {max(0, monster['hp'])})")
                break # 행동을 마쳤으므로 선택 루프 탈출

            elif choice == '2':
                # --- 2. 물약 사용 ---
                if "치유물약" in player.inventory:
                    player.inventory.remove("치유물약") # 인벤토리에서 물약 하나 제거
                    player.heal(30) # shop.py에서 설정한 회복량만큼 회복
                    print("치유물약을 사용하여 체력을 회복했습니다.")
                    break # 행동을 마쳤으므로 선택 루프 탈출
                else:
                    print("사용할 수 있는 치유물약이 없습니다!")
                    # 행동을 선택하지 못했으므로 다시 선택지로 돌아갑니다.
                    
            elif choice == '3':
                # --- 3. 도망가기 ---
                print("전투에서 도망칩니다!")
                print("--- 전투 종료 ---")
                return # 전투 함수 자체를 종료하고 마을(메인 메뉴)로 돌아갑니다.

            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")
        
        # 몬스터가 플레이어의 공격으로 죽었는지 확인
        if monster['hp'] <= 0:
            print(f"\n{monster['name']}을(를) 물리쳤습니다!")
            player.earn_gold(monster['gold'])
            player.gain_exp(monster['exp'])
            break # 전투 루프 탈출

        # --- 몬스터의 턴 ---
        time.sleep(1) # 잠시 멈춰서 전투 흐름 조절
        print(f"\n{monster['name']}의 공격!")
        player.take_damage(monster['attack']) # player.py의 take_damage 메서드 사용

    # 플레이어가 패배했는지 확인
    if not player.is_alive():
        print("플레이어가 쓰러졌습니다...")
    
    print("--- 전투 종료 ---")