import os
import pandas as pd
import numpy as np

counter_list = []
site_hourly_reports = [x for x in os.listdir() if x.endswith(".xlsx")]
counter_files = [x for x in os.listdir() if x.endswith(".csv")]
PATH = '/Users/akinbodebams/PycharmProjects/ben'
# hourly_report_without_extension = [i.rsplit(".", 1)[0].lower() for i in site_hourly_reports]
SITE_LOCATION_DICT = {'BE6556':'Ginde',
                      'KG0093':'Akutupa',
                      'KG0107A':'Ayetoro-Kiri',
                      'NS5084':'Arikya',
                      'NS5084B': 'Arikya II',
                      'NS5085': 'Fadama',
                      'NS5088': 'Wuse I',
                      'NS5088B':'Wuse II'
                      }
# FIlES_DICT = {hourly_report_without_extension[i]: site_hourly_reports[i] for i in range(len(site_hourly_reports))}
date = input('Enter date for daily report. format: "ddmmyy".\n')


def get_hourly_report():

    file = ''
    # looping until expected input is given
    while file not in site_hourly_reports:
        global date
        for i in os.listdir(PATH):
            if i.startswith(f'{date}'):
                file = i
        if file not in site_hourly_reports:
            date = input(f'you entered "{date}", retry example "010121" for 1st of jan 2021.\n').lower()
        else:
            break
    return file


# def counter(starter):
#     df = pd.read_csv()



def file_loader(file):
    df = pd.read_excel(f'{file}')
    return df

def erlang(data):
    result = []
    for i in SITE_LOCATION_DICT:
        result.append(round(data.loc[data['RGU'] == i].Erlang.sum(), 2))
    return result

def hr_availability(data):
    result = []
    for i in SITE_LOCATION_DICT:
        result.append(round((data['RGU'].value_counts()[i])/24)* 100)
    return result

def cdr_cssr_siteavailable_average(data):
    result = {"CDR":[],"CSSR":[],"SiteAvailable":[]}
    data['CDR'] = data['CDR'].fillna(0)
    data['CSSR'] = data['CSSR'].fillna(0)
    data['SiteAvailable'] = data['SiteAvailable'].fillna(0)
    for i in SITE_LOCATION_DICT:
        result['CDR'].append(round(data.loc[data['RGU'] == i].CDR.mean(),2))
        result['CSSR'].append(round(data.loc[data['RGU'] == i].CSSR.mean(), 2))
        result['SiteAvailable'].append(round(data.loc[data['RGU'] == i].SiteAvailable.mean()))
    return result

def TCH_BLOCKING_without_zero(data):
    # data = data.replace(0, np.NaN)
    result = []
    data['TCH_Blocking'] = data['TCH_Blocking'].fillna(0)
    data.drop(data.index[data['TCH_Blocking'] == 0], inplace=True)
    for i in SITE_LOCATION_DICT:
        result.append(round(data.loc[data['RGU'] == i].TCH_Blocking.mean(), 2))

    return result

def SDCCH_Blocking_Rate(data):
    # data = data.replace(0, np.NaN)
    result = []
    data['SDCCH_Blocking_Rate'] = data['SDCCH_Blocking_Rate'].fillna(0)
    data.drop(data.index[data['SDCCH_Blocking_Rate'] == 0], inplace=True)
    for i in SITE_LOCATION_DICT:
        result.append(round(data.loc[data['RGU'] == i].SDCCH_Blocking_Rate.mean(), 2))

    return result




def sites_to_dataframe(data):
    df = pd.DataFrame(SITE_LOCATION_DICT.items(), columns=['SITE ID', 'SITE LOCATION'])
    df['ERLANG'] = [i for i in erlang(data)]
    df['TOTAL ERLANG'] =  [i for i in erlang(data)]
    df['HOUR AVAILABILITY (%)'] = [i for i in hr_availability(data)]
    df['CDR'] = cdr_cssr_siteavailable_average(data)['CDR']
    df['CSSR'] = cdr_cssr_siteavailable_average(data)['CSSR']
    df['SiteAvailable'] = cdr_cssr_siteavailable_average(data)['SiteAvailable']
    df['TCH_BLOCKING'] = [i for i in TCH_BLOCKING_without_zero(data)]
    df['SDCCH_Blocking_Rate'] = [i for i in SDCCH_Blocking_Rate(data)]
    return df

def file_to_csv(data):
    new = data.to_excel('Site_hourly_report.xlsx')
    return new



def main():
    while True:
        # hourly_report = get_hourly_report()
        df = file_loader(get_hourly_report())
        new = sites_to_dataframe(df)
        file_to_csv(new)
        break


if __name__ == "__main__":
    main()

