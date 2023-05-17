import genanki
import CONSTANTS


# Define the note type
model = genanki.Model(
    CONSTANTS.picture_words_id,
    "4) Picture Words",
    fields=[
        {"name": "Word"},
        {"name": "Picture"},
        {"name": "Gender, Personal Connection, Extra Info (Back side)"},
        {"name": "Pronunciation (Recording and/or IPA)"},
        {"name": "Test Spelling? (y = yes, blank = no)"},
    ],
    templates=[
        {
            "name": "Comprehension Card",
            "qfmt": "{{Word}}",
            "afmt": "{{FrontSide}}<hr id=answer>{{Picture}}{{#Pronunciation (Recording and/or IPA)}}<br><font color=blue>{{Pronunciation (Recording and/or IPA)}}</font>{{/Pronunciation (Recording and/or IPA)}}<br><span style='color:grey'>{{Gender, Personal Connection, Extra Info (Back side)}}</span><br><br>",
        },
        {
            "name": "Production Card",
            "qfmt": "{{Picture}}<br><br>\\n\\n<font color=red></font><br><br>\\n\\n<font color=red></font><br><br>",
            "afmt": "{{FrontSide}}<hr id=answer><span style=\"font-size:1.5em;\">{{Word}}</span><br>{{#Pronunciation (Recording and/or IPA)}}<br><font color=blue>{{Pronunciation (Recording and/or IPA)}}</font>{{/Pronunciation (Recording and/or IPA)}}{{#Gender, Personal Connection, Extra Info (Back side)}}<br><font color=grey>{{Gender, Personal Connection, Extra Info (Back side)}}</font>{{/Gender, Personal Connection, Extra Info (Back side)}}<span style=\"\">",
        },
        {
            "name": "Spelling?",
            "qfmt": "{{#Test Spelling? (y = yes, blank = no)}}Spell this word: <br><br>{{Picture}}<br>{{#Pronunciation (Recording and/or IPA)}}<br><font color=blue>{{Pronunciation (Recording and/or IPA)}}</font>{{/Pronunciation (Recording and/or IPA)}}<br>{{/Test Spelling? (y = yes, blank = no)}}",
            "afmt": '<span style="font-size:1.5em;">{{Word}}</span><br><br>{{Picture}}<br><span style="color:grey;">{{Gender, Personal Connection, Extra Info (Back side)}}</span>',
        }
    ],
    css=".card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white;}.card1 { background-color: #FFFFFF; }.card2 { background-color: #FFFFFF; }",
)

# Create a function to add a new card to the deck


def add_card(deck, word, picture, gender_pc_extra, pronunciation, test_spelling):
    # Create the note for the card
    note = genanki.Note(
        model=model,
        fields=[word, picture, gender_pc_extra, pronunciation, test_spelling],
    )

    # Add the note to the deck
    deck.add_note(note)
