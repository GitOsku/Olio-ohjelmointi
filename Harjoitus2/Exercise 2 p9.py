tuo päivämääräkirjasto
tuo aikakirjasto

funktio jolla tarkistetaan herätysajansyntaksi
    jos annetulla herätysajlla on vain yksi osa 
        jos herätysajan tunnit ovat 0 ja 24 välillä 
            palauta Tosi
        
    jos annetulla herätysajlla on kaksi osaa
         jos herätysajan tunnit ovat 0 ja 24 välillä  ja minuutit ovat 0 - 59 välillä
             palauta tosi
    
    jos annetulla herätysajlla on kolme osaa
         jos herätysajan tunnit ovat 0 ja 24 välillä ja minuutit ovat 0 -59  ja sekuntit ovat 0 - 59 välillä
             palauta tosi
    palauta Epätosi jos nämä ehdot eivät täyty
    
pyydetään käyttäjältä herätysaika
    kutsutaan herätysajan syntaksifunktiota
    saadaan herätysaika
    
lista kuinka monta sekunttia on tunnissa minuutissa ja sekunnnissa
herätyksen sekunnit


päivämäärä kirjastosta nykyhetki
nykyhetki sekuntteina
erotus sekuntteina nykyhetken ja herätyksen välinä

jos erotus on pienempi kuin 0
    lisätään vuorokausi sekuntteina
    
tulosta milloin herätys soi 

ohjelma 'nukkuu' kunnes on herätyksen soittoaika

tulosta herää pahvi

