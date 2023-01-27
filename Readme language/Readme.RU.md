<!DOCTYPE html>
<html>
  <head>
      </head>
  <body>
    <h1>Загрузчик изображений Reddit</h1>
    <p>Эта программа использует API Reddit для загрузки изображений из указанного подраздела.</p>
    <h2>Как использовать</h2>
    <ol>
      <li>Введите имя подраздела, из которого вы хотите загрузить изображения</li>
      <li>Программа создаст папку загрузки в текущем каталоге с именем подраздела</li>
      <li>Изображения будут загружены в эту папку</li>
    </ol>
    <h2>Зависимости</h2>
    <ul>
      <li>praw</li>
      <li>запросы</li>
    </ul>
    <h2>Примечания</h2>
    <p>Вы должны иметь действительный client_id и client_secret для использования API Reddit (или использовать мой api, который уже присутствует)</p>
    <h2>Пример</h2>
        <pre>
subreddit_name = input("Введите имя подраздела: ")
download_path = f'./downloads/reddit/{subreddit_name}'
download_images(subreddit_name, download_path)
        </pre>
  </body>
</html>
