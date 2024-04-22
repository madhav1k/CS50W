import time, sys, os

current_dir = os.path.dirname(__file__)
module_dir = os.path.join(current_dir, 'static', '2 etymological wordnet (etymwn)')
sys.path.append(module_dir)

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from entries.models import Entry, EntriesRelation, FamilialRelation
from wiktionary_script import WiktionaryParser
from itertools import zip_longest, chain
from copy import copy

entryobjs_eng = Entry.objects.exclude(english_name="")
entryobjs_lat = Entry.objects.exclude(latinized_name="").exclude(~Q(english_name=""))
entryobjs_wik = Entry.objects.exclude(wiktionary_name="").exclude(~Q(english_name="")).exclude(~Q(latinized_name=""))
entryobjs_ent = Entry.objects.exclude(~Q(english_name="")).exclude(~Q(latinized_name="")).exclude(~Q(wiktionary_name=""))
entryobjs_sorted = sorted(chain(entryobjs_eng, entryobjs_lat, entryobjs_wik, entryobjs_ent), key=lambda x: x.english_name or x.latinized_name or x.wiktionary_name or x.entry)

entryobjs_lower = []
for e in entryobjs_sorted:
    e = copy(e)
    if e.english_name != "":
        e.english_name = e.english_name.lower()
    if e.latinized_name != "":
        e.latinized_name = e.latinized_name.lower()
    if e.wiktionary_name != "":
        e.wiktionary_name = e.wiktionary_name.lower()
    e.entry = e.entry.lower()
    entryobjs_lower.append(e)

# Create your views here.
def index(request):
    return render(request, "entries/index.html")

def results(request):        
    if request.method == 'GET':      
        entry = request.GET.get('q')  
        results = []

        exact_eng = Entry.objects.filter(english_name=entry)
        exact_lat = Entry.objects.filter(latinized_name=entry).exclude(english_name=entry)
        exact_wik = Entry.objects.filter(wiktionary_name=entry).exclude(latinized_name=entry).exclude(english_name=entry)
        exact_ent = Entry.objects.filter(entry=entry).exclude(wiktionary_name=entry).exclude(latinized_name=entry).exclude(english_name=entry)
        exact_sorted = sorted(chain(exact_eng, exact_lat, exact_wik, exact_ent), key=lambda x: x.english_name if x.english_name == entry else x.latinized_name if x.latinized_name == entry else x.wiktionary_name if x.wiktionary_name == entry else x.entry if x.entry == entry else None)

        for obj in entryobjs_sorted:
            if obj.english_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted]:
                results.append(obj)
            elif obj.latinized_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted]:
                results.append(obj)
            elif obj.wiktionary_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted]:
                results.append(obj)
            elif obj.entry.startswith(entry) and obj.id not in [e.id for e in exact_sorted]:
                results.append(obj)
        for obj in entryobjs_lower:
            if obj.english_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted] and obj.id not in [e.id for e in results]:
                results.append([e for e in entryobjs_sorted if e.id == obj.id][0])
            elif obj.latinized_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted] and obj.id not in [e.id for e in results]:
                results.append([e for e in entryobjs_sorted if e.id == obj.id][0])
            elif obj.wiktionary_name.startswith(entry) and obj.id not in [e.id for e in exact_sorted] and obj.id not in [e.id for e in results]:
                results.append([e for e in entryobjs_sorted if e.id == obj.id][0])
            elif obj.entry.startswith(entry) and obj.id not in [e.id for e in exact_sorted] and obj.id not in [e.id for e in results]:
                results.append([e for e in entryobjs_sorted if e.id == obj.id][0])
        num = len(exact_sorted) + len(results)
        if num in [0, 1]:
            res = "result"
        else: 
            res = "results"
        if num == 0:
            return render(request, "entries/results.html", {
                "num": num,
                "message": "0 result found",
                "query": entry,
            })
        return render(request, "entries/results.html", {
            "results": results,
            "exact": exact_sorted,
            "num": f'{num:,}',
            "message": f"{num:,} {res} found",
            "query": entry,
        })
    else:
        return render(request, "entries/index.html")

