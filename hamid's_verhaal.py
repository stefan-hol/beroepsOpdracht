# de imports
import os
import random

# de variablen
q = "q"
w = "w"
e = "e"
r = "r"
t = "t"
y = "y"
naam = ""
naam2 = ""
ant = ""

# de introductie
os. system('cls')
print("Hallo wat is je naam?")
naam = input()
print("Hallo " + naam + " dit verhaal is geïnspireerd op Hamid zijn verhaal en je staat in zijn schoenen.")
print("Hamid is een vluchteling vanuit Syrië en jij gaat een deel van zijn leven meemaken en voor dezelfde keuzes staan.")
print("ben je er klaar voor? [q]=ja [w]=nee")
ant = input()

# het begin
if ant == "q":
	os. system('cls')
	print("Je woont vredig in Syrië met je vrouw en je dochter Amira, daarnaast is je 2de kind onderweg.")
	print("Tot op een dag er een dictator komt die dingen bepaald voor het hele land, alleen op een")
	print("dag zijn de mensen er klaar mee. Er komt een burgeroorlog en jij zit er middenin.")
	print("Paar weken later, de oorlog komt dichterbij en je zoon word geboren hoe noem je hem?")
	print("[r]=Alal(hoop) [t]=Yassin(profeet) [y]=Louay(schild)")
	ant = input()
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1ste keuze
	if ant == "r":
		os. system('cls')
		naam2 = "Alal"
		print(naam2 + " wat een mooie naam.")
		print("8 jaar gaan voorbij je vrouw blijft thuis met de kinderen en poogt ze toch een soort van educatie te geven, ")
		print("terwijl jij met gevaar voor eigen leven werkt in de supermarkt om de hoek. Je leeft in constante angst dat")
		print("de regering dichterbij komt, want je weet dat ze je dan komen halen en alleen omdat je een ander geloof hebt.")
		print("Na nog 2 jaar in angst geleefd te hebben en opeens hoor je een knal, je kijkt waar het vandaan komt. ")
		print("Het kwam van dicht bij thuis, wat doe je?")
		print("[q]= Je rent er geleik naar toe.[w]= Je schreeuwd om hulp en gaat erheen.")
		ant = input()
#2de keuze
		if ant == "q":
			os. system('cls')
			print("Je komt aan en ziet dat je huis op instorten staat, je rent naar binnen en kijkt om je heen dan zie je ")
			print("dat je vrouw geraakt is maar dat je kinderen nog oké zijn. Je pakt ze vast en rent naar buiten en achter je ")
			print("stort het gebouw in met je vrouw er nog in en je geeft jezelf de schuld ook al kon je der niks aan doen.")
			print("Maar gelukkig leven je kinderen nog en op dit moment besluit je te vluchten. Je begint wat rond te vragen en ")
			print("komt uit bij 2 verscillende mannen. De ene laat je in een bootje naar Griekeland varen en de ander laat je in een")
			print("vrachtwagen gaan door Turkije heen. De vrachtwagen is relatief veilig maar je kan wel snel gepakt worden.")
			print("De kans om gepakt te worden op de boot is klein maar het gevaar is groot.")
			print("Dus wat kies je [q]=de vrachtwagen [w]= de boot.")
			ant = input()
#3de keuze___________________________________________________________________________________________________________________________________________-
			if ant == "q":
				os. system('cls')
				print("Je glipt door alle grenscontroles heen en na een helse reis in een overvolle vrachtwagen hebben jij en je kinderen het gehaald.")
				print("Je vraagt asiel aan en na een tijdje in een vluchtelingenkamp te wonen komen jullie dan uiteindelijk in Nederland.")
				print("Jullie leren de taal en burgeren in, de kinderen gaan naar school en jij vind een nieuwe baan.")
				print("Gefeliciteerd je bent nu officieel gevlucht uit Syrië en heb het verhaal uitgespeeld.")
			elif ant == "w":
				os. system('cls')
				print("Je zit op de boot en een paar kilometer voor de kust word een man gek en slaat door het lint,")
				print("de boot dreigt om te slaan en je hebt 2 keuzes.")
				print("[q]= de man kalmeren of [w]= hem van de boot te gooien voordat jullie allemaal omslaan")
				ant = input()
