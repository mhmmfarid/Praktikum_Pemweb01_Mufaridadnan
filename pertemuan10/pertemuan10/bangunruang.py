import math

def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok(p,l,t):
    hasil = p * l * t
    return hasil

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

def tabung (jarijari, tinggi):
    return 2*math.pi * jarijari * (jarijari+tinggi)

def kerucut(jarijari, tinggi):
    return (1/3) *math.pi * jarijari * jarijari * tinggi

print(prisma(3,3,3))