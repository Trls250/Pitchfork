# Pitchfork
Python script used for the [Google Natural Language API](https://cloud.google.com/natural-language/docs/) to extract entities from text reviews in Pitchfork, an online music journal.

To connect to the API you'll need to run this script on a Google virtual cloud machine. For those not familiar with this setup I suggest the [tutorial's by Sentdex](https://pythonprogramming.net/natural-language-api-google-cloud-tutorial/) to get a sense of how to do this.

Once the file is setup, run the python script ffrom the same directory as where the .csv file is saved. You can edit the csv file name by changing it in the code below.

`csv_data = pd.read_csv('Pitchfork_Content_1.csv', encoding = 'utf-8')`

## CSV Structure
 The csv file follows a structure of including the review ID and Text of the review as below:

| Reviewid  | Text |
| ------------- | ------------- |
| Reviewid 1  | Review text  |
| Reviewid 2  | Review text  |

I've modified this file for other analyses that need to connect to Google's Natural Language API. To-do so, the fields in the for loop would need to be modified. The primary importance is that the text you want analyzed by the API goes in the review field as show below.

`review_id = csv_data.loc[csv_data.index[i], 'reviewid']`
`review = csv_data.loc[csv_data.index[i], 'content']`

## Output Structure

|entity_name |	id |	mentions	| metadata	| salience | type	| wiki-page |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
|entity_name extracted by the API | review	id the entity is from | number of mentions in the review	| metadata Google has linked to the entity	| a positive or negative sentiment score associated with the mentions | type of entity (i.e. person or work of art)	| if there is an associated wiki-page with the entity it is shared here |
