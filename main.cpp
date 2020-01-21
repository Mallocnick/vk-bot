#include <iostream>
#include <locale>

#include "item.hpp"
#include "odd.hpp"

using namespace std;

int main()
{
    setlocale( LC_ALL, "rus" );
    const Odd odd1( L"LG", L"M6573", 12828, 1650, Odd::internal,
                    Odd::SATA, 48, 16 ); // Создание объекта odd1 (вызов конструктора с параметрами)
    const Odd odd2; // Создание объекта odd2 (вызов конструктора по умолчанию)

    odd1.show();
    cout << endl;

    odd2.show();
    cout << endl;

    return 0;
}
