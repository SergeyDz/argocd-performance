def main(): 
    generate(10, "in-cluster")
    generate(10, "gke_playground-s-11-4b203270_us-central1-c_cluster-1")

def generate(n, cluster): 
    f = open("./templates/app.template")
    template = f.read()

    for i in range(n):
        name = "argo-performance-" + cluster + "-" + str(i)
        result = template.replace("{{name}}", name).replace("{{cluster}}", cluster)
        target = open("./apps/" + name + ".yml", "w+")
        target.write(result)
        target.close()

    f.close()
    print("Done")

if __name__ == "__main__":
    main()