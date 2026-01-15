#include <string>
#include <iostream>

int main(){


    // size: 27.
    std::string list_of_names[] = {"ascent.png", "descent.png", "seija.png", "chimata.png", "kosuzu.png", "nazrin.png", "reimu.png", "okuu.png", "kyouko.png", "tenshi.png", "cirno.png", "keine.png", "mystia.png", "remilia.png", "flandre.png", "sakuya.png", "wriggle.png", "youmu.png", "yuyuko.png", "seiga.png", "yoshika.png", "momoyo.png", "meiling.png", "sanae.png", "patchouli.png", "yorihime.png", "hijiri.png"};

    // Relative? directory where the cards are installed.
    // TODO: Might want to discern between Windows and Linux here! (and maybe MacOS needs a different path format too...? e.e)


    std::string directory = "../../../Graphics/Cards/";
    // std::string directory = "a";


    std::string list_of_directories[27] = {};

    /*
    for (std::string name : list_of_names[]){
        list_of_directories[name] = name + directory;
        
        cout << list_of_directories[name] << endl;

        }
    */


    // std::size(list_of_names)


    for (int i = 0; i < 27 ; ++i){
        list_of_directories[i] = directory + list_of_names[i];
        
        std::cout << list_of_directories[i] << std::endl;

        }


    return 0;
}
