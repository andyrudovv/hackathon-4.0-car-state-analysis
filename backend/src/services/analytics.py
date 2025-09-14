from typing import Any, Dict
from PIL import Image
import numpy as np
import timm
import torch
import torchvision.transforms as transforms


MODEL_NAME = 'efficientnetv2_s' 
NUM_CLASSES = 5
MODEL_PATH = "src/services/model.pth" # Убедись, что путь правильный
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_car_diagnostic_model():
   
    model = timm.create_model(MODEL_NAME, pretrained=False, num_classes=NUM_CLASSES)
    checkpoint = torch.load(MODEL_PATH, map_location=DEVICE)
    model.load_state_dict(checkpoint['model_state_dict'])
    

    model.to(DEVICE)
    model.eval() 
    
    print(f"✅ Модель успешно загружена! F1-score из файла: {checkpoint.get('f1', 'N/A'):.4f}")
    return model


def process_image(image: Image.Image) -> Dict[str, Any]:
    
    # image_array = np.array(image)

    
    # results = {
    #     "mean_color": image_array.mean(axis=(0, 1)).tolist(),
    #     "shape": image_array.shape,
    #     "size": image_array.size
    # }

    # return results

    pass

def analyze_photo(image: Image.Image) -> Dict[str, Any]:
    # analytics_results = process_image(image)

    # # Load the model
    # # checkpoint = torch.load("src/services/model.pth", map_location="cpu")
    # # print(checkpoint.keys())


    # model = load_car_diagnostic_model()
    # # model.load_state_dict(checkpoint['model_state_dict'])
    # if torch.cuda.is_available():
    #     try:
    #         model.load_state_dict(torch.load("src/services/model.pth", weights_only=True)) # Replace with your actual path
    #     except Exception as e:
    #         print(f"Error loading model on CUDA: {e}")
    #         model.load_state_dict(torch.load("src/services/model.pth", map_location=torch.device('cpu'), weights_only=True))
    # else:
    #     model.load_state_dict(torch.load("src/services/model.pth", map_location=torch.device('cpu'), weights_only=True))
    # model.eval()

    # # Define the transforms
    # inference_transforms = transforms.Compose([
    #     transforms.Resize(512),
    #     transforms.CenterCrop(512),
    #     transforms.ToTensor(),
    #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    # ])

    # # Transform the image
    # input_tensor = inference_transforms(image)
    # input_batch = input_tensor.unsqueeze(0) # create a mini-batch as expected by the model

    # # Move the input and model to GPU for speed if available
    # if torch.cuda.is_available():
    #     input_batch = input_batch.to('cuda')
    #     model.to('cuda')

    # with torch.no_grad():
    #     output = model(input_batch)

    # # The output has unnormalized scores. To get probabilities, you can run a softmax on it.
    # probabilities = torch.nn.functional.softmax(output[0], dim=0)

    # # Define the class names
    # class_names = ['scratch', 'dent', 'rust', 'dirt', 'clean']

    # # Get the predicted class
    # predicted_class_index = torch.argmax(probabilities).item()
    # predicted_class = class_names[predicted_class_index]

    # # Add the prediction to the results
    # analytics_results['predicted_class'] = predicted_class
    # analytics_results['probabilities'] = probabilities.tolist()

    # return analytics_results

    pass