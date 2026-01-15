#include <string>
#include <iostream>

#define STB_IMAGE_IMPLEMENTATION
#include "image_loader/stb_image.h"


// size: 27.
std::string list_of_names[] = {"ascent.png", "descent.png", "seija.png", "chimata.png", "kosuzu.png", "nazrin.png", "reimu.png", "okuu.png", "kyouko.png", "tenshi.png", "cirno.png", "keine.png", "mystia.png", "remilia.png", "flandre.png", "sakuya.png", "wriggle.png", "youmu.png", "yuyuko.png", "seiga.png", "yoshika.png", "momoyo.png", "meiling.png", "sanae.png", "patchouli.png", "yorihime.png", "hijiri.png"};

// Relative? directory where the cards are installed.
// TODO: Might want to discern between Windows and Linux here! (and maybe MacOS needs a different path format too...? e.e)


std::string directory = "../../../Graphics/Cards/";
// std::string directory = "a";


std::string list_of_directories[27];




int width = 1000;
int height = 2000;
int nrChannels = 3;     // Setting the value to "3" handles images as RGB (I think... e.e)

void renderAllCards() {

    for (int i = 0; i < 27; ++i) {

        list_of_directories[i] = directory + list_of_names[i];
        
        unsigned int texture;
        glGenTextures(1, &texture);
        glBindTexture(GL_TEXTURE_2D, texture);
        // set the texture wrapping/filtering options (on currently bound texture)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);

        unsigned char *data = stbi_load(list_of_directories[i], &width, &height, &nrChannels, 0);
        
        if (data)
        {
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGB, GL_UNSIGNED_BYTE, data);
            glGenerateMipmap(GL_TEXTURE_2D);
        }

        else
        {
            std::cout << "Failed to load texture" << std::endl;
        }

        stbi_image_free(data);


    }

    return;
}

int main() {
    renderAllCards();
    return 0;
}
