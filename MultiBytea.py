import base64

class Bytea:
    def code(self, File_Address):
        try:
            with open(File_Address , "rb") as f:
                encode = base64.b64encode(f.read())
        except:
            print("Error 😐 <Link File Address>")
            print("Error 😐 <Link File Address>")
            print("Error 😐 <Link File Address>")
        else:
            with open(f"bytea_python.txt" , "w") as f:
                f.write(encode.decode('utf-8'))

    def file(self, File_Bytea_Address , format):
        try:
            with open(File_Bytea_Address , "rb") as f:
                encode = f.read()    
            decode = base64.b64decode(encode)
        except:
            print("Error 😐 <Link File Address> ")
            print("Error 😐 <Link File Address> ")
            print("Error 😐 <Link File Address> ")
        else:
            try:
                with open(f"file_python.{format}" , "wb") as f:
                    f.write(decode)
            except:
                print("Error 😐 <Format> ")
                print("Error 😐 <Format> ")
                print("Error 😐 <Format> ")


if __name__ == "__main__":
    obj = Bytea()