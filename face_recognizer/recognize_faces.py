import face_recognition
import cv2
import numpy as np
import PIL

import pickle
import os

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)


def generate_facial_data(face_directory):
    known_face_encodings = []
    known_face_names= []

    image_files = [(f.rstrip('.jpg'), os.path.join(face_directory, f)) for f in os.listdir(face_directory) if os.path.isfile(os.path.join(face_directory, f))]
    # Load a sample picture and learn how to recognize it.

    for name, filename in image_files:
        image = face_recognition.load_image_file(filename)
        image_face_encoding = face_recognition.face_encodings(image)[0]

        known_face_encodings.append(image_face_encoding)
        known_face_names.append(name)


    # print(biden_face_encoding)
    # input()

    facial_data = [known_face_names, known_face_encodings]

    return facial_data

def load_facial_data(filepath, fallback_face_dir='known_faces'):
    if not os.path.isfile(filepath):
        print('Generating face_db')
        facial_data = generate_facial_data(fallback_face_dir)

        with open(filepath, 'wb') as f:
            pickle.dump(facial_data, f)
    else:
        print('Loading existing face_db')
        with open(filepath, 'rb') as f:
            facial_data = pickle.load(f)

    return facial_data



def recongnize_from_cv2_video_frame(frame, facial_data, draw_rectangles=False):
    recognized_faces = []
    known_face_names, known_face_encodings = facial_data
    # cut to 1/4 on each dimension, for faster recognition
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # convert image frame to a compatible type
    im = PIL.Image.fromarray(small_frame[:, :, ::-1])
    im = np.array(im.convert('RGB'))
    

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(im)
    #face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    face_encodings = face_recognition.face_encodings(im, face_locations, num_jitters=0, )
    # face_encodings = [None] * len(face_locations)
    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
         # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]

        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            recognized_faces.append(name)

        # Draw a box around the face
        if draw_rectangles:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        
    return recognized_faces



if __name__ == '__main__':
    facial_data = load_facial_data('face_db')
    print(facial_data[0])
    video_capture = cv2.VideoCapture(0)
    process_this_frame = True

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        # frame = biden_image.copy()
        results = recongnize_from_cv2_video_frame(frame, facial_data, draw_rectangles=True)
        # if results:
        #     print(results)


        process_this_frame = not process_this_frame
        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()