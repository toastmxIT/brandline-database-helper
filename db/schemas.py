RUN_QUERY_SCHEMA = {
    'action': {
      'required': True,
        'type': 'string',
        'allowed': ['run']
    },
    'queries': {
        'required': True,
        'type': 'list'
    }
}
