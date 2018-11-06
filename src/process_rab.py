import pandas as pd


# Le o arquivo do RAB
rab = pd.read_csv('../data/base_dados_rab.csv',header=1,
        encoding='latin-1',
        usecols=["CATEGORIA","MODELO","CLASSE","PMD","TRIP_MIN",
                 "PAX_MAX","TIPO_ICAO","ANO_FAB","CD_INTERDICAO"]);
print(f'Total Registros = {rab.shape[0]:d}')

# Elimina qualquer registro que nao seja Normal
rab = rab.drop(rab[rab["CD_INTERDICAO"] != "N"].index)
print(f'Registros Normais = {rab.shape[0]:d}')

# Elimina helicopteros
rab = rab.drop(rab[rab["CLASSE"].astype(str).str[0] == "H"].index)
print(f'Registros Avioes = {rab.shape[0]:d}')

# Elimina gliders
rab = rab.drop(rab[rab["CLASSE"].astype(str).str[1] == "0"].index)
print(f'Registros Avioes Com Motor = {rab.shape[0]:d}')



'''
rab = rab.fillna(0)
rab['ANO_FAB'] = rab.ANO_FAB.astype(int)
rab['TRIP_MIN'] = rab.TRIP_MIN.astype(int)
rab['PAX_MAX'] = rab.PAX_MAX.astype(int)
rab['PMD'] = rab.PMD.astype(int)
'''

#s = rab['TIPO_ICAO'].value_counts().sort_values(ascending=False).head(4)
#rab = pd.DataFrame({'TIPO_ICAO':s.index}).merge(rab, how='left')

print(rab['MODELO'].value_counts().head(10))


#print(rab.groupby("TIPO_ICAO")["MODELO"].value_counts())

