'''
Pre-made app filters for easy filtering.

Feel free to customize!
'''
class Filter:
    def __init__(self, text, lambda_filter):
        self.text = text
        self.function = lambda_filter

# A list of quick filter aliases to apply by default.
default = []

# The available quick filters.
quick = {
    'coop': Filter(
        'Co-op games.',
        lambda x: any('Co-op' in category for category in x['Categories'])
    ),
    'high': Filter(
        'Metracritic scores > 70. (Filters out games without Metacritic scores.)',
        lambda x: x['Metacritic']['score'] > 70
    ),
    'linux': Filter(
        'Linux support.',
        lambda x: 'linux' in x['Platforms']
    ),
    'multi': Filter(
        'Multiplayer.',
        lambda x: 'Multi-player' in x['Categories']
    ),
    'vr': Filter(
        'VR support. (Steam store metadata does not categorize all VR-capable games, so this will miss some.)',
        lambda x: 'VR Support' in x['Categories']
    ),
    'unplayed': Filter(
        'Played less than an hour.',
        lambda x: x['Playtime']['hours'] == 0
    ),
}
