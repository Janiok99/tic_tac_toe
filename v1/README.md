# Tic Tac Toe v1 – Gra Gracz vs Gracz

    Wersja v1 to podstawowa implementacja gry w kółko i krzyżyk dla dwóch graczy.  
    Gracze wykonują ruchy na zmianę, wybierając pola od 1 do 9.

## Funkcjonalności

    - Plansza 3×3 reprezentowana jako lista.
    - Wyświetlanie planszy z numeracją pól.
    - Obsługa ruchów gracza z walidacją:
    - sprawdzanie, czy pole istnieje,
    - sprawdzanie, czy pole jest wolne.
    - Sprawdzanie zwycięstwa:
    - w wierszach,
    - w kolumnach,
    - na przekątnych.
    - Sprawdzanie remisu.
    - Automatyczna zmiana gracza po każdym ruchu.

## Jak działa gra

    1. Program wyświetla pustą planszę.
    2. Gracz X wykonuje ruch.
    3. Gracz O wykonuje ruch.
    4. Po każdym ruchu sprawdzany jest stan gry:
      - zwycięstwo,
      - remis,
      - kontynuacja.
    5. Gra kończy się po wykryciu zwycięzcy lub remisu.

## Cel wersji v1

    Wersja v1 stanowi podstawę do dalszego rozwoju gry.  
    Zawiera pełną logikę rozgrywki dla dwóch osób.
