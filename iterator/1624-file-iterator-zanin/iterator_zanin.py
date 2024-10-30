import os

class FileSystemIterator:
    def __init__(self, root_directory):
        self.root_directory = root_directory

    def __iter__(self):
        # Используем yield from для делегирования итерации в метод _walk
        yield from self._walk(self.root_directory)

    def _walk(self, directory):
        # os.walk возвращает кортежи (текущий каталог, подкаталоги, файлы)
        for dirpath, dirnames, filenames in os.walk(directory):
            print('----------------------------------------')

            # Сначала возвращаем текущий каталог
            yield dirpath
            print('')
            
            # Затем возвращаем все подкаталоги
            for dirname in dirnames:
                yield os.path.join(dirpath, dirname)
            
            # Наконец, возвращаем все файлы
            for filename in filenames:
                yield os.path.join(dirpath, filename)

# Пример использования
if __name__ == "__main__":
    root_dir = "../../IB"  # Замените на нужный путь
    iterator = FileSystemIterator(root_dir)

    for item in iterator:
        print(item)