import genanki
import CONSTANTS


# Define the note type
model = genanki.Model(
    CONSTANTS.minimal_pairs_id,
    "1) Minimal Pairs",
    fields=[
        {"name": "Word 1"},
        {"name": "Recording 1"},
        {"name": "Word 2"},
        {"name": "Recording 2"},
        {"name": "Word 3"},
        {"name": "Recording 3"},
        {"name": "Compare Word 2 to Word 3?"},
        {"name": "Audio"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": "<i>Do you hear</i><br><br>{{Word 1}}<br><br><i> or </i><br><br>{{Word 2}}?<br>{{Recording 1}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 1}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 1}}",
        },
        {
            "name": "Card 2",
            "qfmt": "{{FrontSide}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 2}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 2}}",
        },
        {
            "name": "Card 3",
            "qfmt": "{{#Word 3}}<i>Do you hear</i><br><br>{{Word 1}}<br><br><i> or </i><br><br>{{Word 3}}?<br>{{Recording 1}}{{/Word 3}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 3}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 3}}",
        },
        {
            "name": "Card 4",
            "qfmt": "{{FrontSide}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 1}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 1}}",
        },
        {
            "name": "Card 5",
            "qfmt": "{{#Compare Word 2 to Word 3?}}{{#Word 3}}<i>Do you hear</i><br><br>{{Word 2}}<br><br><i> or </i><br><br>{{Word 3}}?<br>{{Recording 2}}{{/Word 3}}{{/Compare Word 2 to Word 3?}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 2}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 2}}",
        },
        {
            "name": "Card 6",
            "qfmt": "{{#Compare Word 2 to Word 3?}}{{#Word 3}}<i>Do you hear</i><br><br>{{Word 2}}<br><br><i> or </i><br><br>{{Word 3}}?<br>{{Recording 3}}{{/Word 3}}{{/Compare Word 2 to Word 3?}}",
            "afmt": "{{FrontSide}}<hr id=answer>You heard: {{Word 3}}<div style='font-family: Arial; font-size: 20px;'></div>{{Recording 3}}",
        },
    ],
    css=".card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white; }",
)

# Create a function to add a new card to the deck


def add_card(deck, word1, recording1, word2, recording2, word3, recording3, compare_word2_word3, audio):
    # Create the note for the card
    note = genanki.Note(
        model=model,
        fields=[
            word1,
            recording1,
            word2,
            recording2,
            word3,
            recording3,
            compare_word2_word3,
            audio,
        ],
    )

    # Add the note to the deck
    deck.add_note(note)
