#include <stdlib.h> // rand()
#include <iostream> 
#include "pile.hpp"
using namespace std;

int main() {
    PileInt pile;
    pile.init(15);                          // pile de 15 entiers
    while ( ! pile.pleine() )               // remplissage de la pile
        pile.push( rand() % 100 );
    while ( ! pile.vide() )                 // Affichage de la pile
        cout << pile.pop() << " "; cout << endl;
    
    return 0;
}