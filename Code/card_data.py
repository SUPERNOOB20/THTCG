# Thanks to https://www.reddit.com/r/programminghorror/comments/1p5pbgo/comment/nqks6qr/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

"""
from enum import Enum

class CardID(Enum):
    ASCENT = 0
    .
    .
    .
    HIJIRI = 27
"""

list_of_names = ["kosuzu", "nazrin", ...]
cards = {}  # cards = {"ascent.png", }
for name in list_of_names:
    cards[name] = Card(f"{name}.png")

def load_card_data():
    # if no card data exists (a file called card_data.json can't be found), regen_card_data().
    


    class Card:
        def __init__(self, source_file):
            # add other fields as needed
            self.raw = pygame.image.load(source_file).convert_alpha()
            self.smol = pygame.transform.scale(surface = self.raw, size = small)
            self.width, self.height = self.smol.size
            self.data = pygame.image.tobytes(self.raw, "RGBA")

        def change_size(size: str):
            match size:
                case "small":
                    pass
                case "medium":
                    pass
                case "large":
                    pass
                case "":
                    print("ERROR")

    def render_card(...):
        glBindTexture(GL_TEXTURE_2D, card.texture) # add card.texture to class above
        width = card.width
        height = card.width
        card_data = card.data
        color = card.color # add card.color to class above
        # continue with remaining logic


    


    return

regen_card_data()

# databaseOfCards: Dict[str, Dict[Surf, bytes]]

# or...

# databaseOfCards: Dict[int, Dict[Surf, bytes]]