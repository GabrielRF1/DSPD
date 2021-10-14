# DSPD (to be renamed, as I forgot what this was supposed to mean)
## Installing the dependencies
    pip install scrapy
Run the above mentioned command to install scrapy

## Running the scraper
    scrapy crawl dict_bot -O output_name.json -a db_name="db_name" -a lang=<lang> -a index="<index>"
To run the scraper, execute the command above.

You have to specify, via the -a options, the name of the SQlite database in which the data will be stored into, the language you will be building the dictionary, and an index.
To choose a language, use its two-letter code, you can check some of the codes here: https://www.sitepoint.com/iso-2-letter-language-codes/.
Also, check the language_settings.py file to see if the language is supported. If not, feel free to add more languages on there.

the index is used to choose which of the links list will be fed to the scraper; check language_settings.py for the lists.

You may also output the dictionary into a json file through the -O option.

## Warnings
Be aware that you'll be sending a lot of requests to Wiktionary, so don't remove the delay option from scrapy's setting file, unless you want to DoS their site, which you shouldn't! 4 seconds might be a bit too conservative, so feel free to lower it a bit, but don't overdo it!

I also recommend keeping the Autothrottle option as it is, but do whatever as long you don't turn it off.

Lastly, keep ROBOTSTXT_OBEY on. if their site doesn't want bots running around specific pages, respect it, please.
