#WordFeel

WordFeel is a long-time passion project of mine very close to my heart. The whole idea is to attempt to organize words in etymological families rather than lexicographic series.

##Distinctiveness and Complexity

WordFeel is sufficiently distinct as it's neither a social network, e-commerce, encyclopedia or an e-mail client. It is like a hierarchical dictionary structure which the Oxford English Dictionary (www.oed.com) should adopt for its unsurpassed compendium. It is ambitious in its scope to clot together family words rather than being stuck in an alphabetical sequence.

It is sufficiently complex, requiring lots of views and templates. The major challenge of this project for me was the data. I used the Etymological Wordnet database by Gerard de Melo and my own self-compiled Google Keep Notes dataset that took me years to write for this project. I never thought loading a dataset would be so challenging, and made me appreciate and acknowledge Data Engineering. I used scripts to add a  lot of EntriesRelation and WordFamily records, but still had to do some manual labor.

In the project I define Prime Etymons as Etymons which don't have any more primitive etymons of themselves that are not from Proto-Languages. On the left side of an entry's page you are able to see its Variants, Prime Etymons, Etymons, Roots, Related Words, Family Words & Derivatives.

I used PostgreSQL for this for enhanced scalability & security. I faced huge complexity & hurdles in curating the dataset. I faced a lot of problems while parsing & loading the etymwn database (a .tsv file) I used here. My MacBook used to get hot and many times it used to throw an exception after hours of processing shining light at how important it is to write the correct algorithm lest you end up wasting time and resources. I wrote multiple scripts to extract and load the data into Django models. There's still a lot of work to be done on WordFeel, I want to use Machine Learning models to highly accurately extract the relationship data between words from Wiktionary much more properly than etymwn which also seems to have its source in Wiktionary. I have already bought wordfeel.org domain fortunately I was able to save it. 

Also along with relationships there are Wiktionary Etymologies & Definitions that come on the right side of an entry's page that are scraped from wiktionary entries live using bs4 BeautifulSoup library. Earlier I found a really helpful library named "wiktionaryparser" for this task but it had problems like sub-definitions being stripped off when words had them so I took its bones and rewrote & edited a lot of it to make my own script to fit my requirements.

##File Contents

###etymwn_script.py

This script was used to load etymwn data to Entry & EntriesRelation models

###lang_script.py

I sed this script to change the ISO 639-3 and ISO 639-2 language codes from the etymwn dataset to their proper names.

###wiktionary_script.py

This is a pretty major script of the project, I have included this in the root of the app directory also. This scrapes the wiktionary entry page via BeautifulSoup and a class method returns the resulting object when called.

###word_families_script.py

This script used the data from my Google Keep Notes and parsed & loaded the data to the FamilialRelation model. I had to do a lot of work in adding the proper diacritical forms of the words along with each of their proper language names. Also had to add the form used to access the word's wiktionary entry to prevent the scenario of missing wiktionary etymologies and definitions.

###scroll_entries.js

This file is responsible to load the entries in the entries page from the backend asynchronously employing AJAX via an API and implements infinite scroll as long as there are entries left to load.

###search.js

This implements the search with dropdown functionality on the client-side using another API to fetch matching entries from the backend before loading them in the frontend, also employing the AJAX technology in the process.

###styles-index.css

Style Sheet for the index page.

###styles.css

Style Sheet for the rest of the pages.

###entries.html

Template for the Entries page that is also accessible from the navbar which contains a list of all entries in the database.

###entry.html

Template for an entry's own page that is accessible when you click on an entry's name. It contains various forms of related entries on the left and the entry's etymologies and definitions on the right.

###index.html

Template for the index page of WordFeel.

###layout.html

The layout template file extended in most of the templates except the index.

###results.html

The template file used to show results of a search.

###word_families.html

Template for the Word Families page that is also accessible from the navbar which contains a list of all the word families from my hard-compiled Google Keep Notes dataset that I loaded into this project's database.

###urls.py

URL patterns for the app "entries".

###views.py

Views for the URL patterns in the app "entries" used to render templates with context.

###Dockerfile
Just in case I need to use Docker. Made it as instructed in Lecture 7's Notes.

###docker-compose.yml 

Same as above, has link to etymwn-dump.sql, my database's latest dump. Made this also as instructed in Lecture 7's Notes.

###dump-command.txt

The dump Terminal command stored for convenience.

###requirements.txt

The required modules used in the project to install before running the project.

##How to run the application

1. Install the modules in requirements.txt using pip3, download & install PosgreSQL.
2. Create user names "postgres" with password "1234".
3. Run "python3 manage.py makemigrations" & "python3 manage.py migrate" while in project ideally in IDE terminal to create the database schema.
4. cd to project root directory with etymwn-dump.sql and run "psql -d etymwn -U postgres -f etymwn-dump.sql" and provide password "1234".
5. Run "python3 manage.py runserver" and hopefully you are able to see the project in action.