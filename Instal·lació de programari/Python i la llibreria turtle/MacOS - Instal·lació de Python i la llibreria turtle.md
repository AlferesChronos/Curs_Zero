# Instal·lació per MacOS

### Abans de res:

Cal escriure a la terminal la següent línia (prement enter al final).

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Instal·lar Python3.8

Cal escriure a la terminal la següent línia (prement enter al final).

```
brew install python3.8
```

Si no funciona, proveu:

```
brew install python@3.8
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

### Instal·lar pip3

Cal escriure a la terminal cada una de les següent línies (prement enter al final de cada una).

```
curl https://bootstrap.pypa.io/get-pip.py > get_pip.py
python3 get_pip.py
```

Per comprovar que està instal·lat correctament podem executar el següent:

```
pip3 --version
```

I hauria d'apareixer un missatge amb una versió de pip3.

### Instal·lar la llibreria turtle

L'instal·lador es troba a aquesta web: http://pythonturtle.org/

### Comprovació que tot funciona

Ara cal escriure a la terminal la següent línia i prémer enter.

```
python3 -c "import turtle; t = turtle.Turtle(); turtle.done()"
```

Aleshores, si se'ns obre una nova finestra en blanc amb un punter negre al mig és que tot ha funcionat correctament.
