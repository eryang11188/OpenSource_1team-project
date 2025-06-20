import monster_data
import combat
from player import Player

def enter_dungeon(player: Player):
    #몬스터소환
    monster = monster_data.spawn_random_monster()
    print(f"\n야생의 {monster['name']} 이(가) 나타났다!")
    
    #전투 시작
    combat.start_combat(player, monster)