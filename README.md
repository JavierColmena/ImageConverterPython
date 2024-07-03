
## Authors

- [@JavierColmena](https://www.github.com/javiercolmena)


# Image Converter

Image converter within a directory.

## Get Started

Install the ``PILLOW`` library from Python

```bash
  pip install pillow
```
```bash
  python ./main.py -h
```
    
## Commands

### Help

```bash
  python ./main.py -h
```

### Locate the directory with the images. ***

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

### Current format of the images in the folder. ***

```bash
  --toExt "webp"
```

### Image quality (default = 50)

(min = 0 , max = 100)
```bash
  -q 50
```

```bash
  --quality 50
```


## Example

```bash
  python ./main.py --directory "../../Desktop/testImg" --fromExt "jpg" --toExt "webp" --quality 80
```

