#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define PARTICLES 10000
#define STEP_SIZE 0.1
#define DETECTOR_X 1.0

// Function to simulate a single particle's journey
double simulate_particle(void) {
    double x = 0, y = 0;
    while (x < DETECTOR_X) {
        double randVal = (double)rand() / RAND_MAX;
        if (randVal < 0.15) {
            // Move up
            y += STEP_SIZE;
        } else if (randVal < 0.30) {
            // Move down
            y -= STEP_SIZE;
        } else if (randVal < 0.35) {
            // Move left, with reflection if at x=0
            if (x == 0) x += STEP_SIZE; // Reflect
            else x -= STEP_SIZE;
        } else {
            // Move right
            x += STEP_SIZE;
        }

        // Reflection at top and bottom boundaries
        if (y > 1) y = 1 - (y - 1);
        if (y < -1) y = -1 - (y + 1);
    }
    return y;
}

int main() {
    srand(time(NULL)); // Seed the random number generator

    FILE *file = fopen("detector_hits.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < PARTICLES; i++) {
        double y = simulate_particle();
        fprintf(file, "%f\n", y);
    }

    fclose(file);
    printf("Simulation complete. Results stored in detector_hits.txt\n");

    return 0;
}

