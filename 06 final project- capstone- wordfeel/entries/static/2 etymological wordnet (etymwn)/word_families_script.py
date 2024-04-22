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

from entries.models import Entry, EntriesRelation, FamilialRelation

"""
Latin: 
0: language, 1: english_name&wiktionary_name, 2: entry_name&latinized_name

Ancient Greek: 
0+1: language, 2: english_name, 3: wiktionary_name, 4: entry_name, 5: latinized_name
"""

db = """Latin nosco (nōscō): ignore cognition recognize incognito acquaint

Ancient Greek gignosko γιγνώσκω (γιγνώσκω gignṓskō): agnostic gnostic Gnostic

Latin lego (legō): select elect eligible elegant collect intellect intelligent diligent legume leguminous lecture neglect sacrilege lection lesson

Latin ligo (ligō): liable liability rely religion ally alliance reliability reliable ligature obligation oblige ligation ligate league legion

Latin lego (lēgō): college colleague delegate legacy legate relegate allege

Latin spiro (spīrō): conspire inspire respire expire spirit aspire perspire transpire

Latin spes (spēs): despair prosper

Latin capio (capiō): receive reception recipe intercept captive conceive concept perceive perception deceive deception incept inception capacity capture accept recuperate susceptible except exceptional cate cater municipal precept preceptor caption

Latin specio (speciō): expect inspect suspect spectator spectacle spectacular aspect respect perspective prospect specimen spice species speculate spectrum specter

Latin spicio (spiciō): conspicuous

Latin quaero (quaerō): acquire require request exquisite inquire inquisitive conquer query inquest quest

Latin puto (putō): compute computation reputation deputation depute amputation dispute putative impute

Latin ludo (lūdō): illude delude collude allude prelude

Latin sequor (sequor): obsequious prosecute execute executive consecutive persecute pursue segue sect sue suit lawsuit

Latin ago (agō): agile agility agent agenda agitate exact action active actor act navigate variegated castigate purge actuate actuator cogent cogency

Latin facio (faciō): perfect defect affect effect infect confect confectionary facile faculty facility facture manufacture efficient factor factory fact office feasible profit benefit surfeit factitious faction defeat counterfeit
 
Latin teneo (teneō): contain continue continuous attain pertain appertain retain rein retinue maintain detain sustain obtain entertain tenet tenant tenure abstain tenacity tenable untenable

Latin tendo (tendō): ostentation ostentatious attend attention portend contend

Ancient Greek arkho ἄρχω (ἄρχω árkhō): archaic architecture architect archetype hierarchy monarchy oligarchy anarchy archive archaeology

Latin sisto (sistō): consist persist resist exist subsist subsistence

Latin pendo (pendō): suspend suspense expend expense expensive expenditure impend impending append prepend dispend spend stipend compendium pensive compensate perpendicular

Latin pendeo (pendeō): depend pendulous pendant pendulum

Latin peto (petō): compete impetus petition appetite

Latin testis (testis): testament testify testimony attest testis contest detest intestate testate

Latin do (dō): data dative add tradition betray treason render vendor vend

Latin unda (unda): inundate abundant redundant

Latin maneo (maneō): remain mansion immanent manor

Latin traho (trahō): treaty treatise tractate treat extract contract retract attract traction tractor protract tract distract distraught abstract trail trawl detract subtract

Latin tango (tangō): tangible intangible contingent contingency integer entire integral integrate tangent tactile tact tactful

Latin augeo (augeō): augment auction author authority

Latin ante (ante): ancient antique antiquity anterior ancestor advance

Ancient Greek phaino φαίνω (φαίνω phaínō): emphasis fantasy phantom phantasm fantastic phase

Latin sero (serō): exert insert assert series dissertation

Latin iaceo (iaceō): ease adjacent

Latin iacio (iaciō): object subject inject eject jet jut

Latin venio (veniō): avenue revenue invent advent convene convenient venture adventure event prevent

Latin sedeo (sedeō): insidious possess obsess subside

Latin cura (cūra): curious proctor procurator procuracy accuracy proxy secure care

Latin pungo (pungō): poignant compunction 

Latin claudo (claudō): include exclude seclude recluse conclude close clause closure occlude

Latin video (videō): envy view visit visa vision review advise revise

Latin voco (vocō): advocate invoke revoke convoke avow avouch vouch

Ancient Greek lego λέγω (λέγω légō): -logy lexicon logic logo dialogue dialect analogy analogue catalogue

Latin fero (ferō): transfer refer reference relate relative confer conference vociferate collate collation fertile elate

Latin fallo (fallō): fallible infallible fail false default fault

Latin gratus (grātus): gratify gratification gratitude grateful agree disagreeable ingrate

Ancient Greek tasso τάσσω (τᾰ́σσω tássō): syntax syntagn taxonomy tactic tax 

Latin credo (crēdō): creed credo credit accredit credibility credence

Latin mitto (mittō): dismiss mission commission commit committee remission remit emit emission premise

Latin curro (currō): current currency occur recur incur concur precursor succor curricle curriculum course courier cursor cursive

Latin sto (stō): stage stand state status statement instant extant

Latin loquor (loquor): colloquial loquacious eloquence ventriloquist

Latin spargo (spargō): disperse sparse intersperse

Latin cresco (crēscō): concrete accrete recruit accrue increase decrease

Latin caedo (caedō): -cide genocide precise decision incision concise

Latin probo (probō): prove probe probate

Ancient Greek krino κρίνω (κρῑ́νω krī́nō): crisis critic hypocrite diacritic

Latin scio (sciō): science prescient conscience conscious nescient

Latin mando (mandō): command demand remand mandate commend

Latin fundo (fundō): perfuse profuse suffuse fuse fusion confuse refuse

Latin findo (findō): fissure fission

Latin altus (altus): altitude exalt altar haughty

Latin cerno (cernō): excrete discrete discreet decree discern concern

Latin prex (prex): pray precarious imprecate deprecate

Latin horreo (horreō): horror horrid abhor horrific

Latin placo (plācō): placate

Latin placeo (placeō): complacent complaisant please pleasure plea placid

Latin plico (plicō): apply reply comply simple accomplice complex duplex replicate duplicate complicate ply employ deploy imply implicit explicit explicate implicate

Latin tribus (tribus): retribution tribute attribute contribute tribe

Latin reor (reor): reason rational ratio

Latin battuo (battuō): combat debate battle abate

Latin seco (secō): sickle section bisect trisect

Latin trudo (trūdō): thrust intrude intrusive obtrude obtrusive

Latin rego (regō): correct erect direct rectify rectilinear rectangle

Latin donum (dōnum): donate donation condone

Latin scando (scandō): scale ascend descend

Ancient Greek tithemi τίθημι (τῐ́θημῐ títhēmi): thesis synthesis hypothesis antithesis parenthesis epithet

Latin sumo (sūmō): sumptuous sumptuary presume assume resume consume

Latin pono (pōnō): posit position positive compose expose impose repose propose purpose

Latin cado (cadō): cadence case

Latin gradior (gradior): progress regress egress congress aggression grade graduate gradient upgrade downgrade digress

Latin rogo (rogō): derogate interrogate surrogate arrogate arrogant rogue

Latin doceo (doceō): doctor docile document doctrine

Latin duco (dūcō): subdue induce seduce conduct conducive reduce duke abduct

Latin novus (novus): innovate novice renovate novel novelty novate supernova

Latin salio (saliō): salient insult exult resilient assault

Latin valeo (valeō): valid valour"""

