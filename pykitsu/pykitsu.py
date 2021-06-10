# Pykitsu -> A simple api wrapper for the kitsu api written in python

# MODULES
from requests import get # To fetch api json response

# the category (1st) argument for get_info() can be anything from this list
get_info_supported_categories = ['anime', 'manga', 'episodes', 'chapters', 'categories',
'category-favorites', 'anime-characters', 'manga-characters', 'characters', 'streamers',
'streaming-links', 'users', 'user-roles', 'favorites', 'follows',
'linked-accounts', 'blocks', 'profile-link-sites', 'profile-links', 'roles',
'stats', 'library-entries', 'library-entry-logs', 'library-events', 'list-imports',
'media-reaction-votes', 'media-reactions', 'review-likes', 'reviews', 'posts',
'post-likes', 'post-follows', 'comments', 'comment-likes', 'anime-productions',
'anime-staff', 'manga-staff', 'producers', 'people', 'castings',
'group-action-logs', 'group-bans', 'group-invites', 'group-member-notes', 'group-members',
'group-neighbors', 'group-permissions', 'group-reports', 'group-ticket-messages', 'group-tickets',
'leader-chat-messages', 'reports', 'site-announcements']

# Get trending anime/manga
def trending(category):
    category = category.lower()
    if category not in ['anime', 'manga']:
        raise ValueError(f'Invalid argument {category}, it has to be either anime or manga')

    response = get(f'https://kitsu.io/api/edge/trending/{category}').json()
    result = {}
    for i in response['data']:
        result[i['id']] = i['attributes']['canonicalTitle']

    return result

# Search for anime, manga, characters, users
def search(category, query):
    category = category.lower()
    query = query.replace(' ', '%20')
    if category == 'characters':
        placeholder, placeholder2 = 'name', 'canonicalName'
    elif category == 'users':
        placeholder = placeholder2 = 'name'
    elif category in ['anime', 'manga']:
        placeholder, placeholder2 = 'text', 'canonicalTitle'
    else:
        raise ValueError(f'Invalid category {category}, it has to be one of anime, manga, characters or users')

    response = get(f'https://kitsu.io/api/edge/{category}?filter[{placeholder}]={query}').json()

    result = {}
    result['count'] = response['meta']['count']
    for i in response['data']:
        result[i['id']] = i['attributes'][placeholder2]

    return result

# Get explicit info on something from get_info_supported_categories (id required)
def get_info(category, id):
    category = category.lower()
    if category not in get_info_supported_categories:
        raise ValueError(f'Category {category} is not supported')

    response = get(f'https://kitsu.io/api/edge/{category}/{id}').json()
    try:
        response =  response['data']['attributes']
    except KeyError:
        raise KeyError('Error parsing the json response, check the id')

    return response

# Get characters of anime/manga, or the anime/manga a characters features in
def get_family(category, id):
    category = category.lower()
    if category in ['anime', 'manga']:
        response = get(f'https://kitsu.io/api/edge/{category}/{id}/characters').json()
        placeholder, placeholder2 = 'character', 'canonicalName'
    elif category == 'character':
        response = get(f'https://kitsu.io/api/edge/characters/{id}/media-characters').json()
        placeholder, placeholder2 = 'media', 'canonicalTitle'
    else:
        raise ValueError(f'Invalid category {category}, it has to be one of anime, manga or character')

    result = {}
    try:
        for i in response['data']:
            new_response = get(i['relationships'][placeholder]['links']['related']).json()
            result[new_response['data']['id']] = new_response['data']['attributes'][placeholder2]
    except KeyError:
        raise KeyError('Error parsing the json response, check the id')

    return result
