import genanki
import CONSTANTS  


# Define the note type
model = genanki.Model(
    CONSTANTS.mnemonics_id,
    "3) Mnemonics",
    fields=[
        {"name": "Mnemonic Image (Burning, Exploding. Use a picture)"},
        {"name": "Meaning of this mnemonic (Masculine, feminine)"},
        {"name": "Example word for this mnemonic (With pictures)"},
        {"name": "Optional Any extra info (Back side of both cards)Recording of the Word (/IPA)"},
        {"name": "(Just for copy/paste)"},
    ],
    templates=[
        {
            "name": "What's the mnemonic mean?",
            "qfmt": "What's this mnemonic mean?<br><br>{{Mnemonic Image (Burning, Exploding. Use a picture)}}",
            "afmt": "{{FrontSide}} <hr id=answer> {{#Meaning of this mnemonic (Masculine, feminine)}}<i>{{Meaning of this mnemonic (Masculine, feminine)}}<br></i>{{/Meaning of this mnemonic (Masculine, feminine)}} <br> <font color=grey>{{Optional: Any extra info (Back side of both cards)}}</font>",
        },
        {
            "name": "What's the mnemonic for __?",
            "qfmt": "What's the mnemonic for: {{#Meaning of this mnemonic (Masculine, feminine)}}<font color=red>{{Meaning of this mnemonic (Masculine, feminine)}}</font>?<br><br>{{/Meaning of this mnemonic (Masculine, feminine)}}For examples like:<div style='font-family: Arial; font-size: 20px;'>{{Example word for this mnemonic (With pictures)}}</div>",
            "afmt": '{{FrontSide}} <hr id=answer> {{Mnemonic Image (Burning, Exploding. Use a picture)}} {{#Optional: Any extra info (Back side of both cards)}}<br><font color=grey>{{Optional: Any extra info (Back side of both cards)}}</font>{{/Optional: Any extra info (Back side of both cards)}}',
        },
    ],
    css=".card { font-family: arial; font-size: 20px; text-align: center; color: black; background-color: white;}.card1 { background-color: #FFFFFF; }.card2 { background-color: #FFFFFF; }",
)

# Create a function to add a new card to the deck
def add_card(deck, image, meaning, example, optional, just_for_copy_paste):
    # Create the note for the card
    note = genanki.Note(
        model=model,
        fields=[image, meaning, example, optional, just_for_copy_paste],
    )
    
    # Add the note to the deck
    deck.add_note(note)
