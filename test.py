import pandas as pd

credit_card_data = pd.read_csv('creditcard.csv')

legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

legit_sample = legit.sample(n=800)

new_dataset = pd.concat([legit_sample, fraud], axis=0)

new_dataset.to_csv('VS_Code_Pract.csv')