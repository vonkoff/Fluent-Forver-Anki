import genanki
import CONSTANTS



# Define the note type
model = genanki.Model(
    CONSTANTS.spelling_sounds_id,
    "2) Spelling and Sounds",
    fields=[
        {"name": "Spelling (a letter or combination of letters)"},
        {"name": "Example word for that spelling/sound combination"},
        {"name": "Picture of the example word"},
        {"name": "Recording of the Word (/IPA)"},
    ],
    templates=[
        {
            "name": "What's the sound?",
            "qfmt": "What sound does this make?<br><br><div style='font-family: Arial; font-size: 40px;'>{{Spelling (a letter or combination of letters)}}</div><br> as in <b>'{{Example word for that spelling/sound combination}}'</b> <br><br> <div style='margin:0 auto'>{{Picture of the example word}}</div>",
            "afmt": "{{FrontSide}}<hr id=answer>{{#Recording of the Word (/IPA)}}{{Recording of the Word (/IPA)}}{{/Recording of the Word (/IPA)}}<br>r>",
        },
        {
            "name": "What's the spelling?",
            "qfmt": 'How do you spell this word? {{#Recording of the Word (/IPA)}}{{Recording of the Word (/IPA)}} {{/Recording of the Word (/IPA)}}<br> <br> <div style="margin:0 auto">{{Picture of the example word}}</div>',
            "afmt": '<div style="font-family: Arial; font-size: 30px;"">"{{Example word for that spelling/sound combination}}"</b></div> <br><br>(Example for the spelling: "{{Spelling (a letter or combination of letters)}}")>"',
        },
    ],
    css=".card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white;}.card1 { background-color: #FFFFFF; }.card2 { background-color: #FFFFFF; }",
)

# Create a function to add a new card to the deck
def add_card(deck, spelling, example_word, picture_example, recording):
    # Create the note for the card
    note = genanki.Note(
        model=model,
        fields=[spelling, example_word, picture_example, recording],
    )
    
    # Add the note to the deck
    deck.add_note(note)
