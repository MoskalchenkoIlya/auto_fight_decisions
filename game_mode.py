from auto_fight_classes import *
from time import *
"""
Игровой режим
"""
class gameMode:
    def __init__(self):
        self.Boss = baseVillain('Астарот','Чёрный дракон',1000,1500,1000,10,10,10,
                        'Кислотный дождь','Чёрное пламя','Дыхание льда','Буря молний','Замлетрясение','Драконий крик','Проклятье','Затмение',
                        in_attack = {'Тип':'Магия','Значение':10},in_defence={'Тип':'Магия','Значение':10})
        self.Boss.presentation()
    
        self.Ranni = baseHero('Ведьма', 'Ренни', 'Катастрофа', 250, 1000,100, 2,1,7,
                         'Буйство огня', 'Инферно', 'Метеоритный дождь',
                         'Ледяной шквал','Цепная молния','Заморозка крови','Сдавливание сердца',
                         'Земляная ловушка','Торнадо','Марионетка теней','Слепота',
                         in_attack = {'Тип':'Магия','Значение':10},in_defence={'Тип':'Магия','Значение':11})
        self.Ranni.presentation()

        self.Marcus = baseHero('Паладин', 'Маркус', 'Святой', 600,300,850,6,1,3,
                          'Очищение', 'Исцеление','Прикрытие','Защитная стойка','Святой удар',
                          'Воскрешение','Провокация','Вспышка света','Призыв Ангела-хранителя',
                          in_attack = {'Тип':'Сила','Значение':11},in_defence={'Тип':'Сила','Значение':10})
        self.Marcus.presentation()

        self.Ulbert = baseHero('Разбойник','Ульберт','Бесшумный',250,200,1300,1,8,1,
                          'Невидимость','Оглушение','Проникновение в тыл','Внезапный удар','Рассечение вен','Рывок с оглушением','Слепота','Вампиризм','Рваный разрез',
                          in_attack = {'Тип':'Ловкость','Значение':10},in_defence={'Тип':'Ловкость','Значение':9})
        self.Ulbert.presentation()

        self.Inheriel = baseHero('Лучница','Инхериэль','Острый глаз', 300,400,1000,4,5,2,
                            'Абсолютный выстрел','Взрывная стрела','Отравленная стрела','Зажигательная стрела','Парализующий выстрел','Уворот','Град стрел',
                            in_attack = {'Тип':'Ловкость','Значение':10},in_defence={'Тип':'Ловкость','Значение':8})
        self.Inheriel.presentation()

        self.Lutik = baseHero('Бард','Лютик','Заноза',200,500,300,1,3,6,
                         'Подбадривание','Ода силы','Сонет скорости','Песенка ума','Ария восстановления','Мелодия воскрешения','Трунь безнадёжности','Марш замедления','Баллада умерщвления',
                         in_attack = {'Тип':'Магия','Значение':1},in_defence={'Тип':'Магия','Значение':1})
        self.Lutik.presentation()

    def base_attack(self,striker,defender):
        print('{} атакует противника - {}'.format(striker.name,defender.name))
        need_to_attack = 1
        pre_damage = 0
        pre_defence = 0
        if not defender.is_dead():
            if striker.attack['Тип'] == 'Магия' and striker.mana_points >= 100:
                striker.mana_points -= 100            
                pre_damage = striker.intelligence * striker.attack['Значение']                
            elif striker.attack['Тип'] == 'Сила' and striker.stamina_points >= 100:
                striker.stamina_points -= 100            
                pre_damage = striker.force * striker.attack['Значение']
            elif striker.attack['Тип'] == 'Ловкость' and striker.stamina_points >= 50:
                striker.stamina_points -= 50            
                pre_damage = striker.speed * striker.attack['Значение']
            else:
                print('Атака невозможна - не хватает мощи((')
                pre_damage = 0
                                
            if defender.defence['Тип'] == 'Магия' and pre_damage != 0:
                pre_defence = defender.intelligence*(1-(1/defender.defence['Значение']))
            elif defender.defence['Тип'] == 'Сила' and pre_damage != 0:
                pre_defence = defender.force*(1-(1/defender.defence['Значение']))
            elif defender.defence['Тип'] == 'Ловкость' and pre_damage != 0:
                pre_defence = defender.speed*(1-(1/defender.defence['Значение']))
            else:
                pre_defence = 0
        else:
            print('Атака невозможна - персонаж мёртв(')
            need_to_attack = 0
        damage = pre_damage - pre_defence
        if need_to_attack > 0:
            if damage > 0:
                defender.health_points -= damage
                print('{} получает {} урона. Теперь здоровье упало до {}.'.format(defender.name,damage,str(max(defender.health_points,0))))
            else:
                print('Атака бесполезна, как и атакующий персонаж)')

if __name__ == '__main__':
    gm = gameMode()
    while True:
        sleep(1)
        if not gm.Ranni.is_dead():
            gm.base_attack(gm.Ranni,gm.Boss)
        else:
            print('{} мертва((('.format(gm.Ranni.name))
        sleep(1)
        if not gm.Marcus.is_dead():
            gm.base_attack(gm.Marcus,gm.Boss)
        else:
            print('{} мертв((('.format(gm.Marcus.name))
        sleep(1)
        if not gm.Ulbert.is_dead():
            gm.base_attack(gm.Ulbert,gm.Boss)
        else:
            print('{} мертв((('.format(gm.Ulbert.name))
        sleep(1)
        if not gm.Inheriel.is_dead():
            gm.base_attack(gm.Inheriel,gm.Boss)
        else:
            print('{} мертва((('.format(gm.Inheriel.name))
        sleep(1)
        if not gm.Lutik.is_dead():
            gm.base_attack(gm.Lutik,gm.Boss)        
        elif gm.Ranni.is_dead() and gm.Marcus.is_dead() and gm.Ulbert.is_dead() and gm.Inheriel.is_dead() and gm.Lutik.is_dead():
            print('Все мертвы((( Пластмассовый мир победил('.format(gm.Inheriel.name))
            break
        else:
            print('{} мертв((('.format(gm.Lutik.name))
        sleep(1)
            
        if not gm.Boss.is_dead():
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
            gm.base_attack(gm.Boss,gm.Ranni)
            sleep(1)
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
            gm.base_attack(gm.Boss,gm.Marcus)
            sleep(1)
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
            gm.base_attack(gm.Boss,gm.Ulbert)
            sleep(1)
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
            gm.base_attack(gm.Boss,gm.Inheriel)
            sleep(1)
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
            gm.base_attack(gm.Boss,gm.Lutik)
            sleep(1)
            print('У злодея осталось {} единиц маны'.format(gm.Boss.mana_points))
        else:
            print('{} мертв)))'.format(gm.Boss.name))
            break
        
