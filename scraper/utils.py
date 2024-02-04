
def get_crypto_abbreviation(crypto_name: str) -> str:
    """
    Obtain the abbreviation of the cryptocurrencie
    returns: str
    """
    abbreviation = ''
    if crypto_name.isupper():
        abbreviation = crypto_name[:len(crypto_name) // 2]
    else:
        for word in reversed(crypto_name):
            if word.isupper():
                abbreviation = word + abbreviation
            else:
                break

    return abbreviation