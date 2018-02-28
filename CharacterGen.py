import random
statsArr = []
statsRawArr = []
with open('data/racelist.txt', 'r') as(raceList):
	raceList = raceList.read().split(', ')
	race = random.choice(list(raceList))
	with open('data/' + race + 'sub.txt', 'r') as(subList):
		subList = subList.read().split(', ')
		subrace = random.choice(list(subList))
		with open('data/' + subrace + 'stats.txt', 'r') as(statsList):
			statsList = statsList.read().split(', ')
			for i in range (6):
				racial = statsList[i]
				rolls = []
				for j in range(4):
					roll = random.randint(1,6)
					rolls.append(roll)
				stat = sum(rolls) - (min(rolls)) + int(racial)
				statRaw = sum(rolls) - (min(rolls)) 
				statsArr.append(stat)
				statsRawArr.append(statRaw)
			with open('data/classlist.txt', 'r') as(classlist):
				classlist = classlist.read().split(', ')
				clss = random.choice(list(classlist))
				with open('data/' + clss + 'archetype.txt', 'r') as(archetypelist):
					archetypelist = archetypelist.read().split(', ')
					archetype = random.choice(list(archetypelist))
					with open('data/backgroundlist.txt', 'r') as(backgroundlist):
						backgroundlist = backgroundlist.read().split(', ')
						background = random.choice(list(backgroundlist))	
print('Race: ', subrace,)
print('Class: ', archetype)
print('Background: ', background)
print('Raw Stats: ', end='')
for repeat in range(6):
	print(statsRawArr[repeat-1], end=' ')
print('\nRacial Bonuses: ', 'STR: ', statsList[0], ', DEX: ', statsList[1], ', CON: ', statsList[2], ', INT: ', statsList[3], ', WIS: ', statsList[4], ', CHA: ', statsList[5])
print('Stats With Bonuses: ', '\n', 'STR: ', statsArr[0], '\n', 'DEX: ', statsArr[1], '\n', 'CON: ', statsArr[2], '\n', 'INT: ', statsArr[3], '\n', 'WIS: ', statsArr[4], '\n', 'CHA: ', statsArr[5])
if subrace == 'Variant Human':
	print('Extra Stat Choices: +1, +1')
elif subrace in('Half-High Elf', 'Half-Wood Elf', 'Half-Drow'):
		print('Extra Stat Choices: +1')
else: 
	print ('No Extra Stat Choices')