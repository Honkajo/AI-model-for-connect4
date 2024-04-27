# Käyttöohje

## Asennus ja käynnistys

Asenna riippuvuudet komennolla

```bash
poetry install --no-root
```

Käynnistä peli komennolla

```bash
poetry run invoke start
```

## Säännöt

Pelin tavoitteena on luoda neljän pelimerkin suora joko pysty-, vaaka- tai vinosuuntaan. Kumpikin pelaaja vuorollaan pudottaa yhden pelimerkeistään yhteen seitsemästä sarakkeesta,
kunnes toinen pelaajista saa neljän suoran ja voittaa tai pelilauta täyttyy pelimerkeistä ja tulee tasapeli.

Aloittaja valitaan satunnaisesti ja peliä pelataan komentoriviltä valitsemalla sarake painamalla numeroita 1-7. Voittaja ilmoitetaan pelin päättyessä. 

## Testit

Suorita testit komennolla

```bash
poetry run invoke test
```
Testikattavuusraportti saadaan komennolla
```bash
poetry run invoke coverage
```
Tee Pylint-tarkastukset komennolla
```bash
poetry run invoke pylint
```
