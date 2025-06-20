import random


MONSTERS_DB = [
    {'name': '슬라임', 'hp': 25, 'attack': 8, 'defense': 5, 'exp': 5},
    {'name': '고블린', 'hp': 40, 'attack': 12, 'defense': 7, 'exp': 8},
    {'name': '오크',   'hp': 70, 'attack': 18, 'defense': 10, 'exp': 15},
    {'name': '스켈레톤', 'hp': 50, 'attack': 22, 'defense': 4, 'exp': 12},
    {'name': '마법사', 'hp': 30, 'attack': 28, 'defense': 3, 'exp': 20},
]

def spawn_random_monster():
    
    monster_info = random.choice(MONSTERS_DB).copy() # 원본이 아닌 복사본을 사용
    monster_info['gold'] = random.randint(10, 50) # 10~50 사이의 랜덤 골드 추가
    return monster_info