import requests


def create_repository(user, password, team_name, repository_name):
	data = '{"scm": "git", "is_private": "true", "fork_policy": "no_public_forks" }'
	url = f'https://api.bitbucket.org/2.0/repositories/{team_name}/{repository_name}'

	result = requests.post(url, auth=(user, password), data = data)

	sucess = result.status_code == 200

	if sucess:
		result_json = result.json()
		source_url = result_json['links']['source']['href']
		clone_url = result_json['links']['clone'][0]['href']

		print('Successfully created the repository')
		print(f'Created on: {source_url}')
		print(f'You can fork the repository with: git clone {clone_url}')
	else:
		raise Exception('Bad credentials or Bad repository name')
