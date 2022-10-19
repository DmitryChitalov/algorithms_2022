import sys
from collections import namedtuple
from recordclass import recordclass

users = recordclass(                                           #O(1)
    'Roman123',('us123', True),
    'Dmitry333',('su098', True),
    'Victor544',('ssdf', False),
    'Alex23',('werf65', True),
    'Nikolai65',('soie25', False)
)

print(users)                                        #O(1)
