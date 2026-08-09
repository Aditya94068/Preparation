#include <stdio.h>
#include <limits.h>

int solve(int n) {
    int i = 1; 
    int max_remainder = INT_MIN;
    int best_pack_size = 1;

    while (i <= n) {
        int remainder = n % i;
        

        if (remainder >= max_remainder) {
            max_remainder = remainder;
            best_pack_size = i;
        }
        i++;
    }
    return best_pack_size;
}

int main() {
    int n = 12;
    int ans = solve(n);
    printf("%d\n", ans); // आउटपुट: 3
    return 0;
}
