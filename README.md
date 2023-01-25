# Passport Data Extractor

`extractor` is is a command-line interface program to parse and extract data and photo from passport scans.


## Installation and usage
1. Clone github repository:

       git clone https://github.com/abdusattorov/extractor

2. Change directory to `.../passport-extractor`

       cd .../passport-extractor`

3. Create a virtual environment and activate it:

       python -m venv .venv
       source .venv/bin/activate

       *Use python3 on MacOS and Linux*

3. Install necessary dependencies:

       pip install -r requirements.txt

4. Install tesseract.

After finishing the installation process and assuming your current directory is `.../passport-extractor`, you can run `extractor` as a
package:

    python extractor -h

or, provided, your current directory is `/passport-extractor/extractor`, you can directly run the
module:

    python -m extractor -h
    python extractor.py -h


## Functionality

To see help message, please, use `-h/--help` argument: `rss_feed_reader -h`.

    usage: extractor.py [FILEPATH] [--print] [--nophoto]
                        [-h]

    Command-line utility to extract passport photo and data.

    positional arguments:
    FILEPATH    The path to the file.

    optional arguments:
    -h, --help  show this help message and exit
    --print     Prints the result in console instead of saving it into a json file
    --nophoto   Doesn't crop the passport photo


  ## Testing

Tests are yet to be written.

***Test coverage is xx%.***

## Main dependencies
1. OpenCV
2. PassportEye
3. Tesseract