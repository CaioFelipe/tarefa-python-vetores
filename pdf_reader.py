import sys
import subprocess

try:
    import PyPDF2
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2

try:
    reader = PyPDF2.PdfReader(r"c:\Users\Admin\Desktop\PROGRAMACAO\tarefa pyhton\Estruturas_de_Dados_Python_Vetores_exercicios_1.pdf")
    with open(r"c:\Users\Admin\Desktop\PROGRAMACAO\tarefa pyhton\extract.txt", "w", encoding="utf-8") as f:
        for page in reader.pages:
            f.write(page.extract_text() + "\n")
    print("Sucesso")
except Exception as e:
    print(f"Error reading PDF: {e}")
