class ModelPlot:

    def __init__(self,file,doc_id):
        self.file = file
        self.doc_id = doc_id
        self.file.seek(0)

    def generate(self):
        pass