import pickle
import pandas as pd


def predicts(inputs):
    header = ['bloody_stools', 'fecal_leakage', 'swelling', 'dizziness', 'confusion', 'fatigue', 'itching', 'vomiting', 'arm_pain',
              'cough', 'muscle_pain', 'depression', 'fever', 'painful_bowel_moments', 'urine_blood', 'sweating', 'nausea',
              'stiff_neck', 'decreased_appetite', 'weak', 'wheezing', 'bleeding', 'hives', 'bleed', 'headache', 'dry_mouth', 'sweat',
              'stomach_pain', 'stool_pressure', 'anxiety', 'shoulder_pain', 'anus_itching', 'vision_problem', 'abdominal_pain',
              'chest_pain', 'weight_loss', 'diarrhea', 'breath_problems', 'thirsty', 'anus_swelling', 'blood_o_tissue', 'constipation',
              'neck_pain', 'low_heartbeat', 'more_urine', 'low_breath', 'muscle_cramps', 'muscle_spasm', 'yawning', 'rash', 'back_pain',
              'anal_bleeding', 'lump_anus', 'cold', 'skin_rash', 'neck_stiff']

    df = pd.read_csv("Disease_Symptoms.csv")
    disease = set(df.iloc[:, 0])
    disease = list(disease)
    disease.sort()

    model_inputs5 = []
    for x in range(0, len(header)):
        model_inputs5.append(0)

    # inputs = [i.strip() for i in input("Enter Symptoms : ").split()]

    # print(inputs)

    for element in range(0, len(header)):
        for symptom in inputs:
            if symptom == header[element]:
                model_inputs5[element] = 1

    with open("DiseasePrediction(Dec)", "rb") as f:
        Model_Decision_Tree = pickle.load(f)

    pred = Model_Decision_Tree.predict([model_inputs5])

    print(disease[pred[0]])
    return disease[pred[0]]


if __name__ == '__main__':
    # predicts(['fever', 'vomiting', 'headache', 'sweating',
    #           'bloody_stools', 'abdominal_pain', 'diarrhea'])
    pass
