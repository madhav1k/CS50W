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

from entries.models import Entry, EntriesRelation

def add_cognates(cognates):
    cog1 = cognates.split()
    print(cog1)
    cog2 = cog1.copy()
    for c1 in cog1:
        cog2.remove(c1)
        for c2 in cog2:
            c1obj = Entry.objects.filter(entry=c1, language="English")[0]
            if not c1obj.exists():
                c1obj = Entry.objects.create(entry=c1, language="English", featured=True)
            elif c1obj.featured == False:
                c1obj.featured = True
            c2obj = Entry.objects.filter(entry=c2, language="English")[0]
            if not c2obj.exists():
                c2obj = Entry.objects.create(entry=c2, language="English", featured=True)
            elif c2obj.featured == False:
                c2obj.featured = True
            if not EntriesRelation.objects.filter(from_entry=c1obj, to_entry=c2obj, relation_type='cognateof').exists():
                EntriesRelation.objects.create(from_entry=c1obj, to_entry=c2obj, relation_type='cognateof')
            if not EntriesRelation.objects.filter(from_entry=c2obj, to_entry=c1obj, relation_type='cognateof').exists():
                EntriesRelation.objects.create(from_entry=c2obj, to_entry=c1obj, relation_type='cognateof')
            print(f"{c1} is cognate of {c2} and {c2} is cognate of {c1}")

def add_primeetymons_crossderivative(primeetymons, langs, crossderivative):
    print("crossderivative =", crossderivative)
    primeetymons_list = primeetymons.split()
    print("primeetymons = ", primeetymons_list)
    langs_list = langs.split()
    print("langs = ", langs_list)
    crossderivativeobj = Entry.objects.filter(entry=crossderivative, language="English")[0]
    if not crossderivativeobj.exists():
        crossderivativeobj = Entry.objects.create(entry=crossderivative, language="English", featured=True)
    elif crossderivativeobj.featured == False:
        crossderivativeobj.featured = True
    for primeetymon, lang in zip(primeetymons_list, langs_list):
        primeetymonobj = Entry.objects.filter(entry=primeetymon, language=lang)[0]
        if not primeetymonobj.exists():
            primeetymonobj = Entry.objects.create(entry=primeetymon, language=lang, featured=True)
        elif primeetymonobj.featured == False:
            primeetymonobj.featured = True
        if not EntriesRelation.objects.filter(from_entry=primeetymonobj, to_entry=crossderivativeobj, relation_type='primeetymonof').exists():
            EntriesRelation.objects.create(from_entry=primeetymonobj, to_entry=crossderivativeobj, relation_type='primeetymonof')
        if not EntriesRelation.objects.filter(from_entry=crossderivativeobj, to_entry=primeetymonobj, relation_type='crossderivativeof').exists():
            EntriesRelation.objects.create(from_entry=crossderivativeobj, to_entry=primeetymonobj, relation_type='crossderivativeof')
        print(f"{primeetymon} is primeetymon of {crossderivative} and {crossderivative} is crossderivative of {primeetymon}")

def add_root_intraderivatives(root, lang, intraderivatives):
    intraderivatives_list = intraderivatives.split()
    print("intraderivatives =", intraderivatives_list)
    print("root = ", root)
    print("lang = ", lang)
    rootobj = Entry.objects.filter(entry=root, language=lang)[0]
    if not rootobj.exists():
        rootobj = Entry.objects.create(entry=root, language=lang, featured=True)
    elif rootobj.featured == False:
        rootobj.featured = True
    for intraderivative in intraderivatives:
        intraderivativeobj = Entry.objects.filter(entry=intraderivative, language=lang)[0]
        if not intraderivativeobj.exists():
            intraderivativeobj = Entry.objects.create(entry=intraderivative, language=lang, featured=True)
        elif intraderivativeobj.featured == False:
            intraderivativeobj.featured = True
        if not EntriesRelation.objects.filter(from_entry=rootobj, to_entry=intraderivativeobj, relation_type='rootof').exists():
            EntriesRelation.objects.create(from_entry=rootobj, to_entry=intraderivativeobj, relation_type='rootof')
        if not EntriesRelation.objects.filter(from_entry=intraderivativeobj, to_entry=rootobj, relation_type='intraderivativeof').exists():
            EntriesRelation.objects.create(from_entry=intraderivativeobj, to_entry=rootobj, relation_type='intraderivativeof')
        print(f"{root} is root of {intraderivative} and {intraderivative} is intraderivative of {root}")

cognates = "select elect eligible elegant collect intellect intelligent diligent legume leguminous lecture neglect sacrilege lection lesson"
primeetymons = "legere"
langs = ""
crossderivative = "lesson"
root = ""
lang = ""
intraderivatives = ""

#add_cognates(cognates)
#add_primeetymons_crossderivative(primeetymons, langs, crossderivative)
#add_root_intraderivatives(root, lang, intraderivatives)