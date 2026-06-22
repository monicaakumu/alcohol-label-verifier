import boto3


textract = boto3.client(
    "textract",
    region_name="us-east-1"
)


def extract_text_from_file(file_path):

    with open(file_path, "rb") as document:

        response = textract.detect_document_text(
            Document={
                "Bytes": document.read()
            }
        )

    lines = []

    for block in response["Blocks"]:

        if block["BlockType"] == "LINE":
            lines.append(block["Text"])

    return "\n".join(lines)
