#include <iostream>
#include <string>




std::string generateLetters() {
    std::string letters;
    for (char i = 'a'; i <= 'z'; ++i) {
        std::cout << "Letters: " << int(i) << "=> " << i << std::endl;
        letters += i;
    }
    for (char i = 'A'; i <= 'Z'; ++i) {
        std::cout << "Letters: " << int(i) << "=> " << i << std::endl;
        letters += i;
    }
    return letters;
}


std::string generateText() {
    char name[] = "Arman";
    char surname[] = {'T', 'o', 'r', 'g', 'o', 'm', 'y', 'a', 'n','\0'};
    
    return std::string(name) + " " + std::string(surname);
}
int main() {
    // std::string letters = generateLetters();
    // std::cout << "Letters: " << "\n" << letters << std::endl;

    std::cout << "============================" <<  std::endl;

    std::string text = generateText();
    std::cout << text << std::endl;
    return 0;
}