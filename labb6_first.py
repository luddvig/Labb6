import timeit
# trackid<SEP>låtid<SEP>artistnamn<SEP>låttitel

class Song:
    def __init__(self, trackid, songid, artistnamn, songtitel):
        self.trackid = trackid
        self.songid = songid
        self.artistnamn = artistnamn
        self.songtitel = songtitel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn

    def __str__(self):
        return self.artistnamn + " - " + self.songtitel

    def __contains__(self, item):
        if item in self.artistnamn:
            return True
        else:
            return False


def linsok(lista, key):
    """Funktion för linjärsökning. Tar in lista med artistobjekt samt eftersökt artistnamn som str."""
    found = False                       # Default
    for obj in lista:                   # Itererar genom objektslistan, jämför artistnamn med angivet namn
        if key == obj.artistnamn:
            found = True
        else:
            pass
    return found


def binary_search(lista, key):
    """Funktion för binär sökninng. Börjar från mitten, stänger sedan in successivt."""
    #lista.sort()
    low = 0                             # Initierar low
    high = len(lista) - 1               # Initierar high
    found = False                       # Initierar found
    while low <= high and not found:    # Villkor att fortsätta tills (worst cese) low=high, stänger in till mitten
        middle = (low+high) // 2
        if key == lista[middle].artistnamn:
            #print("Hittades")
            found = True
        else:
            if key < lista[middle].artistnamn:
                high = middle - 1
            else:
                low = middle + 1
    return found


def make_hash_list(artistobjektlista):
    """Funktion för att skapa hashlista med dictionary. Tar in lista med artistobjekt."""
    artist_dict = dict()
    for artist_objekt in artistobjektlista:
        artist_dict[artist_objekt.artistnamn] = artist_objekt  # Sätter artistnamn som nyckel, objekt som värde
    return artist_dict


def hashsearch(dicti, key):
    """Funktion för hashsökning. Tar in en dictionary (hashlista) samt eftersök key som type str."""
    if dicti.get(key).artistnamn == key:
        return True
    else:
        return "Hittades inte"


# fil: unique_tracks.txt
def readfile(filename):
    """Funktion för att läsa in fil med artister. Tar in filnamn av tupe str."""
    objekt_lista = list()
    with open(filename, "r") as songfil:
        for rad in songfil:
            ordet = rad.split("<SEP>")
            objekt_lista.append(Song(ordet[0],ordet[1],ordet[2],ordet[3]))
    return objekt_lista


def main():
    filename = "unique_tracks.txt"

    # Olika längder på listan
    longlista = readfile(filename)
    mellanlista = longlista[0:500000]
    kortlista = longlista[0:250000]
    lin_bin = longlista                 # Varieras för olika listor

    # Skapar hashlistan
    hashlista = make_hash_list(longlista)

    # Sorterar listan om binärsökning ska utföras, kommenteras med fördel ut annars ty tidskrävande.
    lin_bin.sort()

    # Olika element i listan att söka efter. Första, sista eller mittersta.
    forsta = lin_bin[0].artistnamn
    sista = lin_bin[-100].artistnamn
    mitten = lin_bin[len(lin_bin)//2].artistnamn

    # Skapar lista med hashnycklar för att söka efter specifikt indext likt linjär- och binärsökning
    key_list = list(hashlista.keys())
    forsta_key = key_list[0]
    sista_key = key_list[-1]
    mitten_key = key_list[len(key_list)//2]

    # Väljer vilken artist som ska användas. Första, sista, mitten - linjär/binär eller hash
    # Väljer vilken lista som ska användas. Lång, mellan, kort eller hash (som också kan vara  lång mellan eller kort)
    lista = lin_bin
    testartist = mitten

    n = len(lista)
    print("Antal element =", n)
    input("Tidtagning, tryck enter")

    # Tidtagning. Obs minskar number till 100 för linsearch, tar mycket lång tid annars
    sok_tid = timeit.timeit(stmt = lambda: binary_search(lista, testartist), number = 10000)  
    print("Sökningen tog", round(sok_tid, 10)/10000, "sekunder") # Minska division från 10000 till 100 om linsearch


main()

