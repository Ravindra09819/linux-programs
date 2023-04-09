


def main():
    batches = {"ppa":12500,"lb":11000,"python":13000,"angular":10000,"lsp":11000}
    print("Enter the batches name")
    name = input()
    print(batches.get(name,"there is no such batche"))
    
if __name__ =="__main__":
    main()