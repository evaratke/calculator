#include <iostream>
using namespace std;

int main() {
    int size;
    cout << "Enter array size: ";
    cin >> size;
    
    int numbers[size];
    cout << "Enter array elements: ";
    for (int index = 0; index < size; index++) {
        cin >> numbers[index];
    }
    
    int totalSum = 0;
    long long totalProduct = 1;
    
    for (int index = 0; index < size; index++) {
        totalSum += numbers[index];
        totalProduct *= numbers[index];
    }
    
    cout << "Sum: " << totalSum << endl;
    cout << "Product: " << totalProduct << endl;
    
    return 0;
}