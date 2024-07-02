
## Authors

- [@JavierColmena](https://www.github.com/javiercolmena)


# Image Converter

Convertidor de imagenes dentro de un directorio.


## COMANDOS

Help

```bash
  -h
```

Ubicar el directorio con las imagenes.*

-d // --directory

```bash
  -d "./Images/"
```

```bash
  --directory "./Images/"
```

Formato actual de las imagenes de la carpeta.*

```bash
  --fromExt "png"
```

Formato al que quieres convertir.*

```bash
  --toExt "webp"
```

Calidad de las imagenes
```bash
  -q 50
```

```bash
  --quality 50
```


## EJEMPLO
##
```bash
  python ./main.py --directory "../../Desktop/testImg" --fromExt "jpg" --toExt "webp" --quality 50
```

