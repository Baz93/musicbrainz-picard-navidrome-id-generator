PLUGIN_NAME = 'Random String Generator'
PLUGIN_AUTHOR = 'Baz93'
PLUGIN_DESCRIPTION = '''
<p>This plugin adds a new scripting function to generate a random string of a specified length.</p>
'''
PLUGIN_VERSION = '1.0'
PLUGIN_API_VERSIONS = ['2.0']

import string
import random
from picard.script import register_script_function

def func_random_string(parser, length):
    length = int(length)
    if length < 1:
        return ""
    letters = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

register_script_function(func_random_string, name='random_string',
    documentation="""`$random_string(length)`

Generates a random string of the specified `length`.""")
