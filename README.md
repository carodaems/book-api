# Book API

## Onderwerp

Boeken zijn een belangrijk deel van mijn leven, daarom besloot ik ze als thema te gebruiken voor het maken van mijn API. Ik wou graag iets maken waarmee ik een persoonlijke lijst van al mijn boeken kon bijhouden. Als ik niet weet welk boek te lezen stuurt de API me een suggestie door een willekeurig boek te selecteren uit de lijst. Ik kan boeken toevoegen aan de lijst, hem opvragen, of een specifiek boek opvragen.

## API

**get_books** stuurt een lijst van alle boeken terug die opgeslagen zijn in de API.

**get_book** stuurt aan de hand van een book_id de details terug van een specifiek boek uit de lijst.

**get_random** boek stuurt een willekeurig boek terug dat is opgeslagen in de API.

**get_cover** spreekt de Google Book API aan met behulp van een get request, die met een opgegeven ISBN nummer de link naar de cover van het boek terugstuurt. Deze request wordt enkel gebruikt om deze weer te geven op de frontend.

**create_book** voegt een nieuw boek toe aan de API, de body van deze request moet overeenkomen met het Pydantic Model dat hiervoor voorzien is. 

## Frontend

Op de frontend is het mogelijk gebruik te maken van 2 GET requests en 1 post request. Met behulp van een searchbar is het mogelijk om aan de hand van een Book ID de eigenschappen van een bijhorend boek op te vragen.

Het is ook mogelijk om op een knop te drukken en een random boek uit de lijst te verkrijgen. 

Ten slotte kan je via een form ook een boek toevoegen aan de lijst.

## OpenAPI Docs

![randomizer-service-carodaems cloud okteto net_docs](https://user-images.githubusercontent.com/91262442/202868533-6161719b-1281-480a-9a77-319e9c5ef267.png)

Bij deze maak ik graag een opmerking over een ondervonden probleem met swagger UI. De description parameters die met de query worden meegegeven worden niet getoond op Swagger UI. Deze issue is aangekaart op enkele fora maar heb hier geen oplossing voor gevonden. De syntax die ik hanteerde in mijn .py script zou na enkele checks ook correct moeten zijn. Hierdoor is er dus geen beschrijving van de parameters op OpenDocs, hoewel dit wel de bedoeling was.

## Screenshots

get_books

![randombooks](https://user-images.githubusercontent.com/91262442/202869472-46b730af-3885-4b8e-a2d6-d1191d1009f6.jpg)

get_book

![getbook](https://user-images.githubusercontent.com/91262442/202869499-c803c496-c4f2-4d8c-8b1b-ceafb75900ae.jpg)

get_random

![randombook](https://user-images.githubusercontent.com/91262442/202869538-87824d43-aa5d-404e-8267-8c6236b4dbc9.jpg)

get_cover

![getcover](https://user-images.githubusercontent.com/91262442/202869578-9df6f2bf-7b0c-40bc-a39c-452f00df112c.jpg)

create_book

![image](https://user-images.githubusercontent.com/91262442/202869941-67a7f62b-f0f3-4988-853a-21266fe6425c.png)

![image](https://user-images.githubusercontent.com/91262442/202869967-f78691df-698f-4d5f-b3b3-e2d3e9002b42.png)

## Links

- Link naar hosted API: https://randomizer-service-carodaems.cloud.okteto.net/
- Link naar front-end GitHub: https://github.com/carodaems/alpine-book
- Link naar hosted front-end: https://carodaems.github.io/alpine-book/
