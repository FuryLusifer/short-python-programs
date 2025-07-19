def build_profile(first, last, **userinfo):
    '''builds user profile.'''
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo

user_profile = build_profile('ram', 'bahadur', height = 190, weight = 70)

print(user_profile)