import subprocess
import sys

def copy_image_to_clipboard(image_path):
    """使用 AppleScript 将图片内容复制到剪切板"""
    apple_script = f'''
    set the clipboard to (read (POSIX file "{image_path}") as JPEG picture)
    '''
    process = subprocess.Popen(['osascript', '-e', apple_script], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.communicate()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        image_path = sys.argv[1]
        copy_image_to_clipboard(image_path)

