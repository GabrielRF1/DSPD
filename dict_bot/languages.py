# coding: utf8
# 400+ languages
# extracted from https://en.wiktionary.org/wiki/Index:All_languages <- Page no longer exists
# , from https://meta.wikimedia.org/wiki/Wiktionary#List_of_Wiktionaries
# and from https://en.wikipedia.org/wiki/List_of_official_languages
# and some were added by hand

linguas = ['Oriya', 'West Frisian', 'Kirundi', 'Mossi', 'Ingush', 'Altay', 'Frisian (West)', 'Kinyarwanda',
           'Rutul', 'Ilocano', 'Papiamentu', 'Estonian', 'Inglês Médio', 'Lao', 'Min Nan', 'Tsonga', 'Gbe',
           'Moldávia', 'Fula', 'Romansch', 'Chinês', 'Letão', 'Oniyan', 'Bambara', 'Avar', 'Dioula', 'Tigrinya', 'Nias',
           'Meitei', 'Guarani', 'iídiche', 'ovelha', 'adighe', 'cacas', 'croata', 'iorubá', 'limburguês', 'tebu', 'tártaro',
           'Samoano', 'Russo', 'Tahitiano', 'Português', 'Grego Antigo', 'Dargwa', 'Sotho', 'Quenya', 'Curdo', 'Moksha',
           'Kalaallisut', 'Inglês antigo', 'Sango', 'Lak', 'Ossétia', 'Tswana', 'Filipino', 'Vilamovian', 'Nogai', 'Montenegrino',
           'Língua de sinais do Zimbábue', 'Sudanês', 'Tabasaran', 'Balinesa', 'Dangme', 'Par', 'Lezgian', 'Tcheco', 'Hindi',
           'Hausa', 'Wolof', 'Volapük', 'Balanta', 'Bhojpuri', 'Cree', 'Mandarim', 'Hebraico', 'Coreano', 'Curdo / Curdo',
           'Chickasaw', 'Sesotho', 'Groenlandês', 'Grego', 'Asante Twi', 'Karachay', 'Esperanto', 'Búlgaro', 'Tuvaluano',
           'Erzya', 'Crimean Tatar', 'Mbelime', 'Breton', 'Urdu', 'Papiamento', 'Inuktitut', 'Kashmiri', 'Kashubian', 'Manx',
           'Rapa Nui', 'Betawi', 'Eslovaco', 'Pali', 'Marshallese', 'Gaélico Escocês', 'Fon-Gbe', 'Tammari', 'Twi', 'Asturiano',
           'Waci-Gbe', 'Dzongkha', 'Georgiano', 'Cazaque', 'Abaza', 'Soninke', 'Chukchi', 'Bedik', 'Interlingue', 'Kanuri',
           'Finlandês', 'Kannada', 'Aghul', 'Cebuano', 'Jola', 'Palauan', 'Inuinnaqtun', 'Aragonês', 'Akan', 'Baixo Saxão',
           'Aromeno', 'Nauruano', 'Telugu', 'Interlíngua', 'Maranao', 'Kalasha', 'Surigaonon', 'Gourmanché', 'Amárico',
           'Francês Antigo', 'Grego, Moderno', 'Bashkir', 'Basco', 'Hiri Motu', 'Boko', 'Cabardiano', 'Sardenho', 'Rusyn',
           'Aramaico', 'Javanês antigo', 'Bokmål', 'Irlandês', 'Taiwan Hokkien', 'Hokkien', 'Abkhaz', 'Uzbek', 'Rade', 'Francês',
           'Valão', 'Biali', 'Occitan', 'Akuapem Twi', 'Quirguiz', 'Creole mauriciano', 'Venda', 'Birmês', 'Pashto', 'Berber',
           'Somali', 'Old Armenian', 'Igbo', 'Latim', 'Abkhazian', 'Serbo-Croatian', 'Dogon', 'Seychellois Creole', 'Afrikaans',
           'Uyghur', 'Kumyk', 'Odia', 'Bomu', 'Central Bicolano', 'Khoisan', 'Nateni', 'Corso', 'Norueguês (Nynorsk)',
           'Karelian', 'Gonja', 'checheno', 'luxemburguês', 'anglo-saxão', 'sérvio', 'nórdico antigo', 'malaio', 'bassari',
           'Comorian', 'Shona', 'Sambal', 'Persa', 'Yom', 'Chichewa', 'Lojban', 'Latgalian', 'Zazaki', 'Cherokee', 'Kalmyk',
           'Armênio', 'Alemão', 'Dagbani', 'Assamês', 'Ivatan', 'Shawiya', 'Saraiki', 'Pitjantjatjara', 'Cóptico',
           'Norte Sotho', 'Waray', 'Yakan', 'Ndau', 'Tsakhur', 'Maia', 'Gagauz', 'Maori', 'Havaiano', 'Norueguês',
           'Cornish', 'Zarma', 'Nzema', 'Árabe', 'Guarani', 'Yukaghir', 'Chirbawe', 'Evenki', 'Lingala', 'Alto Sorbiano',
           'Dawro', 'Tailandês', 'Chamorro', 'Dagaare', 'Albanês', 'Faroês', 'Sindi', 'Japonês', 'Bielorrússia', 'Tok Pisin',
           'Língua de Sinais da Nova Zelândia', 'Tongan', 'Lukpa', 'Turco', 'Inupiak', 'Gujarati', 'Língua de Sinais Americana',
           'Old Prussian', 'Tłįchǫ', 'Bikol', 'Nepali', 'Manding', 'Bosnian', 'Samoa', 'Afar', 'Dendi', 'Taiwan Sign Language',
           'Chinês, mandarim', 'Cherkess', 'Nenets', 'Sakizaya', 'ucraniano', 'Serer', 'Kalanga', 'Proto-eslavo', 'dinamarquês',
           'italiano', 'friuliano', 'Inglês', 'kapampangan', 'romeno', 'semai', 'mandinga', 'balkar', 'mari', 'syenara',
           'Kpelle', 'Zhuang', 'Azerbaijani', 'Manx Gaelic', 'Welsh', 'Cantonese Chinese', 'Western Punjabi', 'Maguindanao',
           'Aymara', 'Alemão Médio Médio', 'Cantonês', 'Bozo', 'Safen', 'Maori', 'Ga', 'Suaíli', 'Zulu', 'Sicília', 'Komi',
           'Inuvialuktun', '粵語', 'Fante', 'Divehi', 'macedônio', 'Aja-Gbe', 'Xwela-Gbe', 'malgaxe', 'indonésio', 'Kissi',
           'Chavacano', 'Chipewyan', 'Hiligaynon', 'Norte e Sul Slavey', 'Baixo Sorbian', 'Tetum', 'Toma', 'Fiji Hindi',
           'Tonga', 'Turkmen', 'Kabye', 'Azeri', 'Anii', 'Rajasthani', 'Khmer', 'Susu', 'Gen-Gbe', 'Tajik', 'Gàidhlig',
           'Punjabi', 'Quechua', 'Khanty', 'Goan Konkani', 'Meio-dia', 'Dhivehi', 'Songhay', 'Shan', 'Formosan', 'Sueco',
           'Sinhala', 'Ladin', 'Foodo', 'Waama', 'Bariba', 'Islandês', 'Lituano', 'Dolgan', 'Mansi', "Gwich'in", 'Romani',
           'Galego', 'Bislama', 'Tamil', 'Livonian', 'Náhuatl', 'Escócia', 'Malinke', 'Sena', 'Holandês', 'Swati', 'Ibanag',
           'Hakka', 'crioulo haitiano', 'Oromo', 'vietnamita', 'Buryat', 'Veps', 'Tagalog', 'Romansh', 'Fijian', 'Komi-Permyak',
           'Wamey', 'Ewe-Gbe', 'Maltês', 'Polonês', 'Nambya', 'Kasem', 'Espanhol', 'Pangasinan', 'Javanese', 'Kinaray-a',
           'Selkup', 'Kirghiz', 'Xhosa', 'Buduma', 'Venetian', 'Rukai', 'Slovene', 'Mongol', 'Tasawaq', 'Malayalam',
           'Ossético', 'Sânscrito', 'Tat', 'Nahuatl', 'Nynorsk', 'Tibetano', 'Esloveno', 'Mandjak', 'Marathi', 'Yobe',
           'Sarikoli', 'Bengali', 'Catalão', 'Udmurt', 'Mon', 'Tamasheq', 'Mamara', 'Língua de Sinais Coreana', 'Inglês Simples',
           'Baixo Alemão', 'Norueguês (Bokmål)', 'Tuvan', 'Chuvash', 'Ido', 'Húngaro', 'Sakha', 'Tausug', 'Cingalês',
           'Aklanon', 'Sami', 'Minangkabau', 'Tarantino', 'Mankanya', 'Hassaniya', 'Võro', 'Dari']

