def extract_values(data, output_file):
        with open(output_file, 'w') as f:
                for value in data.values():
                        f.write(f"{value}\n")


data = {"AFGHANISTAN": "93",
        "AFGHANISTAN (Duplicate)": "93",
        "ALBANIA": "355",
        "ALBANIA (Duplicate)": "355",
        "ALGERIA": "213",
        "ALGERIA (Duplicate)": "213",
        "AMERICAN SAMOA": "1-684",
        "AMERICAN SAMOA (Duplicate)": "1-684",
        "ANDORRA": "376",
        "ANDORRA (Duplicate)": "376",
        "ANGOLA": "244",
        "ANGOLA (Duplicate)": "244",
        "ANGUILLA": "1-264",
        "ANGUILLA (Duplicate)": "1-264",
        "ANTARCTICA AU": "672",
        "ANTARCTICA GSM AQ": "672",
        "ANTIGUA AND BARBUDA": "1-268",
        "ANTIGUA AND BARBUDA (Duplicate)": "1-268",
        "ARGENTINA": "54",
        "ARGENTINA (Duplicate)": "54",
        "ARMENIA": "374",
        "ARMENIA (Duplicate)": "374",
        "ARUBA": "297",
        "ARUBA (Duplicate)": "297",
        "ASCENSION": "247",
        "AUSTRALIA": "61",
        "AUSTRALIA (Duplicate)": "61",
        "AUSTRIA": "43",
        "AUSTRIA (Duplicate)": "43",
        "AZERBAIJAN": "994",
        "AZERBAIJAN (Duplicate)": "994",
        "BAHAMAS": "1-242",
        "BAHAMAS (Duplicate)": "1-242",
        "BAHRAIN": "973",
        "BAHRAIN (Duplicate)": "973",
        "BANGLADESH": "880",
        "BANGLADESH (Duplicate)": "880",
        "BARBADOS": "1-246",
        "BARBADOS (Duplicate)": "1-246",
        "BELARUS": "375",
        "BELARUS (Duplicate)": "375",
        "BELGIUM": "32",
        "BELGIUM (Duplicate)": "32",
        "BELIZE": "501",
        "BELIZE (Duplicate)": "501",
        "BENIN": "229",
        "BENIN (Duplicate)": "229",
        "BERMUDA": "1-441",
        "BERMUDA (Duplicate)": "1-441",
        "BHUTAN": "975",
        "BHUTAN (Duplicate)": "975",
        "BOLIVIA": "591",
        "BOLIVIA (Duplicate)": "591",
        "BOSNIA AND HERZEGOVINA": "387",
        "BOSNIA AND HERZEGOVINA (Duplicate)": "387",
        "BOTSWANA": "267",
        "BOTSWANA (Duplicate)": "267",
        "BRAZIL": "55",
        "BRAZIL (Duplicate)": "55",
        "BRITISH VIRGIN ISLANDS": "1-284",
        "BRITISH VIRGIN ISLANDS (Duplicate)": "1-284",
        "BRUNEI DARUSSALAM": "673",
        "BRUNEI DARUSSALAM (Duplicate)": "673",
        "BULGARIA": "359",
        "BULGARIA (Duplicate)": "359",
        "BURKINA FASO": "226",
        "BURKINA FASO (Duplicate)": "226",
        "BURUNDI": "257",
        "BURUNDI (Duplicate)": "257",
        "CAMBODIA": "855",
        "CAMBODIA (Duplicate)": "855",
        "CAMEROON": "237",
        "CAMEROON (Duplicate)": "237",
        "CAPE VERDE": "238",
        "CAPE VERDE (Duplicate)": "238",
        "CAYMAN ISLANDS": "1-345",
        "CAYMAN ISLANDS (Duplicate)": "1-345",
        "CENTRAL AFRICAN REP": "236",
        "CENTRAL AFRICAN REP (Duplicate)": "236",
        "CHAD": "235",
        "CHAD (Duplicate)": "235",
        "CHILE": "56",
        "CHILE (Duplicate)": "56",
        "CHINA": "86",
        "CHINA (Duplicate)": "86",
        "COLOMBIA": "57",
        "COLOMBIA (Duplicate)": "57",
        "COMOROS": "269",
        "COMOROS MOBILE": "269",
        "CONGO": "242",
        "CONGO (Duplicate)": "242",
        "COOK ISLANDS": "682",
        "COSTA RICA": "506",
        "COSTA RICA (Duplicate)": "506",
        "CROATIA": "385",
        "CROATIA (Duplicate)": "385",
        "CUBA": "53",
        "CYPRUS NORTH TURKCELL MOBILE": "90-392",
        "CYPRUS": "357",
        "CZECH REPUBLIC": "420",
        "CZECH REPUBLIC (Duplicate)": "420",
        "DENMARK": "45",
        "DENMARK OTHER MOBILE": "45",
        "DIEGO GARCIA": "246",
        "DJIBOUTI": "253",
        "DOMINICA": "1-767",
        "DOMINICA (Duplicate)": "1-767",
        "DOMINICAN REPUBLIC": "1-809, 1-829, 1-849",
        "DOMINICAN REPUBLIC (Duplicate)": "1-809, 1-829, 1-849",
        "DR CONGO AFRICELL MOBILE": "243",
        "DR CONGO FIXED": "243",
        "EAST TIMOR": "670",
        "EAST TIMOR (Duplicate)": "670",
        "ECUADOR": "593",
        "ECUADOR (Duplicate)": "593",
        "EGYPT": "20",
        "EGYPT (Duplicate)": "20",
        "EL SALVADOR": "503",
        "EL SALVADOR (Duplicate)": "503",
        "EMSAT": "882",
        "EQUATORIAL GUINEA": "240",
        "EQUATORIAL GUINEA (Duplicate)": "240",
        "ERITREA": "291",
        "ERITREA (Duplicate)": "291",
        "ESTONIA": "372",
        "ESTONIA (Duplicate)": "372",
        "ETHIOPIA": "251",
        "ETHIOPIA (Duplicate)": "251",
        "FALKLAND ISLANDS": "500",
        "FAROE ISLANDS": "298",
        "FAROE ISLANDS (Duplicate)": "298",
        "FIJI": "679",
        "FIJI (Duplicate)": "679",
        "FINLAND": "358",
        "FINLAND (Duplicate)": "358",
        "FRANCE": "33",
        "FRANCE (Duplicate)": "33",
        "FRENCH GUIANA": "594",
        "FRENCH POLYNESIA": "689",
        "FRENCH POLYNESIA (Duplicate)": "689",
        "GABON": "241",
        "GABON (Duplicate)": "241",
        "GAMBIA": "220",
        "GAMBIA (Duplicate)": "220",
        "GEORGIA": "995",
        "GEORGIA (Duplicate)": "995",
        "GERMANY": "49",
        "GERMANY (Duplicate)": "49",
        "GHANA": "233",
        "GHANA (Duplicate)": "233",
        "GIBRALTAR": "350",
        "GIBRALTAR (Duplicate)": "350",
        "GLOBALSTAR": "881",
        "GREECE": "30",
        "GREECE (Duplicate)": "30",
        "GREENLAND": "299",
        "GRENADA": "1-473",
        "GRENADA (Duplicate)": "1-473",
        "GUADELOUPE": "590",
        "GUADELOUPE (Duplicate)": "590",
        "GUAM": "1-671",
        "GUATEMALA": "502",
        "GUATEMALA (Duplicate)": "502",
        "GUINEA": "224",
        "GUINEA (Duplicate)": "224",
        "GUINEA-BISSAU": "245",
        "GUINEA-BISSAU (Duplicate)": "245",
        "GUYANA": "592",
        "GUYANA (Duplicate)": "592",
        "HAITI": "509",
        "HAITI (Duplicate)": "509",
        "HONDURAS": "504",
        "HONDURAS (Duplicate)": "504",
        "HONG KONG": "852",
        "HONG KONG (Duplicate)": "852",
        "HUNGARY": "36",
        "HUNGARY (Duplicate)": "36",
        "ICELAND": "354",
        "ICELAND (Duplicate)": "354",
        "INDIA": "91",
        "INDIA (Duplicate)": "91",
        "INDONESIA": "62",
        "INDONESIA (Duplicate)": "62",
        "INMARSAT": "870",
        "INTERNATIONAL NETWORK M2M": "878",
        "INTERNATIONAL NETWORKS": "882, 883",
        "IRAN": "98",
        "IRAN (Duplicate)": "98",
        "IRAQ": "964",
        "IRAQ (Duplicate)": "964",
        "IRELAND": "353",
        "IRELAND (Duplicate)": "353",
        "IRIDIUM": "8816, 8817",
        "ISRAEL": "972",
        "ISRAEL (Duplicate)": "972",
        "ITALY": "39",
        "ITALY (Duplicate)": "39",
        "IVORY COAST": "225",
        "IVORY COAST (Duplicate)": "225",
        "JAMAICA": "1-876",
        "JAMAICA (Duplicate)": "1-876",
        "JAPAN": "81",
        "JAPAN (Duplicate)": "81",
        "JORDAN": "962",
        "JORDAN (Duplicate)": "962",
        "KAZAKHSTAN": "7",
        "KAZAKHSTAN (Duplicate)": "7",
        "KENYA": "254",
        "KENYA (Duplicate)": "254",
        "KIRIBATI": "686",
        "KOREA NORTH": "850",
        "KOREA SOUTH": "82",
        "KOREA SOUTH (Duplicate)": "82",
        "KOSOVO": "383",
        "KOSOVO (Duplicate)": "383",
        "KUWAIT": "965",
        "KUWAIT (Duplicate)": "965",
        "KYRGYZSTAN": "996",
        "KYRGYZSTAN (Duplicate)": "996",
        "LAOS": "856",
        "LATVIA": "371",
        "LATVIA (Duplicate)": "371",
        "LEBANON": "961",
        "LEBANON (Duplicate)": "961",
        "LESOTHO": "266",
        "LESOTHO (Duplicate)": "266",
        "LIBERIA": "231",
        "LIBERIA (Duplicate)": "231",
        "LIBYA": "218",
        "LIBYA (Duplicate)": "218",
        "LIECHTENSTEIN": "423",
        "LIECHTENSTEIN (Duplicate)": "423",
        "LITHUANIA": "370",
        "LITHUANIA (Duplicate)": "370",
        "LUXEMBOURG": "352",
        "LUXEMBOURG (Duplicate)": "352",
        "MACAO": "853",
        "MACAO (Duplicate)": "853",
        "MACEDONIA": "389",
        "MACEDONIA (Duplicate)": "389",
        "MADAGASCAR": "261",
        "MADAGASCAR (Duplicate)": "261",
        "MALAWI": "265",
        "MALAWI (Duplicate)": "265",
        "MALAYSIA": "60",
        "MALAYSIA (Duplicate)": "60",
        "MALDIVES": "960",
        "MALDIVES (Duplicate)": "960",
        "MALI": "223",
        "MALI (Duplicate)": "223",
        "MALTA": "356",
        "MALTA (Duplicate)": "356",
        "MARSHALL ISLANDS": "692",
        "MARTINIQUE": "596",
        "MARTINIQUE (Duplicate)": "596",
        "MAURITANIA": "222",
        "MAURITANIA (Duplicate)": "222",
        "MAURITIUS": "230",
        "MAURITIUS (Duplicate)": "230",
        "MAYOTTE": "262",
        "MAYOTTE (Duplicate)": "262",
        "MCP SATELLITE": "881",
        "MEXICO": "52",
        "MEXICO (Duplicate)": "52",
        "MICRONESIA": "691",
        "MOLDOVA": "373",
        "MOLDOVA (Duplicate)": "373",
        "MONACO": "377",
        "MONACO (Duplicate)": "377",
        "MONGOLIA": "976",
        "MONGOLIA (Duplicate)": "976",
        "MONTENEGRO": "382",
        "MONTENEGRO (Duplicate)": "382",
        "MONTSERRAT": "1-664",
        "MOROCCO": "212",
        "MOROCCO (Duplicate)": "212",
        "MOZAMBIQUE": "258",
        "MOZAMBIQUE (Duplicate)": "258",
        "MYANMAR": "95",
        "MYANMAR (Duplicate)": "95",
        "NAMIBIA": "264",
        "NAMIBIA (Duplicate)": "264",
        "NAURU": "674",
        "NAURU (Duplicate)": "674",
        "NEPAL": "977",
        "NEPAL (Duplicate)": "977",
        "NETHERLANDS ANTILLES": "599",
        "NETHERLANDS ANTILLES (Duplicate)": "599",
        "NETHERLANDS": "31",
        "NETHERLANDS (Duplicate)": "31",
        "NEW CALEDONIA": "687",
        "NEW ZEALAND": "64",
        "NEW ZEALAND (Duplicate)": "64",
        "NICARAGUA": "505",
        "NICARAGUA (Duplicate)": "505",
        "NIGER": "227",
        "NIGER (Duplicate)": "227",
        "NIGERIA": "234",
        "NIGERIA (Duplicate)": "234",
        "NIUE": "683",
        "NORTHERN MARIANA ISLANDS": "1-670",
        "NORWAY": "47",
        "NORWAY (Duplicate)": "47",
        "OMAN": "968",
        "OMAN (Duplicate)": "968",
        "ONAIR": "88298",
        "PAKISTAN": "92",
        "PAKISTAN (Duplicate)": "92",
        "PALAU": "680",
        "PALAU (Duplicate)": "680",
        "PALESTINE": "970",
        "PALESTINE (Duplicate)": "970",
        "PANAMA": "507",
        "PANAMA (Duplicate)": "507",
        "PAPUA NEW GUINEA": "675",
        "PARAGUAY": "595",
        "PARAGUAY (Duplicate)": "595",
        "PERU": "51",
        "PERU (Duplicate)": "51",
        "PHILIPPINES": "63",
        "PHILIPPINES (Duplicate)": "63",
        "POLAND": "48",
        "POLAND (Duplicate)": "48",
        "PORTUGAL": "351",
        "PORTUGAL (Duplicate)": "351",
        "PUERTO RICO": "1-787, 1-939",
        "PUERTO RICO (Duplicate)": "1-787, 1-939",
        "QATAR": "974",
        "QATAR (Duplicate)": "974",
        "REUNION": "262",
        "REUNION (Duplicate)": "262",
        "ROMANIA": "40",
        "ROMANIA (Duplicate)": "40",
        "RUSSIA": "7",
        "RUSSIA (Duplicate)": "7",
        "RWANDA": "250",
        "RWANDA (Duplicate)": "250",
        "SAINT HELENA": "290",
        "SAINT KITTS AND NEVIS": "1-869",
        "SAINT KITTS AND NEVIS (Duplicate)": "1-869",
        "SAINT LUCIA": "1-758",
        "SAINT LUCIA (Duplicate)": "1-758",
        "SAINT MARTIN": "590",
        "SAINT PIERRE AND MIQUELON": "508",
        "SAINT PIERRE AND MIQUELON (Duplicate)": "508",
        "SAINT VINCENT": "1-784",
        "SAINT VINCENT (Duplicate)": "1-784",
        "SAN MARINO": "378",
        "SAN MARINO (Duplicate)": "378",
        "SAO TOME AND PRINCIPE": "239",
        "SAUDI ARABIA": "966",
        "SAUDI ARABIA (Duplicate)": "966",
        "SEANET": "882",
        "SENEGAL": "221",
        "SENEGAL (Duplicate)": "221",
        "SERBIA": "381",
        "SERBIA (Duplicate)": "381",
        "SEYCHELLES": "248",
        "SEYCHELLES (Duplicate)": "248",
        "SIERRA LEONE": "232",
        "SIERRA LEONE (Duplicate)": "232",
        "SINGAPORE": "65",
        "SINGAPORE (Duplicate)": "65",
        "SLOVAKIA": "421",
        "SLOVAKIA (Duplicate)": "421",
        "SLOVENIA": "386",
        "SLOVENIA (Duplicate)": "386",
        "SOLOMON ISLANDS": "677",
        "SOMALIA": "252",
        "SOMALIA (Duplicate)": "252",
        "SOUTH AFRICA": "27",
        "SOUTH AFRICA (Duplicate)": "27",
        "SOUTH SUDAN": "211",
        "SOUTH SUDAN (Duplicate)": "211",
        "SPAIN": "34",
        "SPAIN (Duplicate)": "34",
        "SRI LANKA": "94",
        "SRI LANKA (Duplicate)": "94",
        "SUDAN": "249",
        "SUDAN (Duplicate)": "249",
        "SURINAME": "597",
        "SURINAME (Duplicate)": "597",
        "SWAZILAND": "268",
        "SWAZILAND (Duplicate)": "268",
        "SWEDEN": "46",
        "SWEDEN (Duplicate)": "46",
        "SWITZERLAND": "41",
        "SWITZERLAND (Duplicate)": "41",
        "SYRIA": "963",
        "SYRIA (Duplicate)": "963",
        "TAIWAN": "886",
        "TAIWAN (Duplicate)": "886",
        "TAJIKISTAN": "992",
        "TAJIKISTAN (Duplicate)": "992",
        "TANZANIA": "255",
        "TANZANIA (Duplicate)": "255",
        "THAILAND": "66",
        "THAILAND (Duplicate)": "66",
        "THURAYA": "88216",
        "TOGO": "228",
        "TOGO (Duplicate)": "228",
        "TOKELAU": "690",
        "TONGA": "676",
        "TRINIDAD AND TOBAGO": "1-868",
        "TRINIDAD AND TOBAGO (Duplicate)": "1-868",
        "TRISTAN DACUNHA": "290",
        "TUNISIA": "216",
        "TUNISIA (Duplicate)": "216",
        "TURKEY": "90",
        "TURKEY (Duplicate)": "90",
        "TURKMENISTAN": "993",
        "TURKMENISTAN (Duplicate)": "993",
        "TURKS AND CAICOS ISLANDS": "1-649",
        "TURKS AND CAICOS ISLANDS (Duplicate)": "1-649",
        "TUVALU": "688",
        "UAE": "971",
        "UAE (Duplicate)": "971",
        "UGANDA": "256",
        "UGANDA (Duplicate)": "256",
        "UKRAINE": "380",
        "UKRAINE (Duplicate)": "380",
        "UNITED KINGDOM": "44",
        "UNITED KINGDOM (Duplicate)": "44",
        "UNITED NATIONS": "882",
        "UNITED STATES": "1",
        "UNIVERSAL INTERNATIONAL FREEPHONE NUMBERS (UIFN)": "800",
        "UPT VISIONNG": "878",
        "URUGUAY": "598",
        "URUGUAY (Duplicate)": "598",
        "US VIRGIN ISLANDS": "1-340",
        "US VIRGIN ISLANDS (Duplicate)": "1-340",
        "UZBEKISTAN": "998",
        "UZBEKISTAN (Duplicate)": "998",
        "VANUATU": "678",
        "VANUATU (Duplicate)": "678",
        "VATICAN": "379",
        "VENEZUELA": "58",
        "VENEZUELA (Duplicate)": "58",
        "VIETNAM": "84",
        "VIETNAM (Duplicate)": "84",
        "VOXBONE": "883",
        "WALLIS AND FUTUNA": "681",
        "WESTERN SAMOA": "685",
        "WESTERN SAMOA (Duplicate)": "685",
        "YEMEN": "967",
        "YEMEN (Duplicate)": "967",
        "ZAMBIA": "260",
        "ZAMBIA (Duplicate)": "260",
        "ZIMBABWE": "263",
        "ZIMBABWE (Duplicate)": "263"
        }
output_file = 'output.txt'
extract_values(data, output_file)
