# Instal·lació pel subsistema Ubuntu de Windows10

Per facilitar-vos la feina transcribint la comandes, el que es pot fer és copiar-la i a la hora d'enganxar-la a la terminal simplement s'ha de fer click dret del ratolí.

### Instal·lar Python3.8

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
sudo apt update
```

```
sudo apt install software-properties-common
```

```
sudo add-apt-repository ppa:deadsnakes/ppa
```

```
sudo apt update
```

```
sudo apt install python3.8
```

Per comprovar que està instal·lat correctament podem executar el següent:

```
python3 ––version
```

Potser aquesta comanda no funciona, així que alternativament es pot intentar:

```
python3 –V
```

I hauria d'apareixer un missatge amb una versió de Python 3.8.

[Source](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)

### Instal·lar pip3

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
sudo apt update
```

```
sudo apt install python3-pip
```

Per comprovar que està instal·lat correctament podem executar el següent:

```
pip3 --version
```

I hauria d'apareixer un missatge amb una versió de pip3.

[Source](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)

### Instal·lar el packet de tkinter

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
sudo apt update
```

```
sudo apt install python3-tk
```

[Source](https://askubuntu.com/questions/815874/importerror-no-named-tkinter-please-install-the-python3-tk-package)

### Instal·lar el Xming X server for Windows

Anar a [aquesta web](https://sourceforge.net/projects/xming/) i descarregar l'instal·lador. Després d'executar-lo cal passar totes les pantalles sense canviar la configuració per defecte fins que ja estigui instal·lat. De moment, no cal obrir-lo.

A continuació, anar al fitxer .bashrc el qual si pot trobar fent 

- tecla windows+r i escrivint %LOCALAPPDATA%
- Packages > CanonicalGroupLimited... > LocalState > rootfs > home > _usuari que tinguis_

Aleshores, obrir-lo amb el `Bloc de Notas` i a l'última línia cal que escriure exactament el següent:

```
export DISPLAY=:0;
```

[Source](https://stackoverflow.com/questions/48254530/tkinter-in-ubuntu-inside-windows-10-error-no-display-name-and-no-display-env)

### Instal·lar la llibreria turtle

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
sudo apt update
```

```
sudo apt-get install -y python3-wxgtk4.0
```

```
python3 -m pip install --user PythonTurtle
```

[Source](https://pypi.org/project/PythonTurtle/)

### Comprovació que tot funciona

Per comprovar que funciona, cal tancar i tornar a obrir la terminal. Després cal buscar l'aplicació Xming i fent doble click la obrirem (no s'obre cap pestanya ni res, però sí que s'obre). Aleshores ja podem anar a la termina i escriure:

```
python3
```

D'aquesta manera se'ns obrirà l'interpret de Python, el qual distingirem perquè on es comença a escriure té els tres caràcters `>>>`. Aleshores aquí mateix, escriurem i executarem el següent:

```
import turtle
```

i després:

```
t = turtle.Turtle()
```

Aleshores, si se'ns obre una nova finestra en blanc amb un punter negre al mig és que tot ha funcionat correctament.