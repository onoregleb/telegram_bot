## Подключение Google Sheets API и Google Drive API к вашему проекту и создание учетных данных

### Шаг 1: Создайте проект в Google Cloud Console
1. Перейдите на [Google Cloud Console](https://console.cloud.google.com/).
2. Войдите в аккаунт Google (если вы еще не вошли).
3. Нажмите **Select a Project** в верхней части страницы и выберите **New Project**.
4. Укажите название проекта (например, **Telegram Feedback Bot**) и нажмите **Create** (Создать).

### Шаг 2: Включите Google Sheets API и Google Drive API
1. В выбранном проекте перейдите в раздел **API & Services > Library**.
2. В строке поиска введите **Google Sheets API** и нажмите на него.
3. Нажмите **Enable**, чтобы активировать API.
4. Повторите тот же процесс для **Google Drive API**.

### Шаг 3: Создайте учетные данные (credentials)
1. Перейдите в раздел **API & Services > Credentials**.
2. Нажмите **Create Credentials** и выберите **Service Account**.
3. Укажите название учетной записи службы (например, **Telegram Bot Service Account**) и нажмите **Create and Continue**.
4. На шаге 2 (Grant this service account access to project) нажмите **Continue** без добавления ролей.
5. На шаге 3 (Grant users access to this service account) нажмите **Done**.

### Шаг 4: Создание JSON-файла с ключами
1. В разделе **Credentials** найдите созданную учетную запись службы и нажмите на ее название.
2. Перейдите во вкладку **Keys** и нажмите **Add Key > Create New Key**.
3. Выберите формат **JSON** и нажмите **Create**. JSON-файл с ключами будет скачан на ваш компьютер.

### Шаг 5: Настройте доступ к Google Таблице
1. Откройте вашу Google Таблицу и нажмите **Настройки доступа**.
2. Скопируйте email адрес учетной записи службы из JSON-файла (ищите поле `"client_email"`).
3. Вставьте этот email адрес в поле добавления пользователей и предоставьте права **Editor** (Редактор).

## Создание бота в Telegram

### Шаг 1: Создайте бота через BotFather
1. Откройте Telegram и найдите @BotFather.
2. Отправьте команду **/start**, чтобы начать работу с BotFather.
3. Используйте команду **/newbot** для создания нового бота.
4. Введите имя для вашего бота (например, **FeedbackBot**).
5. Введите уникальное имя пользователя для бота (например, **feedback_bot**), которое должно заканчиваться на **bot** (например, **feedback_bot**).
6. После создания бота BotFather отправит вам токен API, который выглядит как строка, например, `123456789:ABCDefghIJKlmnoPQRstuVWxyZ`. Сохраните этот токен, он понадобится для подключения бота к вашему коду.