def add_wordfamilies(db):
    n = 0
    db_list = db.split("\n\n")
    for wf in db_list:
        n += 1
        left_list = wf.split(': ')[0].split()
        if left_list[0] == 'Latin':
            lang = left_list[0]
            english_name = left_list[1]
            wiktionary_name = left_list[1]
            entry_name = left_list[2][1:-1]
            latinized_name = left_list[2][1:-1]
        elif left_list[0] == 'Ancient':
            lang = left_list[0] + " " + left_list[1]
            english_name = left_list[2]
            wiktionary_name = left_list[3]
            entry_name = left_list[4][1:]
            latinized_name = left_list[5][0:-1]
            
        if Entry.objects.filter(entry=english_name, language=lang).exists():
            peobj = Entry.objects.filter(entry=english_name, language=lang)[0]
            peobj.entry = entry_name
            peobj.english_name = english_name
            peobj.wiktionary_name = wiktionary_name
            peobj.latinized_name = latinized_name
            peobj.save()
        elif Entry.objects.filter(entry=wiktionary_name, language=lang).exists():
            peobj = Entry.objects.filter(entry=wiktionary_name, language=lang)[0]
            peobj.entry = entry_name
            peobj.english_name = english_name
            peobj.wiktionary_name = wiktionary_name
            peobj.latinized_name = latinized_name
            peobj.save()
        elif Entry.objects.filter(entry=latinized_name, language=lang).exists():
            peobj = Entry.objects.filter(entry=latinized_name, language=lang)[0]
            peobj.entry = entry_name
            peobj.english_name = english_name
            peobj.wiktionary_name = wiktionary_name
            peobj.latinized_name = latinized_name
            peobj.save()
        elif Entry.objects.filter(entry=entry_name, language=lang).exists():
            peobj = Entry.objects.filter(entry=entry_name, language=lang)[0]
            peobj.entry = entry_name
            peobj.english_name = english_name
            peobj.wiktionary_name = wiktionary_name
            peobj.latinized_name = latinized_name
            peobj.save()
        else:
            peobj = Entry.objects.create(entry=entry_name, language=lang, english_name=english_name, wiktionary_name=wiktionary_name, latinized_name=latinized_name)
        right_list = wf.split(': ')[1].split()
        for fw in right_list:
            if Entry.objects.filter(entry=fw, language="English").exists():
                fwobj = Entry.objects.filter(entry=fw, language="English")[0]
            else:
                fwobj = Entry.objects.create(entry=fw, language="English")
            if not FamilialRelation.objects.filter(primeetymon=peobj, familyword=fwobj).exists():
                FamilialRelation.objects.create(primeetymon=peobj, familyword=fwobj)
        print(f"{n}. finished adding {peobj.language} {peobj.entry} to model WordFamily")

def add_english_wiktionary_latinized_names():
    n = 0
    eng_entryobjs = Entry.objects.filter(language="English")
    for obj in eng_entryobjs:
        n += 1
        if obj.english_name == "":
            obj.english_name = obj.entry
        if obj.wiktionary_name == "":
            obj.wiktionary_name = obj.entry
        if obj.latinized_name == "":
            obj.latinized_name = obj.entry
        obj.save()
        print(f"{n}. done with {obj.entry}")

