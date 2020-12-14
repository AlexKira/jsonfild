Работа с myscript.py

1. Установить библиотеку Pandas.
2. Зайти в папку event и запустить myscript.py.
3. При запуске появится запром на добавление JSON файла
4. После добавления, скрипт проверить и добавит необходимые значения в словарь JSON и выведет отформатированый фаил new_file.json.

Пример:
           Input names Json: (1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json)
                            event  ... environment_id
                0  label_selected  ...              2
                1  label_selected  ...              2
                2  label_selected  ...              2
                3  label_selected  ...              2

                [4 rows x 4 columns]
           Input names Json: (1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json)
                            event  ... environment_id
                0  label_selected  ...              2
                1  label_selected  ...              2
                2  label_selected  ...              2
                3  label_selected  ...              2

                [4 rows x 4 columns]
                Empty DataFrame
                Columns: []
                Index: []

        
Schema JSON.
1. Установить библиотеку jsonschema.
2. Зайти в папку schema и запустить generater.py.
3. При запуске появится запроc на добавление Schema JSON

 Пример:
 
  Input JSON schema: sleep_created.schema
'json_data' is not of type 'object'

Failed validating 'type' in schema:
    {'$schema': 'http://json-schema.org/schema#',
     'properties': {'activity_type': {'type': 'string'},
                    'finish_time': {'type': 'string'},
                    'info': {'items': {'properties': {'type': {'type': 'string'},
                                                      'value': {'type': 'number'}},
                                       'required': ['type', 'value'],
                                       'type': 'object'},
                             'type': 'array'},
                    'phases_info': {'items': {'properties': {'duration': {'type': 'number'},
                                                             'percent': {'type': 'number'},
                                                             'type': {'type': 'string'}},
                                              'required': ['duration',
                                                           'percent',
                                                           'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'points': {'items': {'properties': {'x_date': {'type': 'string'},
                                                        'y_value': {'type': 'number'}},
                                         'required': ['x_date', 'y_value'],
                                         'type': 'object'},
                               'type': 'array'},
                    'source': {'type': 'string'},
                    'time_start': {'type': 'string'},
                    'timestamp': {'type': 'string'},
                    'type_ranges': {'items': {'properties': {'date': {'type': 'string'},
                                                             'type': {'type': 'string'}},
                                              'required': ['date', 'type'],
                                              'type': 'object'},
                                    'type': 'array'},
                    'unique_id': {'type': 'string'}},
     'required': ['source',
                  'timestamp',
                  'finish_time',
                  'activity_type',
                  'time_start',
                  'unique_id'],
     'type': 'object'}

On instance:
    'json_data'
(False, 'Given JSON data is InValid')

