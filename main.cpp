#include <iostream>
#include <string>
#include <cstring>
#include <vector>

int countFuncArgs(const char* fn) {
    fn = strchr(fn, '(');
    if (!fn) //Bad Formatting.
        return 0; //Exception should be added.

    if (fn[1] == ')') {
        std::cout << "noargs!\n";
        return 0;
    }

    int i = 0, argc = 1;
    while (fn[i] != 0) {
        if (fn[i] == '"') { //String detection
            int j = i + 1;
            while (fn[j] != 0 && fn[j] != '"')
                if (fn[j] == '\\')
                    j += 2;
                else j++;

            i = j + 1;
        }

        if (fn[i] == ',')
            argc++;

        i++;
    }

    return argc;
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    std::cout << "args: " << countFuncArgs("func(bleh1, bleh2, \"this, is, a, fake, bleh\", bleh3)");
}