import beaufort
import diagonal


def shfaq_menune():
    print("\n" + "=" * 45)
    print("   PROJEKTI 2: KRIPTOGRAFIA")
    print("=" * 45)
    print("1. Beaufort Cipher")
    print("2. Diagonal Transposition Cipher")
    print("3. Dil nga programi")
    print("=" * 45)


def main():
    while True:
        shfaq_menune()
        zgjedhja = input("Zgjidhni një opsion (1, 2 ose 3): ")

        if zgjedhja == '1':
            print("\n--- Beaufort Cipher ---")
            veprimi = input("Shtyp 'E' per Enkriptim ose 'D' per Dekriptim: ").upper()

            if veprimi in ['E', 'D']:
                teksti = input("Shkruani tekstin: ")
                celesi = input("Shkruani çelësin (fjalëkalimin): ")

                # Thërrasim funksionin nga skedari beaufort.py
                rezultati = beaufort.beaufort(teksti, celesi)

                tipi = "Enkriptuar" if veprimi == 'E' else "Dekriptuar"
                print(f"\n[+] Teksti i {tipi}: {rezultati}")
            else:
                print("\n[Gabim] Zgjedhje e gabuar. Shtyp E ose D.")

        elif zgjedhja == '2':
            print("\n--- Diagonal Transposition Cipher ---")
            veprimi = input("Shtyp 'E' per Enkriptim ose 'D' per Dekriptim: ").upper()

            if veprimi in ['E', 'D']:
                teksti = input("Shkruani tekstin: ")

                # Kodi i Personit 2 e llogarit vetë matricën, ndaj nuk kërkojmë çelës
                if veprimi == 'E':
                    rezultati = diagonal.diagonal_encrypt(teksti)
                    print(f"\n[+] Teksti i Enkriptuar: {rezultati}")
                elif veprimi == 'D':
                    rezultati = diagonal.diagonal_decrypt(teksti)
                    print(f"\n[+] Teksti i Dekriptuar: {rezultati}")
            else:
                print("\n[Gabim] Zgjedhje e gabuar. Shtyp E ose D.")

        elif zgjedhja == '3':
            print("\nDuke dalë nga programi. Punë të mbarë!")
            break
        else:
            print("\n[Gabim] Opsion i pavlefshëm. Ju lutem zgjidhni 1, 2 ose 3.")


if __name__ == "__main__":
    main()