/*
 TP2 - exercice 2
 
 Patrice B�chard p1088418 BECP30119404
 
 20 mars 2016
 */
#include "TP2Num2_H.h"//on inclut le header

using namespace std;
//on d�clare la m�thode de notre constructeur par d�faut.
Voiture::Voiture(){
	_sorte=0;//on va utiliser cette m�thode pour la fin de tabVoiture 
}
//On d�clare la m�thode de notre constructeur param�tr� qui initialise notre classe
Voiture::Voiture(int numeroSerie, int sorte, int annee, float prix){
	_numeroSerie=numeroSerie;
	_sorte=sorte;
	_annee=annee;
	_prix=prix;
}
//on d�clare un constructeur de copie
Voiture::Voiture(Voiture const &laVoiture){
	this->_numeroSerie=laVoiture._numeroSerie;
	this->_sorte=laVoiture._sorte;
	this->_annee=laVoiture._annee;
	this->_prix=laVoiture._prix;
}
//on d�clare un destructeur
Voiture::~Voiture(){
	/*Puisqu'on pas d'allocation dynamique de la m�moire le destructeur reste vide*/
}
//on d�clare les m�thodes qui permettent de modifier les diff�rentes valeurs
void Voiture::setNumeroSerie(int numeroSerie){
	_numeroSerie=numeroSerie;
}
void Voiture::setSorte(int sorte){
	_sorte=sorte;
}
void Voiture::setAnnee(int annee){
	_annee=annee;
}
void Voiture::setPrix(float prix){
	_prix=prix;
}
//on d�clare les m�thodes qui permettent d'acc�der aux diff�rentes valeurs
int Voiture::getNumeroSerie(){
	return this->_numeroSerie;
}
int Voiture::getSorte(){
	return this->_sorte;
}
int Voiture::getAnnee(){
	return this->_annee;
}
float Voiture::getPrix(){
	return this->_prix;
}
//on d�clare la m�thode qui permet d'afficher nos valeurs sous forme de string.
string Voiture::afficher(){
	string result=to_string(_numeroSerie)+";"+to_string(_sorte)+";"+to_string(_annee)+";"+to_string(_prix);
	return result;
}

