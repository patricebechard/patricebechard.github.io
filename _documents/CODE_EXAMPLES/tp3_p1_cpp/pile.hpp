#include <string>
#ifndef PILE_H
#define PILE_H
using namespace std;

class PileChar {
    public:
        void init(int taille);                 // création d'une pile
        void push(char n);                          // empiler un char au sommet de la pile
        char pop();                                  // retourner le char au sommet de la pile
        int vide() const;                           // vrai, si la pile est vide
        int pleine() const;                         // vrai, si la pile est pleine
        int getsize() const { return _taille; }
    private:
        int _taille;                                // taille de la pile
        int _sommet;                                // position du char à empiler
        int *_addr;                                 // adresse de la pile
};
#endif
