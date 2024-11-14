#
 Shreyash AI-Enhanced Engagement Tracker for Young Learners (Infosys Internship - October 2024)

## Image Processing

### Libraries or Frameworks Used:
- *OpenCV*: Version 4.10.0.84
- *NumPy*: For array manipulation

### Developed Logics:

#### A) image_bgr2gray
This converts a color image to grayscale.

- *Input:*

  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![Grayscale Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/bgr2gray.png)

#### B) image_blur
This applies a Gaussian blur to an image to reduce noise and detail.

- *Input:*

  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![Blurred Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/blur.png)

#### C) image_contour
This detects contours in a grayscale image using a binary threshold and cv2.findContours(). The contours are drawn onto the original image in green.

- *Input:*

  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*

  ![Contoured Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/contour.png)

#### D) image_crop
This function extracts a specific region of an image based on pixel range and displays the cropped section.

- *Input:*
 
  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![Cropped Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/crop.png)

#### E) image_dilation & erosion
This function applies morphological operations, dilation and erosion, to enhance and reduce features in an image, respectively.

- *Input:*
 
  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*

  ![Eroded Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/dil_ero1.png)
  ![Dilated Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/dil_ero2.png)

#### F) image_edge_detection
This applies the Canny edge detection algorithm to detect edges in a grayscale image.

- *Input:*
 
  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![Edge Detected Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/edge.png)

#### G) image_histogram_equalization
This enhances the contrast of a grayscale image using histogram equalization.

- *Input:*

  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![Histogram Equalized Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/hiseq.png)

#### H) image_hsv
This converts a color image from the BGR color space to HSV.

- *Input:*

  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)

- *Output:*
 
  ![HSV Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/hsv.png)

#### I) image_morphological_transformation
This applies opening and closing morphological operations to a grayscale image to remove noise and fill gaps.

- *Input:*

  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/cristiano.jpg)

- *Output:*
 
  ![Morphologically Transformed Image1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/mortran1.png)
  ![Morphologically Transformed Image2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/mortran2.png)

#### J) image_noise_removal & closing_gaps
This function removes noise and fills gaps using morphological operations.

- *Input:*

  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/cristiano.jpg)

- *Output:*
 
  ![Noise_Removal Image1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/noiserm2.png)
  ![Noise_Removal Image2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/noiserm1.png)

#### K) image_resize
This resizes an image to specified dimensions.

- *Input:*
 
  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/cristiano.jpg)

- *Output:*
 
  ![Resized Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/cd09112c04ac5f48f0ff31e8c8cef4c8b4533d8d/Screenshot%202024-11-14%20181013.png)

#### L) image_rotate
This rotates an image by 90 degrees around its center.

- *Input:*

  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/cristiano.jpg)

- *Output:*

  ![Rotated Image](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/rotate.png)

#### M) image_stack
This function resizes two images to a specified pixel range and combines them both horizontally and vertically. The results are displayed in separate windows.

- *Input:*

  ![Image 1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/lionel.jpg)
  
  ![Image 2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/cristiano.jpg)

- *Output:*

  ![Concatenated Image1](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/stack1.png)
  ![Concatenated Image2](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/eebcdb6a966d86f32ee3d15a587730feaa642b0e/stack2.png)

#### N) image_template
This function performs template matching to locate a template image within a larger image.

## Video Processing

### Libraries or Frameworks Used:
- *OpenCV*: Version 4.10.0.84

### Developed Logics:

#### A) Video_fps
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

#### B) Video_multivideo
This function reads and displays images from a specified folder, printing the dimensions of each image.

#### C) Video_save
This function captures live video and saves it to a specified output file.

#### D) Video_stack
This function reads and resizes two video files, concatenating them horizontally.

#### E) Video_stream
This function captures live video from the webcam and displays it in real-time.

## Annotations

### Libraries or Frameworks Used:
- *OpenCV*: Version 4.10.0.84
- *LabelImg*: Version 1.8.6

### Developed Logics:

#### A) data_segregate
This function organizes images and their label files into matched and unmatched directories.

- *Input:*

![Screenshot 2024-11-13 174954](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/e61832fe20f77c9a027702fc0b89b5bd2a15b8a7/Screenshot%202024-11-14%20013959.png)

- *Output:*

![Screenshot 2024-11-13 174816](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/e61832fe20f77c9a027702fc0b89b5bd2a15b8a7/Screenshot%202024-11-14%20014210.png).

#### B) label
This function draws bounding boxes on images based on annotations in the label files.

- *Input:*

![gun4](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/e61832fe20f77c9a027702fc0b89b5bd2a15b8a7/gun.webp)

