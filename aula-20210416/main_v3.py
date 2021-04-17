import csv

if __name__ == '__main__':

    with open("funcionarios.csv", "r") as _file:
        csv_reader = csv.DictReader(_file, delimiter=';')

        headers = csv_reader.fieldnames

        for item in csv_reader:
            texto = f"""
        {headers[0].upper()}    : {item['id']}
        {headers[1].upper()}    : {item['name']}
        {headers[2].upper()}    : {item['salary']}
        {headers[3].upper()}    : {item['sector']}
        {headers[4].upper()}    : {item['bonus']}
    """
            print(texto)
