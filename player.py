# 플레이어 기능 코드


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.gold = 50
        self.attack = 10
        self.defense = 5
        self.level = 1
        self.exp = 0
        self.inventory = []

    def print_status(self):
        print(f"\n [{self.name}] 상태")
        print(f"레벨: {self.level}  경험치: {self.exp}")
        print(f"체력: {self.hp}/{self.max_hp}")
        print(f"공격력: {self.attack}  방어력: {self.defense}")
        print(f"소지 골드: {self.gold}")
        print(f"인벤토리: {', '.join(self.inventory) if self.inventory else '없음'}\n")

    def take_damage(self, amount):
        damage = max(1, amount - self.defense)
        self.hp -= damage
        print(f"{self.name}은(는) {damage}의 피해를 입었습니다.")
        if self.hp <= 0:
            print(f"{self.name}은(는) 쓰러졌습니다!")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name}의 체력이 {amount}만큼 회복되었습니다. 현재 체력: {self.hp}/{self.max_hp}")

    def earn_gold(self, amount):
        self.gold += amount
        print(f"{amount} 골드를 획득했습니다! (현재 골드: {self.gold})")

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            print(f"{amount} 골드를 사용했습니다. (남은 골드: {self.gold})")
            return True
        else:
            print("골드가 부족합니다.")
            return False

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{amount} 경험치를 얻었습니다!")
        self.check_level_up()

    def check_level_up(self):
        if self.exp >= self.level * 10:
            self.exp -= self.level * 10
            self.level += 1
            self.max_hp += 10
            self.hp = self.max_hp
            self.attack += 2
            self.defense += 1
            print(f"레벨 업! 현재 레벨: {self.level}")
            print(f"체력, 공격력, 방어력이 상승했습니다!")

if __name__ == "__main__":
    p = Player("용사")
    p.print_status()
    p.take_damage(12)
    p.heal(5)
    p.earn_gold(20)
    p.spend_gold(30)
    p.gain_exp(15)
    p.print_status()
