import os

class RecursiveFileSystemIterator:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def __iter__(self):
        # Начинаем обход с корневого каталога
        yield from self._walk(self.root_directory)

    def _walk(self, directory):
        # Возвращаем текущий каталог
        yield directory
        
        # Получаем список подкаталогов и файлов
        dirnames, filenames = [], []
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                dirnames.append(full_path)
            else:
                filenames.append(full_path)

        # Сначала возвращаем все подкаталоги
        for dirname in dirnames:
            yield from self._walk(dirname)  # Рекурсивный вызов для подкаталогов
            
        # Наконец, возвращаем все файлы
        for filename in filenames:
            yield filename

# Пример использования
if __name__ == "__main__":
    root_dir = "/path/to/your/directory"  # Замените на нужный путь
    iterator = RecursiveFileSystemIterator(root_dir)

    for item in iterator:
        print(item)
