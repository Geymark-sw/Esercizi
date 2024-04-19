def check_lenght(s:str) -> None:
    check: int = 10

    if len(s) > check:
        print(f"La lunghezza della stringa è di {len(s)} ed è maggiore di {check}")

    elif len(s) < check:

        print(f"La lunghezza della stringa è di {len(s)} ed è minore di {check}")

    else:

        print(f"La lunghezza della stringa è di {len(s)} ed è uguale al valore {check}")

stringa: str = "BELLO"

check_lenght(stringa)
