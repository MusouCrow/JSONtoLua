'''
# Desc: A terminal tool of JSON to Lua
# Author: Musoucrow
# Since: 2017-5-08
'''

import sys
import json

fileobj = open(sys.argv[1], "r")
content = fileobj.read()
fileobj.close()

content = json.dumps(json.loads(content), indent = 4)
lst = list(content)
length = len(content)
frontPos = -1

for i in range(0, length):
    char = lst[i]
    if (char == '['):
        lst[i] = '{'
    elif (char == ']'):
        lst[i] = '}'
    elif (char == '"' and i < length - 1 and lst[i+1] != ':'):
        frontPos = i
    elif (char == ':' and i >= 2 and lst[i-1] == '"' and lst[i-2] != ':' and frontPos > -1):
        lst[frontPos] = ''
        lst[i-1] = ''
        lst[i] = " ="
        frontPos = -1

lua_path = sys.argv[1].replace(".json", ".lua")
fileobj = open(lua_path, "w")
fileobj.write("return " + ''.join(lst))
fileobj.close()

print("Lua file has been saved to " + lua_path)
