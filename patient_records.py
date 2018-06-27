
TEST_LAYOUT = [
    ['S1','036-N','040-N'],
    ['S2','036-1','040-1'],
    ['S3','036-2','040-2'],
    ['S4','036-M','040-M']
    ]
    
TEST_DATA = [
    [0.43, 0.23, 0.5],
    [0.21, 0.7, 0.25],
    [0.1, 0.002, 0.32],
    [0.08, 0.006, 0.05]
    ]

def get_patient_records(layout, data):
    dict_patientdata = {}
    for rowindex, row in enumerate(layout):
        for columnindex, item in enumerate(row):
            part_item = item.partition('-')
            if part_item[1] == '-':
                if part_item[0] not in patient_data:
                    dict_patientdata[part_item[0]]={}
        
                dict_patientdata[part_item[0]][part_item[2]] = data[rowindex][columnindex]
        
        
    for key in dict_patientdata:
        
        patienttuple = (dict_patientdata[key]['1'],
                        dict_patientdata[key]['2'],
                        dict_patientdata[key]['N'],
                        dict_patientdata[key]['M'])
        
        dict_patientdata[key] = patienttuple
        
    return dict_patientdata


patientrecords = get_patient_records(TEST_LAYOUT,TEST_DATA)

print(patientrecords['036'])
