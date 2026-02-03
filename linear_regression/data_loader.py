def data_loader(filepath):

    X, y = [], []

    with open(filepath) as file:
        next(file)  # Skip header line

        for line in file:
            data = line.strip().split(",")
            y.append(data[0])
            X.append(data[1:])
        
        return X, y

# trial_output = data_loader("../datasets/Housing.csv")
# print(trial_output[0][0])