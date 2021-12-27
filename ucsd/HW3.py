
""" Homework assignment for week 3 """
# Replace this with your name

def words_containing(sentence, letter):
    """ Given a sentence, returns list of words that contain the letter.
        Letter given is lowercase. Sentence can be mixed case, and the
        case should be ignored for searching.
    """
    result = []

    words = sentence.split()

    for word in words:
        if letter in word.lower():
            result.append(word)

    return result

def len_safe(object):
    """Return length of object or -1 if object has no length."""
    try:
        result = len(object)        
    except TypeError:
        result = -1

    return result

def unique(sequence):
    """Yield elements of sequence in order, skipping duplicate values."""
    seen = set()
    for val in sequence:
        if val not in seen:
            seen.add(val)
            yield(val)
