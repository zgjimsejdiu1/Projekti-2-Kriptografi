# Projekti 2: Kriptografia

---

## 1. Udhëzimet e Ekzekutimit

Për të ekzekutuar këtë program, duhet të keni të instaluar Python në kompjuterin tuaj. Ndiqni këto hapa:

1. Klononi këtë repository në kompjuterin tuaj duke përdorur terminalin ose Git:
   `git clone https://github.com/zgjimsejdiu1/Projekti-2-Kriptografi.git`
2. Hapni terminalin ose Command Prompt dhe lundroni brenda dosjes së projektit:
   `cd Projekti-2-Kriptografi`
3. Ekzekutoni skedarin kryesor të programit:
   `python main.py`
4. Programi do të shfaqë një menu interaktive. Përdorni numrat `1`, `2` ose `3` për të naviguar në zgjedhjet tuaja (Enkriptim/Dekriptim) dhe ndiqni udhëzimet në ekran për të dhënë tekstin dhe çelësin.

---

## 2. Përshkrimi i Algoritmeve

### Beaufort Cipher
Beaufort Cipher është një algoritëm klasik i enkriptimit që përdor një çelës (key) për të transformuar tekstin e zakonshëm (plaintext) në tekst të fshehur (ciphertext). Ai është i ngjashëm me Vigenère Cipher, por përdor një formulë të kundërt për gjenerimin e shkronjave.
Në këtë projekt, Beaufort Cipher është implementuar duke përdorur një formulë matematikore mbi alfabetin, ku çdo shkronjë e tekstit kombinohet me një shkronjë të çelësit. Një veçori e rëndësishme është se i njëjti funksion përdoret për enkriptim dhe dekriptim, pasi algoritmi është simetrik.
Ky algoritëm përdoret për qëllime edukative për të kuptuar bazat e kriptografisë klasike dhe mënyrën se si mund të mbrohen mesazhet përmes transformimeve të thjeshta.


### Diagonal Transposition Cipher
Ky program është i shkruar në Python dhe shërben për enkriptimin dhe dekriptimin e tekstit duke përdorur metodën Diagonal Cipher. 
Fillimisht, teksti pastrohet duke larguar hapësirat dhe karakteret jo-alfabetike dhe duke e kthyer në shkronja të mëdha. Më pas krijohet një matricë katrore (grid) ku vendoset teksti rresht pas rreshti, ndërsa nëse ka hapësira të mbetura, ato plotësohen me shkronjën 'X'. 
Për enkriptim, teksti lexohet në mënyrë diagonale nga matrica, duke krijuar një formë të fshehur të mesazhit. 
Për dekriptim, procesi bëhet në mënyrë të kundërt: matrica mbushet në mënyrë diagonale dhe më pas lexohet normalisht për të rikthyer tekstin origjinal, duke hequr karakteret e tepërta. Programi gjithashtu përmban një menu interaktive që i lejon përdoruesit të zgjedhë midis enkriptimit, dekriptimit ose daljes nga programi.

---

## 3. Shembuj të Rezultateve të Ekzekutimit

Më poshtë paraqiten shembuj të rezultateve të nxjerra direkt nga ekzekutimi i programit tonë në terminal.

### Shembull - Beaufort Cipher
* **Veprimi:** Enkriptim dhe Dekriptim
* **Teksti Fillestar:** `KRIPTOGRAFIA`
* **Çelësi:** `CELES`
* **Rezultati i Enkriptuar:** `SNDPZOYUENUE`
* **Testi i Dekriptimit:** Duke futur tekstin `SNDPZOYUENUE` me të njëjtin çelës `CELES`, programi kthen sërish `KRIPTOGRAFIA`.

### Shembull - Diagonal Transposition Cipher
* **Veprimi:** Enkriptim dhe Dekriptim
* **Teksti Fillestar:** `KRIPTOGRAFIA` (Matrica e llogaritur automatikisht është 3x3)
* **Rezultati i Enkriptuar:** `KRTIOAPGFXRIXAXX`
* **Testi i Dekriptimit:** Duke futur tekstin `KRTIOAPGFXRIXAXX`, programi kthen sërish `KRIPTOGRAFIA`. 
*(Shënim: Nëse gjatësia e tekstit nuk krijon një katror perfekt, algoritmi ynë i mbush hapësirat boshe automatikisht me shkronjën 'X')*.