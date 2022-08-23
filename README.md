# Rectangle
Rectangle projekt v jazyku Python je CLI aplikácia s využitím princípov Objektovo Orientovaného Programovania.

V súbore `rect.py` je implementovaná trieda `Rect` reprezentujúca obdĺžnik v rovnie so stranami rovnobežnými s osami súradnic. Každý obdĺžnik je určený celočíselnými súradnicami $(x_1, y_1)$ a $(x_2, y_2)$ ľavého dolného a pravého horného vrcholu. Vždy bude platiť $x_1 \leq x_2$, $y_1 \leq y_2$.

Trieda implementuje nasledujúce metódy:
- konštruktor `__init__(self, x1, y1, x2, y2)`: inicializuje obdĺžnik podľa zadaných súradnic vrcholov.
- `__repr__(self)`: vytvorí stringovú reprezentáciu obdĺžnika v tvare `Rect(x1,y1,x2,y2)`.
- `perimeter(self)`: vracia obvod obdĺžnika.
- `area(self)`: vracia obsah obdĺžnika.
- `__eq__(self, other)`: zistí či sú dva obdĺžniky totožné (majú rovnaké vrcholy). Vracia `True` alebo `False`. Implementuje operátor porovnania `==` (`!=`).
- `__contains__(self, other)`: zistí či je obdĺžnik `other` obsiahnutý neostro vnútri obdĺžnika `self`. Vracia `True` alebo `False`. Implementuje operátor *other* `in` (`not in`) *self*.
- `__and__(self, other)`: spočíta prienik dvoch obdĺžnikov, vracia opäť obdĺžnik. Implementuje operátor `&`. Ak je prienik prázdny, vráti obdĺžnik s $x_1 = x_2 = y_1 = y_2$.
