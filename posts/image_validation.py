def detect_pet(image_path):
    from google.cloud import vision

    client = vision.ImageAnnotatorClient()

    with open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    label_names = [label.description for label in labels]
    key_words = ['Dog', 'Cat', 'Dogs', 'Cats', 'Pet', 'Pets']

    for keyword in key_words:
        if keyword in label_names:
            return True
    return False
