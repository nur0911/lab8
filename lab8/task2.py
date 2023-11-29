import requests
import json
import random

# Task 2.1: Random Character Request
random_character_id = random.randint(1, 826)
character_url = f'https://rickandmortyapi.com/api/character/{random_character_id}'
character_response = requests.get(character_url).json()

# Task 2.2: Response Output
print("Task 2.2: JSON response")
print(json.dumps(character_response, indent=2))

print("\nKeys of the JSON structure:")
print(character_response.keys())

# Task 2.3: Save to File
file_name = f'info_character_{random_character_id}.json'
with open(file_name, 'w') as file:
    json.dump(character_response, file, indent=2)
print(f'\nTask 2.3: JSON response saved to {file_name}')

# Task 2.4: Episode List
episode_urls = character_response['episode']
episode_ids = [int(url.split("/")[-1]) for url in episode_urls]

# Create a file and append each episode URL using append mode
episode_file_name = f'all_episodes_with_character_{random_character_id}.txt'
with open(episode_file_name, 'a') as file:
    for episode_url in episode_urls:
        file.write(episode_url + '\n')
print(f'\nTask 2.4: Episode URLs saved to {episode_file_name}')

# Task 2.5: Episode Response Structure
sample_episode_response = requests.get('https://rickandmortyapi.com/api/episode/1').json()
print("\nTask 2.5: Episode Response Structure")
print(json.dumps(sample_episode_response, indent=2))

# Task 2.6: Episode Class Creation
class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created

# Task 2.7: Episode Data Retrieval
episode_objects = []
for episode_id in episode_ids:
    episode_url = f'https://rickandmortyapi.com/api/episode/{episode_id}'
    episode_data = requests.get(episode_url).json()
    episode_objects.append(Episode(**episode_data))

# Task 2.8: Class Methods (Adding some sample methods to Episode class)
class Episode:
    # Existing __init__ method...

    def get_characters_count(self):
        return len(self.characters)

# Task 2.9: Character Response Structure
sample_character_response = requests.get('https://rickandmortyapi.com/api/character/1').json()
print("\nTask 2.9: Character Response Structure")
print(json.dumps(sample_character_response, indent=2))

# Task 2.10: Character Class Creation
class Character:
    def __init__(self, id, name, status, species, type, gender, origin, location, image, episode, url, created):
        self.id = id
        self.name = name
        self.status = status
        self.species = species
        self.type = type
        self.gender = gender
        self.origin = origin
        self.location = location
        self.image = image
        self.episode = episode
        self.url = url
        self.created = created

# Task 2.11: Character Object Creation
random_character_object = Character(**character_response)

# Task 2.12: Character Class Methods (Adding some sample methods to Character class)
class Character:
    # Existing __init__ method...

    def get_episode_count(self):
        return len(self.episode)

# Task 2.13: Result
print("\nTask 2.13: Result")
print(f"Random Character ID: {random_character_id}")
print(f"Character Name: {random_character_object.name}")
print(f"Episode Count for Character: {random_character_object.get_episode_count()}")
print(f"Sample Episode ID: {sample_episode_response['id']}")
print(f"Sample Episode Name: {sample_episode_response['name']}")
print(f"Characters Count in Sample Episode: {Episode(**sample_episode_response).get_characters_count()}")
