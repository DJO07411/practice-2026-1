import random
import time

class Combattant:
    def __init__(self, nom, pv, attaque_min, attaque_max):
        self.nom = nom
        self.pv_max = pv
        self.pv = pv
        self.attaque_min = attaque_min
        self.attaque_max = attaque_max

    def est_vivant(self):
        return self.pv > 0

    def attaquer(self, cible):
        degats = random.randint(self.attaque_min, self.attaque_max)
        cible.pv -= degats
        print(f"⚔️ {self.nom} наносит {degats} урона {cible.nom}!")
        if not cible.est_vivant():
            print(f"💀 {cible.nom} побеждён!")
        return degats

    def se_soigner(self):
        soin = random.randint(10, 30)
        self.pv = min(self.pv + soin, self.pv_max)
        print(f"❤️ {self.nom} восстанавливает {soin} HP (текущие HP: {self.pv}/{self.pv_max})")
        return soin

    def afficher_stats(self):
        barre_vie = "█" * int((self.pv / self.pv_max) * 20)
        barre_vide = "░" * (20 - len(barre_vie))
        print(f"{self.nom}: {barre_vie}{barre_vide} {self.pv}/{self.pv_max} HP")


def tour_du_joueur(joueur, ennemi):
    print("\n" + "="*40)
    print("🎮 Ваш ход!")
    joueur.afficher_stats()
    ennemi.afficher_stats()

    action = ""
    while action not in ["1", "2"]:
        action = input("Что вы хотите сделать?\n1 - ⚔️ Атаковать\n2 - ❤️ Лечиться\n> ")

    if action == "1":
        joueur.attaquer(ennemi)
    else:
        joueur.se_soigner()


def tour_de_l_ennemi(joueur, ennemi):
    print("\n" + "="*40)
    print(f"🤖 Ход {ennemi.nom}!")
    time.sleep(1)
    ennemi.attaquer(joueur)


def battle_royale():
    print("🏆 ДОБРО ПОЖАЛОВАТЬ В КОРОЛЕВСКУЮ БИТВУ 🏆")
    print("Вы сразитесь с несколькими противниками... один за другим!\n")

    joueur = Combattant("Герой", 120, 15, 35)

    ennemis = [
        Combattant("Гоблин", 40, 8, 20),
        Combattant("Орк", 60, 12, 28),
        Combattant("Вождь гоблинов", 50, 14, 30),
        Combattant("Тролль", 80, 18, 32),
        Combattant("Повелитель войны", 100, 20, 40)
    ]

    for index, ennemi in enumerate(ennemis):
        print("\n" + "🔥"*20)
        print(f"⚔️ НОВЫЙ ПРОТИВНИК: {ennemi.nom} (противник {index+1}/{len(ennemis)})")
        print("🔥"*20)

        while joueur.est_vivant() and ennemi.est_vivant():
            tour_du_joueur(joueur, ennemi)
            if not ennemi.est_vivant():
                print(f"\n✨ Победа над {ennemi.nom}! ✨")
                if joueur.pv < joueur.pv_max:
                    soin_fin_combat = random.randint(15, 35)
                    joueur.pv = min(joueur.pv + soin_fin_combat, joueur.pv_max)
                    print(f"🎉 Вы восстанавливаете {soin_fin_combat} HP между боями!")
                break

            tour_de_l_ennemi(joueur, ennemi)
            if not joueur.est_vivant():
                print(f"\n💀 ИГРА ОКОНЧЕНА — {joueur.nom} был побеждён {ennemi.nom}...")
                return

        if not joueur.est_vivant():
            break

    if joueur.est_vivant():
        print("\n" + "🏆"*20)
        print("🎉 ПОЗДРАВЛЯЮ! Вы выжили против всех противников! 🎉")
        print("🏆 ВЫ ВЫИГРАЛИ КОРОЛЕВСКУЮ БИТВУ 🏆")
        print("🏆"*20)
    else:
        print("\n💀 ИГРА ОКОНЧЕНА 💀")
        print("Спасибо за игру!")


if __name__ == "__main__":
    battle_royale()
