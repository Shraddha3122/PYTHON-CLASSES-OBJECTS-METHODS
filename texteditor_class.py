# Design a TextEditor class with methods to add, delete,
# and find text. Include undo and redo functionality.

class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []
        self.redo_stack = []

    def add_text(self, new_text):
        self.history.append(self.text) 
        self.redo_stack.clear()  
        self.text += new_text

    def delete_text(self, num_chars):
        if num_chars > len(self.text):
            num_chars = len(self.text) 
        deleted_text = self.text[-num_chars:]  
        self.history.append(self.text) 
        self.redo_stack.clear() 
        self.text = self.text[:-num_chars] 

        return deleted_text 

    def find_text(self, search_text):
        return self.text.find(search_text)  

    def undo(self):
        if self.history:
            self.redo_stack.append(self.text)  
            self.text = self.history.pop() 

    def redo(self):
        if self.redo_stack:
            self.history.append(self.text) 
            self.text = self.redo_stack.pop()  

    def get_text(self):
        return self.text

# Example usage:
if __name__ == "__main__":
    editor = TextEditor()
    editor.add_text("Hello, ")
    editor.add_text("Python!")
    print(editor.get_text())  

    editor.delete_text(6)
    print(editor.get_text())  

    editor.undo()
    print(editor.get_text()) 

    editor.redo()
    print(editor.get_text()) 
    
    print(editor.find_text("Python"))  
    print(editor.find_text("Hello"))  