import genanki
import noteTypes.minimal_pairs as minimal_pairs
import noteTypes.spelling_sounds as spelling_sounds
import noteTypes.mnemonics as mnemonic
import noteTypes.picture_words as picture_words
import noteTypes.all_purpose_card as all_purpose_card
import CONSTANTS

croatian_deck_id = 4597123561

# Create a new deck
deck = genanki.Deck(croatian_deck_id, "Croatian Deck Test")

# Add cards to the deck
minimal_pairs.add_card(deck, "apple", "Recording for apple", "orange", "Recording for orange", "apple", "Recording for apple", "")
spelling_sounds.add_card(deck, "apple", "orange", "apple", "Recording for apple")

# Create the package and export it to a file
package = genanki.Package(deck)
package.media_files = []
package.write_to_file("minimal_pairs.apkg")
# minimal_pairs.create_package(deck, "minimal_pairs.apkg")