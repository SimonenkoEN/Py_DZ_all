import os
import json
import csv
import pickle


def get_data(json_file: str, csv_file: str, pickle_file: str, path_: str = None) -> None:
    if path_ is None:
        path_ = os.getcwd()
    data = []
    for dir_path, dir_name, file_name in os.walk(path_):
        d_size = 0
        for file in file_name:
            file_path = os.path.join(dir_path, file)
            tmp_size = os.path.getsize(file_path)
            d_size += tmp_size
            data.append({'parent_dir': dir_path.split('\\')[-1], 
                         'object': file,
                         'type': '<file>', 
                         'size': tmp_size})
        data.append({'parent_dir': dir_path.split('\\')[-2],
                     'object': dir_path.split('\\')[-1], 
                     'type': '<dir>', 
                     'size': d_size})

    with (open(json_file, "w", encoding='utf-8') as jf,
          open(csv_file,'w', newline='', encoding='utf-8') as cf,
          open(pickle_file, 'wb') as pf
    ):
        json.dump(data, jf, ensure_ascii=False, indent=2)

        csv_write = csv.DictWriter(cf, fieldnames=['parent_dir', 'object', 'type', 'size'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(data)
        
        pickle.dump(data, pf)


if __name__=="__main__":
    get_data('data.json', 'data.csv', 'data.pickle')