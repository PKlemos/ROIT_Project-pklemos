import openpyxl
from unidecode import unidecode
import re

def format_excel_file():
    # Carrega o arquivo do Excel
    workbook = openpyxl.load_workbook('..\Data\Output\CNAE_Infos.xlsx')

    # Seleciona a planilha desejada
    worksheet = workbook['data']

    def isCodeColumn(index):
        if index == 0 or index == 2 or index == 4 or index == 6 or index == 8:
            return True
        return False

    # Obtém todos os valores das células
    for row_index, row in enumerate(worksheet.iter_rows()):
        for i, cell in enumerate(row):
            formatted_cell_value = ""
            if row_index == 0:
                formatted_cell_value = unidecode(cell.value.strip()).lower()
            else:
                if isCodeColumn(i):
                    # Remove acentos e caracteres especiais da célula
                    formatted_cell_value = re.sub(
                        r'[^\w\s]', '', cell.value.strip())
                else:
                    formatted_cell_value = unidecode(cell.value.strip()).lower()
            cell.value = formatted_cell_value
    try:
        workbook.save('..\Data\Output\CNAE_Infos.xlsx')
        return "Arquivo salvo com sucesso!"
    except Exception as e:
        return f"Erro ao salvar arquivo: {e}"
format_excel_file()
