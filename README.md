## Описание

1. Сначала мы импортируем необходимые библиотеки - Pandas и random.
2. Затем мы создаем исходный DataFrame с помощью функции pd.DataFrame(). В этом примере у нас есть столбец 'whoAmI', который содержит значения "robot" и "human".
3. Мы создаем пустой DataFrame one_hot_data, который будет использоваться для one-hot кодирования.
4. Мы получаем уникальные значения столбца 'whoAmI' с помощью метода unique().
5. Для каждого уникального значения мы создаем новый столбец в one_hot_data с помощью оператора [] и метода astype(int), который преобразует значения в целочисленный тип данных.
6. Мы устанавливаем опцию отображения таблицы с помощью метода set_option() и выводим результат с помощью метода head().

## Результат

Результат работы кода будет выглядеть следующим образом:

   human  robot
0      1      0
1      0      1
2      1      0
3      0      1
4      0      1