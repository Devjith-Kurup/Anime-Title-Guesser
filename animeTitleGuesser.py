import random

animes = ["ONE PIECE", "NARUTO", "BLUE LOCK", "BLEACH", "MY HERO ACADEMIA", "CHAINSAWMAN", "HUNTER X HUNTER", "SPY X FAMILY", "TOKYO REVENGERS", "TOKYO GHOUL", "RE:ZERO", "ONE PUNCH MAN", "NO GAME NO LIFE", "BLACK CLOVER","GOD OF HIGHSCHOOL", "PRISON SCHOOL", "ATTACK ON TITAN", "EIGHTY SIX", "FOOD WARS", "CAUTIOUS HERO", "JOJO'S BIZZARE ADVENTURE", "HIGHSCHOOL DXD", "SILENT VOICE", "YOUR NAME", "BLACK BUTLER", "ANOTHER", "A PLACE FURTHER THAN UNIVERSE", "SEVEN DEADLY SINS", "INITIAL D", "ASSASINATION CLASSROOM", "BANANA FISH", "FIRE FORCE", "DEATH NOTE", "DEATH PARADE", "VIOLET EVERGARDEN", "WEATHERING WITH YOU", "DEMON SLAYER", "JUJUTSU KAISEN", "DRAGON BALL Z", "YOUR LIE IN APRIL", "MONSTER", "THE DEVIL IS A PART-TIMER", "HIGHSCHOOL OF DEAD", "GARDEN OF WORDS", "FAIRY TAIL", "SWORD ART ONLINE", "PROMISED NEVERLAND", "POKEMON", "GRAND BLUE", "HORIMIYA", "HYOUKA", "MOB PSYCHO 100", "THE DAILY LIFE OF IMMORTAL KING", "VINLAND SAGA", "GINTAMA", "ASOBI ASOBASE", "THE RISING OF THE SHIELD HERO", "FULLMETAL ALCHEMIST", "AHO GIRL", "BERSERK", "BOKU NO PICO", "DEVILMAN CRYBABY", "DR. STONE", "FRUITS BASKET", "BONGOU STRAY DOGS", "CLASSROOM OF THE ELITE", "DARLING IN THE FRANXX", "ERASED", "BEASTARS", "SPIRITED AWAY", "RANKING OF KINGS", "KOMI-SAN CAN'T COMMUNICATE"]

print("---------------------- GUESS THE ANIME TITLE ----------------")

while True:
	try:
		rounds = int(input("\nRounds: "))
	except:
		print("Enter a number!")
		continue
	else:
		if rounds <= 0 or rounds > len(animes):
			print("Enter a number range(1 - " + str(len(animes)) + ")!")
			continue
		break

animeGuessed = []
round = rounds + 1
score = rounds * 10

while True :
	while True:
		anime = list(random.choice(animes))
		if str(anime) in animeGuessed:
			continue
		else:
			animeGuessed.append(str(anime))
			break
			
	animeTitle = []
	guesses = []
	wrongGuess = 0
	
	print("\n-------------------------------------------------------------------")
	print("ROUND " + str(round - rounds))
	
	for letter in anime:
		if letter.isalpha():
			animeTitle.append("_")
		else:
			animeTitle.append(letter)
			
	while "_" in animeTitle:
		print("\n")
		for letter in animeTitle:
			print(letter, end = " ")
			
		guessLetter = input("\n\nGuess a letter: ").upper()
		
		if guessLetter.isalpha() and len(guessLetter) == 1:
			if guessLetter in guesses:
				print("\nYou have already guessed this letter!")
				continue
			else:
				guesses.append(guessLetter)
		else:
			continue
			
		if guessLetter not in anime:
			print("\nThis Anime Title doesnt contain '" + guessLetter + "'!")
			wrongGuess += 1
			score -= 1
			
		while guessLetter in anime:
			for letter in anime:
				if letter == guessLetter:
					animeTitle[anime.index(letter)] = guessLetter
					anime[anime.index(letter)] = "*"
					
	print("\n")
	
	for letter in animeTitle:
		print(letter, end = " ")
	rounds  -= 1
	print("\n\nYou guesssed the Anime Title correctly!")
	
	if wrongGuess > 0:
		print("Guessed wrong letter " + str(wrongGuess) + " times!")
	
	if rounds == 0:
		print("\n-------------------------------------------------------------------")
		print("\nSCORE: " + str(score))
		print("\n-------------------------------------------------------------------")
		break
