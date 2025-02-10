#include <stdio.h>

int main() {
    char nama[50];
    int panjang, lebar, pilihan;

    printf("SELAMAT DATANG DI KALKULATOR PERSEGI PANJANG\n\n");
    
    printf("Masukkan nama: ");
    scanf("%s", nama);

    printf("Masukkan nilai panjang: ");
    scanf("%d", &panjang);

    printf("Masukkan nilai lebar: ");
    scanf("%d", &lebar);

    printf("\nNilai apa yang mau kamu cari?\n");
    printf("Ketik 1: Luas persegi panjang\n");
    printf("Ketik 2: Keliling persegi panjang\n");
    
    printf("\nJawaban: ");
    scanf("%d", &pilihan);

    printf("\nHai %s\n", nama);

    if (pilihan == 1) {
        printf("Luas persegi panjang adalah: %d\n", panjang * lebar);
    } else if (pilihan == 2) {
        printf("Keliling persegi panjang adalah: %d\n", 2 * (panjang + lebar));
    } else {
        printf("Pilihan tidak valid!\n");
    }

    return 0;
}
