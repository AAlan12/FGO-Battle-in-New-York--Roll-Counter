print('~$~'*10+' GILFEST '+'~$~'*10)
rolls = int(input('Digite quantas roletas você deseja fazer: '))
ceNero = lore = fouHp = fouAtq = bigDiamond = goldFruit = silverFruit = bronzeFruit = serpentJewel = meteorHorseshoe = 0
proofOfHero = foolsChain = secretGemOfSaber = secretGemOfArcher = secretGemOfLancer = secretGemOfRider = 0
secretGemOfCaster = secretGemOfAssassin = secretGemOfBerserker = magicGemOfSaber = magicGemOfArcher = magicGemOfLancer = 0
magicGemOfRider = magicGemOfCaster = magicGemOfAssassin = magicGemOfBerserker = gemOfSaber = gemOfArcher = gemOfLancer = 0
gemOfRider = gemOfCaster = gemOfAssassin = gemOfBerserker = blazeOfWisdom = fireOfWisdom = manaPrism = qP = friendPoints = 0
lotteryCurrency = cont = 0
for rolleta in range(1, rolls +1):
    if rolleta <= 5:
        ceNero += 1
    elif rolleta == 6:
        lore += 1  
    elif rolleta == 7 or rolleta == 9:
        fouHp += 1
    elif rolleta == 8 or rolleta == 10:
        fouAtq +=1
    bigDiamond += 4
    goldFruit += 1
    silverFruit += 2
    bronzeFruit += 3
    serpentJewel += 2
    meteorHorseshoe += 2
    proofOfHero += 3
    foolsChain += 3
    secretGemOfSaber += 1
    secretGemOfArcher += 1
    secretGemOfLancer += 1
    secretGemOfRider += 1
    secretGemOfCaster += 1
    secretGemOfAssassin += 1
    secretGemOfBerserker += 1
    magicGemOfSaber += 2
    magicGemOfArcher += 2
    magicGemOfLancer += 2
    magicGemOfRider += 2
    magicGemOfCaster += 2
    magicGemOfAssassin += 2
    magicGemOfBerserker += 2
    gemOfSaber += 2
    gemOfArcher += 2
    gemOfLancer += 2
    gemOfRider += 2
    gemOfCaster += 2
    gemOfAssassin += 2
    gemOfBerserker += 2
    blazeOfWisdom += 25
    fireOfWisdom += 15
    manaPrism += 45  
    qP += 447
    friendPoints += 8
    lotteryCurrency += 600        
print('''Com {} rolls, são necessários {} Lottery Currency, você vai obter :
ceNero = {}
lore = {}
fouHp = {}
fouAtq = {}
bigDiamond = {}
goldFruit = {}
silverFruit = {}
bronzeFruit = {}
serpentJewel = {}
meteorHorseshoe = {}
proofOfHero = {}
foolsChain = {}
secretGemOfSaber = {}
secretGemOfArcher = {}
secretGemOfLancer = {}
secretGemOfRider = {}
secretGemOfCaster = {}
secretGemOfAssassin = {}
secretGemOfBerserker = {}
magicGemOfSaber = {}
magicGemOfArcher = {}
magicGemOfLancer = {}
magicGemOfRider = {}
magicGemOfCaster = {}
magicGemOfAssassin = {}
magicGemOfBerserker = {}
gemOfSaber = {}
gemOfArcher = {}
gemOfLancer = {}
gemOfRider = {}
gemOfCaster = {}
gemOfAssassin = {}
gemOfBerserker = {}
blazeOfWisdom = {}
fireOfWisdom = {}
manaPrism = {}
qP = {}
friendPoints = {}
'''.format(rolls, lotteryCurrency, ceNero,lore, fouHp ,fouAtq, bigDiamond, goldFruit,silverFruit, bronzeFruit, serpentJewel, meteorHorseshoe, 
proofOfHero, foolsChain,secretGemOfSaber, secretGemOfArcher, secretGemOfLancer, secretGemOfRider, secretGemOfCaster, 
secretGemOfAssassin, secretGemOfBerserker, magicGemOfSaber , magicGemOfArcher , magicGemOfLancer, magicGemOfRider, 
magicGemOfCaster, magicGemOfAssassin, magicGemOfBerserker, gemOfSaber, gemOfArcher, gemOfLancer, gemOfRider, gemOfCaster,
gemOfAssassin, gemOfBerserker, blazeOfWisdom, fireOfWisdom, manaPrism, qP, friendPoints)) 
print('~$~'*10 + ' ZASSHUMU ' + '~$~'*10)     