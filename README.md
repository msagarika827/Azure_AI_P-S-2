AZURE AI VISION IMAGE ANALYSIS PROJECT

This project demonstrates the use of Azure AI Vision service to analyze images by generating captions, detecting objects, identifying people, and tagging relevant features within images. Using the Azure AI Vision SDK, this application enables easy integration of image analysis functionality into applications, making it possible to interpret visual input programmatically.

𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄
The purpose of this project is to utilize Azure AI Vision’s capabilities to:
1. Generate captions for images.
2. Detect and tag objects and people within images.
3. Remove image backgrounds or create foreground mattes.

𝗣𝗿𝗲𝗿𝗲𝗾𝘂𝗶𝘀𝗶𝘁𝗲𝘀

- Azure Account: Access to an Azure subscription with permissions to create resources.
- Azure AI Services Resource: An Azure AI Services multi-service account to handle image analysis requests.
- Visual Studio Code: For code editing and running the application.
- SDKs and Libraries: The Azure AI Vision SDK and other required packages (installation steps below).

Setup Instructions

1. 𝗖𝗹𝗼𝗻𝗲 𝘁𝗵𝗲 𝗥𝗲𝗽𝗼𝘀𝗶𝘁𝗼𝗿𝘆:
   git clone https://github.com/MicrosoftLearning/mslearn-ai-vision
2. Open the Project in Visual Studio Code:
   Open the `mslearn-ai-vision` folder in Visual Studio Code.

3. 𝗜𝗻𝘀𝘁𝗮𝗹𝗹 𝗗𝗲𝗽𝗲𝗻𝗱𝗲𝗻𝗰𝗶𝗲𝘀:
   - Python: Run the following command:
     
     pip install azure-ai-vision-imageanalysis==1.0.0b3
   

4. **Configure Azure AI Service**:
   - Open the Azure portal and create a new Azure AI Services resource in **** with the following:
     - Region: ***
     - Pricing Tier:  ***    
     - Python: `.env`

5. Run the Application:
   - In the terminal, navigate to the `image-analysis` directory, then run:
     - Python:
       python image-analysis.py images/street.jpg
   

𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 𝗮𝗻𝗱 𝗙𝘂𝗻𝗰𝘁𝗶𝗼𝗻𝗮𝗹𝗶𝘁𝘆

1. Analyze Image Captions
Generates descriptive captions for images using Azure AI Vision's image analysis capabilities.

2. Tag Image Contents
Tags relevant objects and features in the image to provide a better context.

3. Detect and Highlight Objects and People
Uses bounding boxes to detect objects and people within images and labels them.

4. Background Removal
Generates foreground matte by removing the background from an image, useful for various applications.

𝗖𝗼𝗱𝗲 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲

- image-analysis: Contains the main code files for C# (`Program.cs`) and Python (`image-analysis.py`).
- Configuration Files: `.env` or `appsettings.json` for endpoint and key settings.
- Images Folder: Includes sample images used for testing (`images/street.jpg`, `images/building.jpg`, etc.).

![Screenshot 2024-11-05 124836](https://github.com/user-attachments/assets/c6d235a5-9339-4662-9be1-fb1170e93760)

![Screenshot 2024-11-05 125005](https://github.com/user-attachments/assets/5503d710-3b7c-40e0-89f2-96e35e62ce82)