def search_api(request):
    value = request.GET.get("value")
    if value == "":
        return JsonResponse({
        "ids": [],
        "entries": [],
        "languages": [],
        "num": 0,
    })
    searchedobjs = []

    exact_eng = Entry.objects.filter(english_name=value)
    exact_lat = Entry.objects.filter(latinized_name=value).exclude(english_name=value)
    exact_wik = Entry.objects.filter(wiktionary_name=value).exclude(latinized_name=value).exclude(english_name=value)
    exact_ent = Entry.objects.filter(entry=value).exclude(wiktionary_name=value).exclude(latinized_name=value).exclude(english_name=value)

    exact_sorted = sorted(chain(exact_eng, exact_lat, exact_wik, exact_ent), key=lambda x: x.english_name if x.english_name == value else x.latinized_name if x.latinized_name == value else x.wiktionary_name if x.wiktionary_name == value else x.entry if x.entry == value else None)

    for e in exact_sorted:
        searchedobjs.append(e)
    for obj in entryobjs_sorted:
        if len(searchedobjs) >= 8:
            break
        if obj.english_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append(obj)
        elif obj.latinized_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append(obj)
        elif obj.wiktionary_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append(obj)
        elif obj.entry.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append(obj)
    for obj in entryobjs_lower:
        if len(searchedobjs) >= 8:
            break
        if obj.english_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append([e for e in entryobjs_sorted if e.id == obj.id][0])
        elif obj.latinized_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append([e for e in entryobjs_sorted if e.id == obj.id][0])
        elif obj.wiktionary_name.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append([e for e in entryobjs_sorted if e.id == obj.id][0])
        elif obj.entry.startswith(value) and obj.id not in [e.id for e in searchedobjs]:
            searchedobjs.append([e for e in entryobjs_sorted if e.id == obj.id][0])

    ids = []
    entries = []
    latinized = []
    languages = []
    num = len(searchedobjs)
    for i in range(num):
        ids.append(searchedobjs[i].id)
        entries.append(searchedobjs[i].entry)
        latinized.append(searchedobjs[i].latinized_name)
        languages.append(searchedobjs[i].language)
    return JsonResponse({
        "ids": ids,
        "entries": entries,
        "latinized": latinized,
        "languages": languages,
        "num": num,
    })

class Definitions:
    def __init__(self, dic):
        self.partOfSpeech = dic['partOfSpeech']
        self.text = dic['text']['line']
        self.definitions = ''
        i = 1
        while True:
            if f'{i}' in dic['text']:
                if i == 1:
                    self.definitions += '<ol>'
                self.definitions += '<li>' + dic['text'][f'{i}']['main']
                ii = 1
                while True:
                    if f'{ii}' in dic['text'][f'{i}']:
                        if ii == 1:
                            self.definitions += '<ol>'
                        self.definitions += '<li>' + dic['text'][f'{i}'][f'{ii}'] + '</li>'
                        if f'{ii+1}' not in dic['text'][f'{i}']:
                            self.definitions += '</ol>'
                        ii += 1
                    else:
                        break
                self.definitions += '</li>'
                if f'{i+1}' not in dic['text']:
                    self.definitions += '</ol>'
                i += 1
            else:
                break

