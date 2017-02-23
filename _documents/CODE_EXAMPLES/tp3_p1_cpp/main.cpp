//
// TP3 - exercice 1
//
// Patrice Béchard p1088418 BECP30119404
// Louis Bilodeau-Gravel p1086241 BILL12069509
//
// 17 avril 2016
//

#include <iostream>
#include <string>
#include "pile.hpp"

using namespace std;

int do_op(char op, int a, int b)
{
    switch(op)
    {
        case '+':                           //on applique le symbole aux deux operandes
            return a+b;
            break;
        case '-':
            return a-b;
            break;
        case '*':
            return a*b;
            break;
        case '/':
            return a/b;
            break;
        default:
            throw runtime_error("unknown op");
    }
}



int main() {
    string laChainePolonaise;
    cout<<"Entrer la chaîne de caractères dans la notation polonaise voulant être calculée : \n\n";
    cin>>laChainePolonaise;                     //la chaine que l'on veut calculer est entrée
    cout<<endl;
    PileChar pileoperande;                      //création de la pile
    int taille=laChainePolonaise.size();        //et on trouve la taille
    pileoperande.init(taille);                  //la pile a cette taille
    for(char& symbole : laChainePolonaise){
        int operande1, operande2;
        int valeur;
        if (symbole!='+'&&symbole!='-'&&symbole!='*'&&symbole!='/'){        //si c'est juste un nombre
            pileoperande.push(symbole);}
        else{                                               //c'est un operateur
            operande2=pileoperande.pop()-'0';        //operande 2 en premier pour respecter
            operande1=pileoperande.pop()-'0';        //l'ordre quand on a - ou / (converti avec ascii)
            valeur=do_op(symbole,operande1,operande2);      //la fonction do_op calcule le resultat
            valeur=valeur+'0';                              //et on remet pour la table ascii
            pileoperande.push(valeur);
        }
    }
    cout<<"Le résultat que l'expression en notation polonaise "<<laChainePolonaise<<" est : "<<pileoperande.pop()-'0'<<"\n\n";
    
    return 0;
}
