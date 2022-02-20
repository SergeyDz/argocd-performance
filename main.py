def main(): 
    generate(200, "in-cluster")
    generate(1, "gke_playground-s-11-8818bdd8_us-central1-c_cluster-1")

def generate(n, cluster): 
    f = open("./templates/app.template")
    template = f.read()
    clusterName = cluster[0:10].replace("_", "-")

    for i in range(n):
        name = "argo-performance-" + clusterName + "-" + str(i)
        result = template.replace("{{name}}", name).replace("{{cluster}}", cluster)
        target = open("./apps/" + name + ".yml", "w+")
        target.write(result)
        target.close()

    f.close()
    print("Done")

if __name__ == "__main__":
    main()