import csv

class MockRun:
    records: dict = {}
    output_path: str

    def __init__(self, output_path:str) -> None:
        self.output_path = output_path

    def get_max_record_len(self):
        max_len = 0
        for k in self.records.keys():
            record_len = len(self.records[k])
            if max_len < record_len:
                max_len = record_len
        return max_len

    def log(self, key:str, value) -> None:
        if key not in self.records: # if we have not seen this key before
            self.records[key] = [] # initialize an empty list
        self.records[key].append(value) # append the new value
        self.save()

    def save(self) -> None:
        # https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
        csv_columns = ["idx"] + list(self.records.keys())
        csv_file = self.output_path + "mock_run_output.csv"
        keys = self.records.keys()
        max_len = self.get_max_record_len()
        print("max_len",max_len)
        try:
            with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for i in range(max_len):
                    data = { "idx": i }
                    for k in keys:
                        if i < len(self.records[k]):
                            data[k] = self.records[k][i]
                        else:
                            data[k] = None
                    
                    writer.writerow(data)
            print("Saved catalog data")
        except IOError:
            print("I/O error")

        



def get_run_logger(use_azure: bool, output_path: str):
    """tries to return an azure Run instance if applicable and available
       else defaults to MockRun instance

    Args:
        use_azure (bool): whether to use azure

    Returns:
        azureml.core.Run or MockRun
    """

    print("use_azure", use_azure)
    if use_azure: # if we want to use azure
        try:
            from azureml.core import Run
            return Run.get_context()
        except ImportError:
            print("Error when importing azureml.core", ImportError)
            return MockRun(output_path)
    else:
        return MockRun(output_path)
