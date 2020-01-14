playlist = {
    'name': 'Chill with Lily',
    'author': 'Lily',
    'songs': [
        {'title': 'name1', 'author': ['auth1', 'auth2'], 'duration': 3.44, 'date added': '2014-08-27'},
        {'title': 'name2', 'author': ['auth3', 'auth4'], 'duration': 3.3, 'date added': '2014-09-08'},
        {'title': 'name3', 'author': ['auth1', 'auth2'], 'duration': 2.44, 'date added': '2019-09-27'}
    ]
}
total_length = 0
for song in playlist['songs']:
    total_length += song['duration']
print(total_length)
