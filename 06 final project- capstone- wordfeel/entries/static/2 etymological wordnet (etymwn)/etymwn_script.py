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

import pandas

etymwn = pandas.read_csv("/Users/Madhavik/Downloads/edX/02 CS50W 2020/06 final project- capstone- wordfeel/assets/etymwn.tsv", sep='\t', header=None)

column_labels = ["from_entry", "relation_type", "to_entry"]
etymwn.columns = column_labels

EntryRelations_df = pandas.DataFrame(columns=column_labels)

#['rel:etymological_origin_of' 'rel:has_derived_form' 'rel:is_derived_from' 'rel:etymology' 'rel:etymologically_related' 'rel:variant:orthography' 'rel:derived'x 'rel:etymologically'x]
total = len(etymwn.index)
for index, row in etymwn.iterrows():
    if row["from_entry"].startswith("eng:") and row["relation_type"] == "rel:etymology":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["to_entry"].startswith("eng:") and row["relation_type"] == "rel:etymological_origin_of":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["from_entry"].startswith("eng:") and row["relation_type"] == "rel:has_derived_form":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["from_entry"].startswith("eng:") and row["relation_type"] == "rel:is_derived_from":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["to_entry"].startswith("eng:") and row["relation_type"] == "rel:derived":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["from_entry"].startswith("eng:") and row["to_entry"].startswith("eng:") and row["relation_type"] == "rel:etymologically_related":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    if row["from_entry"].startswith("eng:") and row["relation_type"] == "rel:variant:orthography":
        EntryRelations_df = pandas.concat([EntryRelations_df, pandas.DataFrame([row])], ignore_index=True)
    print("Done making EntryRelations_df at index:", index, "of", total)

print("finished for loop 1")
total = len(EntryRelations_df.index)
for index, row in EntryRelations_df.iterrows():
    if not Entry.objects.filter(entry=row['from_entry'].split(': ')[1], language=row['from_entry'].split(':')[0]).exists():
        Entry_from = Entry(entry=row['from_entry'].split(': ')[1], language=row['from_entry'].split(':')[0])
        Entry_from.save()
    else:
        Entry_from = Entry.objects.filter(entry=row['from_entry'].split(': ')[1], language=row['from_entry'].split(':')[0])[0]
    if not Entry.objects.filter(entry=row['to_entry'].split(': ')[1], language=row['to_entry'].split(':')[0]).exists():
        Entry_to = Entry(entry=row['to_entry'].split(': ')[1], language=row['to_entry'].split(':')[0])
        Entry_to.save()
    else:
        Entry_to = Entry.objects.filter(entry=row['to_entry'].split(': ')[1], language=row['to_entry'].split(':')[0])[0]
    EntryRelations_row = EntriesRelation(from_entry=Entry_from, relation_type=row['relation_type'], to_entry=Entry_to)
    EntryRelations_row.save()
    print("Saved row to EntryRelations model at index:", index, "of", total)

print("finished for loop 2")

# what is left? to switch Entry object language codes with full forms and add meanings to Entry objects