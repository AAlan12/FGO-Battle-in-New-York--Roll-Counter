print('~$~'*10+' GILFEST '+'~$~'*10)
rolls = int(input('Enter how many roulettes you want to make: '))
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
print(f'''With {rolls} rolls, are necessary {lotteryCurrency} Lottery Currency, you will get:
Nero Bride CE = {ceNero}
Lore = {lore}
Fou Hp = {fouHp}
Fou Atq = {fouAtq}
Big Diamond = {bigDiamond}
Gold Fruit = {goldFruit}
Silver Fruit = {silverFruit}
Bronze Fruit = {bronzeFruit}
Serpent Jewel = {serpentJewel}
Meteor Horseshoe = {meteorHorseshoe}
Proof Of Hero = {proofOfHero}
Fools Chain = {foolsChain}
Secret Gem Of Saber = {secretGemOfSaber}
Secret Gem Of Archer = {secretGemOfArcher}
Secret Gem Of Lancer = {secretGemOfLancer}
Secret Gem Of Rider = {secretGemOfRider}
Secret Gem Of Caster = {secretGemOfCaster}
Secret Gem Of Assassin = {secretGemOfAssassin}
Secret Gem Of Berserker = {secretGemOfBerserker}
Magic Gem Of Saber = {magicGemOfSaber}
Magic Gem Of Archer = {magicGemOfArcher}
Magic Gem Of Lancer = {magicGemOfLancer}
Magic Gem Of Rider = { magicGemOfRider}
Magic Gem Of Caster = {magicGemOfCaster}
Magic GemO f Assassin = {magicGemOfAssassin}
Magic Gem Of Berserker = {magicGemOfBerserker}
Gem Of Saber = {gemOfSaber}
Gem Of Archer = {gemOfArcher}
Gem Of Lancer = {gemOfLancer}
Gem Of Rider = {gemOfRider}
Gem Of Caster = {gemOfCaster}
Gem Of Assassin = {gemOfAssassin}
Gem Of Berserker = {gemOfBerserker}
Blaze Of Wisdom = {blazeOfWisdom}
Fire Of Wisdom = {fireOfWisdom}
Mana Prism = {manaPrism}
QP = {qP}
Friend Points = {friendPoints *1000}
''')
print('~$~'*10 + ' ZASSHUMU ' + '~$~'*10)     