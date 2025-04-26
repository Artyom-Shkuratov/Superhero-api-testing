# Superhero API Testing
## Описание проекта
### В проекте реализована функция get_tallest_hero_by_gender_and_work(gender, has_job), которая:

### Делает GET-запрос API:
https://akabab.github.io/superhero-api/api/all.json

1-Фильтрует супергероев по полу (Male/Female) и наличию работы (True/False)

2-Среди отфильтрованных героев находит самого высокого и возвращает его имя

   - Если по заданным условиям героев нет — возвращает None

## Описание работы функции
### Функция get_tallest_hero_by_gender_and_work:

- Получает все данные о героях через API-запрос
- Проверяет успешность ответа от сервера (status_code == 200)
- Фильтрует героев по указанному полу и наличию работы:
- gender — строка "Male" или "Female"
- has_job — булево значение (True или False)
- Выбирает героя с максимальным ростом
- Возвращает имя самого высокого героя, если такой найден
- Если подходящих героев нет — возвращает None

## Описание тестов


### test_get_response_status_code_is_200
- Проверяет, что API возвращает код ответа 200 OK


### test_get_tallest_hero_returns_valid_name
- Проверяет, что функция возвращает строку с именем героя для разных комбинаций пола и наличия работы

### test_height_list_short_returns_none
- Проверяет, что если в данных у героя нет роста, функция возвращает None

### test_empty_height_string_returns_none
- Проверяет, что если строка роста пустая, функция корректно возвращает None

### test_invalid_gender_returns_none
- Проверяет, что если пол указан некорректно (UnknownGender), функция возвращает None

### test_number_instead_of_gender_returns_none
- Проверяет, что если в пол передано число вместо строки, функция возвращает None

### test_empty_gender_returns_none
- Проверяет, что если передать пустую строку вместо пола, результат будет None

### test_non_boolean_has_job_returns_none
- Проверяет, что если в параметр has_job передано не булевое значение (например, строка "yes"), функция вернёт None

### test_null_gender_returns_none
- Проверяет, что при пустом значении пола и неправильном has_job результат будет None

