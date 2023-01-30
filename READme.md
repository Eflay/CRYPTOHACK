Cryptohack Synthèses

### *L'algorithme Euclidien*

Cette algorithme permet de trouver le plus grand diviseur commun (GCD) de deux nombres entiers positifs.

Par exemple :

a = 210 et b = 45

Si l'on divise 210 par 45, ça nous donne 4 avec un reste de 30.

1. 210 = 4 * 45 + 30
2. 45 = 1 * 30 + 15
3. 30 = 2 *15 + 0

Le plus grand diviseur commun des deux nombres est le dernier reste avant zéro. Ici, il est égal à 15

###### <u>Généralisation</u>

En entrée : Deux entiers positifs a et b.

En sortie : le plus grand diviseur commun g de a et b

Si a < b, il faut alors échanger a et b.

Diviser a par b et avoir le reste r. Si r = 0, alors le plus grand diviseur commun est b.

Sinon itérer en remplaçant a par b et b par r.

### *L'identité de Bezout alias l'algorithme Euclidien étendu*

Ce théorème affirme que : **"Si a et b sont des nombres entiers positifs, il y a toujours des entiers m et n de telle sorte que le GCD(a, b) = a * m + b * n"**

A présent, nous devons nous positionner par rapport au reste.

Reprenons l'exemple précédent avec 210 et 45 : 
1. 30 = 210 - 4 * 45
2. 15 = 45 - 1 * 30 
3. 15 = 45 - 1 * (1 * 210 - 4* 45)
4. 15 = -1 * 210 + 5 * 45

Ce qui nous donne 15 = 210 * -1 + 45 * 5 (a * m + b * n).
Comme nous le voyons, il faut remonter l'algorithme Euclidien toujours en gardant le reste final comme égalité.

Voir cahier p1 pour démonstration.

### *La théorie de la congruence*
Cette théorie dit : **"Deux entiers sont congruents modulo m si a = b mod m".**

Pour trouver b, il suffit de faire a mod m = b

voir p2 du cahier.

### *Le petit théorème de Fermat*
Ce théorème dit : "Si p est un nombre premier, alors pour n'importe quelle a, le nombre a^p - a est un multiple de p"

Ce qui veut dire :
- a^p = a mod p

Si p est un nombre premier et que a est un nombre entre 1 et p-1 alors :
- a^p-1 = 1 mod p

Si p est un nombre premier, a n'importe quelle nombre mais que p ne divise pas a, alors :
- a^p-1 = 1 mod p

voir p2 du cahier