'''
Базовые классы для автобоя
'''

class BaseCharacter:
    """Базовый класс персонажа"""

    name = '' # Имя
    alias = '' # Прозвище
    
    max_health_points = 0 # Максимум и текущее здоровье
    health_points = 0
    
    max_mana_points = 0 # Максимум и текущая мана
    mana_points = 0
    
    max_stamina_points = 0 # Максимум и текущая выносливость
    stamina_points = 0

    force = 0 # Показатели Сила/скорость/интеллект/атака/защита
    speed = 0
    intelligence = 0

    skills = [] # список способностей(скиллов)

    def __init__(self, in_name, in_alias,
                 in_max_helth, in_max_mana, in_max_stamina,
                 in_force, in_speed, in_intelligence, 
                 *in_skills, in_attack,in_defence):
        
        self.name = in_name
        self.alias = in_alias
        
        self.max_health_points = max(in_max_helth,self.max_health_points)
        self.max_mana_points = max(in_max_mana,self.max_mana_points)
        self.max_stamina_points = max(in_max_stamina,self.max_stamina_points)
        
        self.health_points = self.max_health_points
        self.mana_points = self.max_mana_points
        self.stamina_points = self.max_stamina_points

        self.force = max(in_force,self.force)
        self.speed = max(in_speed,self.speed)
        self.intelligence = max(in_intelligence,self.intelligence)
        self.attack = in_attack
        self.defence = in_defence
        
        self.skills = list(in_skills)            

    def presentation(self):

        print('Персонаж {} {} появился!'.format(self.name,self.alias))
        print('Его здоровье равно: {}'.format(str(self.health_points)))
        print('Мана: {}'.format(str(self.mana_points)))
        print('Выносливость: {}'.format(str(self.stamina_points)))
        print('Его показатели Сила/Скорость/Интеллект/Атака/Защита: {}/{}/{}/{}/{}'.format(self.force,self.speed,self.intelligence,self.attack['Значение'],self.defence['Значение']))
        print('В список его способностей входят: {}'.format(', '.join(self.skills)))

    def is_dead(self):
        return self.health_points <= 0
    
class baseHero(BaseCharacter):
    """Базовый класс героя"""
    
    hero_class_name = ''
    
    def __init__(self, in_class, in_name, in_alias,
                 in_max_helth, in_max_mana, in_max_stamina,
                 in_force, in_speed, in_intelligence,
                 *in_skills,in_attack,in_defence):
        
        super().__init__(in_name, in_alias, in_max_helth, in_max_mana, in_max_stamina, in_force, in_speed, in_intelligence,*in_skills,  in_attack = in_attack,in_defence = in_defence)
        self.hero_class_name = in_class
        
    def presentation(self):
        
        print('{} {} - {} - присоединяется к отряду героев!'.format(self.name,self.alias,self.hero_class_name))
        print('Здоровье: {}'.format(str(self.health_points)))
        print('Мана: {}'.format(str(self.mana_points)))
        print('Выносливость: {}'.format(str(self.stamina_points)))
        print('Показатели Сила/Скорость/Интеллект/Атака/Защита: {}/{}/{}/{}/{}'.format(self.force,self.speed,self.intelligence,self.attack['Значение'],self.defence['Значение']))
        print('В список способностей входят: {}'.format(', '.join(self.skills)))        
        print()

class baseVillain(BaseCharacter):
    """Базовый класс злодея"""
    
    def __init__(self, in_name, in_alias,
                 in_max_helth, in_max_mana, in_max_stamina,
                 in_force, in_speed, in_intelligence,
                 *in_skills, in_attack,in_defence):
        
        super().__init__(in_name, in_alias, in_max_helth, in_max_mana, in_max_stamina, in_force, in_speed, in_intelligence, *in_skills, in_attack = in_attack,in_defence = in_defence)
        
    def presentation(self):
        
        print('Злодей {} {} возродился и угрожает миру!'.format(self.name,self.alias))
        print('Здоровье: {}'.format(str(self.health_points)))
        print('Мана: {}'.format(str(self.mana_points)))
        print('Выносливость: {}'.format(str(self.stamina_points)))
        print('Показатели Сила/Скорость/Интеллект/Атака/Защита: {}/{}/{}/{}/{}'.format(self.force,self.speed,self.intelligence,self.attack['Значение'],self.defence['Значение']))
        print('В список способностей входят: {}'.format(', '.join(self.skills)))        
        print()
  


    
    
