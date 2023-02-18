import random


def randomer(words):
    return random.choice(words)


names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

names.append(input("Hello. This is you first randomly generated name. Enter your name to begin: "))
while True:
    chosen_name = randomer(names)
    chosen_place = randomer(places)
    chosen_verb = randomer(verbs)
    chosen_noun = randomer(nouns)
    chosen_adverb = randomer(adverbs)
    chosen_detail = randomer(details)

    print(f"{chosen_name} from {chosen_place} {chosen_adverb} {chosen_verb} {chosen_noun} {chosen_detail}")

    cont = input("Do you wish to generate a new sentence? Enter [y] if you mean yes: ")
    if cont == "y":
        inp = input("Do you wish to add to the word pool? Enter [y] if you mean yes: ")
        if inp == "y":
            choice = input("Type [name], [place], [verb], [noun], [adverb] or [detail]: ")
            if choice == "name":
                names.append(input("Enter desired name: "))
            elif choice == "place":
                places.append(input("Enter desired place: "))
            elif choice == "verb":
                verbs.append(input("Enter desired verb: "))
            elif choice == "noun":
                nouns.append(input("Enter desired noun: "))
            elif choice == "adverb":
                adverbs.append(input("Enter desired adverb: "))
            else:
                details.append(input("Enter details: "))
            continue
    else:
        print("Stopping generator!")
        break
