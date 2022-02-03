import re
from collections import Counter

find_words = re.findall(r'\w+', open('onegin.txt',
                                     encoding='utf-8').read().lower())

print(Counter(find_words).most_common(10))  # -> [('и', 155), ('в', 68),
# ('не', 48), ('он', 45), ('я', 45), ('на', 38), ('как', 32),
# ('но', 25), ('что', 25), ('с', 24)]
