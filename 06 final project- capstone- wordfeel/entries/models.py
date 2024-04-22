from django.db import models

# Create your models here.

class Entry(models.Model):
    entry = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200, default="") # for search
    wiktionary_name = models.CharField(max_length=200, default="") # for wiktionary
    latinized_name = models.CharField(max_length=200, default="")
    language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.language} {self.entry}"

class EntriesRelation(models.Model):
    from_entry = models.ForeignKey(Entry, related_name='relations_as_fromentry', on_delete=models.CASCADE)
    relation_type = models.CharField(max_length=50)
    to_entry = models.ForeignKey(Entry, related_name='relations_as_toentry', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.from_entry}'s {self.relation_type} is {self.to_entry}"
    
class FamilialRelation(models.Model):
    primeetymon = models.ForeignKey(Entry, related_name="wordfamilies_as_primeetymon", on_delete=models.CASCADE)
    familyword = models.ForeignKey(Entry, related_name="wordfamilies_as_familyword", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.primeetymon} is prime etymon of family word {self.familyword}"