lenguas = ['Oriya', 'Frisón occidental', 'Kirundi', 'Mossi', 'Ingushetia', 'Altay', 'Frisón (occidental)', 'Kinyarwanda',
           'Rutul', 'Ilocano', 'Papiamento', 'Estonio', 'Inglés medio', 'Lao', 'Min Nan', 'Tsonga', 'Gbe',
           'Moldovo', 'Fula', 'Romansch', 'Chino', 'Letón', 'Oniyan', 'Bambara', 'Avar', 'Dioula', 'Tigrinya', 'Nias',
           'Meitei', 'Guaraní', 'Yiddish', 'Ewe', 'Adyghe', 'Khakas', 'Croatian', 'Yoruba', 'Limburgish', 'Tebu', 'Tatar',
             'Samoano', 'Ruso', 'Tahitiano', 'Portugués', 'Griego antiguo', 'Dargwa', 'Sotho', 'Quenya', 'Kurdo', 'Moksha',
             'Kalaallisut', 'Inglés antiguo', 'Sango', 'Lak', 'Ossetian', 'Tswana', 'Filipino', 'Vilamovian', 'Nogai', 'Montenegrin',
             'Lenguaje de señas de Zimbabue', 'Sundanés', 'Tabasaran', 'Balinés', 'Dangme', 'Even', 'Lezgian', 'Checo', 'Hindi',
             'Hausa', 'Wolof', 'Volapük', 'Balanta', 'Bhojpuri', 'Cree', 'Mandarín', 'Hebreo', 'Coreano', 'Kurdo/Kurdî',
             'Chickasaw', 'Sesotho', 'Groenlandés', 'Griego', 'Asante Twi', 'Karachay', 'Esperanto', 'Búlgaro', 'Tuvaluano',
             'Erzya', 'Tártaro de Crimea', 'Mbelime', 'Bretón', 'Urdu', 'Papiamento', 'Inuktitut', 'Kashmiri', 'Kashubian', 'Manx',
             'Rapa Nui', 'Betawi', 'Slovak', 'Pali', 'Marshallese', 'Scottish Gaelic', 'Fon-Gbe', 'Tammari', 'Twi', 'Asturian',
             'Waci-Gbe', 'Dzongkha', 'Georgian', 'Kazakh', 'Abaza', 'Soninke', 'Chukchi', 'Bedik', 'Interlingue', 'Kanuri',
             'Finlandés', 'Kannada', 'Aghul', 'Cebuano', 'Jola', 'Palauano', 'Inuinnaqtun', 'Aragonés', 'Akan', 'Bajo sajón',
             'arrumano', 'nauruano', 'telugu', 'interlingua', 'maranao', 'kalasha', 'surigaonon', 'gourmanché', 'amhárico',
             'Francés antiguo', 'Griego, Moderno', 'Bashkir', 'Vasco', 'Hiri Motu', 'Boko', 'Kabardian', 'Sardinian', 'Rusyn',
             'arameo', 'antiguo javanés', 'bokmål', 'irlandés', 'taiwanés Hokkien', 'Hokkien', 'abjasio', 'uzbeco', 'rade', 'francés',
             'Walloon', 'Biali', 'Occitan', 'Akuapem Twi', 'Kyrgyz', 'Mauritian Creole', 'Venda', 'Birman', 'Pashto', 'Berber',
             'Somalí', 'Armenio antiguo', 'Igbo', 'Latín', 'Abjasio', 'Serbocroata', 'Dogon', 'Criollo de Seychelles', 'Afrikaans',
             'Uigur', 'Kumyk', 'Odia', 'Bomu', 'Central Bicolano', 'Khoisan', 'Nateni', 'Córcega', 'Noruego (Nynorsk)',
             'Careliano', 'Gonja', 'Checheno', 'Luxemburgués', 'Anglosajón', 'Serbio', 'Nórdico antiguo', 'Malayo', 'Bassari',
             'Comorano', 'Shona', 'Sambal', 'Persa', 'Yom', 'Chichewa', 'Lojban', 'Latgalian', 'Zazaki', 'Cherokee', 'Kalmyk',
             'armenio', 'alemán', 'Dagbani', 'asamés', 'Ivatan', 'Shawiya', 'Saraiki', 'Pitjantjatjara', 'copto',
             'Sotho del norte', 'Waray', 'Yakan', 'Ndau', 'Tsakhur', 'Maya', 'Gagauz', 'Maorí', 'Hawaiano', 'Noruego',
             'Cornish', 'Zarma', 'Nzema', 'Árabe', 'Guarani', 'Yukaghir', 'Chirbawe', 'Evenki', 'Lingala', 'Alto sorabo',
             'Dawro', 'Tailandés', 'Chamorro', 'Dagaare', 'Albanés', 'Feroés', 'Sindhi', 'Japonés', 'Bielorruso', 'Tok Pisin',
             'Lenguaje de señas de Nueva Zelanda', 'Tongano', 'Lukpa', 'Turco', 'Inupiak', 'Gujarati', 'Lenguaje de señas estadounidense',
             'Prusiano antiguo', 'Tłįchǫ', 'Bikol', 'Nepalí', 'Manding', 'Bosnio', 'Samoa', 'Afar', 'Dendi', 'Lenguaje de señas de Taiwán',
             'Chino, Mandarín', 'Cherkess', 'Nenets', 'Sakizaya', 'Ucraniano', 'Serer', 'Kalanga', 'Proto-Eslavo', 'Danés',
             'Italiano', 'friulano', 'inglés', 'kapampangan', 'rumano', 'semai', 'mandinka', 'balkar', 'mari', 'syenara',
             'Kpelle', 'Zhuang', 'Azerbaijani', 'Manx Gaelic', 'Welsh', 'Cantonese Chinese', 'Western Punjabi', 'Maguindanao',
             'aymara', 'bajo alemán medio', 'cantonés', 'bozo', 'safen', 'maorí', 'ga', 'swahili', 'zulú', 'siciliano', 'komi',
             'Inuvialuktun', '粵語', 'Fante', 'Divehi', 'macedonio', 'Aja-Gbe', 'Xwela-Gbe', 'malgache', 'indonesio', 'Kissi',
             'Chavacano', 'Chipewyan', 'Hiligaynon', 'North and South Slavey', 'Lower Sorbian', 'Tetum', 'Toma', 'Fiji Hindi',
             'Tonga', 'Turkmen', 'Kabye', 'Azeri', 'Anii', 'Rajasthani', 'Khmer', 'Susu', 'Gen-Gbe', 'Tajik', 'Gàidhlig',
             'Punjabi', 'Quechua', 'Khanty', 'Goan Konkani', 'Mediodía', 'Dhivehi', 'Songhay', 'Shan', 'Formosa', 'Sueco',
             'Sinhala', 'Ladin', 'Foodo', 'Waama', 'Bariba', 'Islandés', 'Lituano', 'Dolgan', 'Mansi', 'Gwich\'in', 'Romani',
             'Gallego', 'Bislama', 'Tamil', 'Livonian', 'Náhuatl', 'Scots', 'Malinke', 'Sena', 'Dutch', 'Swati', 'Ibanag',
             'Hakka', 'Criollo haitiano', 'Oromo', 'Vietnamita', 'Buryat', 'Veps', 'Tagalog', 'Romansh', 'Fijian', 'Komi-Permyak',
             'Wamey', 'Ewe-Gbe', 'Maltés', 'Polaco', 'Nambya', 'Kasem', 'Español', 'Pangasinan', 'Javanese', 'Kinaray-a',
             'Selkup', 'Kirghiz', 'Xhosa', 'Buduma', 'Venetian', 'Rukai', 'Slovene', 'Mongolian', 'Tasawaq', 'Malayalam',
             'Ossetic', 'Sánscrito', 'Tat', 'Náhuatl', 'Nynorsk', 'Tibetano', 'Esloveno', 'Mandjak', 'Marathi', 'Yobe',
              'Sarikoli', 'Bengalí', 'Catalán', 'Udmurt', 'Mon', 'Tamasheq', 'Mamara', 'Lenguaje de señas coreano', 'Inglés simple',
              'Bajo alemán', 'Noruego (Bokmål)', 'Tuvan', 'Chuvash', 'Ido', 'Húngaro', 'Sakha', 'Tausug', 'Sinhalese',
              'Aklanon', 'Sami', 'Minangkabau', 'Tarantino', 'Mankanya', 'Hassaniya', 'Võro', 'Dari']

