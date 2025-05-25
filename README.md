# 📦 Barcode Generator (EAN-13) | Γεννήτρια Γραμμωτού Κώδικα

> **Description | Περιγραφή**  
> A simple Python app with a graphical interface for generating EAN-13 barcodes and saving them as PNG images to your desktop.  
> Μια απλή εφαρμογή Python με γραφικό περιβάλλον για δημιουργία γραμμωτών κωδίκων EAN-13 και αποθήκευσή τους σε μορφή PNG στην επιφάνεια εργασίας.

---

## ✅ Features | Χαρακτηριστικά

- ✔️ Input validation for 12-digit EAN-13 codes  
  Επαλήθευση εισόδου 12 ψηφίων (το 13ο υπολογίζεται αυτόματα)
- ✔️ Custom file name & format selection  
  Ορισμός ονόματος και μορφής αρχείου
- ✔️ Saves barcode to your Desktop in PNG format  
  Αποθήκευση του barcode στην επιφάνεια εργασίας (PNG)
- ✔️ Clean and simple Tkinter GUI  
  Απλό και καθαρό γραφικό περιβάλλον με Tkinter

---

## ⚙️ Requirements | Απαιτήσεις

- Python 3.x
- [`python-barcode`](https://pypi.org/project/python-barcode/)
- `Pillow` (for PNG output)

📦 Install dependencies:
```bash
pip install -r requirements.txt
