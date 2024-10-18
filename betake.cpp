#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Function to calculate simple interest
double calculateSimpleInterest(double principal, int period) {
    const double rate = 0.10; // 10% fixed rate
    return principal * rate * period;
}

// Function to perform string operations
class StringOperations {
public:
    static string copy(const string& str) {
        return str;
    }

    static string reverse(const string& str) {
        string reversed = str;
        std::reverse(reversed.begin(), reversed.end());
        return reversed;
    }

    static string toUppercase(const string& str) {
        string upper = str;
        transform(upper.begin(), upper.end(), upper.begin(), ::toupper);
        return upper;
    }

    static string toLowercase(const string& str) {
        string lower = str;
        transform(lower.begin(), lower.end(), lower.begin(), ::tolower);
        return lower;
    }

    static bool compare(const string& str1, const string& str2) {
        return str1 == str2;
    }
};

int main() {
    double loanAmount;
    int loanPeriod;

    // Get loan amount and period from user
    cout << "Enter loan amount: ";
    cin >> loanAmount;
    cout << "Enter loan period (in years): ";
    cin >> loanPeriod;

    // Calculate and display simple interest
    double interest = calculateSimpleInterest(loanAmount, loanPeriod);
    cout << "Simple Interest: " << interest << endl;

    // String operations
    string inputString;
    cout << "Enter a string for operations: ";
    cin.ignore(); // Clear newline from previous input
    getline(cin, inputString);

    cout << "Copy: " << StringOperations::copy(inputString) << endl;
    cout << "Reverse: " << StringOperations::reverse(inputString) << endl;
    cout << "Uppercase: " << StringOperations::toUppercase(inputString) << endl;
    cout << "Lowercase: " << StringOperations::toLowercase(inputString) << endl;

    string compareString;
    cout << "Enter another string to compare: ";
    getline(cin, compareString);
    cout << "Strings are " << (StringOperations::compare(inputString, compareString) ? "equal" : "not equal") << endl;

    return 0;
}