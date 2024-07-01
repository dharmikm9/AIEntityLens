import requests

def call_ner_api(text):
    url = 'http://127.0.0.1:5000/ner'
    myobj = {'qry': text}

    try:
        # Make POST request to the API
        response = requests.post(url, json=myobj)

        # Check if request was successful (status code 200)
        if response.status_code == 200:
            return response.json()  # Assuming API returns JSON data
        else:
            print(f"Request failed with status code {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None


# Function to extract entities by category
def extract_entities_by_category(json_data, category):
    entities = []
    for entity in json_data['ner']:
        entity_type = entity['entity'][2:]  # Extracting 'PER', 'LOC', 'ORG' from 'B-PER', 'B-LOC', 'B-ORG'
        if category.lower() == 'person' and entity_type == 'PER':
            entities.append({
                'word': entity['word'],
                'score': entity['score']
            })
        elif category.lower() == 'location' and entity_type == 'LOC':
            entities.append({
                'word': entity['word'],
                'score': entity['score']
            })
        elif category.lower() == 'organization' and entity_type == 'ORG':
            entities.append({
                'word': entity['word'],
                'score': entity['score']
            })
    return entities


if __name__ == '__main__':
    print()
    extracted_ner_obj = extract_ner("My Name is Dharmik Mehta and I'm from India.")

    # Example usage:
    category_name = "org"
    entities = extract_entities_by_category(extracted_ner_obj, category_name)

    # Print the extracted entities
    print(f"Entities for category '{category_name}':")
    for entity in entities:
        print(f"  Word: {entity['word']}, Score: {entity['score']}")

