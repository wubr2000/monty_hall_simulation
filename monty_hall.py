import numpy as np

def simulate_prizedoor(nsim):
  return np.random.random_integers(0, high=2, size=nsim)

def simulate_guess(nsim):
  return np.zeros(nsim, dtype=np.int)

def goat_door(prizedoors, guesses):

    #strategy: generate random answers, and
    #keep updating until they satisfy the rule
    #that they aren't a prizedoor or a guess
    result = np.random.randint(0, 3, prizedoors.size)
    while True:
        bad = (result == prizedoors) | (result == guesses)
        if not bad.any():
            return result
        result[bad] = np.random.randint(0, 3, bad.sum())

def switch_guess(guesses, goatdoors):

    #strategy: generate random answers, and
    #keep updating until they satisfy the rule
    #that they aren't the original guess or a goat door
    result = np.random.randint(0, 3, guesses.size)
    while True:
        bad = (result == guesses) | (result == goatdoors)
        if not bad.any():
            return result
        result[bad] = np.random.randint(0, 3, bad.sum())

def win_percentage(guesses, prizedoors):
    return (guesses == prizedoors).mean()*100


nsim = 10000

#keep guesses
print "Win percentage when keeping original door"
print win_percentage(simulate_prizedoor(nsim), simulate_guess(nsim))

#switch
pd = simulate_prizedoor(nsim)
guess = simulate_guess(nsim)
goats = goat_door(pd, guess)
guess = switch_guess(guess, goats)
print "Win percentage when switching doors"
print win_percentage(pd, guess).mean()

