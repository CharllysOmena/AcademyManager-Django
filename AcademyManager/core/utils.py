from django.db.models import Q 

def achar_index_barras(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def converter_data_numero_db(pesquisa): 
    if pesquisa:
        if '/' in pesquisa: 
            indexes = achar_index_barras(pesquisa, '/') 
            dia = pesquisa[indexes[0] - 2: indexes[0]] 
            mes = pesquisa[indexes[0] + 1: indexes[0] + 3] 
            if len(indexes) > 1: 
                ano = pesquisa[indexes[1] + 1 : indexes[1] + 5]
                data_db = f'{ano}-{mes}-{dia}' 
            else:
                if mes == '': 
                    data_db = f'-{dia}' 
                else:
                    data_db = f'-{mes}-{dia}'
            return data_db 
    return pesquisa 

def montador_de_filtro(cls, campos_desejados, pesquisa):
    campos_pesquisa = []
    campos_do_modelo = cls._meta.get_fields()
    for desejado in campos_desejados : 
        for campo in campos_do_modelo: 
            if campo.name == desejado: 
                campos_pesquisa.append(campo)  
    filtro = None
    for campo in campos_pesquisa:
        if not campo.is_relation : 
            if filtro == None:
                filtro = (Q(('%s__icontains' % campo.name, pesquisa)))
                if 'data_' in campo.name: 
                    filtro = (Q(('%s__icontains' % campo.name, converter_data_numero_db(pesquisa))))
            else:
                if 'data_' in campo.name:
                    filtro.add(Q(('%s__icontains' % campo.name, converter_data_numero_db(pesquisa))), Q.OR)
                else: 
                    filtro.add(Q(('%s__icontains' % campo.name, pesquisa)), Q.OR)             
    return filtro 
