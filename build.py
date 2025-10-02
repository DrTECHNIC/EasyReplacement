import os
import sys
import subprocess
import platform
import shutil


def install_dependencies():
    """Устанавливает необходимые зависимости для сборки."""
    dependencies = ['pyinstaller', 'pillow']
    for dep in dependencies:
        try:
            if dep == 'pillow':
                import PIL
            elif dep == 'pyinstaller':
                import PyInstaller
            print(f"{dep} уже установлен")
        except ImportError:
            print(f"Установка {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
            print(f"{dep} успешно установлен")


def copy_public_folder():
    """Копирует папку public в директорию сборки если она существует."""
    if os.path.exists("public"):
        if not os.path.exists("build_temp/public"):
            os.makedirs("build_temp/public", exist_ok=True)
        for item in os.listdir("public"):
            src_path = os.path.join("public", item)
            dst_path = os.path.join("build_temp/public", item)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
                print(f"Скопирован файл: {item}")
        print("Папка public скопирована в build_temp")
    else:
        print("Папка public не найдена, сборка продолжится без иконки")


def build_executable():
    """Собирает проект в исполняемый файл."""
    system = platform.system()
    if system == "Windows":
        output_name = "cipher_tool.exe"
        separator = ";"
    else:
        output_name = "cipher_tool"
        separator = ":"
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", output_name.replace('.exe', ''),
        "--distpath", ".",
        "--workpath", "build_temp",
        "--specpath", "build_temp",
    ]
    if os.path.exists("public"):
        cmd.extend(["--add-data", f"public{separator}public"])
    ico_path = "icon.ico"
    png_path = "public/icon.png"
    if os.path.exists(ico_path):
        cmd.extend(["--icon", ico_path])
        print(f"Иконка для EXE: {ico_path}")
    elif os.path.exists(png_path):
        cmd.extend(["--icon", png_path])
        print(f"Иконка для EXE (из PNG): {png_path}")
    else:
        print("Файл иконки не найден, EXE будет со стандартной иконкой")
    cmd.append("main.py")
    print("Запуск сборки...")
    try:
        subprocess.check_call(cmd)
        print(f"Сборка завершена! Исполняемый файл: {output_name}")
        cleanup()
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при сборке: {e}")
        print("Убедитесь, что папка public существует и содержит файл icon.png")
        print("Или установите Pillow для конвертации PNG в ICO: pip install pillow")
        sys.exit(1)


def cleanup():
    """Удаляет временные файлы после сборки."""
    temp_dirs = ["build_temp"]
    for temp_dir in temp_dirs:
        if os.path.exists(temp_dir):
            try:
                shutil.rmtree(temp_dir)
                print(f"Удалена временная директория: {temp_dir}")
            except Exception as e:
                print(f"Ошибка при удалении {temp_dir}: {e}")
    spec_file = "cipher_tool.spec"
    if os.path.exists(spec_file):
        try:
            os.remove(spec_file)
            print(f"Удален файл: {spec_file}")
        except Exception as e:
            print(f"Ошибка при удалении {spec_file}: {e}")


def main():
    """Основная функция процесса сборки."""
    print("Начало процесса сборки...")
    if not os.path.exists("public"):
        os.makedirs("public")
        print("Создана папка 'public' для ресурсов")
        print("Пожалуйста, поместите файл icon.png в папку 'public'")
        return
    icon_png_path = "./public/icon.png"
    if not os.path.exists(icon_png_path):
        print(f"ВНИМАНИЕ: Файл иконки PNG не найден: {icon_png_path}")
        print("Приложение будет без иконки в окне.")
    icon_ico_path = "icon.ico"
    if not os.path.exists(icon_ico_path):
        print(f"ВНИМАНИЕ: Файл иконки ICO не найден: {icon_ico_path}")
        print("Будет использован PNG файл с автоматической конвертацией в ICO")
        print("Для этого требуется установленный Pillow")
    if not os.path.exists("build_temp"):
        os.makedirs("build_temp")
    copy_public_folder()
    install_dependencies()
    build_executable()
    print("Сборка завершена успешно!")


if __name__ == "__main__":
    main()
