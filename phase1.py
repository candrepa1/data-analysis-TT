import pandas as pd

# https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/PERMISOS-EMISIONES-ATMOSFERICAS-CORPOBOYACA/mnk6-hfcu/about_data
df = pd.read_csv('PERMISOS_EMISIONES_ATMOSFERICAS_CORPOBOYACA_20240323.csv')

# pandas stores string pointers as objects given its length variability

#df['munin'] = df['munin'].astype(str) 
#df['vereda'] = df['vereda'].astype(str) 
#df['tipo_fuente'] = df['tipo_fuente'].astype(str)
#df['equi_control'] = df['equi_control'].astype(str)
#df['tipo_activ'] = df['tipo_activ'].astype(str)
#df['proceso'] = df['proceso'].astype(str)
df['fecha_otro'] = pd.to_datetime(df['fecha_otro'])
df['fecha_ven'] = pd.to_datetime(df['fecha_ven'])
#df['vigente'] = df['vigente'].astype(str)
#df['cont_evaluad'] = df['cont_evaluad'].astype(str)
#df['tipo_comb'] = df['tipo_comb'].astype(str)
#df['estudio'] = df['estudio'].astype(str)
#df['tit_minero'] = df['tit_minero'].astype(str)
#df['observacion'] = df['observacion'].astype(str)

print(df.dtypes)

def getMissingValuePercentage():
    columnsPercentage = []
    for columnName in df.columns:
        percentage = (pd.isna(df[columnName]).sum() * 100) / len(df.index)
        if percentage:
            columnsPercentage.append({'columnName': columnName, 'percentage': percentage })
    print(f'There are {len(columnsPercentage)} columns with missing values, out of {len(df.columns)} columns')
    return sorted(columnsPercentage, key=lambda x: x['percentage'], reverse=True)

def reviewColumnUniqueValues(columnName):
    print(df[columnName].unique())

