# Author: Arthur Cadore M. Barcella
## importing the libs used in code: 
import sys
import base64
import json
import zlib

def string2json(inputFilename, outputFilename):
    with open(inputFilename) as fin:
        exchangeStr = fin.read().strip()

    ## Firts, remove the firts byte of the string, wich is "0", this byte is used for version purpuses (currently unused). 
    versionByte = exchangeStr[0]

    ## Second, base64 decode the string, to get the zlib compressed string. 
    decoded = base64.b64decode(exchangeStr[1:])

    ## Tird, inflate the compressed string using zlib decompress. The decompression need to use the UTF-8 character formatter. 
    miniJsonStr = zlib.decompress(decoded).decode('utf8')

    ## Once the string was decompressed, the json string will be unserialized to get the correct identation. 
    jsonStr = json.dumps(json.loads(miniJsonStr), sort_keys=True, indent=4) 

    ## Save the json string into archive. 
    with open(outputFilename, 'w') as fout:
        fout.write(jsonStr)

# To run the code script. 
## Verify if the execution has the correct args. 
if len(sys.argv) != 3:
    print("Usage: python script.py <input_filename> <output_filename>")
    sys.exit(1)

inputFilename = sys.argv[1]
outputFilename = sys.argv[2]

## Execute the decompress function
string2json(inputFilename, outputFilename)
