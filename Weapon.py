from random import choice

class Weapon:
	def __init__(self):
		self.variety = choice(self.varieties)
		self.condition = choice(list(self.conditions))

	def getCondition(self):
		return self.condition

	def getVariety(self):
		return self.variety

	class Variety:
		def __init__(self, name, pickupChance):
			self.name = name
			self.pickupChance = pickupChance

		def getName(self):
			return self.name

		def getPickupChance(self):
			return self.pickupChance

	class Condition:
		def __init__(self, name):
			self.name = name

		def getName(self):
			return self.name

class Weapon_Melee(Weapon):
	varieties = [Weapon.Variety("sword", 0), Weapon.Variety("baseball bat", 0), Weapon.Variety("axe", 0),
		Weapon.Variety("polearm", 0), Weapon.Variety("chainsaw", 0), Weapon.Variety("spear", 0),
		Weapon.Variety("scythe", 0), Weapon.Variety("dagger", 0), Weapon.Variety("knife", 0),
		Weapon.Variety("club", 0), Weapon.Variety("hammer", 0), Weapon.Variety("stick", 0),
		Weapon.Variety("whip", 0)]
	conditions = [Weapon.Condition("broken"), Weapon.Condition("rusty"), Weapon.Condition("bent"),
		Weapon.Condition("small"), Weapon.Condition("large"), Weapon.Condition("pristine")]

class Weapon_Ranged(Weapon):
	varieties = [Weapon.Variety("crossbow", 0), Weapon.Variety("slingshot", 0), Weapon.Variety("boomerang", 0),
		Weapon.Variety("javelin", 0), Weapon.Variety("shotgun", 0), Weapon.Variety("pistol", 0)]
	conditions = [Weapon.Condition("broken"), Weapon.Condition("jammed"), Weapon.Condition("functional"),
		Weapon.Condition("rusty"), Weapon.Condition("small"), Weapon.Condition("large"),
		Weapon.Condition("pristine")]
