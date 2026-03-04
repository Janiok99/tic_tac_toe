# Gra w kółko i krzyżyk w Pythonie (v1 → v2)
    To repozytorium przedstawia dwie wersje gry w kółko i krzyżyk napisanej w Pythonie.  
    Projekt ma charakter edukacyjny i pokazuje, jak rozwijać prostą grę krok po kroku, dodając nowe      funkcje i rozszerzając logikę.

## Struktura projektu
    tic_tac_toe/
    │
    ├── v1/
    │   ├── tic_tac_toe_pvp.py       
    │   ├── README.md
    ├── v2/
    │   ├── tic_tac_toe_pvp_ai.py              
    │   ├── README.md            
    │          
    ├── README.md              

## Opis wersji

### v1 – Gra Gracz vs Gracz  
    Podstawowa wersja gry, w której dwóch graczy gra na zmianę na jednej planszy.  
    Zawiera pełną logikę gry: wyświetlanie planszy, obsługę ruchów, sprawdzanie zwycięstwa i remisu.

### v2 – Gra Gracz vs Gracz / Gracz vs AI  
    Rozszerzona wersja, która dodaje menu wyboru trybu gry.  
    W trybie AI komputer wykonuje ruchy losowo, wybierając spośród wolnych pól.

## Jak uruchomić dowolną wersję

    1. Wejdź do folderu wybranej wersji, np.:
        cd v2
    2. Uruchom plik:
        python tic_tac_toe_pvp_ai.py

## Cel projektu

    Projekt pokazuje, jak rozwijać prostą grę:

        - od wersji dla dwóch graczy,
        - do wersji z wyborem trybu i prostą sztuczną inteligencją.

    Każda wersja jest samodzielna i może być uruchomiona niezależnie.
