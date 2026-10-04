import polars as pl

# Örnek cihaz verileri
data = {
    "cihaz_adi": [
        "SUNUCU-MAIN",
        "SUNUCU-01",
        "SUNUCU-02",
        "PC-01",
        "PC-02",
        "SUNUCU-03"
    ],
    "sicaklik": [72.5, 85.3, 91.7, 67.2, 88.9, 95.4],
    "durum": [
        "Normal",
        "Normal",
        "Kritik",
        "Normal",
        "Uyari",
        "Kritik"
    ]
}

# Polars DataFrame oluştur
df = pl.DataFrame(data)

# Lazy sorgu
sonuc = (
    df.lazy()
    .filter(
        (pl.col("durum") != "Kritik") &
        (pl.col("cihaz_adi") != "SUNUCU-MAIN")
    )
    .collect()
)

print("=== FİLTRELENMİŞ VERİ ===")
print(sonuc)
