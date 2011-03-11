from django.utils.translation import ugettext_lazy as _
import datetime

# Datetime object representing time of last country list update
COUNTRIES_LAST_UPDATE = datetime.datetime(2011, 3, 11, 16, 15)

# List of countries and its ISO codes
# source: http://www.iso.org/iso/country_codes/iso_3166_code_lists.htm
COUNTRIES = (
    # ('<ISO 3166-1 alpha-2 uppercase code>', _("<uppercase official English short name>")),
    ('AF', _("AFGHANISTAN")),
    ('AX', _("ALAND ISLANDS")),
    ('AL', _("ALBANIA")),
    ('DZ', _("ALGERIA")),
    ('AS', _("AMERICAN SAMOA")),
    ('AD', _("ANDORRA")),
    ('AO', _("ANGOLA")),
    ('AI', _("ANGUILLA")),
    ('AQ', _("ANTARCTICA")),
    ('AG', _("ANTIGUA AND BARBUDA")),
    ('AR', _("ARGENTINA")),
    ('AM', _("ARMENIA")),
    ('AW', _("ARUBA")),
    ('AU', _("AUSTRALIA")),
    ('AT', _("AUSTRIA")),
    ('AZ', _("AZERBAIJAN")),
    ('BS', _("BAHAMAS")),
    ('BH', _("BAHRAIN")),
    ('BD', _("BANGLADESH")),
    ('BB', _("BARBADOS")),
    ('BY', _("BELARUS")),
    ('BE', _("BELGIUM")),
    ('BZ', _("BELIZE")),
    ('BJ', _("BENIN")),
    ('BM', _("BERMUDA")),
    ('BT', _("BHUTAN")),
    ('BO', _("BOLIVIA, PLURINATIONAL STATE OF")),
    ('BQ', _("BONAIRE, SAINT EUSTATIUS AND SABA")),
    ('BA', _("BOSNIA AND HERZEGOVINA")),
    ('BW', _("BOTSWANA")),
    ('BV', _("BOUVET ISLAND")),
    ('BR', _("BRAZIL")),
    ('IO', _("BRITISH INDIAN OCEAN TERRITORY")),
    ('BN', _("BRUNEI DARUSSALAM")),
    ('BG', _("BULGARIA")),
    ('BF', _("BURKINA FASO")),
    ('BI', _("BURUNDI")),
    ('KH', _("CAMBODIA")),
    ('CM', _("CAMEROON")),
    ('CA', _("CANADA")),
    ('CV', _("CAPE VERDE")),
    ('KY', _("CAYMAN ISLANDS")),
    ('CF', _("CENTRAL AFRICAN REPUBLIC")),
    ('TD', _("CHAD")),
    ('CL', _("CHILE")),
    ('CN', _("CHINA")),
    ('CX', _("CHRISTMAS ISLAND")),
    ('CC', _("COCOS (KEELING) ISLANDS")),
    ('CO', _("COLOMBIA")),
    ('KM', _("COMOROS")),
    ('CG', _("CONGO")),
    ('CD', _("CONGO, THE DEMOCRATIC REPUBLIC OF THE")),
    ('CK', _("COOK ISLANDS")),
    ('CR', _("COSTA RICA")),
    ('CI', _("COTE D'IVOIRE")),
    ('HR', _("CROATIA")),
    ('CU', _("CUBA")),
    ('CW', _("CURACAO")),
    ('CY', _("CYPRUS")),
    ('CZ', _("CZECH REPUBLIC")),
    ('DK', _("DENMARK")),
    ('DJ', _("DJIBOUTI")),
    ('DM', _("DOMINICA")),
    ('DO', _("DOMINICAN REPUBLIC")),
    ('EC', _("ECUADOR")),
    ('EG', _("EGYPT")),
    ('SV', _("EL SALVADOR")),
    ('GQ', _("EQUATORIAL GUINEA")),
    ('ER', _("ERITREA")),
    ('EE', _("ESTONIA")),
    ('ET', _("ETHIOPIA")),
    ('FK', _("FALKLAND ISLANDS (MALVINAS)")),
    ('FO', _("FAROE ISLANDS")),
    ('FJ', _("FIJI")),
    ('FI', _("FINLAND")),
    ('FR', _("FRANCE")),
    ('GF', _("FRENCH GUIANA")),
    ('PF', _("FRENCH POLYNESIA")),
    ('TF', _("FRENCH SOUTHERN TERRITORIES")),
    ('GA', _("GABON")),
    ('GM', _("GAMBIA")),
    ('GE', _("GEORGIA")),
    ('DE', _("GERMANY")),
    ('GH', _("GHANA")),
    ('GI', _("GIBRALTAR")),
    ('GR', _("GREECE")),
    ('GL', _("GREENLAND")),
    ('GD', _("GRENADA")),
    ('GP', _("GUADELOUPE")),
    ('GU', _("GUAM")),
    ('GT', _("GUATEMALA")),
    ('GG', _("GUERNSEY")),
    ('GN', _("GUINEA")),
    ('GW', _("GUINEA-BISSAU")),
    ('GY', _("GUYANA")),
    ('HT', _("HAITI")),
    ('HM', _("HEARD ISLAND AND MCDONALD ISLANDS")),
    ('VA', _("HOLY SEE (VATICAN CITY STATE)")),
    ('HN', _("HONDURAS")),
    ('HK', _("HONG KONG")),
    ('HU', _("HUNGARY")),
    ('IS', _("ICELAND")),
    ('IN', _("INDIA")),
    ('ID', _("INDONESIA")),
    ('IR', _("IRAN, ISLAMIC REPUBLIC OF")),
    ('IQ', _("IRAQ")),
    ('IE', _("IRELAND")),
    ('IM', _("ISLE OF MAN")),
    ('IL', _("ISRAEL")),
    ('IT', _("ITALY")),
    ('JM', _("JAMAICA")),
    ('JP', _("JAPAN")),
    ('JE', _("JERSEY")),
    ('JO', _("JORDAN")),
    ('KZ', _("KAZAKHSTAN")),
    ('KE', _("KENYA")),
    ('KI', _("KIRIBATI")),
    ('KP', _("KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF")),
    ('KR', _("KOREA, REPUBLIC OF")),
    ('KW', _("KUWAIT")),
    ('KG', _("KYRGYZSTAN")),
    ('LA', _("LAO PEOPLE'S DEMOCRATIC REPUBLIC")),
    ('LV', _("LATVIA")),
    ('LB', _("LEBANON")),
    ('LS', _("LESOTHO")),
    ('LR', _("LIBERIA")),
    ('LY', _("LIBYAN ARAB JAMAHIRIYA")),
    ('LI', _("LIECHTENSTEIN")),
    ('LT', _("LITHUANIA")),
    ('LU', _("LUXEMBOURG")),
    ('MO', _("MACAO")),
    ('MK', _("MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF")),
    ('MG', _("MADAGASCAR")),
    ('MW', _("MALAWI")),
    ('MY', _("MALAYSIA")),
    ('MV', _("MALDIVES")),
    ('ML', _("MALI")),
    ('MT', _("MALTA")),
    ('MH', _("MARSHALL ISLANDS")),
    ('MQ', _("MARTINIQUE")),
    ('MR', _("MAURITANIA")),
    ('MU', _("MAURITIUS")),
    ('YT', _("MAYOTTE")),
    ('MX', _("MEXICO")),
    ('FM', _("MICRONESIA, FEDERATED STATES OF")),
    ('MD', _("MOLDOVA, REPUBLIC OF")),
    ('MC', _("MONACO")),
    ('MN', _("MONGOLIA")),
    ('ME', _("MONTENEGRO")),
    ('MS', _("MONTSERRAT")),
    ('MA', _("MOROCCO")),
    ('MZ', _("MOZAMBIQUE")),
    ('MM', _("MYANMAR")),
    ('NA', _("NAMIBIA")),
    ('NR', _("NAURU")),
    ('NP', _("NEPAL")),
    ('NL', _("NETHERLANDS")),
    ('NC', _("NEW CALEDONIA")),
    ('NZ', _("NEW ZEALAND")),
    ('NI', _("NICARAGUA")),
    ('NE', _("NIGER")),
    ('NG', _("NIGERIA")),
    ('NU', _("NIUE")),
    ('NF', _("NORFOLK ISLAND")),
    ('MP', _("NORTHERN MARIANA ISLANDS")),
    ('NO', _("NORWAY")),
    ('OM', _("OMAN")),
    ('PK', _("PAKISTAN")),
    ('PW', _("PALAU")),
    ('PS', _("PALESTINIAN TERRITORY, OCCUPIED")),
    ('PA', _("PANAMA")),
    ('PG', _("PAPUA NEW GUINEA")),
    ('PY', _("PARAGUAY")),
    ('PE', _("PERU")),
    ('PH', _("PHILIPPINES")),
    ('PN', _("PITCAIRN")),
    ('PL', _("POLAND")),
    ('PT', _("PORTUGAL")),
    ('PR', _("PUERTO RICO")),
    ('QA', _("QATAR")),
    ('RE', _("REUNION")),
    ('RO', _("ROMANIA")),
    ('RU', _("RUSSIAN FEDERATION")),
    ('RW', _("RWANDA")),
    ('BL', _("SAINT BARTHELEMY")),
    ('SH', _("SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA")),
    ('KN', _("SAINT KITTS AND NEVIS")),
    ('LC', _("SAINT LUCIA")),
    ('MF', _("SAINT MARTIN (FRENCH PART)")),
    ('PM', _("SAINT PIERRE AND MIQUELON")),
    ('VC', _("SAINT VINCENT AND THE GRENADINES")),
    ('WS', _("SAMOA")),
    ('SM', _("SAN MARINO")),
    ('ST', _("SAO TOME AND PRINCIPE")),
    ('SA', _("SAUDI ARABIA")),
    ('SN', _("SENEGAL")),
    ('RS', _("SERBIA")),
    ('SC', _("SEYCHELLES")),
    ('SL', _("SIERRA LEONE")),
    ('SG', _("SINGAPORE")),
    ('SX', _("SINT MAARTEN (DUTCH PART)")),
    ('SK', _("SLOVAKIA")),
    ('SI', _("SLOVENIA")),
    ('SB', _("SOLOMON ISLANDS")),
    ('SO', _("SOMALIA")),
    ('ZA', _("SOUTH AFRICA")),
    ('GS', _("SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS")),
    ('ES', _("SPAIN")),
    ('LK', _("SRI LANKA")),
    ('SD', _("SUDAN")),
    ('SR', _("SURINAME")),
    ('SJ', _("SVALBARD AND JAN MAYEN")),
    ('SZ', _("SWAZILAND")),
    ('SE', _("SWEDEN")),
    ('CH', _("SWITZERLAND")),
    ('SY', _("SYRIAN ARAB REPUBLIC")),
    ('TW', _("TAIWAN, PROVINCE OF CHINA")),
    ('TJ', _("TAJIKISTAN")),
    ('TZ', _("TANZANIA, UNITED REPUBLIC OF")),
    ('TH', _("THAILAND")),
    ('TL', _("TIMOR-LESTE")),
    ('TG', _("TOGO")),
    ('TK', _("TOKELAU")),
    ('TO', _("TONGA")),
    ('TT', _("TRINIDAD AND TOBAGO")),
    ('TN', _("TUNISIA")),
    ('TR', _("TURKEY")),
    ('TM', _("TURKMENISTAN")),
    ('TC', _("TURKS AND CAICOS ISLANDS")),
    ('TV', _("TUVALU")),
    ('UG', _("UGANDA")),
    ('UA', _("UKRAINE")),
    ('AE', _("UNITED ARAB EMIRATES")),
    ('GB', _("UNITED KINGDOM")),
    ('US', _("UNITED STATES")),
    ('UM', _("UNITED STATES MINOR OUTLYING ISLANDS")),
    ('UY', _("URUGUAY")),
    ('UZ', _("UZBEKISTAN")),
    ('VU', _("VANUATU")),
    ('VE', _("VENEZUELA, BOLIVARIAN REPUBLIC OF")),
    ('VN', _("VIET NAM")),
    ('VG', _("VIRGIN ISLANDS, BRITISH")),
    ('VI', _("VIRGIN ISLANDS, U.S.")),
    ('WF', _("WALLIS AND FUTUNA")),
    ('EH', _("WESTERN SAHARA")),
    ('YE', _("YEMEN")),
    ('ZM', _("ZAMBIA")),
    ('ZW', _("ZIMBABWE")),
)