languages = ['Oriya', 'West Frisian', 'Kirundi', 'Mossi', 'Ingush', 'Altay', 'Frisian (West)', 'Kinyarwanda',
             'Rutul', 'Ilocano', 'Papiamentu', 'Estonian', 'Middle English', 'Lao', 'Min Nan', 'Tsonga', 'Gbe',
             'Moldovan', 'Fula', 'Romansch', 'Chinese', 'Latvian', 'Oniyan', 'Bambara', 'Avar', 'Dioula', 'Tigrinya', 'Nias',
             'Meitei', 'Guaraní', 'Yiddish', 'Ewe', 'Adyghe', 'Khakas', 'Croatian', 'Yoruba', 'Limburgish', 'Tebu', 'Tatar',
             'Samoan', 'Russian', 'Tahitian', 'Portuguese', 'Ancient Greek', 'Dargwa', 'Sotho', 'Quenya', 'Kurdish', 'Moksha',
             'Kalaallisut', 'Old English', 'Sango', 'Lak', 'Ossetian', 'Tswana', 'Filipino', 'Vilamovian', 'Nogai', 'Montenegrin',
             'Zimbabwean sign language', 'Sundanese', 'Tabasaran', 'Balinese', 'Dangme', 'Even', 'Lezgian', 'Czech', 'Hindi',
             'Hausa', 'Wolof', 'Volapük', 'Balanta', 'Bhojpuri', 'Cree', 'Mandarin', 'Hebrew', 'Korean', 'Kurdish/Kurdî',
             'Chickasaw', 'Sesotho', 'Greenlandic', 'Greek', 'Asante Twi', 'Karachay', 'Esperanto', 'Bulgarian', 'Tuvaluan',
             'Erzya', 'Crimean Tatar', 'Mbelime', 'Breton', 'Urdu', 'Papiamento', 'Inuktitut', 'Kashmiri', 'Kashubian', 'Manx',
             'Rapa Nui', 'Betawi', 'Slovak', 'Pali', 'Marshallese', 'Scottish Gaelic', 'Fon-Gbe', 'Tammari', 'Twi', 'Asturian',
             'Waci-Gbe', 'Dzongkha', 'Georgian', 'Kazakh', 'Abaza', 'Soninke', 'Chukchi', 'Bedik', 'Interlingue', 'Kanuri',
             'Finnish', 'Kannada', 'Aghul', 'Cebuano', 'Jola', 'Palauan', 'Inuinnaqtun', 'Aragonese', 'Akan', 'Low Saxon',
             'Aromanian', 'Nauruan', 'Telugu', 'Interlingua', 'Maranao', 'Kalasha', 'Surigaonon', 'Gourmanché', 'Amharic',
             'Old French', 'Greek, Modern', 'Bashkir', 'Basque', 'Hiri Motu', 'Boko', 'Kabardian', 'Sardinian', 'Rusyn',
             'Aramaic', 'Old Javanese', 'Bokmål', 'Irish', 'Taiwanese Hokkien', 'Hokkien', 'Abkhaz', 'Uzbek', 'Rade', 'French',
             'Walloon', 'Biali', 'Occitan', 'Akuapem Twi', 'Kyrgyz', 'Mauritian Creole', 'Venda', 'Burmese', 'Pashto', 'Berber',
             'Somali', 'Old Armenian', 'Igbo', 'Latin', 'Abkhazian', 'Serbo-Croatian', 'Dogon', 'Seychellois Creole', 'Afrikaans',
             'Uyghur', 'Kumyk', 'Odia', 'Bomu', 'Central Bicolano', 'Khoisan', 'Nateni', 'Corsican', 'Norwegian (Nynorsk)',
             'Karelian', 'Gonja', 'Chechen', 'Luxembourgish', 'Anglo-Saxon', 'Serbian', 'Old Norse', 'Malay', 'Bassari',
             'Comorian', 'Shona', 'Sambal', 'Persian', 'Yom', 'Chichewa', 'Lojban', 'Latgalian', 'Zazaki', 'Cherokee', 'Kalmyk',
             'Armenian', 'German', 'Dagbani', 'Assamese', 'Ivatan', 'Shawiya', 'Saraiki', 'Pitjantjatjara', 'Coptic',
             'Northern Sotho', 'Waray', 'Yakan', 'Ndau', 'Tsakhur', 'Mayan', 'Gagauz', 'Maori', 'Hawaiian', 'Norwegian',
             'Cornish', 'Zarma', 'Nzema', 'Arabic', 'Guarani', 'Yukaghir', 'Chirbawe', 'Evenki', 'Lingala', 'Upper Sorbian',
             'Dawro', 'Thai', 'Chamorro', 'Dagaare', 'Albanian', 'Faroese', 'Sindhi', 'Japanese', 'Belarusian', 'Tok Pisin',
             'New Zealand Sign Language', 'Tongan', 'Lukpa', 'Turkish', 'Inupiak', 'Gujarati', 'American Sign Language',
             'Old Prussian', 'Tłįchǫ', 'Bikol', 'Nepali', 'Manding', 'Bosnian', 'Samoa', 'Afar', 'Dendi', 'Taiwan Sign Language',
             'Chinese, Mandarin', 'Cherkess', 'Nenets', 'Sakizaya', 'Ukrainian', 'Serer', 'Kalanga', 'Proto-Slavic', 'Danish',
             'Italian', 'Friulian', 'English', 'Kapampangan', 'Romanian', 'Semai', 'Mandinka', 'Balkar', 'Mari', 'Syenara',
             'Kpelle', 'Zhuang', 'Azerbaijani', 'Manx Gaelic', 'Welsh', 'Cantonese Chinese', 'Western Punjabi', 'Maguindanao',
             'Aymara', 'Middle Low German', 'Cantonese', 'Bozo', 'Safen', 'Māori', 'Ga', 'Swahili', 'Zulu', 'Sicilian', 'Komi',
             'Inuvialuktun', '粵語', 'Fante', 'Divehi', 'Macedonian', 'Aja-Gbe', 'Xwela-Gbe', 'Malagasy', 'Indonesian', 'Kissi',
             'Chavacano', 'Chipewyan', 'Hiligaynon', 'North and South Slavey', 'Lower Sorbian', 'Tetum', 'Toma', 'Fiji Hindi',
             'Tonga', 'Turkmen', 'Kabye', 'Azeri', 'Anii', 'Rajasthani', 'Khmer', 'Susu', 'Gen-Gbe', 'Tajik', 'Gàidhlig',
             'Punjabi', 'Quechua', 'Khanty', 'Goan Konkani', 'Noon', 'Dhivehi', 'Songhay', 'Shan', 'Formosan', 'Swedish',
             'Sinhala', 'Ladin', 'Foodo', 'Waama', 'Bariba', 'Icelandic', 'Lithuanian', 'Dolgan', 'Mansi', "Gwich'in", 'Romani',
             'Galician', 'Bislama', 'Tamil', 'Livonian', 'Náhuatl', 'Scots', 'Malinke', 'Sena', 'Dutch', 'Swati', 'Ibanag',
             'Hakka', 'Haitian Creole', 'Oromo', 'Vietnamese', 'Buryat', 'Veps', 'Tagalog', 'Romansh', 'Fijian', 'Komi-Permyak',
             'Wamey', 'Ewe-Gbe', 'Maltese', 'Polish', 'Nambya', 'Kasem', 'Spanish', 'Pangasinan', 'Javanese', 'Kinaray-a',
             'Selkup', 'Kirghiz', 'Xhosa', 'Buduma', 'Venetian', 'Rukai', 'Slovene', 'Mongolian', 'Tasawaq', 'Malayalam',
             'Ossetic', 'Sanskrit', 'Tat', 'Nahuatl', 'Nynorsk', 'Tibetan', 'Slovenian', 'Mandjak', 'Marathi', 'Yobe',
             'Sarikoli', 'Bengali', 'Catalan', 'Udmurt', 'Mon', 'Tamasheq', 'Mamara', 'Korean Sign Language', 'Simple English',
             'Low German', 'Norwegian (Bokmål)', 'Tuvan', 'Chuvash', 'Ido', 'Hungarian', 'Sakha', 'Tausug', 'Sinhalese',
             'Aklanon', 'Sami', 'Minangkabau', 'Tarantino', 'Mankanya', 'Hassaniya', 'Võro', 'Dari']


select_languages_list = {
    'en': languages,
    'pt': linguas,
    'es': lenguas,
}
