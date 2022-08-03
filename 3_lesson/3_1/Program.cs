//Cортировка выбором/заменой

Console.WriteLine("Введите количество элементов массива: ");
int n = Convert.ToInt32(Console.ReadLine());
// Заполнение массива
int[] array = new int[n];
for (int i = 0; i < n; i++)
{
    Console.Write("Введите число: ");
    array[i] = Convert.ToInt32(Console.ReadLine());
}
Console.WriteLine("Начальный массив: [" + string.Join(", ", array) + "]");
// Сортировка
for (int i = 0; i < n - 1; i++)
{
    int min_index = i;
    for (int j = i+1; j < n; j++)
    {
        if (array[j] < array[min_index]) min_index = j;
    }
    int temp;
    temp = array[min_index];
    array[min_index] = array[i];
    array[i] = temp;
}
Console.WriteLine("Отсортированный массив: [" + string.Join(", ", array) + "]");