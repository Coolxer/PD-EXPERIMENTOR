# PD-EXPERIMENTOR

## Środowisko badawcze przybliżonych metod stacjonarnych rozwiązywania układów równań liniowych wykorzystujące bibliotekę [equiter](https://github.com/Coolxer/PD-EQUITER-LIBRARY).

_Realizacja w ramach pracy dyplomowej "Analiza i realizacja wybranych algorytmów przybliżonego rozwiązywania układów równań liniowych" KRK/13/4028_

**\*Autor:** Łukasz Miłoś 161883

---

## Zawartość

Środowisko badawcze powstało w celu przetestowania biblioteki [equiter](https://github.com/Coolxer/PD-EQUITER-LIBRARY).

Najważniejsze cechy środowiska:

- umożliwia generowanie rozmaitych URL poprzez tworzenie różnego typu macierzy i wektorów o różnej wielkości
- automatycznie rozwiązuje układ równań stacjonarnymi metodami iteracyjnymi
- tworzy pliki wynikowe w postaci tekstowej
- tworzy wykresy graficzne porównujące zbieżność według wskaźnika liczby wykonanych iteracji i czasu obliczeń oraz błędu agregowanego na każdym etapie
- umożliwia wykonywanie zarówno pojedynczych jak i grupowych eksperymentów
- zapewnia pełną automatyzację procesu badawczego i prostą obsługę

Wartą uwagi jest możliwość grupowania eksperymentów według rozmiaru układu, typu macierzy wejściowej, zadanej tolerancji, wartości wektora x0.

---

## Wymagania

Oprócz samej biblioteki niezbędne są dodatkowe narzędzia:

- interpreter [Python](https://www.python.org/downloads/) (zalecana wersja 3.\*)
- biblioteka [NumPy](https://numpy.org/install/) (niekiedy instalowana razem z Python'em)
- biblioteka [SciPy](https://www.scipy.org/install.html)
- biblioteka [tkinter](https://docs.python.org/3/library/tkinter.html) (zazwyczaj instalowana razem z interpreterem, o ile nie odznaczono tej opcji podczas instalacji)
- biblioteka [matplotlib](https://matplotlib.org/stable/users/installing.html)
- biblioteka [pandas](https://pandas.pydata.org/)
- biblioteka [dataframe_image](https://pypi.org/project/dataframe-image/)
- dowolny edytor tekstowy (zalecany edytor kodu źródłowego, np. [Visual Studio Code](https://code.visualstudio.com/))

---

## Instalacja

Repozytorium należy pobrać przy pomocy systemu kontroli wersji [git](https://git-scm.com/) albo "ręcznie" w formacie .zip, a następnie wypakować.

Repozytorium zawiera podmoduł o nazwie [PD-EQUITER-LIBRARY](https://github.com/Coolxer/PD-EQUITER-LIBRARY) stanowiący bibliotekę implementującą metody iteracyjne. W związku z tym proces pobierania środowiska badawczego jest nieco bardziej skomplikowany:

- w przypadku korzystania z systemu kontroli wersji git należy pobrać również zależności dotyczące podmodułu. W tym celu do polecenia git clone należy dodać argument --recurse-submodules, tak jak poniżej

```console
git clone --recurse-submodules https://github.com/Coolxer/PD-EXPERIMENTOR
```

- w przypadku "ręcznego" pobierania środowiska katalog PD-EQUITER-LIBRARY zawierający podmoduł będzie pusty. Należy zatem pobrać ten podmoduł samodzielnie [tutaj](https://github.com/Coolxer/PD-EQUITER-LIBRARY), a następnie przenieść go do tego katalogu.

**_UWAGA:_** Warto zmienić nazwę katalogu PD-EQUITER-LIBRARY na **_equiter_**. Jest to zalecane podejście ze względu na prostotę i możliwość podążania za tym samouczkiem.

**_UWAGA:_** Środowisko badawcze powinno być podkatalogiem bieżącego projektu, a więc skrypty wykorzystujące środowisko powinny być wyżej w hierarchii katalogów. Innymi słowy nie należy umieszczać własnych skryptów wewnątrz katalogu środowiska!

**_UWAGA:_** Po ściągnięciu środowiska zalecana jest zmiana nazwy głównego katalogu na **_experimentor_**. Jest to skrótowa nazwa ułatwiająca korzystanie z biblioteki. Jeśli chcesz podążać dalej za poradnikiem zmiana nazwy jest niezbędna!

Po przygotowaniu biblioteki, we własnym pliku Python (z rozszerzeniem \*.py) można przystąpić do importu biblioteki.\*\*\*\*

```python
import experimentor as exp
```

---

## Jak to działa?

Poniżej zaprezentowano jedynie urywek możliwości środowiska badawczego.

### Przykład

W celu zapoznania się z biblioteką zalecane jest uruchomienie poniższego przykładu

```python
import experimentor as exp

experiment_name = "my_experiment_001"
size = 1000
matrix_type = exp.sparse
max_iterations = 2000
tolerance = 0.0001
w_values = [1.1, 1.3, 1.5]

exp.do_single_experiment(experiment_name, size, matrix_type, max_iterations, tolerance, w_values)
```

Efektem wykonania powyższego kodu będzie wyświetlenie następujących informacji w konsoli / terminalu:

```console
#############################################################
######### Eksperyment:  my_experiment_001 ###########

Generowanie macierzy głównej ...
Generowanie / Obliczanie / Wczytywanie wektora wyrazów wolnych ...
Rozwiązywanie układu metodą Jacobiego ...
Rozwiązywanie układu metodą Gaussa-Seidela ...
Rozwiązywanie układu metodą SOR ...
    - dla parametru 'w': 1.1
    - dla parametru 'w': 1.3
    - dla parametru 'w': 1.5
Zapisywanie informacji o eksperymencie ...
Zapisywanie liczby wyk. iteracji ...
Zapisywanie czasu obliczeń ...
Zapisywanie błędów ...
Zapisywanie szczegółowych wyników ...
Rysowanie wykresu liczby wyk. iteracji dla wszystkich metod ...
Rysowanie wykresu czasu obliczeń dla wszystkich metod...
Rysowanie wykresu liczby wyk. iteracji tylko dla metody SOR ...
Rysowanie wykresu czasu obliczeń tylko dla metody SOR...
Rysowanie wykresu błędu agregowanego dla wszystkich metod...
Rysowanie wykresu błędu agregowanego tylko dla metody SOR...


Eksperyment my_experiment_001 zakończony sukcesem!
#############################################################
```

## Dodatkowe informacje

W przypadku metody SOR badane jest kilka wartości parametru relaksacji (podanych przez użytkownika), a wynik biorący udział w porównaniu z metodą Jacobiego i metodą Gaussa-Seidela jest najlepszym wynikiem uzyskanym przy pomocy metody SOR. Przyjęto najlepszy rezultat (zamiast najgorszego lub średniej), ponieważ pozostałe metody również dążą do najlepszego wyniku.
