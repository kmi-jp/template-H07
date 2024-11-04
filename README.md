# H07: Data 4

## DataFrame a Series v balíčku `data`
V balíčku `data` upravte metody `DataFrame.from_csv()` a `Series.from_csv()` tak, aby namísto textu přijímaly instanci třídy `pathlib.Path` pomoci parametru `filepath` (tedy soubor s příponou `csv`). Použíjte balíček `csv`.

```python
import pathlib
from data.dataframe import DataFrame

df = DataFrame.from_csv(filepath=pathlib.Path.cwd() / "input.csv")
```
## Soubor `sum_points.py`

Pomocí balíčku `data` napište jednoduchý script `sum_points.py` (není součástí balíčku), který v adresáři `results` sečte zisk bodů z domácích úkolů předmětu KMI/JP uložených v `csv` souborech končící příponou `.csv` (pouze). Poté v pracovním adresáři vytvoří soubor ve formátu `output.json`, který obsahuje součty bodů přes jednotlivé úkoly. Výsledný soubor má mít následující obsah:

```json
{"L01E01": 39, "L01E02": 38, "L01E03": 38, "L01E04PEP": 38, "L02E01": 36, "L02E02": 35, "L02E03": 35, "L02E04PEP": 37, "L03E01": 36, "L03E02": 31, "L04E01": 31, "L04E02": 32, "L04E03": 29, "L05E01": 31, "L05E02": 21, "L06E01": 17, "L06E02": 5}
```

Soubory s příponou `.csv` obsahují nejprve sloupec se součtem všech odevzdaných úkolů daného studenta (ten nesčítejte), a poté sloupec pro každý úkol (hodnoty "1" nebo "").

Výsledný soubor obsahuje vždy název úkolu a součet získaných bodů (např. tedy úkol L01E01 splnilo 39 studentů). **Tento soubor do repozitáře neposílejte!**

**Při řešení použíjte v maximální míře funkcionalitu Vašeho balíčku `data` a `json`.**


## Lokální testování
Funkčnost řešení ověříte následujícím příkazem:

```bash
pytest
```