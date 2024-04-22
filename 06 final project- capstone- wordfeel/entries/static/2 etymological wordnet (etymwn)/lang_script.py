import sys, os
import django

parent_dir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_dir2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
parent_dir3 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(parent_dir1)
sys.path.append(parent_dir2)
sys.path.append(parent_dir3)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wordfeel.settings")
django.setup()

from entries.models import Entry, EntryRelations

lang = {
    "aaq": "Eastern Abnaki", "abe": "Western Abnaki", "adt": "Adnyamathanha", "afr": "Afrikaans", "aii": "Assyrian Neo-Aramaic",
    "akk": "Akkadian", "akz": "Alabama", "ale": "Aleut", "alq": "Algonquin", "amh": "Amharic",
    "amj": "Amdang", "ang": "Old English", "ara": "Arabic", "arn": "Mapudungun", "ary": "Moroccan Arabic",
    "arz": "Egyptian Arabic", "auc": "Waorani", "ave": "Avestan", "aze": "Azerbaijani", "bak": "Bashkir",
    "bdy": "Bandjalang", "ben": "Bengali", "bft": "Balti", "bis": "Bislama", "bod": "Tibetan",
    #25
    "bre": "Breton", "bul": "Bulgarian", "byn": "Bilin", "cat": "Catalan", "ces": "Czech",
    "chc": "Catawba", "chn": "Chinook Jargon", "cho": "Choctaw", "chr": "Cherokee", "cmn": "Mandarin Chinese",
    "cop": "Coptic", "cor": "Cornish", "cre": "Cree", "cym": "Welsh", "dan": "Danish",
    "del": "Delaware", "dep": "Pidgin Delaware", "deu": "German", "div": "Dhivehi", "dtd": "Ditidaht",
    "dum": "Middle Dutch", "egy": "Egyptian", "ell": "Modern Greek", "emn": "Eman", "eng": "English",
    #50
    "enm": "Middle English", "enn": "Engenni", "epo": "Esperanto", "ess": "Central Siberian Yupik", "est": "Estonian",
    "eus": "Basque", "fao": "Faroese", "fas": "Persian", "fin": "Finnish", "fon": "Fon",
    "fra": "French", "frc": "Cajun French", "frm": "Middle French", "fro": "Old French", "gae": "Guarequena",
    "gez": "Geez", "gil": "Gilbertese", "gla": "Scottish Gaelic", "gle": "Irish", "glg": "Galician",
    "gmh": "Middle High German", "gml": "Middle Low German", "goh": "Old High German", "got": "Gothic", "grc": "Ancient Greek",
    #75
    "guj": "Gujarati", "gul": "Sea Island Creole English", "gwi": "Gwich'in", "hak": "Hakka Chinese", "hat": "Haitian",
    "haw": "Hawaiian", "hbs": "Serbo-Croatian", "heb": "Hebrew", "hin": "Hindi", "hit": "Hittite",
    "hop": "Hopi", "hun": "Hungarian", "hur": "Halkomelem", "hye": "Armenian", "idb": "Indo-Portuguese",
    "ike": "Eastern Canadian Inuktitut", "ikt": "Inuinnaqtun", "iku": "Inuktitut", "ind": "Indonesian", "inz": "Ineseño",
    "ipk": "Inupiaq", "isl": "Ipiko", "ita": "Italian", "jam": "Jamaican Creole English", "jbo": "Lojban",
    #100
    "jpn": "Japanese", "kal": "Kalaallisut", "kan": "Kannada", "kat": "Georgian", "kaz": "Kazakh",
    "khm": "Khmer", "kin": "Kinyarwanda", "kju": "Kashaya", "kky": "Guugu Yimidhirr", "kld": "Gamilaraay",
    "kok": "Konkani", "kon": "Kongo", "kor": "Korean", "kur": "Kurdish", "lad": "Ladino",
    "lao": "Lao", "lat": "Latin", "lav": "Latvian", "lit": "Lithuanian", "lkt": "Lakota",
    "lou": "Louisiana Creole", "ltz": "Luxembourgish", "lug": "Ganda", "luo": "Luo", "lut": "Lushootseed",
    #125
    "mah": "Marshallese", "mak": "Makasar", "mal": "Malayalam", "mar": "Marathi", "mas": "Masai",
    "mbc": "Macushi", "mic": "Mi'kmaq", "mkd": "Macedonian", "mnc": "Manchu", "mnk": "Mandinka",
    "moh": "Mohawk", "mon": "Mongolian", "mri": "Maori", "msa": "Malay", "mwl": "Mirandese",
    "mya": "Burmese", "nah": "Nahuatl", "nan": "Min Nan Chinese", "nap": "Neapolitan", "naq": "Khoekhoe",
    "nav": "Navajo", "nci": "Classical Nahuatl", "ndo": "Ndonga", "nep": "Nepali", "nld": "Dutch",
    #150
    "non": "Old Norse", "nor": "Norwegian", "nov": "Novial", "nys": "Nyungar", "odt": "Old Dutch",
    "oji": "Ojibwa", "ood": "Tohono O'odham", "ori": "Oriya", "ota": "Ottoman Turkish", "p_sla": "Proto-Slavic",
    "pan": "Punjabi", "pau": "Palauan", "peo": "Old Persian", "phn": "Phoenician", "pim": "Powhatan",
    "pis": "Pijin", "pli": "Pali", "pml": "Lingua Franca", "pol": "Polish", "por": "Portuguese",
    "pus": "Pushto", "quc": "K'iche'", "que": "Quechua", "rap": "Rapanui", "rme": "Angloromani",
    #175
    "rmq": "Caló", "rom": "Romany", "ron": "Romanian", "rop": "Kriol", "rue": "Rusyn",
    "rus": "Russian", "san": "Sanskrit", "scn": "Sicilian", "sco": "Scots", "see": "Seneca",
    "sga": "Old Irish", "shh": "Shoshoni", "sin": "Sinhala", "slk": "Slovak", "slv": "Slovenian",
    "smo": "Samoan", "sna": "Shona", "sot": "Southern Sotho", "spa": "Spanish", "sqi": "Albanian",
    "srs": "Sarsi", "sth": "Shelta", "sux": "Sumerian", "swa": "Swahili", "swe": "Swedish",
    #200
    "syc": "Classical Syriac", "tah": "Tahitian", "tam": "Tamil", "tat": "Tatar", "tel": "Telugu",
    "tgl": "Tagalog", "tha": "Thai", "tir": "Tigrinya", "tiv": "Tiv", "tnq": "Taino",
    "ton": "Tongan", "tpi": "Tok Pisin", "tsn": "Tswana", "tur": "Turkish", "twi": "Twi",
    "uig": "Uighur", "ukr": "Ukrainian", "umb": "Umbundu", "urd": "Urdu", "uzb": "Uzbek",
    "vec": "Venetian", "vie": "Vietnamese", "vol": "Volapük", "wam": "Wampanoag", "wit": "Wintu",
    #225
    "wol": "Wolof", "wrh": "Wiradjuri", "xaa": "Andalusian Arabic", "xcl": "Classical Armenian", "xho": "Xhosa",
    "xng": "Middle Mongolian", "xno": "Anglo-Norman", "xnt": "Narragansett", "yid": "Yiddish", "yol": "Yola",
    "yor": "Yoruba", "yue": "Yue Chinese", "yxg": "Yagara", "zku": "Kaurna", "zul": "Zulu"
    #240
}

entryobjs = Entry.objects.all()
total = entryobjs.count()
def do(entryobjs, total):
    for e in entryobjs:
        e.language = lang[e.language]
        e.save()
        print("done", e.id, "of", total)

def undo(entryobjs):
    for e in entryobjs:
        if e.language in lang.values():
            keys = [k for k in lang if lang[k] == e.language]
            e.language = keys[0]
            e.save()
            print("done", e.id)

do(entryobjs, total)