#['rel:etymological_origin_of' 'rel:etymology' 'rel:has_derived_form' 'rel:is_derived_from' 'rel:etymologically_related' 'rel:variant:orthography' 'rel:derived'(absent) 'rel:etymologically'(absent)]
def entry(request, entry_id):
    entryobj = Entry.objects.filter(id=entry_id)[0]

    # def find_primeetymons(entryobj):
    #     etymons_checkfrom = EntriesRelation.objects.filter(to_entry=entryobj, relation_type="rel:etymological_origin_of")
    #     etymons_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:etymology")

    #     if not etymons_checkfrom.exists() and not etymons_checkto.exists():
    #         return [entryobj]
    #     primeetymons = []
    #     for er in etymons_checkfrom:
    #         if er.from_entry.id not in [e.id for e in primeetymons]:
    #             primeetymons.append(er.from_entry)
    #     for er in etymons_checkto:
    #         if er.to_entry.id not in [e.id for e in primeetymons]:    
    #             primeetymons.append(er.to_entry)
    #     for e in primeetymons:
    #         primeetymons.remove(e)
    #         primeetymons += find_primeetymons(e)
    #     return primeetymons

    # primeetymons = find_primeetymons(entryobj)

    etymons_checkfrom = EntriesRelation.objects.filter(to_entry=entryobj, relation_type="rel:etymological_origin_of")
    etymons_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:etymology")

    etymons = []
    for e in etymons_checkfrom:
        if e.from_entry.id not in [e.id for e in etymons]:
            etymons.append(e.from_entry)
    for e in etymons_checkto:
        if e.to_entry.id not in [e.id for e in etymons]:    
            etymons.append(e.to_entry)

    roots_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:is_derived_from")
    
    roots = []
    for e in roots_checkto:
        if e.to_entry.id not in [e.id for e in roots]:
            roots.append(e.to_entry)
    
    relatedwords_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:etymologically_related")
    relatedwords_checkfrom = EntriesRelation.objects.filter(to_entry=entryobj, relation_type="rel:etymologically_related")
    
    relatedwords = []
    for e in relatedwords_checkto:
        if e.to_entry.id not in [e.id for e in relatedwords]:
            relatedwords.append(e.to_entry)
    for e in relatedwords_checkfrom:
        if e.from_entry.id not in [e.id for e in relatedwords]:
            relatedwords.append(e.from_entry)
    
    primeetymons = []
    familywords = []
    wordfamilies = []
    if FamilialRelation.objects.filter(primeetymon=entryobj).exists():
        childfws_checkfw = FamilialRelation.objects.filter(primeetymon=entryobj)
        wfdict = {}
        wfdict['fws'] = []
        for e in childfws_checkfw:
            if e.familyword.id not in [e.id for e in wfdict['fws']]:
                familywords.append(e.familyword)
                wfdict['fws'].append(e.familyword)
        wordfamilies.append(wfdict)
                
    elif FamilialRelation.objects.filter(familyword=entryobj).exists():
        pes_checkpe = FamilialRelation.objects.filter(familyword=entryobj)
        for e in pes_checkpe:
            wfdict = {}
            primeetymons.append(e.primeetymon)
            wfdict['pe'] = []
            wfdict['pe'].append(e.primeetymon)
            wfdict['fws'] = []
            siblingfws_checkfw = FamilialRelation.objects.filter(primeetymon=e.primeetymon)
            for ee in siblingfws_checkfw:
                if ee.familyword.id not in [e.id for e in wfdict['fws']] and ee.familyword.id != entryobj.id:
                    familywords.append(ee.familyword)
                    wfdict['fws'].append(ee.familyword)
            wordfamilies.append(wfdict)
    
    derivatives_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:etymological_origin_of")
    derivatives_checkfrom = EntriesRelation.objects.filter(to_entry=entryobj, relation_type="rel:etymology")
    
    derivatives1 = []
    for e in derivatives_checkto:
        if e.to_entry.id not in [e.id for e in derivatives1]:
            derivatives1.append(e.to_entry)
    for e in derivatives_checkfrom:
        if e.from_entry.id not in [e.id for e in derivatives1]:    
            derivatives1.append(e.from_entry)
    
    derivatives2_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:has_derived_form")
    
    derivatives2 = []
    for e in derivatives2_checkto:
        if e.to_entry.id not in [e.id for e in derivatives2]:
            derivatives2.append(e.to_entry)
    
    variants_checkto = EntriesRelation.objects.filter(from_entry=entryobj, relation_type="rel:variant:orthography")
    variants_checkfrom = EntriesRelation.objects.filter(to_entry=entryobj, relation_type="rel:variant:orthography")

    variants_orthographic = []
    variants_unorthographic = []
    for e in variants_checkto:
        if e.to_entry.language == entryobj.language and e.to_entry.id not in [e.id for e in variants_orthographic]:
            variants_orthographic.append(e.to_entry)
    for e in variants_checkfrom:
        if e.from_entry.language == entryobj.language and e.from_entry.id not in [e.id for e in variants_unorthographic] and e.from_entry.id not in [e.id for e in variants_orthographic]:
            variants_unorthographic.append(e.from_entry)

    parser = WiktionaryParser()
    if entryobj.wiktionary_name != "":
        word = parser.fetch(entryobj.wiktionary_name, language=entryobj.language)
    elif entryobj.entry != "":
        word = parser.fetch(entryobj.entry, language=entryobj.language)
    elif entryobj.english_name != "":
        word = parser.fetch(entryobj.english_name, language=entryobj.language)
    elif entryobj.latinized_name != "":
        word = parser.fetch(entryobj.latinized_name, language=entryobj.language)
    n = len(word)

    etymologies = [word[i]['etymology'] for i in range(n)]
    definitions = [[Definitions(dic) for dic in word[i]['definitions']] for i in range(n)]

    zip = []
    for (n, e, d) in zip_longest(range(1, n+1), etymologies, definitions, fillvalue=''):
        zip.append({'number': n, 'etymology': e, 'definitions': d})
    
    return render(request, "entries/entry.html", {
            "entry": entryobj.entry,
            "latinized": entryobj.latinized_name,
            "language": entryobj.language,
            "primeetymons": primeetymons,
            "primeetymonslen": len(primeetymons),
            "etymons": etymons,
            "etymonslen": len(etymons),
            "roots": roots,
            "rootslen": len(roots),
            "relatedwords": relatedwords,
            "relatedwordslen": len(relatedwords),
            "wordfamilies": wordfamilies,
            "familywordscount": len(familywords),
            "derivatives1": derivatives1,
            "derivatives1len": len(derivatives1),
            "derivatives2": derivatives2,
            "derivatives2len": len(derivatives2),
            "derivativeslen": len(derivatives1) + len(derivatives2),
            "variants_orthographic": variants_orthographic,
            "variants_unorthographic": variants_unorthographic,
            "variantslen": len(variants_orthographic) + len(variants_unorthographic),
            "zip": zip,
            "n": n,
        })


