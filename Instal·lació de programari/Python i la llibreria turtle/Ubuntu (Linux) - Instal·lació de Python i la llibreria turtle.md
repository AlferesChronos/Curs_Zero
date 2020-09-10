# Instal·lació per Ubuntu

Per facilitar-vos la feina transcribint la comandes, el que es pot fer és copiar-la i a la hora d'enganxar-la a la terminal simplement s'ha de fer click dret del ratolí.

### Instal·lar Python3.8

Normalment Python ja ve instal·lat pel propi sistema operatiu ubuntu, així que només cal fer a la comanda de comprovació. Si saltés algun error, caldria fer el següent:

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
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

Ara cal escriure a la terminal la següent línia i prémer enter.

```
python3 -c "import turtle; t = turtle.Turtle(); turtle.done()"
```

Aleshores, si se'ns obre una nova finestra en blanc amb un punter negre al mig és que tot ha funcionat correctament.

