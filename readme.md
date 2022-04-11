# PD-EXPERIMENTOR

## Środowisko badawcze przybliżonych metod stacjonarnych rozwiązywania układów równań liniowych wykorzystujące bibliotekę [equiter](https://github.com/Coolxer/PD-EQUITER-LIBRARY).

_Realizacja w ramach pracy dyplomowej "Analiza i realizacja wybranych algorytmów przybliżonego rozwiązywania układów równań liniowych" KRK/13/4028_

**\*Autor:** Łukasz Miłoś 161883\*

---

## Zawartość

Środowisko badawcze powstało w celu przetestowania biblioteki [equiter](https://github.com/Coolxer/PD-EQUITER-LIBRARY).

Najważniejsze cechy środowiska:

- umożliwia generowanie różnego typu macierzy i wektorów o różnej wielkości
- automatycznie rozwiązuje układ równań stacjonarnymi metodami iteracyjnymi
- tworzy pliki wynikowe w postaci tekstowej
- tworzy wykresy graficzne porównujące zbieżność według wskaźnika liczby wykonanych iteracji i czasu obliczeń
- zapewnia pełną automatyzację procesu badawczego i prostą obsługę

System pozwala m.in. na porównanie zbieżności poszczególnych metod iteracyjnych względem badanego układu równań. Możliwość generowania szerokiego spektrum macierzy wejściowych, a co za tym idzie układów, pozwala na przetestowanie skuteczności metod względem różnych typów macierzy wejściowych.

---

## Wymagania

Oprócz samej biblioteki niezbędne są dodatkowe narzędzia:

- interpreter [Python](https://www.python.org/downloads/) (zalecana wersja 3.\*)
- biblioteka [NumPy](https://numpy.org/install/) (niekiedy instalowana razem z Python'em)
- biblioteka [SciPy](https://www.scipy.org/install.html)
- biblioteka [tkinter](https://docs.python.org/3/library/tkinter.html) (zazwyczaj instalowana razem z interpreterem, o ile nie odznaczono tej opcji podczas instalacji)
- biblioteka [matplotlib](https://matplotlib.org/stable/users/installing.html)
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

Po przygotowaniu biblioteki, we własnym pliku Python (z rozszerzeniem \*.py) można przystąpić do importu biblioteki.

```python
import experimentor as exp
```

---

## Jak to działa?

### Przykład

W celu zapoznania się z biblioteką zalecane jest uruchomienie poniższego przykładu

```python
import experimentor as exp

experiment_name = "my_experiment_001"
matrix_type = exp.matrix_type.random
matrix_size = 1000

exp.do_experiment(experiment_name, matrix_type, matrix_size)

```

Efektem wykonania powyższego kodu będzie wyświetlenie następujących informacji w konsoli / terminalu:

```console
Zapisywanie macierzy ...
Zapisywanie innych parametrow ...
Trwa rozwiazywanie ukladu metoda Jacobiego ...
Trwa rozwiazywanie ukladu metoda Gaussa-Seidela ...
Trwa rozwiazywanie ukladu metoda SOR ...
    SOR: w: 1.1
    SOR: w: 1.3
    SOR: w: 1.5
    SOR: w: 1.7
    SOR: w: 1.9
Zapisywanie rezultatow ...
Generowanie wykresow ...
```

A także wyświetlenie następujących wykresów:
![title](md_images/example_iterations.png)

![title](md_images/example_times.png)

### Omówienie działania

#### Wstęp

Użytkownik podaje 3 parametry funkcji badawczej:

- **_experiment_name_** (str) - nazwę eksperymentu (czyli nazwę katalogu głównego z konfiguracją i wynikami)
- **_matrix_type_** (wybór opcji) - typ macierzy wejściowej układu (wybór za pomocą obiektu **_matrix_type_**), dostępne możliwości to:

  - 'sparse': rzadka, wygenerowana przy pomocy zewnętrznej biblioteki
  - 'random': pełna wygenerowana w sposób losowy
  - 'diagonal': diagonalna, wygenerowana w sposób losowy
  - 'band': wstęgowa (pasmowa) o szerokości 3
  - 'lower_triangular': dolno-trójkątna
  - 'upper_triangular': górno-trójkątna
  - 'external': zewnętrzna, pobrana ze źródeł zewnętrznych

- **_matrix_size_** (int) - rozmiar macierzy wejściowej układu

Z perspektywy użytkownika ważne jest to, że w katalogu **_data_**, wewnątrz środowiska, zostanie utworzony katalog o nazwie eksperymentu, czyli **_name_**.

#### Konfiguracja

Odpowiednia macierz zostanie wygenerowana, podobnie jak wektor wyrazów wolnych, o ile nie istnieje (plik może już istnieć w katalogu **_exp_data_** o nazwie **_b\_[matrix_size]_**). Wektor wyrazów wolnych może być bowiem dzielony pomiędzy różne eksperymenty, w celu zbadania innych zależności. Wszelkie dane konfiguracyjne zostaną zapisane wewnątrz katalogu doświadczenia, ale w specjalnie przygotowanym katalogu config, czyli:

```console
      experimentor/data/[experiment_name]/config
```

Pliki konfiguracyjne tworzone w ramach katalogu **_config_** to:

- **_A.txt_** - plik zawierający macierz wejściową układu
- **_general.txt_** - plik zawierający nazwę eksperymentu, typ macierzy i rozmiar układu
- **_parameters.txt_** - plik zawierający dane konfiguracyjne metod, takie jak dokładność obliczeń, maksymalna liczba iteracji, parametr relaksacji

#### Obliczenia

Następnie wykonywane są obliczenia za pomocą stacjonarnych metod przybliżonych rozwiązywania URL, przy pomocy biblioteki [equiter](https://github.com/Coolxer/PD-EQUITER-LIBRARY).

#### Wyniki

Wyniki obliczeń zapisywane są wewnątrz katalogu **_results_** o ścieżce:

```console
      experimentor/data/[experiment_name]/results
```

Wyniki można podzielić na tekstowe i graficzne.

W przypadku wyników tekstowych powstaje folder **_txt_**, a wewnątrz niego tworzone są następujące elementy:

- plik **_iterations.txt_** zawierający liczbę wykonanych iteracji niezbędnych do rozwiązania danego układu przez poszczególne metody
- plik **_times.txt_** zawierający czas obliczeń poszczególnych metod
- katalog **_solution_** wewnątrz, którego zostały utworzone pliki tekstowe zawierające wektor rozwiązań układu, osobno dla każdej z metod (jacobi.txt, gauss_seidel.txt, sor.txt)

W przypadku wyników graficznych powstaje folder **_img_**, a wewnątrz niego tworzone są następujące elementy:

- **_iterations.png_** - wykres porównujący liczbę wykonanych iteracji przez poszczególne metody dla danego układu
- **_times.png_** - wykres porównujący czas obliczeń poszczególnych metod dla danego układu

---

## Dodatkowe informacje

W przypadku metody SOR badane jest kilka wartości parametru relaksacji, a wynik biorący udział w porównaniu z metodą Jacobiego i metodą Gaussa-Seidela jest najlepszym wynikiem uzyskanym przy pomocy metody SOR. Przyjęto najlepszy rezultat (zamiast najgorszego lub średniej), ponieważ pozostałe metody również dążą do najlepszego wyniku.
