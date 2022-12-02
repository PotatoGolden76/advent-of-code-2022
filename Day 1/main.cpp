// 1
#include <fstream>
#include <iostream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>

int main()
{
    std::ifstream in("input.txt");

    // char line[50];
    std::string line;
    int elf = 0;
    std::vector<int> elves = {0};
    while (!in.eof())
    {
        std::getline(in, line);
        if (line == "\n" || line == "")
        {
            elf++;
            elves.push_back(0);
        } else {
            // std::cout << line << std::endl;
            elves[elf] += std::stoi(line);
        }
    }

    //Show top elf
    // std::cout << *std::max_element(elves.begin(), elves.end());

    //Show top 3
    std::sort(elves.begin(), elves.end());
    // std::cout << *(elves.end()-1) << std::endl;
    // std::cout << *(elves.end()-2) << std::endl;
    // std::cout << *(elves.end()-3) << std::endl;

    int sum = *(elves.end()-1) + *(elves.end()-2) + *(elves.end()-3);
    std::cout << sum;

    in.close();
    return 0;
}