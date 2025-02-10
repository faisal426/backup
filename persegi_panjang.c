#include <stdio.h>

int main() {
    char nama[50];
    float panjang, lebar;
    int pilihan;

    printf("SELAMAT DATANG DI KALKULATOR PERSEGI PANJANG\n\n");
    
    printf("Masukkan nama: ");
    scanf("%s", nama);

    printf("Masukkan nilai panjang: ");
    scanf("%f", &panjang);

    printf("Masukkan nilai lebar: ");
    scanf("%f", &lebar);

    printf("\nNilai apa yang mau kamu cari?\n");
    printf("Ketik 1: Luas persegi panjang\n");
    printf("Ketik 2: Keliling persegi panjang\n");
    
    printf("\nJawaban: ");
    scanf("%d", &pilihan);

    printf("\nHai %s\n", nama);

    if (pilihan == 1) {
        printf("Luas persegi panjang adalah: %.2f\n", panjang * lebar);
    } else if (pilihan == 2) {
        printf("Keliling persegi panjang adalah: %.2f\n", 2 * (panjang + lebar));
    } else {
        printf("Pilihan tidak valid!\n");
    }

    return 0;
}
