import unittest
from datetime import datetime

from promtp_speech_generator import CreateSpeech
from prompt_extract_file_content import MyExtractorFileContent

class TestExtractContentFromFiles(unittest.TestCase):

    def test_extract_file_content(self):
        """
         This is the method to extract contents 
        from .pdf, .doc, .txt and .docx files
        """
        extract = MyExtractorFileContent()
        status,response = extract.extract_from_pdf("files/eugenio-articulo-348-2-10-20201209.pdf")
        print(response)
        st, resp = extract.read_page_content(19)
        
        #
        self.assertEqual(status, True)

        #
        self.assertEqual(st, True)
        #
        #self.assertEqual(resp, "Invalid value for [page_number]")

    def test_extract_file_content_generate_audio(self):
        """
         This is the method to extract contents 
        from .pdf, .doc, .txt and .docx files
        """
        extract = MyExtractorFileContent()
        status,response = extract.extract_from_pdf("files/eugenio-articulo-348-2-10-20201209.pdf")
        print(f"===== Number of pages {response}")
        #
        self.assertEqual(status, True)
       
        st, text = extract.read_page_content()
        #print(f"{text}")
        #
        #self.assertEqual(st, True)
       

        st2, file_path = MyExtractorFileContent.generate_audio(input_text=text, speed=.89, chunk_by="delimiter")
        print(file_path)
        #self.assertEqual(st2, True)

        
        #
        #self.assertEqual(resp, "Invalid value for [page_number]")


    def test_create_stream_speech(self):
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
       

        status, code, file_path = CreateSpeech(speech,model_voice='echo', file_name="audio")\
            .generate()
        print(f'===== Request finished =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        print(file_path)
        print(f'===== Start the response verification =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        self.assertEqual(code, 200)
        self.assertEqual(status, True)
        print(f'===== End verification =====  {datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}')
        """

if __name__ == '__main__':
    unittest.main()
        


