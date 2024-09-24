#Zur Wiederholung:
#
#Grundlegende Datentypen:
#
#   int - kurzform von Integer, speichern zahlen in Python3 bis zum ende des verfügbaren speichers, allerdings ist dieses natürlich systemabhängig
#   float - kurzvorm von floating point, eine dynamische zahl mit unterstützung für nachkommazahlen. Python gibt auch bei integer mathe einen float zurück wenn das endresultat nicht in einen integer passt, z.B. 3(int)/2(int) = 1.5(float)
#   str - strings, aus dem englischen da es sich hier um ketten an zeichen handelt, oder halt um einen string of characters. Ironischerweise besitzt python kein Char type.
#   list - eine datensammlung die beliebige typen in sich haben kann, und auch nicht intern konsistent sein muss. [1, "käse", 2] ist genauso valide wie [1, 2, 3]
#
#Basisfunktionen:
#
#   print("Text Hier!") zum ausgeben von text
#
#   if x == y: zum überprüfen mithilfe von true/false tests
#   
#   while x < 100: zum wiederholen von code solange die prüfung false zurückgibt
#
#   while True: für endlose schleifen die mit einem break innerhalb des codeblocks beender werden
#
#   for element in iterator: fürs benutzen jedes elementes in einem iterator, wie zum beispiel einer liste
#

#   Methoden
#
#   Die implizierten funktionen von typen nennt man Methoden.
#   Die häufigsten bei den simpleren datentypen sind convertoren und checks, wie hier das (eher sinnlose) is_integer()
#

zahl:int = 0
print(zahl.is_integer())

#
#   das gleiche gibt es auch bei floats
#   hier ist das ganze natürlich nützlicher, da es uns sagt ob die zahl eine volle zahl ist
#

kommazahl: float = 1.1
print(kommazahl.is_integer())

#   
#   Bei strings zum beispiel gibt es die methoden upper und lower 
#   nützliche finktionen wenn man zum beispiel string input miteinander vergleichen möchte
#   ohne dabei rücksicht auf groß und kleinschreibung zu nehmen
#
#   wichtig hier - strings können nicht 'in place' modifiziert werden, deswegen geben diese funktionen einen neuen string zurück.
#

wort: str = "Käse"
wort = wort.upper()
print(wort)
wort = wort.lower()
print(wort)

#
#   bei listen geht es mit den methoden etwas weiter, hier werden natürlich methoden gebraucht
#   die liste zu manipulieren durch einsetzen oder ansetzen von elementen
#   erstmal definieren wir eine liste.
#

liste = ["b","c","d"]
print(liste)

#
#   um etwas neues ans ende der liste anzusetzen, benutzen wir append()
#

liste.append("e")
print(liste)    

#
#   wenn wir hingegen ans anfang etwas hinzufügen wollen, benötigen wir einen insert()
#   insert allerdings funktioniert bei jeder stelle, auch in der mitte, deswegen benötigt
#   diese funktion an erster stelle erstmal den 'index' , für den anfang einer liste wäre dies 0
#

liste.insert(0, "a")
print(liste)

#
#   jetzt ist unsere liste nicht mehr ["b","c","d"] sondern ["a","b","c","d","e"]
#   wenn wir also wieder sachen entfernen möchten, benutzen wir befehle wie pop()   
#   ohne angabe eines index entfernt dies immer das letze element
#

buchstabe:str = liste.pop()
print(liste)
print(buchstabe)

#
#   für das entfernen von elementen am anfang hingegen, benötigt die funktion einen index
#   in diesem fall ist es der anfang also wieder die 0
#

buchstabe:str = liste.pop(0)
print(liste)
print(buchstabe)

#   
#   wichtige sind solche befehle da listen nicht arbiträr durch index erweiter werden können,
#   also bei ["a","b","c"] sagen zu wollen das liste[3] = "d" ist, verursacht einen crash
#

zaehler = 0
liste_aufgabe = [1,2,3,4]

#
#   Kurze Aufgabe:
#   schreibe eine while schleife die die zahl 1 vier mal an die liste anfügt
#   also:
#   while zaehler < 4:
#       liste_aufgabe.append(1)
#       zaehler += 1
#
#   anschließend das ganze umgekehrt, für jedes element in der liste einmal liste_aufgabe.pop() auszuführen
#   aufpassen hier - obwohl bei for nummer in liste_aufgabe die variable nummer definiert wrid
#   wird sie hier nicht verwendet.
#

print(liste_aufgabe)

#
#   man würde nun erwarten das die liste leer ist, allerdings wird die liste hierduch nur wieder halbiert
#   for schleifen bei iteratoren zählen im hintergrund ganz geheim, also sobald die liste bei der ersten 4 ankommt,
#   ist für die for schleife die liste vorbei, da vier von den - jetzt maximalen - vier elementan abgelaufen wurden.
#

#
#   strings sind übrigens auch iterierbar und damit vollkommen kompatibel mit for
#

satz = "Python ist eine einfache sprache!"
for buchstabe in satz:
    print(buchstabe)
