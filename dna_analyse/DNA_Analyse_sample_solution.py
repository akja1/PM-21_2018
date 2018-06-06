nukleotide ={"A": {'name': "Adenin", 'gewicht': 313210, 'compl': 'T'},
             "T": {'name': "Thymin", 'gewicht': 304200, 'compl': 'A'},
             "G": {'name': "Guanin", 'gewicht': 329210, 'compl': 'G'},
             "C": {'name': "Cytosin", 'gewicht': 289180, 'compl': 'C'},
             }


# Molekulargewichte in mg/mol
molek_gewicht_oh = {"OH" : 17010}            
          # freie OH-Gruppe am 3'-Ende eines DNA-Fragments
                      
                     
from collections import Counter

def ist_valide_sequenz(seq, alphabet, match_case=False):
    """Prüfe, ob eine Sequenz nur Buchstaben des erlaubten Alphabets enthält.

    Als Alphabet kann als iterierbare Buchstabenfolge beliebigen Typs
    übergeben werden.
    Mit match_case=True muss die Groß-/Kleinschreibung der des Alphabets
    entsprechen.
    """

    if match_case == False:
        # Groß-/Kleinschreibung soll keine Rolle spielen.
        # Deshalb wandeln wir die Sequenz und das Alphabet in Großbuchstaben
        # um. Für das Alphabet ist das am einfachsten, wenn wir es zuerst
        # in einen string verwandeln.
        seq = seq.upper()
        alphabet = ''.join(alphabet).upper()
    for c in seq:
        if c not in alphabet:
            return False
    return True


def hole_dna_sequenz(erlaubte_nukleotide):
    """Liefere eine vom Nutzer erfragte und validierte DNA-Sequenz.

    Um gültig zu sein, darf die Sequenz nur aus den Buchstaben
    aus erlaubte_nukleotide (in Groß- oder Kleinschreibung) bestehen.
    """

    while True:
        sequence = input('Gib eine DNA-Sequenz ein: ')

        if ist_valide_sequenz(sequence, erlaubte_nukleotide):
            return sequence.upper()

        # Dieser Teil wird ausgeführt wenn die Bedingung hinter if
        # nicht erfüllt war.
        print()
        print(
            'Bei der Eingabe handelt es sich nicht um eine gültige '
            'DNA-Sequenz!'
            )
        print()
        print()

def revers_komplimentaere_dna():
    pass
def basenhaeufigkeiten():
    pass

if __name__ == '__main__':
    # Sequenz einlesen
    # ----------------
    seq = hole_dna_sequenz(nukleotide)

    # Berechnungen
    # ------------

    # Sequenzlänge
    seqlen = len(seq)
    # Basenhäufigkeiten
    basenhaeufigkeiten = Counter(seq)
    
    for nukleotid, anzahl in basenhaeufigkeiten.items():
        print(" Das Nukleotid %s kommt %s Mal vor" % (nukleotide[nukleotid]['name'], anzahl))
    # GC-Gehalt
    gc_gehalt = 100 * (n_g+n_c) / seqlen
    # Molekulargewicht
    mw_gesamt = sum(int(seq[nukleotide[gewicht]]) + molek_gewicht_oh[OH]  # in mg/mol

    # Ausgabe
    # -------
    print()
    print('Eingelesene Sequenz:', seq)
    print()
    print('Länge:', seqlen)
    print()
    print('Base\tHäufigkeit')
    print('G', n_g, sep='\t')
    print('A', n_a, sep='\t')
    print('T', n_t, sep='\t')
    print('C', n_c, sep='\t')
    print()
    print('% GC-Gehalt:', gc_gehalt)
    print()
    print('Molekulargewicht:', mw_gesamt/1000, 'g/mol')
