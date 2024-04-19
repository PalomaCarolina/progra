#include <stdio.h>
#include <stdlib.h>
#define MAX 100
#define MIN 0

struct preguntas {
    char mascota[11];
    char postre[50];
    char mama[25];
    float edad;
};

int main(){
    struct preguntas contrasenia;
    //struct estudiante grupoPE[MAX/2];
    //int n, i;

    printf ("\nIngresa nombre de tu mascota:");
    scanf ("%s", contrasenia.mascota);
    while(getchar()!='\n');
    printf ("\nIngresa tu postre favorito: ");
    scanf ("%[^\n]", contrasenia.postre);
    while(getchar()!='\n');
    printf ("\nProporciona el nombre de tu mama: ");
    scanf ("%[^\n]", contrasenia.mama);
    while(getchar()!='\n');
    printf ("\nProporciona tu edad: ");
    scanf ("%f", &contrasenia.edad);
    while(getchar()!='\n');

    printf("\nTu mascota es %s , tu postre favorito es %s, el nombre de tu mama es %s y actualmente tienes una edad de %2.2f\n", contrasenia.mascota, contrasenia.postre, contrasenia.mama, contrasenia.edad);


    return 0;
}
