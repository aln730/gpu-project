import torch
from torchvision import transforms
from PIL import Image
from transformers import VisionEncoderDecoderModel, AutoTokenizer

# Load pre-trained model and tokenizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning").to(device)
tokenizer = AutoTokenizer.from_pretrained("gpt2")

# Preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def generate_caption(image_path):
    """Generates a caption for a given image."""
    img = Image.open(image_path).convert("RGB")
    img_tensor = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model.generate(img_tensor, max_length=20, num_beams=5)
        caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return caption
