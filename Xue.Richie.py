#!/usr/bin/python
print("Content-Type: text/html\n\n")

p = open('pokemon.csv', 'r')
dataList = p.read()

template = """<!DOCTYPE HTML>
    <html>
      <head>
          <link rel="stylesheet" href="mystyle.css"> 
      </head>
      <body>
        @BODY@
      </body>
    </html>"""

TYPES = ["Normal", "Fighting", "Fire", "Water", "Grass", "Flying", "Electric", "Poison", "Rock", "Ground", "Bug", "Ghost", "Fairy", "Steel", "Ice", "Dragon", "Psychic"]

def convertTo2D(data):
    dataList = data.split("\n")
    pokemon2DList = []
    for eachPokemon in dataList:
        pokemon2DList.append(eachPokemon.split(","))
    return pokemon2DList

fullPokemonList = convertTo2D(dataList)[:152]

number = []
names = []

for eachPokemon in fullPokemonList[1:]:
    number.append(eachPokemon[0])
    names.append(eachPokemon[1])

def makeHTMLtable(pokemon2DList):
    table = '\t<table border=1 class="nice" >\n'
    for i in range(len(pokemon2DList) - 1):
        table += "\t\t<tr><td><img src=img/front/" + str(i) + ".png></td><td><img src=img/back/" + str(i) + ".png></td><td>" + pokemon2DList[i][0] + '</td><td><a href="' + pokemon2DList[i][1] + '.html">' + pokemon2DList[i][1] + "</a></td><td>" + pokemon2DList[i][2] + "</td><td>" + pokemon2DList[i][3] + "</td><td>" + pokemon2DList[i][4] + "</td><td>" + pokemon2DList[i][5] + "</td><td>" + pokemon2DList[i][6] + "</td><td>" + pokemon2DList[i][7] + "</td><td>" + pokemon2DList[i][8] + "</td><td>" + pokemon2DList[i][9] + "</td><td>" + pokemon2DList[i][10] + "</td><td>" + pokemon2DList[i][11] + "</td><td>" + pokemon2DList[i][12] + "</td></tr>\n"
    table += "\t</table>\n"
    return table
    
def generateNavBar():
    navBar = '''
        <nav>
        <ul> <!-- these items are navbar options -->
          <li><a href="HomePage.html">HomePage</a></li>
          <li><a href="">Types</a>
             <ul> <!-- these are item2 dropdown options -->
    '''
    navBar2 = '''
             </ul>
          </li>
          <li><a href="AllPokemon.html">All Pokemon</a></li>
          <li><a href="Top10Pokemon.html">Top 10</a></li>
        </ul>
      </nav>
      '''
    typeDropDown = ""
    for i in TYPES:
        VARIABLE = i + "_Type"
        typeDropDown += '''\t\t<li><a href="''' + VARIABLE + '''.html">''' + VARIABLE + '''</a></li>\n'''
    navBarFull = navBar + typeDropDown + navBar2
    return navBarFull

def makeSpecificHTMLtable(pokemon2DList):
    table = '\t<table border=1 class="nice">\n'
    for i in range(len(pokemon2DList)):
        table += "\t\t<tr><td><img src=img/front/" + pokemon2DList[i][0] + ".png></td><td><img src=img/back/" + pokemon2DList[i][0] + ".png></td><td>" + pokemon2DList[i][0] + "</td><td>" + pokemon2DList[i][1] + "</td><td>" + pokemon2DList[i][2] + "</td><td>" + pokemon2DList[i][3] + "</td><td>" + pokemon2DList[i][4] + "</td><td>" + pokemon2DList[i][5] + "</td><td>" + pokemon2DList[i][6] + "</td><td>" + pokemon2DList[i][7] + "</td><td>" + pokemon2DList[i][8] + "</td><td>" + pokemon2DList[i][9] + "</td><td>" + pokemon2DList[i][10] + "</td><td>" + pokemon2DList[i][11] + "</td><td>" + pokemon2DList[i][12] + "</td></tr>\n"
    table += "\t</table>\n"
    return table

