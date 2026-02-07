/*********************************
 * Автор:     Иккерт А.С.        *
 * Название:  Обработка массивов *
 * Вариант:   7                  *
 *********************************/



#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    
    // Ввод размера матрицы и значения k
    cout << "Enter the size of the square matrix: ";
    cin >> n;
    
    cout << "Enter k value (from 1 to " << n << "): ";
    cin >> k;
    
    // Корректировка k
    k = k - 1;
    
    // создаем матрицу
    vector<vector<int>> V(n, vector<int>(n));
    
    cout << "Enter matrix elements " << n << "x" << n << ":" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> V[i][j];
        }
    }
    
    // вывод оригинальной матрицы
    cout << "\nOriginal matrix V:" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << V[i][j] << " ";
        }
        cout << endl;
    }
    
    // Создаем новую матрицу
    vector<vector<int>> result(n - 1, vector<int>(n - 1));
    
    int new_i = 0;
    for (int i = 0; i < n; i++) {
        if (i == k) continue; // Пропускаем k строку
        
        int new_j = 0;
        for (int j = 0; j < n; j++) {
            if (j == k) continue; // Пропускаем k столбец
            
            result[new_i][new_j] = V[i][j];
            new_j++;
        }
        new_i++;
    }
    
    // Вывод результатов
    cout << "\nMatrix after removing " << k + 1 << "-th row and " << k + 1 << "-th column:" << endl;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - 1; j++) {
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    
    return 0;
}