import requests

def list_repository_collaborators(user, token, org, repo, affiliation='all'):
    #doc: https://docs.github.com/en/rest/reference/repos#list-repository-collaborators
    query_url = f"https://api.github.com/repos/{org}/{repo}/collaborators"

    headers = {
        'accept': 'application/vnd.github.v3+json'
    }

    per_page = 100
    response_len = per_page
    return_var = list()

    page = 0
    response_len = per_page
    while response_len == per_page:
        page += 1
        response = requests.get(
            query_url,
            headers=headers,
            params={
                'per_page': per_page,
                'page': page
                'affiliation': affiliation #outside for the task
            },
            auth=(user, token)
        )

        response_json = response.json()
        return_var += response_json
        response_len = len(response_json)

    return return_var
    
