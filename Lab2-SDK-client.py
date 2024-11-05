#Enviroment
AI_SERVICE_ENDPOINT=YOUR_AI_SERVICES_ENDPOINT
AI_SERVICE_KEY=YOUR_AI_SERVICES_KEY
#SDK-Program
from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw
import sys
from matplotlib import pyplot as plt
from azure.core.exceptions import HttpResponseError
import requests
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential


def main():
    global cv_client
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')

        # Get image
        image_file = 'images/street.jpg'
        if len(sys.argv) > 1:
            image_file = sys.argv[1]
        with open(image_file, "rb") as f:
            image_data = f.read()

        # Authenticate Azure AI Vision client
        cv_client = ImageAnalysisClient(
            endpoint=ai_endpoint,
            credential=AzureKeyCredential(ai_key)
        )

        # Analyze image
        AnalyzeImage(image_file, image_data, cv_client)

        # Background removal
        BackgroundForeground(ai_endpoint, ai_key, image_file)
    except Exception as ex:
        print(ex)


def AnalyzeImage(image_filename, image_data, cv_client):
    print('\nAnalyzing image...')
    try:
        # Get result with specified features to be retrieved
        result = cv_client.analyze(
            image_data=image_data,
            visual_features=[
                VisualFeatures.CAPTION,
                VisualFeatures.DENSE_CAPTIONS,
                VisualFeatures.TAGS,
                VisualFeatures.OBJECTS,
                VisualFeatures.PEOPLE
            ],
        )
    except HttpResponseError as e:
        print(f"Status code: {e.status_code}")
        print(f"Reason: {e.reason}")
        print(f"Message: {e.error.message}")
        return

    # Display analysis results
    # Get image captions
    if result.caption:
        print("\nCaption:")
        print(" Caption: '{}' (confidence: {:.2f}%)".format(result.caption.text, result.caption.confidence * 100))

    # Get image dense captions
    if result.dense_captions:
        print("\nDense Captions:")
        for caption in result.dense_captions.list:
            print(" Caption: '{}' (confidence: {:.2f}%)".format(caption.text, caption.confidence * 100))

    # Get image tags
    if result.tags:
        print("\nTags:")
        for tag in result.tags.list:
            print(" Tag: '{}' (confidence: {:.2f}%)".format(tag.name, tag.confidence * 100))

    # Get objects in the image
    if result.objects:
        print("\nObjects in image:")
        image = Image.open(image_filename)
        fig = plt.figure(figsize=(image.width / 100, image.height / 100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'
        for detected_object in result.objects.list:
            print(" {} (confidence: {:.2f}%)".format(detected_object.tags[0].name, detected_object.tags[0].confidence * 100))
            r = detected_object.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)
            plt.annotate(detected_object.tags[0].name, (r.x, r.y), backgroundcolor=color)
        
        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'objects.jpg'
        fig.savefig(outputfile)
        print(' Results saved in', outputfile)

    # Get people in the image
    if result.people:
        print("\nPeople in image:")
        image = Image.open(image_filename)
        fig = plt.figure(figsize=(image.width / 100, image.height / 100))
        plt.axis('off')
        draw = ImageDraw.Draw(image)
        color = 'cyan'
        for detected_people in result.people.list:
            r = detected_people.bounding_box
            bounding_box = ((r.x, r.y), (r.x + r.width, r.y + r.height))
            draw.rectangle(bounding_box, outline=color, width=3)

        # Save annotated image
        plt.imshow(image)
        plt.tight_layout(pad=0)
        outputfile = 'people.jpg'
        fig.savefig(outputfile)
        print(' Results saved in', outputfile)


def BackgroundForeground(endpoint, key, image_file):
    # Define the API version and mode
    api_version = "2023-02-01-preview"
    mode = "foregroundMatting"  # Can be "foregroundMatting" or "backgroundRemoval"

    # Remove the background from the image or generate a foreground matte
    print('\nRemoving background from image...')
    url = f"{endpoint}computervision/imageanalysis:segment?api-version={api_version}&mode={mode}"
    headers = {
        "Ocp-Apim-Subscription-Key": key,
        "Content-Type": "application/json"
    }
    image_url = f"https://github.com/MicrosoftLearning/mslearn-ai-vision/blob/main/Labfiles/01-analyze-images/Python/image-analysis/{image_file}?raw=true"
    body = {"url": image_url}

    response = requests.post(url, headers=headers, json=body)
    image = response.content
    with open("background.png", "wb") as file:
        file.write(image)
    print(' Results saved in background.png\n')


if _name_ == "_main_":
    main()


#Output
'''
Caption:
 Caption: 'a man walking a dog on a leash on a street' (confidence: 82.06%)

Dense Captions:
 Caption: 'a man walking a dog on a leash on a street' (confidence: 82.07%)
 Caption: 'a man walking on a street' (confidence: 69.02%)
 Caption: 'a yellow car on the street' (confidence: 78.22%)
 Caption: 'a black dog walking on the street' (confidence: 75.31%)
 Caption: 'a blurry image of a blue car' (confidence: 82.01%)
 Caption: 'a yellow taxi cab on the street' (confidence: 72.44%)

Tags:
 Tag: 'outdoor' (confidence: 99.87%)
 Tag: 'land vehicle' (confidence: 99.02%)
 Tag: 'vehicle' (confidence: 98.89%)
 Tag: 'building' (confidence: 98.55%)
 Tag: 'road' (confidence: 95.98%)
 Tag: 'wheel' (confidence: 95.14%)
 Tag: 'street' (confidence: 94.71%)
 Tag: 'person' (confidence: 93.01%)
 Tag: 'clothing' (confidence: 91.19%)
 Tag: 'taxi' (confidence: 90.95%)
 Tag: 'car' (confidence: 84.01%)
 Tag: 'dog' (confidence: 82.68%)
 Tag: 'yellow' (confidence: 77.08%)
 Tag: 'walking' (confidence: 74.11%)
 Tag: 'city' (confidence: 64.80%)
 Tag: 'woman' (confidence: 57.53%)

Objects in image:
 car (confidence: 72.40%)
 taxi (confidence: 77.00%)
 person (confidence: 78.10%)
 dog (confidence: 54.40%)
  Results saved in objects.jpg

People in image:
  Results saved in people.jpg

Removing background from image...
  Results saved in background.png 
'''

