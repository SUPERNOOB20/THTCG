// Thanks to https://www.reddit.com/r/programminghorror/comments/1p5pbgo/comment/nqks6qr/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

#include <string>
#include "card_data.h"

#define STB_IMAGE_IMPLEMENTATION
#include "image_loader/stb_image.h"


std::string list_of_names[27] = {"ascent.png", "descent.png", "seija.png", "chimata.png", "kosuzu.png", "nazrin.png", "reimu.png", "okuu.png", "kyouko.png", "tenshi.png", "cirno.png", "keine.png", "mystia.png", "remilia.png", "flandre.png", "sakuya.png", "wriggle.png", "youmu.png", "yuyuko.png", "seiga.png", "yoshika.png", "momoyo.png", "meiling.png", "sanae.png", "patchouli.png", "yorihime.png", "hijiri.png"};

// Relative? directory where the cards are installed.
// TODO: Might want to discern between Windows and Linux here! (and maybe MacOS needs a different path format too...? e.e)
std::string directory = "../../../Graphics/Cards";

std::string list_of_directories[27] = {};

for (name : list_of_names){
    list_of_directories[name] = name + directory;
    }

cards = {}      // cards = {Card("ascent.png"), Card("descent.png"), Card("seija.png"), etc.}

for (name : list_of_directories){
    cards[name] = Card(name)
    }

void load_given_card_data()
{
    // if no card data exists (a file called card_data.json can't be found), regen_card_data().
    


    class Card:
        __init__(self, source_file):
            add other fields as needed
            self.raw = pygame.image.load(source_file).convert_alpha()
            self.smol = pygame.transform.scale(surface = self.raw, size = small)
            self.width, self.height = self.smol.size
            self.data = pygame.image.tobytes(self.raw, "RGBA")

        change_size(size: str):
            match size:

                // small is the size of a card in the battlefield... so 10vh and 20vw.
                case "small":
                // set the mipmap to 2.



                // medium is the size of a card in fullscreen (for example on the gallery or when choosing cards) (fullscreen card).
                case "medium":
                // set the mipmap to 1.



                // large is the size of a portrait in zoomed-in gallery view (fullscreen portrait).
                case "large":
                // set the mipmap to 0.



                case "":
                cout << "ERROR 1: Invalid card size :(" << endl;



    void render_card(...)
        {
        glBindTexture(GL_TEXTURE_2D, card.texture)      // Adds card.texture to class above
        width = card.width
        height = card.width
        card_data = card.data
        color = card.color          // Adds card.color to class above
        // continue with remaining logic
        }

}   

void regen_card_data()
    {
        return;
    }

// databaseOfCards: Dict[str, Dict[Surf, bytes]]

// or...

// databaseOfCards: Dict[int, Dict[Surf, bytes]]
