import unittest
from datetime import datetime

from promtp_speech_generator import CreateSpeech

class TestSpeechGenerator(unittest.TestCase):

    def test_speech(self):
        """
        This is the method to test the speech genrator 

        APPROCH - 

        INPUT: ['The quick brown fox jumped over the lazy dog.']
        OUTPUT: [True, 200, 'speechs/speech.mp3']

        """
        print("===== Start the unitary test =====  ")
        print("===== Start the request =====  ")

        speech = """
        This script will print “The file exists.” 
        if the file at the specified path exists, and 
        “The file does not exist.” otherwise. This works for both files and directories. 
        If you want to specifically check for a file and not a directory, you can use os.path.isfile(file_path). 
        Similarly, os.path.isdir(file_path) can be used to check if a directory exists at the specified path
        """

        status, code, file_path = CreateSpeech(speech,model_voice='echo', file_name="audio")\
            .generate()
        print(f'===== Request finished =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        print(file_path)
        print(f'===== Start the response verification =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        self.assertEqual(code, 200)
        self.assertEqual(status, True)
        print(f'===== End verification =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')


if __name__ == '__main__':
    unittest.main()
        


