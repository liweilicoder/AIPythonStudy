import os
import ipywidgets as widgets
from IPython.display import display

def list_files_in_directory(directory='.'):
    """
    Lists all non-hidden files in the specified directory.

    Args:
        directory (str): The directory to list files from. Defaults to the current working directory.
    """
    try:
        files = [f for f in os.listdir(directory) if (not f.startswith('.') and not f.startswith('_'))]
        for f in files:
            print(f)

        return files

    except Exception as e:
        print(f"An error occurred while listing files: {e}")


def upload_txt_file(directory='.'):
    """
    Uploads a text file and saves it to the specified directory.

    Args:
        directory (str): The directory where the uploaded file will be saved.
    """
    # 创建文件上传小部件，只接受 .txt 文件，且不允许同时上传多个文件
    upload_widget = widgets.FileUpload(
        accept='.txt',  # Accept text files only
        multiple=False  # Do not allow multiple uploads
    )

    # 创建输出小部件，用于显示上传结果和错误信息
    output = widgets.Output()

    # Function to handle file upload
    # 定义处理文件上传事件的回调函数
    def handle_upload(change):
        # 使用输出小部件的上下文管理器，确保所有输出都显示在指定区域
        with output:
            # 清除之前的输出内容
            output.clear_output()
            # Read the file content
            # 从上传的小部件中获取文件内容（字节形式）
            content = upload_widget.value[0]['content']
            # 获取上传的文件名
            name = upload_widget.value[0]['name']
            # 计算文件大小（以 KB 为单位）
            size_in_kb = len(content) / 1024

            # 检查文件大小是否超过 3KB
            if size_in_kb > 10:
                # 文件过大，显示错误提示并返回
                print(f"Your file is too large, please upload a file that doesn't exceed 10KB.")
                return

            # Save the file to the specified directory
            # 以二进制写入模式打开文件，准备保存上传的内容
            filepath = os.path.join(directory, name)

            with open(filepath, 'wb') as f:
                # 将文件内容写入磁盘
                f.write(content)
            # Confirm the file has been saved
            # 显示上传成功的提示信息
            print(f"The {name} file has been uploaded.")

    # Attach the file upload event to the handler function
    # 将上传小部件的 'value' 变化事件绑定到处理函数
    upload_widget.observe(handle_upload, names='value')

    # 在 Jupyter Notebook 中显示上传小部件和输出区域
    display(upload_widget, output)