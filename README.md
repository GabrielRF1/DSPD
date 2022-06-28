# DSPD
## Installing the dependencies
    pip install scrapy
Run the above mentioned command to install scrapy

## Running the scraper
    scrapy crawl dict_bot -O <output_dir>.json -a db_name="<db_dir>" -a lang=<iso-2letter-langcode> -a base_lang=<iso-2letter-langcode> -s JOBDIR=<job_dir>
To run the scraper, execute the command above.

Where, lang is the iso two letter code for the language you want to extract data. base_lang is the language the target language will be translated to (e.g. spanish to english, lang would be es and en would be base_lang). db_name is used to specify in which directory the database can be found (ou should be created). JOBDIR is for specifying where the crawling progress will be saved

You may also output the dictionary into a json file through the -O option.