- *Output:*

![gun4](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/e61832fe20f77c9a027702fc0b89b5bd2a15b8a7/gun.jpeg)

#### C) label_manipulate
This function updates class numbers in label files for object detection tasks.

- *Input:*

![Screenshot 2024-11-13 174620](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/e61832fe20f77c9a027702fc0b89b5bd2a15b8a7/Screenshot%202024-11-14%20015018.png)

- *Output:*

![Screenshot 2024-11-13 174644](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/Screenshot%202024-11-14%20020659.png)

## Face Recognition

### Libraries or Frameworks Used:
- *OpenCV*: Version 4.10.0.84
- *LabelImg*: Version 1.8.6
- *dlib*: Version 19.24.6
- *face_recognition*: Version 1.3.0
- *imutils*: Version 0.5.4

### Developed Logics:

#### A) Face_recognition
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/02ef414e5188b3ce7c0b3cf56c4b5a8e46fe99b9/face_recog.png)

#### B) atten_score
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

1. *Setup*: Loads His/Her's face data and initializes detectors.
2. *Face Recognition*: Compares detected faces with the known face, identifying if it's a match.
3. *Attentiveness Check*: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
4. *Logging*: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
5. *Display*: Shows video with face labels, attentiveness status, and facial landmarks. 

Exits on 'q' press, ensuring the final save to Excel.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/atten_score.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/atten_score_excel.png)

#### C) avg_atten_score
This captures webcam video, performs face recognition for "His/Her's face," calculates attentiveness based on the head pose, and logs the data into an Excel file every 30 seconds. Here is a summary of its key actions:

1. *Face Recognition*: Uses face_recognition to identify "His/Her's face" by comparing face encodings.
2. *Head Pose Detection*: Calculates the head pose (yaw, pitch) using dlib's facial landmark predictor to assess attentiveness.
3. *Attentiveness Calculation*: Computes an attentiveness score based on yaw and pitch, with values between 0 (not attentive) and 1 (fully attentive).
4. *Logging*: Every 30 seconds, the script saves recognized face data (name, date, time, attentiveness, attention score, and screenshot) into an Excel file.
5. *Display and Feedback*: Shows real-time video with facial landmarks, attentiveness status, and face bounding boxes.

The final output includes an Excel file with logged details and an average attentiveness score at the end of the session. The user can stop the video stream by pressing 'q'.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/avg_atten_score.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/avg_atten_excel.png)

#### D) excel_sc
This is for face recognition with time-based logging looks well-structured and includes the logic to save screenshots and log attendance into an Excel file.

1. *Efficiency*: Resizing frames to 640x480 is good for speed. You can reduce the size further if needed.
2. *File Saving*: Screenshots are saved in "Teja_screenshots(5)", and Excel is updated every 30 seconds.
3. *Recognition Timings*: Logs every 30 seconds for the same person and logs every 5 minutes to avoid multiple entries in short time frames.
4. *Error Handling*: Proper try-except block for handling errors.
5. *Termination*: Exits when the 'q' key is pressed.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/excel_sc.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/excel_sc_e.png)

#### E) excel_sc_dt
This uses OpenCV and face_recognition to detect and recognize a specific face (His/Her's) from a webcam feed. Upon recognition, a screenshot is saved, and the attendance (name, date, time, screenshot path) is logged into an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures attendance is only logged every 5 minutes for the same person. The attendance data is stored in a DataFrame and periodically exported to an Excel file.

Key Features:
- Real-time face detection and recognition
- Saves screenshots with timestamp
- Logs attendance to Excel every 30 seconds
- Avoids multiple logs within a 5-minute interval for the same person

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/excel_sc_dt.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/excel_sc_dt_e.png)

#### F) landmark
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

1. *Face Recognition*: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
2. *Attentiveness Detection*: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
3. *Logging*: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
4. *Live Feedback*: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.

The system continues until you press 'q' to exit.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/landmark.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/landmark_excel.png)

#### G) test
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/test.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/testexcel.png)

#### H) tools
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

- *Input:*

![shreyash](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/b12e15bee9dc12259818ed89f57aab3c65a6a430/face%20recognition/shreyash.jpg)

- *Output:*

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/fb4c117a444c7ec787443cc4c4116b1fcfb7fa92/tools.png)

![](https://github.com/Shreyashwadgaonkar/shreyash_AI-Enhanced-Engagement-Tracker_Infosys_Internship_Oct2024/blob/44dac9d2ab3c82977499660946ca89705744d15c/toolsexcel.png)
