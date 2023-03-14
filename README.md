# Reddit-Api-Test
Тест Reddit API с помощью python и robot framework

Шаги:
1. Обязательно создать App на реддите по ссылке https://www.reddit.com/prefs/apps (я делал for personal use)
2. В файл variables.py ввести App ID и App Secret - без них нет доступа к api
3. В файл variables.py ввести Username и Password от Reddit - аналогично нет доступа к api без них
4. По желанию в файле variables.py ввести свой POST_ID (сейчас введён мой)
5. Для изменения запроса поиска треда изменить search_key в variables.py

После первой удачной попытки авторизации токен сохраняется в файле token
Пункты 2 и 3 нужны для авторизации OAuth2
