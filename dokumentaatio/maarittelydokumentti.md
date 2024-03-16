# Vaatimusmäärittely

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatintutkinto

Dokumentaation kieli: suomi

## Ohjelmointikielet

Käytän ohjelmointikielenäni Pythonia ja voin arvioida sekä suomen- että englanninkielisiä töitä. Muita varsinaisia ohjelmointikieliä en hallitse tarpeeksi, jotta voisin vertaisarvioida niitä.

## Tavoite

Projektin tavoitteena on luoda tekoälyvastustaja Connect4-peliin. Toteutan tekoälyn minmax-algoritmilla, jota on tehostettu alpha-beta-karsinnalla. Aion hyödyntää hajautustauluja pelitilanteiden tallentamiseen.

Ongelmat, joita tämä projekti pyrkii ratkaisemaan painottuvat tekoälyn optimointiin. 

+Tavoitteena on
    * pyrkiä karsimaan mahdollisimman paljon turhia siirtoja tekoälyn arvioinnista
    * järjestää mahdolliset siirrot järkevästi(aloitetaan keskeltä ja edetään reunoja kohti) 
    * pyrkiä tehostamaan iteratiivista syvenemistä niin pitkälle kuin aikarajan puitteissa on mahdollista.

## Aika- ja tilavaativuudet

Kun minmax-algoritmia käytetään alpha-beta karsinnalla, aikavaativuus on O(b<sup>d</sup>), missä b on pelipuun haarautumistekijä ja d on puun syvyys. Tilavaativuus puolestaan on O(d). Tämä siksi, että algoritmin tarvitsee muistaa ainoastaan polku juuresta nykyiseen solmuun, joten tilavaativuus riippuu suoraan tutkittavan puun syvyydestä

## Algoritmit

[Minmax-algoritmi](https://en.wikipedia.org/wiki/Minimax)

[Alpha-beta-karsinta](https://en.wikipedia.org/wiki/Alpha-beta_pruning)