#4de keuze
				if ant == "q":
					print("Je weet hem te kalmeren de rest van de reis is het doodstil maar uiteindelijk kom je aan in Griekeland")
					print("Je vraagt asiel aan en na een tijdje in een vluchtelingenkamp te wonen komen jullie dan uiteindelijk in Nederland.")
					print("Jullie leren de taal en burgeren in, de kinderen gaan naar school en jij vind een nieuwe baan.")
					print("Gefeliciteerd je bent nu officieel gevlucht uit Syrië en heb het verhaal uitgespeeld.")

#einde
				elif ant == "w":
					print("Je gaat naar de man toe en vecht voor een paar seconden maar uiteindelijk vallen jullie beide van de boot en verdrinken jullie.")
					print("Maar om 1 of andere reden ben je toch opgelucht want je kinderen zullen waarschijnlijk het vaste land halen en met die gedachten")
					print("verlaat het laatste beetje lucht je longen. Je kinderen halen de kust en weten in een weeshuis te komen en te leven als wees")
					print("voor de rest van hun leven. Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")
#einde
		else:
			os. system('cls')
			print("Je schreeuwt om hulp en na een paar seconden komt iemand naar je toe je wijst naar de plek waar de klap vandaan kwam en rent erheen.")
			print("Je komt aan rent naar binnen met de man nog voordat je bij de woonkamer komt stort het gebouw in met iedereen erin.")
			print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")
#_____________________________________________________________________________________________________________________________________________________________________
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1ste keuze
	elif ant == "t":
		os. system('cls')
		naam2 = "Yassin"
		print(naam2 + " wat een mooie naam.")
		print("8 jaar gaan voorbij je vrouw blijft thuis met de kinderen en poogt ze toch een soort van educatie te geven, ")
		print("terwijl jij met gevaar voor eigen leven werkt in de supermarkt om de hoek. Je leeft in constante angst dat")
		print("de regering dichterbij komt, want je weet dat ze je dan komen halen en alleen omdat je een ander geloof hebt.")
		print("Na nog 2 jaar in angst geleefd te hebben en opeens hoor je een knal, je kijkt waar het vandaan komt. ")
		print("Het kwam van dicht bij thuis, wat doe je?")
		print("[q]= Je rent er geleik naar toe.[w]= Je schreeuwd om hulp en gaat erheen.")
		ant = input()

#2de keuze
		if ant == "q":
			os. system('cls')
			print("Je rent erheen gaat naar binnen en ziet dat je dochter Amira vast zit, je vrouw dood is en je zoontje bij Amira zit om te helpen")
			print("maar tevergeefs. Je poogt Amira los te maken maar het lukt niet en je besluit Yassin naar buiten te brengen. eenmaal buiten")
			print("wil je naar binnen maar het gebouw is al ingestort. Je denkt bij jezelf wat nou als ik hulp had gehaald dan had Amira nog geleefd")
			print("maar je beseft je dan dat je zoon gespaart is. Op dit moment besluit je te vluchten. Je begint wat rond te vragen en ")
			print("komt uit bij 2 verscillende mannen. De ene laat je in een bootje naar Griekeland varen en de ander laat je in een")
			print("vrachtwagen gaan door Turkije heen. De vrachtwagen is relatief veilig maar je kan wel snel gepakt worden.")
			print("De kans om gepakt te worden op de boot is klein maar het gevaar is groot.")
			print("Dus wat kies je [q]=de vrachtwagen [w]= de boot.")
			ant = input()
