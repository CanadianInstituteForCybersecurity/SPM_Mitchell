#Silly song to test using github and travis ci

beer = 99

while (beer > 1):
    if (beer > 2):
        print(beer, " bottles of beer on the wall, ",beer," bottles of beer, take one down pass it around ", beer-1, " bottles of beer on the wall")
        beer = beer-1
    else:
        print(beer, " bottles of beer on the wall, ",beer," bottles of beer, take one down pass it around ", beer-1, " bottle of beer on the wall")
        beer = beer-1

print("One bottle of beer on the wall, one bottle of beer, take it down pass it around no more bottles of beer on the wall")
beer = beer-1

print("The song is over, thank you for reading it.")