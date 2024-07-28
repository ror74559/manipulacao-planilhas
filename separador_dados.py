import pandas as pd

def process_planilha(input_file_path, output_file_path):
    # Carregar a planilha
    df = pd.read_excel(input_file_path)

    # Selecionar colunas que contêm "Marks"
    marks_columns = [col for col in df.columns if 'Marks' in col]
    marks_columns.insert(0,'Roll No')
    marks_columns.pop(marks_columns.index('Total Marks'))
    marks_columns.append('Total Marks')

    # Criar uma nova planilha conforme especificado
    # Inicializar a primeira coluna em branco
    new_marks_df = pd.DataFrame()
    new_marks_df[' '] = ''

    # Atualizar os números das colunas Marks e adicioná-las à nova planilha
    for i, col in enumerate(marks_columns, start=1):
        new_marks_df[str(i)] = df[col].astype(int)

    # Salvar a nova planilha com as modificações
    new_marks_df.to_excel(output_file_path, index=False)

# Caminho do arquivo de entrada e de saída
input_file_path = 'AMERF_6_ano_2_bimestre_of.xls' #planilha gerada pelo app EVABEE
output_file_path = 'AMERF_o_6_Ano_sep.xlsx'

# Processar a planilha
process_planilha(input_file_path, output_file_path)
print('finalizado')
