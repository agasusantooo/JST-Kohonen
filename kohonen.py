data_vektor = [[1, 1, 0, 0],
               [0, 0, 0, 1],
               [1, 0, 0, 0],
               [0, 0, 1, 1]]

jumlah_klaster = 2
laju_pembelajaran = 0.6
penurunan_laju = 0.5
radius = 0
jumlah_epoch = 4

def inisialisasi_bobot(jumlah_klaster, panjang_vektor):
    seed = 42
    random.seed(seed)
    bobot = []
    for _ in range(jumlah_klaster):
        bobot.append([random.random() for _ in range(panjang_vektor)])
    return bobot

def jarak_euclidean(vektor1, vektor2):
    return sum((x - y) ** 2 for x, y in zip(vektor1, vektor2)) ** 0.5

def latih_som_verbose(data, bobot, laju_pembelajaran, penurunan_laju, jumlah_epoch):
    for epoch in range(jumlah_epoch):
        print(f"Epoch {epoch + 1}:")
        for i, vektor in enumerate(data):
            jarak = [jarak_euclidean(vektor, klaster) for klaster in bobot]

            indeks_bmu = jarak.index(min(jarak))

            bobot_lama = bobot[indeks_bmu][:]
            bobot[indeks_bmu] = [w + laju_pembelajaran * (v - w) for w, v in zip(bobot[indeks_bmu], vektor)]

            print(f"  Iterasi {i + 1}:")
            print(f"    Data: {vektor}")
            print(f"    Jarak ke Klaster: {jarak}")
            print(f"    BMU (Klaster {indeks_bmu + 1}): {bobot_lama} -> {bobot[indeks_bmu]}")

        laju_pembelajaran *= penurunan_laju
        print(f"  Laju Pembelajaran: {laju_pembelajaran:.4f}\n")
    return bobot

if __name__ == "__main__":
    import random

    bobot = inisialisasi_bobot(jumlah_klaster, len(data_vektor[0]))

    bobot_akhir = latih_som_verbose(data_vektor, bobot, laju_pembelajaran, penurunan_laju, jumlah_epoch)
