import genanki
import CONSTANTS

# Define the note type
model = genanki.Model(
    CONSTANTS.picture_words_id,
    "4) Picture Words",
    fields=[
        {"name": "Front (Example with word blanked out or missing)"},
        {"name": "Front (Picture)"},
        {"name": "Front (Definitions, base word, etc.)"},
        {"name": "Back (a single word/phrase, no context)"},
        {"name": "- The full sentence (no words blanked out)"},
        {"name": "- Extra Info (Pronunciation, personal connections, conjugations, etc)"},
        {"name": "• Make 2 cards? (y = yes, blank = no)"},
        {"name": "• Test Spelling (Insert sound file/pronunciation here to test, leave blank otherwise)"},
        {"name": "(Copy and paste area)"},
    ],
    templates=[
        {
            "name": "Card 1: What word fits into the blank?",
            "qfmt": "{{Front (Example with word blanked out or missing)}}<br><br><div style='font-family: Arial; font-size: 20px;'>{{Front (Picture)}}</div><br><div style='font-family: Arial; font-size: 20px;color:red'>{{Front (Definitions, base word, etc.)}}</div>",
            "afmt": "{{FrontSide}}<hr id=answer>{{Back (a single word/phrase, no context)}}<br><br><strong><div style='font-family: Arial; font-size: 20px;'>{{- The full sentence (no words blanked out)}}</div></strong><br><div style='font-family: Arial; font-size: 20px;color:grey;'>{{- Extra Info (Pronunciation, personal connections, conjugations, etc)}}</div>",
        },
        {
            "name": "Optional Card 2: Give an example for this word",
            "qfmt": '{{#• Make 2 cards? ("y" = yes, blank = no)}}{{Back (a single word/phrase, no context)}}{{/• Make 2 cards? ("y" = yes, blank = no)}}',
            "afmt": '{{FrontSide}}<hr id=answer>{{Front (Example with word blanked out or missing)}}<br><br><strong><div style="font-family: Arial; font-size: 20px;">{{- The full sentence (no words blanked out)}}</div></strong><br><div style="font-family: Arial; font-size: 20px;">{{Front (Picture)}}</div><br><div style="font-family: Arial; font-size: 20px;color:red">{{Front (Definitions, base word, etc.)}}</div><br><div style="font-family: Arial; font-size: 20px;color:grey;">{{- Extra Info (Pronunciation, personal connections, conjugations, etc)}}</div>;',
        },
        {
            "name": "Optional Card #3: Test spelling (For Chinese, Japanese)",
            "qfmt": '{{#• Test Spelling (Insert sound file/pronunciation here to test, leave blank otherwise)}}Spell this word:<br><br>{{Front (Example with word blanked out or missing)}}<br><br><div style="font-family: Arial; font-size: 20px;">{{Front (Picture)}}</div><br><div style="font-family: Arial; font-size: 20px;color:red">{{Front (Definitions, base word, etc.)}}</div><br>{{• Test Spelling (Insert sound file/pronunciation here to test, leave blank otherwise)}}{{/• Test Spelling (Insert sound file/pronunciation here to test, leave blank otherwise)}}',
            "afmt": "{{Back (a single word/phrase, no context)}}<br><br><strong><div style='font-family: Arial; font-size: 20px;'>{{- The full sentence (no words blanked out)}}</div></strong><br><div style='font-family: Arial; font-size: 20px;color:grey;'>{{- Extra Info (Pronunciation, personal connections, conjugations, etc)}}</div><hr id=answer>{{FrontSide}}",
        }
    ],
    css='.card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white; }',
)

# Create a function to add a new card to the deck
def add_card(deck, word, picture, extra_info, recording, test_spelling):
    # Create the note for the card
    note = genanki.Note(
        model=model,
        fields=[word, picture, extra_info, recording, test_spelling],
    )
    
    # Add the note to the deck
    deck.add_note(note)
