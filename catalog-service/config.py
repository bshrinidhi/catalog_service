import os

# Use ConfigMaps to override environment variables


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    # DATABASE_HOST = os.getenv('DATABASE_URL')
    # DATABASE_PORT = os.getenv('DATABASE_PORT')
    # DATABASE_KEYSPACE = os.getenv('DATABASE_KEYSPACE')
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 9042
    DATABASE_KEYSPACE = 'assessment'


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DATABASE_HOST = "localhost"
    DATABASE_PORT = 9042

class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
