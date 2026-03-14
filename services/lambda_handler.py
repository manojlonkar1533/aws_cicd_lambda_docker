import json
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Hello from Lambda container image!',
            'commit': 'IMAGE_TAG_PLACEHOLDER'
        })
    }

if __name__ == "__main__":
    result = lambda_handler({}, None)
    print("result is :", result)