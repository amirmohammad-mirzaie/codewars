# https://www.codewars.com/kata/5962d557be3f8bb0ca000010
def help_clean(sample, cutoff):
    isClean = True
    mean = sum(sample)/len(sample)
    power = [(item-mean)**2 for item in sample]
    sd = ((sum(power))/(len(sample)))**0.5

    for item in (list(sample)):
        if (item > (mean + cutoff * sd)) or (item < (mean - cutoff * sd)):
            isClean = False
            sample.remove(item)
    if isClean:
        return mean

    return help_clean(sample, cutoff)

def clean_mean(sample, cutoff):

    return round(help_clean(sample, cutoff), 2)