#____________________________________________________________________________________________________________________________________________________________________
			if ant == "q":
				os. system('cls')
				print("Je komt aan in Turkije en der word gecontroleerd, je word gevonden en jij en Yassin worden terugestuurd.")
				print("Terug in Syrië sta je voor een keuze, het nog is proberen of te blijven leven in Syrië wat kies je?")
				print("[q]= blijven en [w]= opnieuw vluchten.")
				ant = input()
				if ant == "q":
					print("Je vraagt wat rond naar de bootsman maar het leger heeft in de gaten dat je opnieuw wilt vluchten en opeens midden")
					print("in de nacht worden jij en Yassin ontvoerd en geëxecuteerd.")
					print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")
				elif ant == "w":
					print("Je leeft je leven uit onder het gezach van de dictator, het is zwaar maar jij en Yassin slaan jullie erdoorheen.")
					print("Helaas heb je niet kunnen vluchten maar je hebt toch nog een leven gedeeld met je zoon.")
					print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")

			elif ant == "w":
				print("Je zit op de boot en een paar kilometer voor de kust word een man gek en slaat door het lint,")
				print("de boot dreigt om te slaan en je hebt 2 keuzes.")
				print("[q]= de man kalmeren of [w]= hem van de boot te gooien voordat jullie allemaal omslaan")
				ant = input()
#4de keuze
				if ant == "q":
					print("Je weet hem te kalmeren de rest van de reis is het doodstil maar uiteindelijk kom je aan in Griekeland")
					print("Je vraagt asiel aan en na een tijdje in een vluchtelingenkamp te wonen komen jullie dan uiteindelijk in Nederland.")
					print("Jullie leren de taal en burgeren in. Yassin gaat naar school en jij vind een nieuwe baan.")
					print("Gefeliciteerd je bent nu officieel gevlucht uit Syrië en heb het verhaal uitgespeeld.")

#einde
				elif ant == "w":
					print("je gaat naar de man toe en vecht voor een paar seconden maar uiteindelijk vallen jullie bijden van de boot en verdriken jullie")
					print("maar om 1 of andere reden ben je toch opgelucht want Yassin zal waarschijnlijk het vaste land halen, en met die gedachten")
					print("verlaat ook het laatste beetje lucht je longen. Yassin weet de kust te halen en beland in een weeshuiswaar hij zijn leven leeft zonder familie.")
					print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")
#____________________________________________________________________________________________________________________________________________________________________________________
		else:
			os. system('cls')
			print("Je schreeuwt om hulp en na een paar seconden komt iemand naar je toe je wijst naar de plek waar de klap vandaan kwam en rent erheen.")
			print("Je je gaat naar binnen en ziet dat je dochter Amira vast zit, je vrouw dood is en je zoontje bij Amira zit om te helpen")
			print("Je gaat naar Amira toe en bevrijd haar met de vreemde man en rent geleik met je kinderen naar buiten.")
			print("Op dit moment besluit je te vluchten je vraagt wat rond en je komt al snel bij 2 mannen die je wel kunnen helpen. ")
			print("De ene laat je in een bootje naar Griekeland varen en de ander laat je gaan in een vrachtwagen door")
			print("Turkije heen. De vrachtwagen is relatief veilig maar je kan wel snel gepakt worden.")
			print("De kans om gepakt te worden op de boot is klein maar het gevaar is groot.")
			print("Dus wat kies je [q]=de vrachtwagen [w]= de boot.")
			ant = input()
			if ant == "q":
				os. system('cls')
				print("Je komt aan in Turkije en der word gecontroleerd, je word gevonden en jij en je kinderen worden terugestuurd.")
				print("Terug in Syrië sta je voor een keuze, het nog is proberen of te blijven leven in Syrië wat kies je?")
				print("[q]= blijven en [w]= opnieuw vluchten.")
				ant = input()
				if ant == "q":
					print("Je vraagt wat rond naar de bootsman maar het leger heeft in de gaten dat je opnieuw wilt vluchten en opeens midden")
					print("in de nacht worden jij en je kinderen ontvoerd en geëxecuteerd.")
					print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")
				elif ant == "w":
					print("Je leeft je leven uit onder het gezach van de dictator, het is zwaar maar jij en je kinderen slaan jullie erdoorheen.")
					print("Helaas heb je niet kunnen vluchten maar je hebt toch nog een leven gedeeld met je kinderen.")
					print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")

			elif ant == "w":
				os. system('cls')
				print("Na een tijdje in het bootje te zitten begint het te stormen, der komen hoge golven je vreest voor je leven en na een tijdje ")
				print("houd het bootje het niet meer en het slaat om. Je grijpt je kinderen en je poogt je hoofd boven water te houden maar tevergeefs.")
				print("Na een tijdje houd je het niet meer en verdrink je met je kinderen in je armen.")
				print("Je hebt het helaas niet gehaald en voor jou stopt het verhaal hier.")
