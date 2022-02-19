def main(): 
    f = open("./templates/app.template")
    template = f.read()

    for i in range(1500):
        name = "argo-performance-" + str(i)
        result = template.replace("{{name}}", name)
        target = open("./apps/" + name + ".yml", "w+")
        target.write(result)
        target.close()

    f.close()
    print("Done")

if __name__ == "__main__":
    main()