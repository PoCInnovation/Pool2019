---
layout: page
title: Une journée de rétro-ingénierie
permalink: reverse-00-teacher
---

Si on est sur un public qui a déjà fait un de reverse ou qui, du moins,
connaît les enjeux du bas niveau et n'a pas peur d'un listing assembleur,
on peut se passer d'une intro et aller tout de suite à la démo.

Autrement, il est super important de rassurer le public afin d'éviter tout
"blocage". Beaucoup de débutants restent perplexes devant l'assembleur et ne
savent pas quoi faire. Il faut alors forcer l'étudiant à traduire ligne par
ligne le code vers du C. On peut alors lui montrer qu'une fois qu'on a
identifié tel ou tel pattern et fait le lien avec du C, il est très facile de
le repérer à nouveau et l'exercice devient de plus en plus facile.

Il faut aussi insister sur le fait que l'assembleur peut s'apprendre sur le tas
mais qu'il est important de poser des questions aux assistants ou faire des
recherches Google. Pour ceux qui veulent en savoir plus, j'aime bien
[Le langage assembleur](https://www.editions-eni.fr/livre/le-langage-assembleur-maitrisez-le-code-des-processeurs-de-la-famille-x86-9782746065086)
de Olivier CAUET. Attention, peut être un peu cher pour ce que c'est mais c'est
cool de l'avoir dans la collection.

Parmi les exercices, il y a des binaires compilés avec `clang` pour le 32
bits. Il faut donc prévenir les étudiants qu'ils doivent installer les
librairies partagées 32 bits. Les noms des paquets varient selon les
distributions. Pour Fedora, ça devrait suffire :

```
sudo dnf install glibc.i686
```

Les lignes de compilation sont données en commentaire dans le code source
des exercices.

**Attention : Au niveau de la correction, certains exercices peuvent être
résolus facilement avec `ltrace`. Les étudiants doivent tout de même répondre à
toutes les questions. On peut considérer que si, dans leurs explications, il
n'y a pas au moins autant d'informations que dans cette correction, ce n'est
pas bon.**


## Exercice 00

On installe GDB, peu importe la distribution Linux il devrait être dans les
dépots. Pour Peda, on suit simplement le [GitHub](https://github.com/longld/peda).

Une fois GDB installé, on part sur une petite démonstration. On peut faire
la démo sur l'exercice 01. Il faut leur montrer :

* comment lancer GDB avec un binaire
* comment désassembler
* syntaxe AT&T vs. syntaxe Intel (on fait tout en Intel mais c'est au cas où
ils voient de l'autre sur un tutoriel)
* comment lire un listing (offsets, format d'une ligne d'ASM)
* rapide présentation de la mémoire, comment lire à une adresse
* comment exécuter le programme
* placer un point d'arrêt
* affichage de PEDA lorsqu'on avance en step (sans trop rentrer dans les
détails pour le moment)


## Exercice 01

[Sources du binaire ici...](assets/reverse-00/ex01/bin01.c)

Ce binaire est un programme affichant "Hello, World !". Mais le programme
exécute aussi du code inutile avant le binaire. Il faut pousser les étudiants
à vraiment regarder le listing. C'est sur cet exercice qu'il faut être le plus
présent, donner des indices et aider. Il ne faut pas les dégoûter mais au
contraire attiser la curiosité.

Pas de difficulté particulière autrement. Dès que quelques étudiants ont
terminé, on corrige ensemble. Comme ça, on remet une couche sur GDB et on en
profite pour présenter les notions suivantes :

* registres
* la stack
* prologue/épilogue de fonction
* instructions `call`/`ret`

Si besoin de révision, [bon article avec des schémas et tout](https://beta.hackndo.com/fonctionnement-de-la-pile/).


## Exercice 02

[Sources du binaire ici...](assets/reverse-00/ex02/bin02.c)

Le flag peut être trouvé avec `ltrace` :

```
ltrace ./bin02 aled

__libc_start_main(0x80484b0, 2, 0xffb48f84, 0x8048570 <unfinished ...>
strcmp("aled", "quoi_de_neuf_docteur")                                                               = -1
printf("Non, c'est pas bon...\n"Non, c'est pas bon...
)                                                                    = 22
+++ exited (status 1) +++
```

Ou bien avec `strings` :

```
strings bin02

[...]
I want a password as argument.
quoi_de_neuf_docteur
C'est bingo !
Non, c'est pas bon...
[...]
```

Peu importe comment l'étudiant trouve, on lui montre l'autre méthode.


## Exercice 03

[Sources du binaire ici...](assets/reverse-00/ex03/bin03.c)

Prologue :

```
0x080484f0 <+0>:	push   ebp
0x080484f1 <+1>:	mov    ebp,esp
0x080484f3 <+3>:	push   ebx
0x080484f4 <+4>:	sub    esp,0x34
```

On a donc `0x34`, soit 52 octets réservés. 

La boucle :

```
0x08048582 <+146>:	call   0x80483d0 <strlen@plt>
0x08048587 <+151>:	mov    DWORD PTR [ebp-0x18],eax   # loc18 = strlen(flag)
0x0804858a <+154>:	mov    DWORD PTR [ebp-0x1c],0x0   # loc1c = 0, notre compteur
0x08048591 <+161>:	mov    eax,DWORD PTR [ebp-0x1c]
0x08048594 <+164>:	cmp    eax,DWORD PTR [ebp-0x18]   # if (loc1c >= loc18)
0x08048597 <+167>:	jae    0x80485dc <main+236>       # fin de la boucle
0x0804859d <+173>:	mov    eax,DWORD PTR [ebp-0x1c]
0x080485a0 <+176>:	mov    ecx,DWORD PTR [ebp-0x14]   # loc14 est le pointeur vers flag
0x080485a3 <+179>:	movsx  eax,BYTE PTR [ecx+eax*1]   # eax = flag[loc1c]
0x080485a7 <+183>:	cmp    eax,0x5f                   # if (flag[loc1c] != '_')
0x080485ac <+188>:	jne    0x80485b7 <main+199>       # on continue
0x080485b2 <+194>:	jmp    0x80485cc <main+220>       # sinon on saute le bloc
0x080485b7 <+199>:	mov    eax,DWORD PTR [ebp-0x1c]
0x080485ba <+202>:	mov    ecx,DWORD PTR [ebp-0x14]
0x080485bd <+205>:	movsx  edx,BYTE PTR [ecx+eax*1]   # edx = flag[loc1c]
0x080485c1 <+209>:	sub    edx,0x20                   # flag[loc1c] -= 20
0x080485c7 <+215>:	mov    bl,dl                      # on passe en majuscule
0x080485c9 <+217>:	mov    BYTE PTR [ecx+eax*1],bl
0x080485cc <+220>:	mov    eax,DWORD PTR [ebp-0x1c]
0x080485cf <+223>:	add    eax,0x1                    # loc1c++
0x080485d4 <+228>:	mov    DWORD PTR [ebp-0x1c],eax
0x080485d7 <+231>:	jmp    0x8048591 <main+161>       # et on boucle
```

Nous avons donc les variables locales suivantes :

* `loc18`, longueur de la chaîne
* `loc1c`, notre compteur
* `loc14`, pointeur vers le flag, chaîne en train d'être parcourue

L'adresse du flag est :

```
Breakpoint 1, 0x080485a0 in main ()
gdb-peda$ x/x $ebp-0x14
0xffffd714:	0x0804a008
gdb-peda$ x/s 0x0804a008
0x804a008:	"avec_effet_de_serre"
```

On a `EBP-0x14` qui vaut `0xffffd714`. A cette adresse se trouve le pointeur
vers notre flag (avant parcours ici) : `0x0804a008`.

Ce pointeur est par exemple déréférencé en `main+179` :

```
0x80485a3 <main+179>:	movsx  eax,BYTE PTR [ecx+eax*1]
```

On ajoute EAX (`loc1c`) à ECX (`loc14`, ou encore `EBP-0x14`) puis on
déréférence pour récupérer le caractère dans `EAX`.

Le mot de passe est `AVEC_EFFET_DE_SERRE`.


## Exercice 04

[Sources du binaire ici...](assets/reverse-00/ex04/bin04.c)

+132 à +137 :

```
0x08048554 <+132>:	mov    eax,DWORD PTR [ebp-0xc]
0x08048557 <+135>:	mov    eax,DWORD PTR [eax]
0x08048559 <+137>:	mov    DWORD PTR [ebp-0x10],eax
0x0804855c <+140>:	mov    eax,DWORD PTR [eax]
0x0804855e <+142>:	mov    DWORD PTR [ebp-0x14],eax
```

On a `EBP-0xC` qui est déréférencé. Cela correspond à récupérer `argv[1]`, le
pointeur ayant déjà été incrémenté en +70 :

```
0x08048513 <+67>:	mov    eax,DWORD PTR [ebp-0xc]
0x08048516 <+70>:	add    eax,0x4
0x0804851b <+75>:	mov    DWORD PTR [ebp-0xc],eax
```

Attention, si on sent que l'étudiant est perdu parce qu'il n'a pas vu le
`++argv`, on peut lui dire. C'est quand même pas mal frustrant... :p

Le pointeur est sauvegardé pour un usage futur. On va ensuite le déréférencer
encore une fois sur 4 octets. Cela revient à un `*((uint32_t *)(pointeur))`.
Ces 4 octets sont finalement stockés dans une variable locale.

+152 à +158 :

```
0x08048568 <+152>:	mov    eax,DWORD PTR [ebp-0x10]
0x0804856b <+155>:	mov    eax,DWORD PTR [eax+0x4]
0x0804856e <+158>:	mov    DWORD PTR [ebp-0x1c],eax
```

On a `EBP-0x10` qui est récupéré : c'est le pointeur que nous venons de stocker,
soit `argv[1]`. Ce pointeur est incrémenté de 4 puis déréférencé à nouveau
sur 4 octets. C'est notre équivalent de `*((uint32_t *)(pointeur) + 1)`. On
récupère ainsi les 4 octets suivants. On peut donc voir `argv[1]` non pas
comme une chaîne de caractères mais comme un `uint64_t` que nous traitons
en deux `uint32_t`.

La fonction `soap` prend deux valeurs non signées sur 4 octets en paramètre.
Ces deux valeurs sont parcourues octets par octets. Les octets sont XORés deux
à deux. Le résultat de ce XOR est retourné. La destination du résultat n'est
pas importante si l'étudiant ne l'évoque pas.

On a beaucoup des déréférenciations, le `xor`, une boucle, rien de particulier.

```
0x08048460 <+0>:	push   ebp
0x08048461 <+1>:	mov    ebp,esp
0x08048463 <+3>:	push   ebx
0x08048464 <+4>:	push   esi
0x08048465 <+5>:	sub    esp,0x14                 # 14 octets de local
0x08048468 <+8>:	mov    eax,DWORD PTR [ebp+0xc]  # argument1
0x0804846b <+11>:	mov    ecx,DWORD PTR [ebp+0x8]  # argument2
0x0804846e <+14>:	lea    edx,[ebp-0x10]           # pointeur vers argument2
0x08048471 <+17>:	lea    esi,[ebp-0xc]            # pointeur vers argument1
0x08048474 <+20>:	mov    DWORD PTR [ebp-0xc],ecx  # copie de l'argument 2
0x08048477 <+23>:	mov    DWORD PTR [ebp-0x10],eax # copie de l'argument 1
0x0804847a <+26>:	mov    DWORD PTR [ebp-0x14],esi # pointeur vers argument 1
0x0804847d <+29>:	mov    DWORD PTR [ebp-0x18],edx # pointeur vers argument 2
0x08048480 <+32>:	mov    DWORD PTR [ebp-0x1c],0x0 # compteur
0x08048487 <+39>:	cmp    DWORD PTR [ebp-0x1c],0x4 # si >= 4
0x0804848e <+46>:	jae    0x80484c1 <soap+97>      # fin de la boucle
0x08048494 <+52>:	mov    eax,DWORD PTR [ebp-0x18] # argument 2
0x08048497 <+55>:	mov    ecx,DWORD PTR [ebp-0x1c] # compteur
0x0804849a <+58>:	movzx  eax,BYTE PTR [eax+ecx*1] # argument2[compteur]
0x0804849e <+62>:	mov    ecx,DWORD PTR [ebp-0x14] # argument 1
0x080484a1 <+65>:	mov    edx,DWORD PTR [ebp-0x1c] # compteur
0x080484a4 <+68>:	movzx  esi,BYTE PTR [ecx+edx*1] # argument1[compteur]
0x080484a8 <+72>:	xor    esi,eax                  # le xor entre les deux caractères
0x080484aa <+74>:	mov    eax,esi                  # résultat
0x080484ac <+76>:	mov    bl,al                    # partie basse
0x080484ae <+78>:	mov    BYTE PTR [ecx+edx*1],bl  # argument1[compteur] = résultat
0x080484b1 <+81>:	mov    eax,DWORD PTR [ebp-0x1c] # compteur
0x080484b4 <+84>:	add    eax,0x1                  # ++compteur
0x080484b9 <+89>:	mov    DWORD PTR [ebp-0x1c],eax
0x080484bc <+92>:	jmp    0x8048487 <soap+39>      # et on boucle
0x080484c1 <+97>:	mov    eax,DWORD PTR [ebp-0xc]  # résultat en valeur de retour
0x080484c4 <+100>:	add    esp,0x14
0x080484c7 <+103>:	pop    esi
0x080484c8 <+104>:	pop    ebx
0x080484c9 <+105>:	pop    ebp
0x080484ca <+106>:	ret
```

Les arguments sont poussés sur la stack avant l'instruction `call` :

```
0x080485a2 <+210>:	mov    DWORD PTR [esp],eax
0x080485a5 <+213>:	mov    DWORD PTR [esp+0x4],ecx
0x080485a9 <+217>:	call   0x8048460 <soap>
```

La valeur de retour se trouve dans EAX après l'appel :

```
0x080485a9 <+217>:	call   0x8048460 <soap>
0x080485ae <+222>:	mov    ecx,DWORD PTR [ebp-0x2c]
0x080485b1 <+225>:	mov    DWORD PTR [ecx+0x4],eax
```

Le pointeur finit sauvegardé dans l'espace local.

Le préfixe `ds` signifie *data segment*. Ce pointeur fait référence à une
variable globale initialisée. On peut en profiter pour parler un peu
[des segments](https://en.wikipedia.org/wiki/Data_segment).

Le XOR est une opération symétrique. Il suffit donc de B X C pour retrouver A.

Pour le mot de passe, on se récupère les octets de la variable globale :

```
gdb-peda$ x/s 0x80498f8
0x80498f8 <belier>:	"\026\207\004\b"
gdb-peda$ x/s * 0x80498f8
0x8048716:	"1337W00T"
```

Puis les octets en dur dans le binaire qui sont passés à `soap` :

```
0x08048561 <+145>:	mov    DWORD PTR [ebp-0x18],0x76667c7d
[...]
0x08048571 <+161>:	mov    DWORD PTR [ebp-0x20],0x670c7519
```

On en fait un `uint64_t` : `0x670c751976667c7d`. Attention à l'ordre des deux
`uint32_t` dans le `uint64_t`. Il n'y a pas de problème de boutisme mais le
"deuxième" doit être mis en premier. Ce qui nous fait 8 octets des deux
côtés, on peut XORer :

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  uint64_t ok = 0x670c751976667c7d;
  const char *oklm = "1337W00T";

  uint8_t *zer = (uint8_t *)&ok;
  char r[9] = {0};

  for (size_t i = 0; i < 8; ++i)
    r[i] = zer[i] ^ oklm[i];

  printf("Flag: %s !\n", r);
  return EXIT_SUCCESS;
}

// clang solve.c -o solve
// ./solve
// Flag: LOUANE<3 !
```

Le mot de passe demandé est donc `LOUANE<3`.

## Exercice 05

[Sources du binaire ici...](assets/reverse-00/ex05/bin05.c)

On est sur un binaire strippé... On va se retrouver l'adresse de la fonction
`main` en regardant quel argument est passé à la routine
`__libc_start_main@plt`.

On récupère le point d'entrée du programme :

```
gdb-peda$ info file
Symbols from "/challenges/ex05/bin05".
Local exec file:
	`/challenges/ex05/bin05', file type elf32-i386.
	Entry point: 0x8048360
	0x08048134 - 0x08048147 is .interp
	0x08048148 - 0x08048168 is .note.ABI-tag
        [...]
```

Il faut bien expliquer aux étudiants la différence entre point d'entrée et
fonction `main`. On peut explorer les instructions à partir de là :

```
gdb-peda$ x/50i 0x8048360
   [...]
   0x8048375:	push   ecx
   0x8048376:	push   esi
   0x8048377:	push   0x804845b
   0x804837c:	call   0x8048350 <__libc_start_main@plt>
   0x8048381:	hlt
   0x8048382:	xchg   ax,ax
   [...]
```

On a donc `0x804845b`. C'est l'adresse de notre fonction `main` :

```
gdb-peda$ x/20i 0x804845b
   0x804845b:	lea    ecx,[esp+0x4]
   0x804845f:	and    esp,0xfffffff0
   0x8048462:	push   DWORD PTR [ecx-0x4]
   0x8048465:	push   ebp
   0x8048466:	mov    ebp,esp
   0x8048468:	push   ebx
   0x8048469:	push   ecx
   0x804846a:	mov    ebx,ecx
   0x804846c:	cmp    DWORD PTR [ebx],0x1
```

On retombe sur un prologue de fonction, on voit un check sur le nombre
d'aguments... On est au bon endroit !

Un peu plus bas dans le listing du `main` :

```
0x80484aa:	mov    edx,DWORD PTR ds:0x804982c
0x80484b0:	add    edx,0x25
0x80484b3:	sub    esp,0x8
0x80484b6:	push   eax
0x80484b7:	push   edx
0x80484b8:	call   0x8048310 <strcmp@plt>
0x80484bd:	add    esp,0x10
```

On a un `strcmp` entre EAX (entrée utilisateur) et un autre pointeur
(`ds:0x804982c + 0x25`). On va voir ce qui se passe :

```
gdb-peda$ x/s * 0x804982c
0x8048590:	"c'est pas le quartier qui me quitte, c'est moi j'quitte le quartier"
gdb-peda$ x/s 0x8048590
0x8048590:	"c'est pas le quartier qui me quitte, c'est moi j'quitte le quartier"
gdb-peda$ x/s (0x8048590 + 0x25)
0x80485b5:	"c'est moi j'quitte le quartier"
gdb-peda$
```

Le mot de passe demandé est donc `c'est moi j'quitte le quartier` !


## Exercice 06

[Sources du binaire ici...](assets/reverse-00/ex06/bin06.c)

On est sur du bytecode Python :

```
file bin06

bin06: python 2.7 byte-compiled
```

On décompile le code avec `uncompyle` :

```python
uncompyle6 bin06.pyc

# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.4.2 (default, Sep 25 2018, 22:02:39)
# [GCC 4.9.2]
# Embedded file name: ./bin06.py
# Compiled at: 2019-01-02 16:26:15
import sys
FLAG = 8405166

def main(argc, argv):
    if argc < 2:
        sys.stderr.write('Il me faut un argument...\n')
        return -1
    userInput = argv[1]
    if str(FLAG) == userInput:
        sys.stdout.write('Bravo !\n')
        return 0
    sys.stdout.write("Ce n'est pas bon...\n")
    return 1


if __name__ == '__main__':
    ret = main(len(sys.argv), sys.argv)
    sys.exit(ret)
# okay decompiling bin06.pyc
```

On a pas mal d'autres modules qui peuvent fonctionner : `unpyclib`,
`decompyle`... C'est l'étudiant qui choisit mais il faut décourager
l'utilisation de GDB et le pousser à trouver ce qui répond à son problème.

Le mot de passe est donc `8405166`.


## Exercice 07

On est sur un binaire écrit en Go :

```
strings bin07 | grep "runtime.go"

*runtime.gobuf
runtime.gogetenv
runtime.gomcache
runtime.gosweepdone
runtime.gosweepone
[...]
```

GDB est plus ou moins capable de travailler avec ce genre de binaire...
Commençons par regarder les fonctions du module `main` :

```
gdb-peda$ set loggin on
Copying output to gdb.txt.
gdb-peda$ info functions
[...]
```

Le logging est utile quand la sortie de GDB est aussi fat...

```
cat gdb.txt | grep main
File /home/oursin/go/src/re/main.go:
void main.main(void);
void main.test(struct string, struct string);
void runtime.main(void);
void runtime.main.func1(void);
void runtime.main.func2(bool *);
void main.init(void);
```

La fonction `test` semble intéressante, on peut poser un point d'arrêt
dessus :

```
gdb-peda$ b main.test
Breakpoint 1 at 0x4883f0: file /home/oursin/go/src/re/main.go, line 10.
gdb-peda$ r
Starting program: /challenges/ex07/bin07
AAAAAAAAAAAAAAAAAAAA
[----------------------------------registers-----------------------------------]
RAX: 0x4bd326 ("RmFpdGVzRHVHb0JhbmRlRGVCYXRhcmRzSIGFPE: floating-point exceptionSIGTTOU: background write to ttybufio: invalid use of UnreadBytebufio: invalid use of UnreadRunebufio: tried to fill full bufferend outs"...)
RBX: 0x1c
RCX: 0x1c
RDX: 0x1c
RSI: 0xc00008c000 ("QUFBQUFBQUFBQUFBQUFBQUFBQUE=")
RDI: 0xc000080cb8 ("QUFBQUFBQUFBQUFBQUFBQUFBQUE=")
RBP: 0xc000080f88 --> 0xc000080f90 --> 0x428887 (<runtime.main+519>:	mov    eax,DWORD PTR [rip+0x1467bf]        # 0x56f04c <runtime.runningPanicDefers>)
RSP: 0xc000080c48 --> 0x488b79 (<main.main+1561>:	mov    rbp,QWORD PTR [rsp+0x338])
RIP: 0x4883f0 (<main.test>:	mov    rcx,QWORD PTR fs:0xfffffffffffffff8)
R8 : 0x4
R9 : 0x0
R10: 0x34 ('4')
R11: 0x1
R12: 0x40 ('@')
R13: 0x40 ('@')
R14: 0x4
R15: 0x100
EFLAGS: 0x206 (carry PARITY adjust zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x4883ed:	int3
   0x4883ee:	int3
   0x4883ef:	int3
=> 0x4883f0 <main.test>:	mov    rcx,QWORD PTR fs:0xfffffffffffffff8
   0x4883f9 <main.test+9>:	lea    rax,[rsp-0x18]
   0x4883fe <main.test+14>:	cmp    rax,QWORD PTR [rcx+0x10]
   0x488402 <main.test+18>:	jbe    0x488553 <main.test+355>
   0x488408 <main.test+24>:	sub    rsp,0x98
[------------------------------------stack-------------------------------------]
0000| 0xc000080c48 --> 0x488b79 (<main.main+1561>:	mov    rbp,QWORD PTR [rsp+0x338])
0008| 0xc000080c50 --> 0xc000080cb8 ("QUFBQUFBQUFBQUFBQUFBQUFBQUE=")
0016| 0xc000080c58 --> 0x1c
0024| 0xc000080c60 --> 0x4bd326 ("RmFpdGVzRHVHb0JhbmRlRGVCYXRhcmRzSIGFPE: floating-point exceptionSIGTTOU: background write to ttybufio: invalid use of UnreadBytebufio: invalid use of UnreadRunebufio: tried to fill full bufferend outs"...)
0032| 0xc000080c68 --> 0x20 (' ')
0040| 0xc000080c70 --> 0xc000080cb8 ("QUFBQUFBQUFBQUFBQUFBQUFBQUE=")
0048| 0xc000080c78 --> 0x1c
0056| 0xc000080c80 --> 0x0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, main.test (flag=..., input=...) at /home/oursin/go/src/re/main.go:10
10	/home/oursin/go/src/re/main.go: No such file or directory.
```

Il en faut pas plus... On repère la chaîne `RmFpdGVzRHVHb0JhbmRlRGVCYXRhcmRz`
sur la pile. Et on récupère le flag :

```
echo -n "RmFpdGVzRHVHb0JhbmRlRGVCYXRhcmRz" | base64 --decode
FaitesDuGoBandeDeBatards
```


## Exercice 08

Le binaire de cet exercice utilise plusieurs protections anti-debug :

* recherche des variables d'environnement `LINES` et `COLUMNS`
* détection d'un débogueur avec `ptrace`
* sighandler sur `SIGSEGV` permettant d'exécuter du code qui, en apparence,
devrait terminer le programme : le comportement est différent dans GDB et
hors GDB
* morceau de code chiffré (XOR), déchiffré à l'exécution
* binaire strippé

De part la construction du binaire, on ne va pas aller chercher
`__libc_start_main@plt` nous même pour repérer la fonction `main` comme on l'a
fait précédemment. On va plutôt utiliser la technique du `backtrace` qui est
plus "automatique". On commence par `ltrace` le binaire pour espérer retrouver
une fonction connue :

```
ltrace ./siglol
getenv("COLUMNS")                                                                                      = nil
signal(SIGSEGV, 0x55cab5675199)                                                                        = 0
getenv("LINES")                                                                                        = nil
[...]
ptrace(0, 0, 1, 0)                                                                                     = -1
puts("ARRETEZ DE ME SUIVRE"ARRETEZ DE ME SUIVRE
)                                                                           = 21
```

Mis à part le code XORé, toutes les protections sont alors exposées. Le
premier appel à `getenv` se situe avant toute autre protection anti-debug
donc pas de pression :

```
gdb-peda$ b * getenv
Breakpoint 1 at 0x1030
gdb-peda$ r
[...]
Breakpoint 1, __GI_getenv (name=0x555555556084 "COLUMNS") at getenv.c:35
35	getenv.c: No such file or directory.
gdb-peda$ bt
#0  __GI_getenv (name=0x555555556084 "COLUMNS") at getenv.c:35
#1  0x0000555555555419 in ?? ()
#2  0x00007ffff7a52b45 in __libc_start_main (main=0x5555555553fd, argc=0x1, argv=0x7fffffffe6f8, init=<optimized out>, fini=<optimized out>,
    rtld_fini=<optimized out>, stack_end=0x7fffffffe6e8) at libc-start.c:287
#3  0x00005555555550ce in ?? ()
```

La trace nous révèle l'appel à `__libc_start_main`. Son premier paramètre est
l'adresse de `main` : `0x5555555553fd`. On peut poser un point d'arrêt
dessus et désamorcer toutes les protections que l'on connaît alors :

```
gdb-peda$ b * 0x5555555553fd
Breakpoint 2 at 0x5555555553fd
gdb-peda$ unset env LINES               # bypass getenv()
gdb-peda$ unset env COLUMNS             # bypass getenv()
gdb-peda$ handle SIGSEGV pass noprint   # bypass SIGSEGV
gdb-peda$ unptrace                      # bypass ptrace()
Breakpoint 3 at 0x555555555070
'ptrace' deactivated
[...]
gdb-peda$ r
[...]
Breakpoint 2, 0x00005555555553fd in ?? ()
gdb-peda$ x/20i $rip
=> 0x5555555553fd:	push   rbp
   0x5555555553fe:	mov    rbp,rsp
   0x555555555401:	sub    rsp,0x10
   0x555555555405:	mov    QWORD PTR [rbp-0x8],0x0
   0x55555555540d:	lea    rdi,[rip+0xc70]        # 0x555555556084
   0x555555555414:	call   0x555555555030 <getenv@plt>
```

A partir de là, on peut commencer à se balader dans le code, regarder les
routines...

La fonction qui nous intéresse est la dernière à être appelée par `main` :

```
0x555555555499:	call   0x5555555552d7
0x55555555549e:	leave
0x55555555549f:	ret
```

On regarde :

```
gdb-peda$ x/70i 0x5555555552d7

[...]
0x555555555346:	mov    eax,DWORD PTR [rbp-0x4]          # the counter
0x555555555349:	lea    rdx,[rip+0x2d90]                 # XORed code
0x555555555350:	movzx  eax,BYTE PTR [rax+rdx*1]         # xored[counter]
0x555555555354:	mov    edx,eax                          # to EDX
0x555555555356:	movzx  eax,BYTE PTR [rip+0x2dfa]        # global variable (shoud be 0 at this point)
0x55555555535d:	xor    eax,edx                          # XOR operation
0x55555555535f:	mov    ecx,eax                          # saved XORed byte
0x555555555361:	mov    eax,DWORD PTR [rbp-0x4]          # get counter back
0x555555555364:	lea    rdx,[rip+0x2d75]                 # where to write result
0x55555555536b:	mov    BYTE PTR [rax+rdx*1],cl          # write result
0x55555555536e:	add    DWORD PTR [rbp-0x4],0x1          # increment counter
0x555555555372:	cmp    DWORD PTR [rbp-0x4],0x74         # should we end ?
0x555555555376:	jbe    0x555555555346                   # loop
[...]
0x555555555381:	mov    eax,DWORD PTR [rbp-0x8]          # another counter
0x555555555384:	lea    rdx,[rip+0x2d55]                 # XORed code
0x55555555538b:	movzx  eax,BYTE PTR [rax+rdx*1]         # xored[counter]
0x55555555538f:	mov    edx,DWORD PTR [rbp-0x8]          # counter
0x555555555392:	sub    edx,0x6e                         # kind of key
0x555555555395:	xor    eax,edx                          # xor operation
0x555555555397:	mov    ecx,eax                          # save result
0x555555555399:	mov    eax,DWORD PTR [rbp-0x8]          # get counter back
0x55555555539c:	lea    rdx,[rip+0x2d3d]                 # XORed code
0x5555555553a3:	mov    BYTE PTR [rax+rdx*1],cl          # write result
0x5555555553a6:	add    DWORD PTR [rbp-0x8],0x1          # increment counter
0x5555555553aa:	cmp    DWORD PTR [rbp-0x8],0x74         # should we end ?
0x5555555553ae:	jbe    0x555555555381                   # loop
[...]
0x5555555553ce:	mov    rdi,rax
0x5555555553d1:	call   rdx                              # call clean code
0x5555555553d3:	test   eax,eax
```

On a deux boucles qui viennent XOR notre bout de code chiffré. La première
peut être ignorée étant donné que la variable globale utilisée comme clé
est en fait la valeur de retour de `getenv()`. Etant donné que nous avons
`unset LINES` et `COLUMNS`, sa valeur devrait être `0`, ce qui ne modifie pas
le code.

La deuxième boucle déchiffre effectivement le code. On peut aller voir
un peu ce qui se passe :

```
gdb-peda$ b * 0x5555555553d1
Breakpoint 4 at 0x5555555553d1
gdb-peda$ c
Continuing.





Rentre une string frer:
ABCDEFGHI

Breakpoint 4, 0x00005555555553d1 in ?? ()
[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffe1e0 ("ABCDEFGHI")
RBX: 0x0
RCX: 0xff
RDX: 0x5555555580e0 --> 0x8d48c03148db3148
RSI: 0x7fffffffe1e0 ("ABCDEFGHI")
RDI: 0x7fffffffe1e0 ("ABCDEFGHI")
RBP: 0x7fffffffe5f0 --> 0x7fffffffe610 --> 0x0
RSP: 0x7fffffffe1e0 ("ABCDEFGHI")
RIP: 0x5555555553d1 (call   rdx)
[...]
[-------------------------------------code-------------------------------------]
   0x5555555553c0:	lea    rdx,[rip+0x2d19]        # 0x5555555580e0
   0x5555555553c7:	lea    rax,[rbp-0x410]
   0x5555555553ce:	mov    rdi,rax
=> 0x5555555553d1:	call   rdx
[...]
```

On remarque que notre entrée est passée en paramètre. On peut imaginer
qu'on se rapproche de la routine de vérification. On s'affiche le
code déchiffré :

```
gdb-peda$ n
0x00005555555580e0 in ?? ()
gdb-peda$ x/50i $rip
0x5555555580e0:	xor    rbx,rbx
0x5555555580e3:	xor    rax,rax
0x5555555580e6:	lea    rax,[rip+0xfffffffffffffff9]
0x5555555580ed:	add    rax,0xe
0x5555555580f1:	jmp    rax
0x5555555580f3:	adc    dh,BYTE PTR [rbx-0x776b7ce]      # who cares up to there
0x5555555580f9:	jmp    0x555555558109                   # start of the loop
0x5555555580fe:	xor    cl,bl                            # XOR operation
0x555555558100:	add    bl,0x3                           # add 0x03 to key
0x555555558103:	mov    BYTE PTR [rax],cl                # write result
0x555555558105:	add    rax,0x1                          # ++userInput (pointer)
0x555555558109:	mov    cl,BYTE PTR [rax]                # *userInput
0x55555555810b:	test   cl,cl                            # should we end ?
0x55555555810d:	jne    0x5555555580fe                   # loop
0x555555558113:	sub    rdx,0x60
0x555555558117:	xor    rbx,rbx
0x55555555811a:	mov    rax,rsi
0x55555555811d:	mov    bl,0x48                          # length of xoredFlag (loop condition)
0x55555555811f:	mov    cl,BYTE PTR [rdx]                # *xoredFlag
0x555555558121:	cmp    BYTE PTR [rax],cl                # if *xored(userInput) != xoredFlag
0x555555558123:	jne    0x555555558140                   # jump to badboy
0x555555558129:	sub    bl,0x1                           # decrement loop condition
0x55555555812c:	add    rax,0x1                          # ++xored(userInput)
0x555555558130:	add    rdx,0x1                          # ++xoredFlag (pointer)
0x555555558134:	test   bl,bl                            # should we end ?
0x555555558136:	jne    0x55555555811f                   # loop
0x55555555813c:	xor    rax,rax                          # goodboy
0x55555555813f:	ret
0x555555558140:	mov    eax,0x1                          # badboy
0x555555558145:	ret
```

On va se mettre au niveau du XOR pour choper la valeur de départ de la clé :

```
gdb-peda$
[...]
RBX: 0x32 ('2')
[...]
[-------------------------------------code-------------------------------------]
   0x5555555580f3:	adc    dh,BYTE PTR [rbx-0x776b7ce]
   0x5555555580f9:	jmp    0x555555558109
   0x5555555580fe:	xor    cl,bl
=> 0x555555558100:	add    bl,0x3
   0x555555558103:	mov    BYTE PTR [rax],cl
   0x555555558105:	add    rax,0x1
   0x555555558109:	mov    cl,BYTE PTR [rax]
   0x55555555810b:	test   cl,cl
[------------------------------------stack-------------------------------------]
[...]
```

La clé commence à `0x32` puis est incrémentée de `0x03` à chaque fois. Il
nous manque plus que les octets XORés :

```
gdb-peda$ b * 0x55555555811d
Breakpoint 5 at 0x55555555811d
gdb-peda$ c
Continuing.
[...]
RDX: 0x555555558080 --> 0x182129455c595954
[...]
   0x555555558113:	sub    rdx,0x60
   0x555555558117:	xor    rbx,rbx
   0x55555555811a:	mov    rax,rsi
=> 0x55555555811d:	mov    bl,0x48
   0x55555555811f:	mov    cl,BYTE PTR [rdx]
   0x555555558121:	cmp    BYTE PTR [rax],cl
   0x555555558123:	jne    0x555555558140
   0x555555558129:	sub    bl,0x1
[...]
gdb-peda$ p/d 0x48
$7 = 72
gdb-peda$ x/72c $rdx
0x555555558080:	0x54	0x59	0x59	0x5c	0x45	0x29	0x21	0x18
0x555555558088:	0x28	0x28	0x3e	0xc	0x35	0x38	0x3	0x3c
0x555555558090:	0x3d	0x0	0x1b	0x1f	0x31	0x4	0x1a	0x28
0x555555558098:	0x18	0x12	0xee	0xdc	0xe1	0xfb	0xe3	0xfc
0x5555555580a0:	0xcd	0xf6	0xf0	0xfa	0xf2	0xcd	0xfb	0xc3
0x5555555580a8:	0xcf	0xf2	0xd2	0xd2	0xc4	0xdb	0xc9	0xe0
0x5555555580b0:	0xa3	0xb3	0xad	0xa8	0x91	0xa4	0xba	0x88
0x5555555580b8:	0xbc	0xb1	0x81	0x84	0xb9	0x88	0xb3	0x9d
0x5555555580c0:	0x93	0x99	0x94	0x94	0x90	0x66	0x61	0x7a
gdb-peda$
```

Et on récupère le flag :

```c
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>


const uint8_t xored[] = {
  0x54, 0x59, 0x59, 0x5c, 0x45, 0x29, 0x21, 0x18,
  0x28, 0x28, 0x3e, 0x0c, 0x35, 0x38, 0x03, 0x3c,
  0x3d, 0x00, 0x1b, 0x1f, 0x31, 0x04, 0x1a, 0x28,
  0x18, 0x12, 0xee, 0xdc, 0xe1, 0xfb, 0xe3, 0xfc,
  0xcd, 0xf6, 0xf0, 0xfa, 0xf2, 0xcd, 0xfb, 0xc3,
  0xcf, 0xf2, 0xd2, 0xd2, 0xc4, 0xdb, 0xc9, 0xe0,
  0xa3, 0xb3, 0xad, 0xa8, 0x91, 0xa4, 0xba, 0x88,
  0xbc, 0xb1, 0x81, 0x84, 0xb9, 0x88, 0xb3, 0x9d,
  0x93, 0x99, 0x94, 0x94, 0x90, 0x66, 0x61, 0x7a
};

int main(void) {
  uint8_t clean[sizeof(xored) + 1] = {0};

  uint8_t key = 0x32;
  for (size_t i = 0; i < sizeof(xored); ++i) {
    clean[i] = xored[i] ^ key;
    key += 0x3;
  }

  printf("Flag is : [%s]\n", clean);

  return EXIT_SUCCESS;
}

// clang solve.c -o solve
// $ ./solve
// Flag is : [flag{he_ben_ca_c_est_un_bon_gros_chall_de_barbu_avec_un_flag_a_rallonge}]
```

C'est tout bon !


## Exercice 09

On insiste pour avoir un retour ! Et on indique aux étudiants que si ils
veulent continuer ils peuvent nous envoyer des questions par mail !
