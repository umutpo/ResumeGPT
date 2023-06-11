import configparser

if __name__ == '__main__':
    config_parser = configparser.ConfigParser()
    config_parser.read('./config/keys_config.cfg')

    OPEN_AI_API_KEY = config_parser.get('openai', 'api_key')
    OPEN_AI_ORGANIZATION_ID = config_parser.get('openai', 'organization_id')