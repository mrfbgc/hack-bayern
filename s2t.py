import azure.cognitiveservices.speech as speechsdk
import os

# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "70a634b3cde34188844735f4397c7996", "germanywestcentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

print("Say something...")

# Start speech recognition and get the result
result = speech_recognizer.recognize_once()

# Define the file path for saving the recognized text
text_file_path = "C:/Users/arifb/bayern-healthcare-hackathon/voice-data/recognized_voice_output.txt"


# Checks the result and saves recognized text to a file if speech was recognized
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    recognized_text = result.text
    print("Recognized: {}".format(recognized_text))
    
    # Save recognized voice to the text file
    with open(text_file_path, "w") as file:
        file.write("Recognized Speech:\n")
        file.write(recognized_text)

elif result.reason == speechsdk.ResultReason.NoMatch:
    print("No speech could be recognized: {}".format(result.no_match_details))
    
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Speech Recognition canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
