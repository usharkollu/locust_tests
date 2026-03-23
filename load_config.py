import os

class LoadTestConfig:
    """Environment-specific load test configuration."""

    CONFIGS = {
        'dev': {
            'users': 5,
            'spawn_rate': 2,
            'run_time': '1m',
            'thresholds': {
                'p95_response_time': 1000,
                'failure_rate': 5.0
            }
        },
        'stg': {
            'users': 10,
            'spawn_rate': 2,
            'run_time': '5s',
            'thresholds': {
                'p95_response_time': 500,
                'failure_rate': 1.0
            }
        },
        'prod': {
            'users': 15,
            'spawn_rate': 2,
            'run_time': '6s',
            'thresholds': {
                'p95_response_time': 400,
                'failure_rate': 0.1
            }
        }
    }

    @classmethod
    def get(cls, env=None):
        env = env or os.getenv('LOCUST_ENV', 'stg')
        return cls.CONFIGS.get(env, cls.CONFIGS['stg'])