#__________________________________________________________________________________________________________________________________________________________________-
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1ste keuze
	else:
		os. system('cls')
		naam2 = "Louay"
		print(naam2 + " wat een mooie naam.")
		print("8 jaar gaan voorbij je vrouw blijft thuis met de kinderen en poogt ze toch een soort van educatie te geven, ")
		print("terwijl jij met gevaar voor eigen leven werkt in de supermarkt om de hoek. Je leeft in constante angst dat")
		print("de regering dichterbij komt, want je weet dat ze je dan komen halen en alleen omdat je een ander geloof hebt.")
		print("Na nog 2 jaar in angst geleefd te hebben en opeens hoor je een knal, je kijkt waar het vandaan komt. ")
		print("Het kwam van dicht bij thuis, wat doe je?")
		print("[q]= Je rent er geleik naar toe.[w]= Je schreeuwd om hulp en gaat erheen.")
		ant = input()
#2de keuze
		if ant == "q":
			os. system('cls')
			print("Je komt aan en ziet dat je huis op instorten staat, je rent naar binnen en kijkt om je heen dan zie je ")
			print("dat je vrouw geraakt is maar dat je kinderen nog oké zijn. Je pakt ze vast en rent naar buiten en achter je ")
			print("stort het gebouw in met je vrouw er nog in en je geeft jezelf de schuld ook al kon je der niks aan doen.")
			print("Maar gelukkig leven je kinderen nog en op dit moment besluit je te vluchten. Je begint wat rond te vragen en ")
			print("komt uit bij 2 verscillende mannen. De ene laat je in een bootje naar Griekeland varen en de ander laat je in een")
			print("vrachtwagen gaan door Turkije heen. De vrachtwagen is relatief veilig maar je kan wel snel gepakt worden.")
			print("De kans om gepakt te worden op de boot is klein maar het gevaar is groot.")
			print("Dus wat kies je [q]=de vrachtwagen [w]= de boot.")
			ant = input()
#3de keuze
			if ant == "q":
				os. system('cls')
				print("Je glipt door alle grenscontroles heen en na een helse reis in een overvolle vrachtwagen hebben jij en je kinderen het gehaald.")
				print("Je vraagt asiel aan en na een tijdje in een vluchtelingenkamp te wonen komen jullie dan uiteindelijk in Nederland.")
				print("Jullie leren de taal en burgeren in, de kinderen gaan naar school en jij vind een nieuwe baan.")
				print("Gefeliciteerd je bent nu officieel gevlucht uit Syrië en heb het verhaal uitgespeeld.")
			elif ant == "w":
				os. system('cls')
				print("Na een tijdje in het bootje te zitten begint het te stormen, der komen hoge golven je vreest voor je leven en na een tijdje ")
				print("houd het bootje het niet meer en het slaat om. Je grijpt je kinderen en je poogt je hoofd boven water te houden maar tevergeefs.")
				print("Na een tijdje houd je het niet meer en verdrink je met je kinderen in je armen.")
				print("Je hebt het helaas niet gehaald en voor jou stopt het verhaal hier.")
#einde
		else:
			os. system('cls')
			print("Je schreeuwt om hulp en na een minuut komt iemand naar je toe je wijst naar de plek waar de klap vandaan kwam en rent erheen.")
			print("Je komt aan maar het is al te laat het gebouw is al ingestort en je bent nu alles kwijt geraakt door 1 man. ")
			print("Je ziet geen nut meer in vluchten en sluit jezelf aan in het verzet waar je het niet lang volhoud,")
			print("want uiteindelijk stap je op een landmijn, en dat is je einde.")
			print("Je hebt het helaas niet gehaald dus voor jou stopt het verhaal hier.")

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# einde
else:
		print("Dat is jammer volgende keer beter.")
