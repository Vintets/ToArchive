
# Проект  ToArchive

---------------------------------------------------------

## Description

Added date to name file and added file to archive.


## Зависимости Requirements

![Python version](https://img.shields.io/badge/python-3.12%2B-blue?logo=python&logoColor=ffdd54)
> Требуется Python 3.12+

Установка зависимостей:
```sh
pip3 install -r requirements.txt
```
Используется
```py7zr```


## Конфигурирование Configuration

Optional config file in file folder!
`config.toml`

```toml
# CONFIGURATION
[main]
path_to_archive = 'Архивы'
archive_name = 'supertest'

[filename]
path_to_archive = 'Архивы'
archive_name = 'filename'
...
```
``path_to_archive`` : Path to archive (foldername)  
``archive_name`` : New archive name (is empty - default = filename)  
``[main]`` : default section  
``[filename]`` : section -  rule for filename    



## Usage

### Запуск

```bash
python ToArchive.py <file>
```
- аргумент `file` передаётся путь к файлу


____

## License

![License](https://img.shields.io/badge/license-MIT-green)  

/*******************************************************
 * Copyright 2026 Vintets <programmer@vintets.ru> - All Rights Reserved
 * Written by Vintets <programmer@vintets.ru>, July 2026
*******************************************************/  
