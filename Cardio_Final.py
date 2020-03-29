import pickle
from termcolor import colored

# accuracy ==> 72%

with open("Models\HeartDisease", "rb") as f:
    randomForest = pickle.load(f)

model_inputs = [17623, 2, 169, 82.0, 150, 100, 1, 1, 0, 0, 1]
model_inputs1 =[22630 ,1, 169, 80.0, 120, 80, 1,1,0,0,1] 

prediction = randomForest.predict([model_inputs1])[0]
print()
if prediction:
    print(colored("Patient Maybe Suffering from Cardiovascular disease", "red"))
else:
    print(colored("Patient is safe", "green"))
