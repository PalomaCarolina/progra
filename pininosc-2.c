▪ #include <stdio.h>
▪ int main( ) {
▪ int x, y, residuo, cociente;
▪ char r;
▪ printf(“este programa devuelve el cociente de una división\n”);
▪ do {
▪ do {
▪ printf (“Proporcione el valor de X y Y en el rango 1-100\n”);
▪ scanf(“%d %d”, &x, &y);
▪ while(getchar( )!=‘\n’);
▪ if (x<1 || y<1 || x>100 || y>100)
▪ printf (“dato inv\240lido\n”);
▪ } while (x<1 || y<1 || x>100 || y>100);
▪ residuo =x;
▪ cociente=0;
▪ if (x>y){
▪ while (residuo>=y) {
▪ residuo=residuo-y;
▪ cociente=cociente+1;
▪ }
▪ }
▪ printf (“el cociente es: %d\n“, cociente);
▪ do {
▪ printf (“Teclee S para continuar o N para salir: ”);
▪ scanf(“%c”, &r);
▪ while(getchar( )!=‘\n’);
▪ if (r!=’S’ && r != ‘s’ && r!=’N’ && r != ‘n’) {
▪ printf (“dato inv\240lido\n”);
▪ }
▪ } while (r!=’S’ && r != ‘s’ && r!=’N’ && r != ‘n’);
▪ } while (r==‘S’ || r==‘s’);
▪ return 0;
▪ }