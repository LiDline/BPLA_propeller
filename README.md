# BPLA

Здесь представлена небольшая работа по исследованию винта, лопасти которого представляют собой профиль крыла. Подробнее ознакомиться можно [тут](https://hedgedoc.auto-sys.su/px_bhyu2TTapW_uVCvvQzA?both).

## 1 Состав проекта

1. Папка "calculation results":
- "BPLA, series 1 - инт.csv" - проинтерполированные результаты расчётов.
- BPLA, series 1.csv - результаты расчётов (Используемый пакет: сетка - Ansys Mesh, решатель - Fluent).
- interpolation.py - скрипт интерполяции (по сечениям).
2. Папка func, где лежат используемые функции.
- cross_points_f.py - поиск координаты точки пересечения при заданной силе тяги.
- cross_points_mx_w.py - поиск координаты точки пересечения при заданных оборотах винта.
- data_for_plot.py - создание таблицы с объектами класса график.
- prepare_data.py - подготовка данных для графиков.
- graph.py - методы отрисовки графика.
- tabs.py - наполненние dashboard.
3. app.py - приложение.
4. graphs.ipynb - черновик с графиками.

## 2 Запуск программы
Запуск осуществляется в черновике "graphs.ipynb", либо "app.py" - dashboard.

## 3 Используемые библиотеки
Используемые библиотеки:
- plotly;
- datetime;
- numpy;
- pandas;
- dash;
- dash_bootstrap. 
____
Все используемые библиотеки указаны в файле requirements.txt. Для быстрой установки отсутствующих библиотек в терминале выполните: 
```
pip install -r requirements.txt
```