#script for first simple google keep database

import sys, os
import django

parent_dir1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
parent_dir2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(parent_dir1)
sys.path.append(parent_dir2)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wordfeel.settings")
django.setup()

from entries.models import Entry, EntriesRelation

def add_siblings(siblings):
    sib = siblings.split()
    print(sib)
    sib2 = sib.copy()
    for s1 in sib:
        sib2.remove(s1)
        for s2 in sib2:
            s1E = Entry.objects.filter(entry=s1)[0]
            s2E = Entry.objects.filter(entry=s2)[0]
            EntriesRelation.objects.create(from_entry=s1E, to_entry=s2E, relation_type='sibling')
            print(f"done from {s1} to {s2} and from {s2} to {s1}")

def add_etymons_child(etymons, child):
    print("child =", child)
    et = etymons.split()
    print("etymons = ", et)
    for etymon in et:
        etymonE = Entry.objects.filter(entry=etymon)[0]
        childE = Entry.objects.filter(entry=child)[0]
        EntriesRelation.objects.create(from_entry=childE, to_entry=etymonE, relation_type='etymon')
        EntriesRelation.objects.create(from_entry=etymonE, to_entry=childE, relation_type='child')
        print(f"{child}'s etymon is {etymon} and {etymon}'s child is {child}")



siblings = "select elect eligible elegant collect intellect intelligent diligent legume leguminous lecture neglect sacrilege lection lesson"
etymons = "legere"
child = "lesson"


#add_etymons_child(etymons, child)
#add_siblings(siblings)




