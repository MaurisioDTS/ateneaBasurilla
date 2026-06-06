# atenea md5 flag gui

*gui mínima para generar flags de atenea a partir de un texto.*

<img width="524" height="201" alt="Captura de pantalla_20260606_103614" src="https://github.com/user-attachments/assets/35ef97a1-0809-4756-a5e3-ce2b352a24f8" />

## esto pa k es

escribes una cadena y te devuelve `flag{<md5_en_hex>}`. el hash es el mismo que harías en bash con:

```bash
echo -n 'tu_cadena' | md5sum
```

## requisitos

- python 3
- tkinter (viene con la stdlib en la mayoría de distros linux)

## uso

se puede compilar para linux sin ningún problema, pero no he probado en windows. el script corre igual en los 2.

```bash
python3 atenea_basurilla.py
```

compila para hacer dobleclick haciendo:

```bash
./build.sh
```

## autor

- **yo** — *basurilla inútil*

## licencia

yu good my frien¿?

---
