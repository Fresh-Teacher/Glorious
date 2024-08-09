#include <stdio.h>

int main() {
    int choice;
    float length, width, radius, base, height;

    printf("Enter the shape you want to calculate (1. Square, 2. Circle, 3. Triangle): ");
    scanf("%d", &choice);

    if (choice == 1) {
        printf("Enter length and width: ");
        scanf("%f %f", &length, &width);
        printf("Area of square: %.2f\n", length * width);
    }

    if (choice == 2) {
        printf("Enter radius: ");
        scanf("%f", &radius);
        printf("Area of circle: %.2f\n", 3.14 * radius * radius);
    }

    if (choice == 3) {
        printf("Enter base and height: ");
        scanf("%f %f", &base, &height);
        printf("Area of triangle: %.2f\n", 0.5 * base * height);
    }

    return 0;
}
