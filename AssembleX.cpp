#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <filesystem>

namespace fs = std::filesystem;

int main(int argc, char* argv[]) 
{
    std::string testbench_file = "phoeniX_Testbench.v";
    std::string option = argv[1];
    std::string project_name = argv[2];
    std::string output_name = project_name + "_firmware" + ".hex";
    
    std::string directory;
    if (option == "sample") 
    {
        directory = "Sample_Assembly_Codes";
    } else if (option == "code") 
    {
        directory = "User_Codes";
    } else 
    {
        throw std::invalid_argument("Options are: sample, code");
    }
    
    std::string input_file;
    for (const auto& entry : fs::directory_iterator("Software/" + directory + "/" + project_name)) 
    {
        if (entry.path().extension() == ".txt") 
        {
            input_file = entry.path().string();
            break;
        }
    }
    
    std::string output_file = "Software/" + directory + "/" + project_name + "/" + output_name;
    
    std::ifstream file(input_file);
    std::vector<std::string> lines;
    std::string line;
    while (std::getline(file, line)) 
    {
        lines.push_back(line);
    }
    file.close();
    
    std::vector<std::string> modified_lines;
    for (const auto& line : lines) 
    {
        modified_lines.push_back(line.substr(2));
    }
    
    std::vector<std::string> final_hex_code;
    for (const auto& elem : modified_lines) 
    {
        if (elem != "") 
        {
            final_hex_code.push_back(elem);
        }
    }
       
    return 0;
}