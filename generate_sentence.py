import pickle
import random
import sys
from os import system

def generate_sen(screen_name):

	chain = pickle.load(open("downloaded/%s/chain.p" % screen_name, "rb"))

	new_review = []
	sword1 = "BEGIN"
	sword2 = "NOW"

	while True:
	    sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
	    if sword2 == "END":
	        break
	    new_review.append(sword2)

	return (' '.join(new_review))

if __name__ == '__main__':
    if(sys.argv[1] == "-say"):
        sentence = generate_sen(sys.argv[2]).replace("\"",'').replace("'", '').replace("#", '');
        print("\n" + sentence + "\n")
        system("say '%s'" % sentence)
    else:
        sentence = generate_sen(sys.argv[1]).replace("\"",'').replace("'", '').replace("#", '');
        print("\n" + sentence + "\n")
