import argparse
import json

import cv2

from passporteye import read_mrz


# create the stdin parser object
parser = argparse.ArgumentParser(
    prog="Passport Parser",
    usage=f"extractor.py [FILEPATH] [--print] [--nophoto]\n{'[-h]': >24}",
    description="Command-line utility to extract passport photo and data.",
    allow_abbrev=False,
    epilog="Enjoy the program :)",
)

parser.add_argument(
    "filepath", metavar="FILEPATH", type=str, help="The path to the file."
)

# --print-only flag
parser.add_argument(
    "--print", action="store_true", help="Prints the result in console instead of saving it into a json file"
)

# --no-photo flag
parser.add_argument(
    "--nophoto", action="store_true", help="Doesn't crop the passport photo"
)

args = parser.parse_args()


def extract_photo(filepath: str) -> None:
    """Extract the passport photo and save.

    :param filepath: The path to the file.
    """
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
    )

    if len(faces) != 0:
        for (x, y, w, h) in faces:
            # Reminder: The variables x,y,w,h are being hardcoded.
            # Might have to be changed depending on the input images size.
            y -= 45
            x -= 20
            roi_color = image[y:y + h + 80, x:x + w + 38]
            print("[INFO] Face found. Saving locally.")
            cv2.imwrite('face.jpg', roi_color)
    else:
        print("[INFO] Could not find the face.")

    
def main() -> None:
    """Main function.
    """
    print("[INFO] Extracting data from the image.")
    try:
        mrz = read_mrz(args.filepath)
        # convert the mrz object into a dict
        mrz_dict = mrz.to_dict() if mrz is not None else {'mrz_type': None, 'valid': False, 'valid_score': 0}

        # if --print flag is False save the extracted data into a json file
        if not args.print:
            with open("mrz.json", "w") as f:
                json.dump(mrz_dict, f)
                print("[INFO] Saved the extracted into mrz.json file at the root directory.")
        else:
            print("\n", json.dumps(mrz_dict, indent=2), "\n")

        # if --nophoto flag is False extract the passport photo and save it
        if not args.nophoto:
            print("[INFO] Extracting the passport photo from the image")
            extract_photo(args.filepath)
    except FileNotFoundError as exc:
        print(f"[ERROR] {exc}")


main()
