import json

def lambda_handler(event, context):
    """
    Simple Lambda function that returns a greeting
    """
    name = event.get('name', 'World')
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': f'Hello, {name}!',
            'event': event
        })
    }
'''

**requirements.txt:** (if you have dependencies)
'''
# Add your Python dependencies here
# Example:
# requests==2.31.0