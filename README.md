# youtext
Приложение для генерации статей по видеороликам из YouTube.

## Стек программы
[ChatGPT](https://platform.openai.com/docs/guides/gpt/chat-completions-api), [Whisper](https://github.com/openai/whisper), Django, JavaScript.

## Как запустить проект
1. Требуется сделать git clone проекта;
2. Прописать в терминале docker-compose build;
3. Прописать в терминале docker-compose app;
4. Подождать загрузки модели [Whisper](https://github.com/openai/whisper) для распознавания речи, загрузки русского языка для исправления орфографических ошибок;
5. Проект будет доступен по адресу [http://localhost:8000/](http://localhost:8000/)
название, сделать докер compose build, потом докер compose app. Компиляция может занять более 15 минут. Сделать скриншоты 1 страницы, сделать скриншоты 2 страницы (то есть показать, как работает)
## Дизайн проекта
![Палитра проекта](https://i.imgur.com/BGu3mqK.png)
