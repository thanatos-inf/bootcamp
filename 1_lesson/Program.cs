// Наибольший общий делитель (НОД) и Наименьшее общее кратное (НОК)

int n = 140;
int m = 175;
int result = m * n;
while (n != m)
{
    if (n > m)
        n = n - m;
    else
        m = m - n;
    
    Console.WriteLine(n);
    Console.WriteLine(m);
    Console.WriteLine();
}

Console.WriteLine(result / m);
