/*
 TP2 - exercice 2
 
 Patrice Béchard p1088418 BECP30119404

 
 20 mars 2016
 */
#include <iostream>
#include <iomanip>
#include "TP2Num2Voiture.cpp"//on inclut le fichier qui contient nos méthodes

using namespace std;
//on déclare notre tableau de pointeur sur nos objets
Voiture* tabVoiture[200];

int main(){
	//on initialise 10 voiture 
	tabVoiture[0]=new Voiture(12345678,1,1993,14500.00);
	tabVoiture[1]=new Voiture(23456789,2,1996,22899.99);
	tabVoiture[2]=new Voiture(34567890,3,1985,4700.00);
	tabVoiture[3]=new Voiture(45678901,1,2007,23115.99);
	tabVoiture[4]=new Voiture(56789012,1,2010,56789.95);
	tabVoiture[5]=new Voiture(67890123,2,2014,21500.50);
	tabVoiture[6]=new Voiture(78901234,3,1998,700.00);
	tabVoiture[7]=new Voiture(89012345,2,2005,6700.00);
	tabVoiture[8]=new Voiture(90123456,3,2001,36789.80);
	tabVoiture[9]=new Voiture(12345679,1,1994,18000.00);
	//on initialise une voiture de plus pour indiquer la fin de tabVoiture
	tabVoiture[10]=new Voiture();
	int i=0;//compteur
	//boucle permettant de trier le tableau en ordre croissant
	while (i<200){
		if (tabVoiture[i]->getSorte()==0){//condition si on est à la fin de tabVoiture
			break;
		}
		int j=0;//compteur
		while(j<200){
			if (tabVoiture[j]->getSorte()==0){//condition si on est à la fin de tabVoiture
				break;
			}
			//on compare les numéros de séries et on permutte si nécessaire
			if (tabVoiture[i]->getNumeroSerie()<tabVoiture[j]->getNumeroSerie()){
				Voiture temporaire;
				temporaire=*tabVoiture[i];
				*tabVoiture[i]=*tabVoiture[j];
				*tabVoiture[j]=temporaire;
			}
			j++;	
		}
		i++;	
	}
	int j=0;
	int nombreVoiture=i;//on réutilise notre compteur du nombre de voiture 
	//on se déclare plusieurs variables
	float totalVente=0;
	int nombreVoitureAmericaine20000=0;
	int nombreVoiture2003=0;
	int nombreVoitureJaponaise=0;
	float sommePrixJaponaise=0;
	float prixMoyenJaponaise;
	int numSerieMeilleur;
	float prixMeilleur=100000;
	//boucle sur les voitures
	while(j<i){
		totalVente+=tabVoiture[j]->getPrix();//fait la somme des ventes
		if(tabVoiture[j]->getSorte()==1 && tabVoiture[j]->getPrix()>20000){
			nombreVoitureAmericaine20000++;//fait la somme des voitures américaines de plus de 20000$
		}
		if(tabVoiture[j]->getAnnee()>=2003){//calcule le nombre de voiture récente
			nombreVoiture2003++;
		}
		if(tabVoiture[j]->getSorte()==2){//calcule le nombre de voiture japonaise
			nombreVoitureJaponaise++;
			sommePrixJaponaise+=tabVoiture[j]->getPrix();//calcule la somme du prix des japonaise
		}
		if(tabVoiture[j]->getSorte()==1){//trouve le meilleur prix américain
			if(tabVoiture[j]->getPrix()<prixMeilleur){
				prixMeilleur=tabVoiture[j]->getPrix();
				numSerieMeilleur=tabVoiture[j]->getNumeroSerie();
			}
		}
		j++;
	}
	prixMoyenJaponaise=sommePrixJaponaise/nombreVoitureJaponaise;//calcule le prix moyen
	
	//formatage de sortie
	i=0;
	cout<<setw(20)<<" "<<"LISTE DES VOITURES VENDUES\n"<<endl;
	cout<<left<<setw(28)<<"NO SERIE"<<setw(20)<<"SORTE"<<setw(14)<<"ANNEE"<<"PRIX"<<endl;
	while(i<10){
		string s;
		if (tabVoiture[i]->getSorte()==1){
			s="americaine";
		}
		if (tabVoiture[i]->getSorte()==2){
			s="japonaise";
		}
		if (tabVoiture[i]->getSorte()==3){
			s="autre";
		}
		cout<<setiosflags(ios::fixed);
		cout<<setfill('*')<<setw(8)<<tabVoiture[i]->getNumeroSerie()<<setfill(' ')
		<<setw(20)<<" "<<left<<setw(20)<<s<<setfill('*')<<setw(4)<<tabVoiture[i]->getAnnee()
		<<setfill(' ')<<setw(10)<<" "<<setfill('*')<<setw(5)<<setprecision(2)<<tabVoiture[i]->getPrix()<<"$"<<endl;
		i++;
	}
	cout<<"\nTOTAL : "<<nombreVoiture<<" voitures pour un montant de "<<setprecision(2)<<totalVente<<"$\n"<<endl;
	cout<<"Nombre de voitures americaines de 20000$ ou plus : "<<nombreVoitureAmericaine20000<<endl;
	cout<<"Nombre de voitures recentes (2003 et plus) : "<<nombreVoiture2003<<"\n"<<endl;
	cout<<"Prix moyen d'une voiture japonaise : "<<setprecision(2)<<prixMoyenJaponaise<<"$\n"<<endl;
	cout<<setw(8)<<numSerieMeilleur<<" est la voiture americaine la moins chere ("<<setprecision(2)<<prixMeilleur<<"$)"<<endl;
	
	return 0;
}
/*Exemple d'exécution du code:
                    LISTE DES VOITURES VENDUES

NO SERIE                    SORTE               ANNEE         PRIX
12345678                    americaine          1993          14500.00$
12345679                    americaine          1994          18000.00$
23456789                    japonaise           1996          22899.99$
34567890                    autre               1985          4700.00$
45678901                    americaine          2007          23115.99$
56789012                    americaine          2010          56789.95$
67890123                    japonaise           2014          21500.50$
78901234                    autre               1998          700.00$
89012345                    japonaise           2005          6700.00$
90123456                    autre               2001          36789.80$

TOTAL : 10 voitures pour un montant de 205696.23$

Nombre de voitures americaines de 20000$ ou plus : 2
Nombre de voitures recentes (2003 et plus) : 4

Prix moyen d'une voiture japonaise : 17033.50$

12345678 est la voiture americaine la moins chere (14500.00$)

--------------------------------
Process exited after 0.1398 seconds with return value 0
Press any key to continue . . .*/
