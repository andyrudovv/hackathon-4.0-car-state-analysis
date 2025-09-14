import torch
import timm
import torch.nn as nn
from torchvision import transforms
from PIL import Image
from collections import OrderedDict

# Labels (same order as training)
LABELS = ['scratch', 'dent', 'rust', 'dirt', 'clean']


class CarDamageModel(nn.Module):
    def __init__(self, num_classes=5):
        super(CarDamageModel, self).__init__()
        # backbone without classifier
        self.backbone = timm.create_model(
            'tf_efficientnetv2_s', pretrained=False, num_classes=0
        )
        in_features = self.backbone.num_features
        self.fc = nn.Linear(in_features, num_classes)

    def forward(self, x):
        features = self.backbone(x)
        return self.fc(features)


def load_model(weights_path="src/services/model.pth", device="cpu"):
    model = CarDamageModel(num_classes=len(LABELS))

    # Load checkpoint with safe unpickling (PyTorch ≥2.6 fix)
    checkpoint = torch.load(weights_path, map_location=device, weights_only=False)
    print(checkpoint[:100])
    state_dict = None
    if "model_state_dict" in checkpoint:
        state_dict = checkpoint['model_state_dict']
    else:
        state_dict = checkpoint
    # print(list(state_dict.keys())[:30])


    # Load weights (allow missing keys if necessary)
    missing, unexpected = model.load_state_dict(state_dict, strict=False)
    print("Missing:", missing)
    print("Unexpected:", unexpected)

    model.to(device)
    model.eval()
    return model


# Same preprocessing as training
transform = transforms.Compose([
    transforms.Resize(512),
    transforms.CenterCrop(512),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])


def predict_image(model, image: Image.Image, device="cpu", threshold=0.5):
    image = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(image)
        probs = torch.sigmoid(outputs).cpu().numpy()[0]

    # round to 3 decimals
    results = {LABELS[i]: round(float(probs[i]), 3) for i in range(len(LABELS))}
    preds = {LABELS[i]: float(probs[i]) for i in range(len(LABELS))}

    return {"probs": results, "preds": preds}


def analyze_photo(image: Image.Image, device="cpu", threshold=0.5):
    model = load_model()
    res = predict_image(model, image, device, threshold)
    print(res)
    return res
