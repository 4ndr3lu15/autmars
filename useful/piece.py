class Piece:
    #corpo_img = None
    #tamanho_img = None
    #tipo_img = None

    def __init__(self, text_prompt, width, height, model, seed, iterations):
        self._text_prompt = text_prompt
        self._width = width
        self._height = height
        self._model = model
        self._seed = seed
        self._iterations = iterations
        self.image = '' # os path
        self.likes = []

    def runModel(self):
      pass

    def stopModel(self):
      pass