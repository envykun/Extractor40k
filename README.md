# Extractor 40.000

This tool was created to extract unit data from the new codices of 10th edition of the tabletop game Warhammer 40k.

# How to use

Put any number of pdf files into the input folder and run the python script in the command line with `python main.py`.
Every file will be parsed and the result will be created in the output folder. Every pdf will generate its own json output e.g.
`input/space-marines` -> `output/space-marines.json`.

# JSON Object format

The JSON Object of a single unit within one json file is as follows:
