def resolve(d, tokens):
    """
    This function takes in a list of tokens (strings, integers or a combination) and a dictionary from token to token and returns a list of the resolved tokens in the same order.
    """
    key, value = list(d.keys()), list(d.values())
    all = key + value + tokens
    assert [i for i in all if (type(i) == str and not i.isalpha()) or (type(i) == float) or (type(i) == int and i <= 0)] == [], "Error!"
    def recur(token, dictionary):
        if token not in dictionary:
            return token
        else:
                n_token = dictionary.get(token)
                if token == dictionary.get(n_token):
                    return token
                else:
                    try:
                        if n_token in dictionary:
                            return recur(n_token, dictionary)
                        else:
                            return n_token
                    except RecursionError:
                        return token
    resolved = []
    for k in tokens:
        resolved.append((recur(k, d)))
    return resolved

def bin(l_ints, l_bins):
    """
    This function takes a list of integers and a list of the lower limit of bins, write a function named bin to return the number of elements in each bin as a list.
    """
    assert (l_bins[-1] <= l_ints[-1]), "Error!"
    temp = len(l_bins)
    l_bins.append(l_ints[-1] + 1)
    bins = []
    for i in range(temp):
        count = 0
        a, b = l_bins[i], l_bins[i + 1]
        for j in range(a, b):
            if j in l_ints:
                count += 1
        bins.append(count)
    return bins