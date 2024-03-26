#include <iostream>
#include <vector>
#include <cmath>

float f(float a, float b, float c, float d, float x) {
    return a * std::pow(x, 3) + b * std::pow(x, 2) + c * x + d;
}

int main() {
    int a,b,c,d;
    std::cin >> a >> b >> c >> d;
    
    if (a < 0) {
        a *= -1;
        b *= -1;
        c *= -1;
        d *= -1;
    }

    float l = -3001;
    float r = 3001;

    float x = r;
    while (std::abs(f(a,b,c,d,x)) > std::pow(10, -6)) {
        x = (l + r) / 2;
        if (f(a,b,c,d,x) > 0) {
            r = x;
        } else {
            l = x
        }
    }
    std::cout << x;
}