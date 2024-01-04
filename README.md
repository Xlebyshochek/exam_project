Аннотация к проекту:

Общее описание: Проект представляет собой автоматизированные тесты для взаимодействия с веб-сайтом https://www.fila.com/. Тесты написаны с использованием библиотеки Selenium WebDriver и фреймворка для тестирования PyTest. Вся функциональность разделена на несколько страниц: MainPage, ProductsPage, ProductPage, CartPage, и CheckoutPage, каждая из которых представляет определенный функциональный блок.

Структура проекта:

Базовый класс (base_class.py):

Base: Основной класс, который содержит общие методы и свойства для взаимодействия с веб-страницей. Включает методы для проверки соответствия названия, цены, размера, цвета, и текущего URL ожидаемым значениям. Также есть метод для создания скриншота страницы.
Страницы (main_page.py, products_page.py, product_page.py, cart_page.py, checkout_page.py):

MainPage: Содержит методы для навигации к странице с продуктами и осуществления различных действий на главной странице, таких как закрытие всплывающего окна с предложением.
ProductsPage: Реализует методы для фильтрации продуктов по различным параметрам, таким как цвет, размер, тип, цена и пол. Также предоставляет метод для выбора продукта после применения фильтров.
ProductPage: Содержит методы для выбора размера продукта, добавления его в корзину и перехода в корзину для оформления заказа.
CartPage: Предоставляет методы для навигации на страницу оформления заказа (checkout) из корзины.
CheckoutPage: Реализует методы для заполнения информации на странице оформления заказа.
Тестовый сценарий (test_project.py):

test_buy_product: Тестирование полного цикла оформления заказа. Включает в себя последовательность действий: переход на страницу продуктов, фильтрация и выбор продукта, добавление его в корзину и оформление заказа.
Помощники (fixtures):

notification: Фикстура PyTest для вывода сообщений перед и после выполнения тестов.
Запуск и зависимости:

Проект использует язык программирования Python и библиотеки Selenium и PyTest.
Для управления браузером используется Chrome WebDriver.
Для запуска тестов необходимо установить Python, библиотеки Selenium и PyTest, а также совместимую версию браузера и его WebDriver.
Замечания:

Проект содержит довольно подробные логи и сообщения об успешности/неуспешности выполнения каждого шага, что облегчает отладку и понимание процесса тестирования.
Важно поддерживать актуальность WebDriver и библиотек для Selenium и PyTest для обеспечения совместимости с новыми версиями браузеров и исправлением возможных ошибок.
Тестовый сценарий test_buy_product может быть дополнен новыми шагами в зависимости от требований и возможностей сайта.
