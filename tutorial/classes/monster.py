class Monster(object):

    version = 1.0

    def __init__(self, name, mclass, hitpoints, armor):
        self.name = name
        self.mclass = mclass
        self.hitpoints = hitpoints
        self.armor = armor

    def __str__(self):
        template = "{name} {mclass} {hitpoints}={armor}"
        return template.format(name=self.name, mclass=self.mclass,
                               hitpoints=self.hitpoints, armor=self.armor)

    name = ""
    mclass = ""
    hitpoints = 0
    armor = 0


