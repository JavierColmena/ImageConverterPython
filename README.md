
## Authors

- [@JavierColmena](https://www.github.com/javiercolmena)


# Image Converter

Convertidor de imagenes dentro de un directorio.


## Get Started

Install the ``PILLOW`` library from Python

```bash
  pip install pillow
```
```bash
  python ./main.py -h
```
    
## Comandos

### Help

```bash
  python ./main.py -h
```

### Ubicar el directorio con las imagenes. ***

```bash
  -d "./Images/"
```

```bash
  --directory "./Images/"
```

### Formato actual de las imagenes de la carpeta. ***

```bash
  --fromExt "png"
```

### Formato al que quieres convertir. ***

```bash
  --toExt "webp"
```

### Calidad de las imagenes (default = 50)

(min = 0 , max = 100)
```bash
  -q 50
```

```bash
  --quality 50
```


## Ejemplo

```bash
  python ./main.py --directory "../../Desktop/testImg" --fromExt "jpg" --toExt "webp" --quality 80
```

