from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd
import os

#Set your Google service account JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'google_service_account.json'

#Authorize with your Google service account JSON
language_client = language.LanguageServiceClient()

#Import your text data to pandas dataframe for sentiment analysis
csv_data = pd.read_csv('Pitchfork_Content_1.csv', encoding = 'utf-8')

#Create an empty list
output = []

#Simple loop that iterates over dataframe review data and stores in nested list
for i in range(0,len(csv_data.index)): #loops through dataframe total rows
    review_id = csv_data.loc[csv_data.index[i], 'reviewid'] 
    review = csv_data.loc[csv_data.index[i], 'content'] #extracts the iterated review
    document = types.Document(
	content=review,
	type=enums.Document.Type.PLAIN_TEXT) #set as google doc that represents text
    entities = language_client.analyze_entities(document).entities
  # entity_sentiment = language_client.analyze_entity_sentiment(document).entities
    entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION', 'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')
  # sentiment = language_client.analyze_sentiment(document=document).document_sentiment #send to google nlp api for analysis
    features={
    "extractEntitySentiment": True,
    }
    for e in entities:
        result = {"id": review_id, "entity_name": e.name, "type": entity_type[e.type], "metadata": e.metadata, "salience": e.salience, "wiki-page": e.metadata.get('wikipedia_url', '-'), "mentions": e.mentions[0].type } #store data into dictionary
        output.append(result.copy()) #appends dictionary to list
        print(result)

df = pd.DataFrame(output) #save nested list to pandas data frame

df.to_csv('pitchfork_sentiment1utf8.csv', sep='|', encoding='utf-8')