def entries(request):
    num = Entry.objects.count()
    lang = Entry.objects.values('language').distinct().count()
    if num in [0, 1]:
        entries = "entry"
    else:
        entries = "entries"
    if lang in [0, 1]:
        languages = "language"
    else:
        languages = "languages"
    return render(request, "entries/entries.html", {
        "num": f'{num:,}',
        "entries": entries,
        "lang": f'{lang:,}',
        "languages": languages,
    })

def scroll_entries_api(request):
    q = int(request.GET.get("q") or 40)
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + q - 1))
    ids = []
    entries = []
    latinized= []
    languages = []
    finished = "false"
    num = end - start + 1
    r = range(start, end + 1)

    last_index = len(entryobjs_sorted) - 1
    if start <= last_index <= end or last_index == -1:
        finished = "true"
        num = last_index - start + 1
        r = range(start, last_index + 1)

    for i in r:
        ids.append(entryobjs_sorted[i].id)
        entries.append(entryobjs_sorted[i].entry)
        latinized.append(entryobjs_sorted[i].latinized_name)
        languages.append(entryobjs_sorted[i].language)
    
    time.sleep(1)
    return JsonResponse({
        "ids": ids,
        "entries": entries,
        "latinized": latinized,
        "languages": languages,
        "num": num,
        "finished": finished,
    })

def word_families(request):
    wordfamilies = []
    num = FamilialRelation.objects.values('primeetymon').distinct().count()
    if num in [0, 1]:
        wfs = "word family"
    else:
        wfs = "word families"
    pekeys = FamilialRelation.objects.values_list('primeetymon', flat=True).distinct()
    pekeys = sorted(pekeys, key=lambda x: Entry.objects.filter(id=x)[0].english_name)
    for pekey in pekeys:
        wordfamily = {}
        wordfamily['pe'] = Entry.objects.filter(id=pekey)[0]
        wordfamily['fws'] = []
        wfobjs = FamilialRelation.objects.filter(primeetymon=pekey)
        wfobjs = sorted(wfobjs, key=lambda x: x.familyword.english_name)
        for wfobj in wfobjs:
            wordfamily['fws'].append(wfobj.familyword)
        wordfamilies.append(wordfamily)
    return render(request, "entries/word_families.html", {
       "num": num,
       "wfs": wfs,
       "wordfamilies": wordfamilies,
    })