def makeSpecificPokemonHTMLtable(pokemon2DList):
        table = '\t<table border=1 class="nice">\n'
        table += "\t\t<tr><td><img src=img/front/" + pokemon2DList[0] + ".png width=192 height=192></td><td><img src=img/back/" + pokemon2DList[0] + ".png width=192 height=192></td><td>" + pokemon2DList[0] + "</td><td>" + pokemon2DList[1] + "</td><td>" + pokemon2DList[2] + "</td><td>" + pokemon2DList[3] + "</td><td>" + pokemon2DList[4] + "</td><td>" + pokemon2DList[5] + "</td><td>" + pokemon2DList[6] + "</td><td>" + pokemon2DList[7] + "</td><td>" + pokemon2DList[8] + "</td><td>" + pokemon2DList[9] + "</td><td>" + pokemon2DList[10] + "</td><td>" + pokemon2DList[11] + "</td><td>" + pokemon2DList[12] + "</td></tr>\n"
        table += "\t</table>\n"
        return table     

def generateHomePage():
    c = open('HomePage.html','w')
    head = "<title>\n"
    head += "\t\tMY HOMEPAGE!\n"
    head += "\t  </title>"
    body = generateNavBar()
    body += "<h1>HomePage</h1>"
    body += "<p>I love Pokemon. I play it everyday on my phone. I play Pokemon Go with my friend Zidane and we go around to catch Pokemon. My favorite Pokemon is Mewtwo because I want to look like them. :) </p>"
    body += '<img src=img/front/150.png width=400 height=400 class="center" ><img src=img/back/150.png width=400 height=400 class="center">'
    body += '''<p>Pokemon Number: 150 
               Pokemon Name: Mewtwo 
               Type: Psychic 
               Total Stats: 680
               HP: 106
               Attack: 110
               Def: 90
               Sp. Atk: 154
               Sp. Def: 90
               Speed: 130
               Generation: 1
               Legendary?: True</p>'''
    final = template.replace("@BODY@", body)
    final = final.replace("@HEAD@", head)
    c.write(final)
    return final
    
def generateTypePage(pokeList,pokeType, outputFileName):
    c = open(f'{outputFileName}.html','w')
    specificPokemonList = []
    specificImgList = []
    for eachPokemon in pokeList:
        if pokeType in eachPokemon:
            specificPokemonList.append(eachPokemon)
            specificImgList.append(eachPokemon[0])
    TypePage = generateNavBar()
    TypePage += makeSpecificHTMLtable(specificPokemonList)
    final = template.replace("@BODY@", TypePage)
    c.write(final)

def generatePokedexPage():
    c = open('AllPokemon.html','w')
    table = generateNavBar()
    table += "<h1>ALL THE POKEMON</h1>"
    table += "<p>This is a pokedex with every single generation one pokemon! There are 151 pokemon and they are all very cool</p>"
    table += makeHTMLtable(convertTo2D(dataList))
    final = template.replace("@BODY@", table) 
    c.write(final)
    c.close
    return final

def generatePokemonPage(outputFileName):
    for aPokemon in range(len(outputFileName) + 1):
        print(aPokemon)
        c = open(f'{outputFileName[aPokemon - 1]}.html','w')
        MonPage = "<h1> Pokemon #: " + number[aPokemon - 1] + "   Name:" + names[aPokemon - 1] + "</h1>"
        MonPage += makeSpecificPokemonHTMLtable(fullPokemonList[aPokemon])
        MonPage += '<a href="allpokemon.html">All Pokemon</a>'
        final = template.replace("@BODY@", MonPage)
        c.write(final)
        c.close()


def generateTop10():
    c = open('Top10Pokemon.html','w')
    table = generateNavBar()
    wholeList = convertTo2D(dataList)
    favorite = [12,35,39,49,86,151,143,133,113,137]
    specificPokemonList = []
    for eachFavorite in favorite:
        specificPokemonList.append(wholeList[eachFavorite])
    table += "<h1> My favorites </h1>"
    table += "<p>I like these because they all have a really adorable design and my girlfriend likes them too so win-win! Porygon is my favorite because it is like polygon and it reminds me of the turtles from Netlogo!</p>"
    table += makeSpecificHTMLtable(specificPokemonList)
    final = template.replace("@BODY@", table)
    c.write(final)
    c.close()

print(generateHomePage())
generatePokedexPage()
for eachType in TYPES:
    generateTypePage(convertTo2D(dataList), eachType, eachType + "_Type")
generateTop10()
generatePokemonPage(names)
