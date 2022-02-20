from random import randrange

def main(): 
    projects(30)
    generate(400, "in-cluster")
    generate(200, "gke_playground-s-11-8818bdd8_us-central1-c_cluster-1")

def generate(n, cluster): 
    f = open("./templates/app.template")
    template = f.read()
    clusterName = cluster[0:10].replace("_", "-")

    for i in range(n):
        j = randrange(30)
        name = "argo-performance-" + clusterName + "-" + str(i)
        result = template.replace("{{name}}", name).replace("{{cluster}}", cluster).replace("{{project}}", "project-" + str(j))
        target = open("./apps/generated/" + name + ".yml", "w+")
        target.write(result)
        target.close()

    f.close()
    print("Done")


def projects(n):
    f = open("./templates/project.template")
    template = f.read()

    for i in range(n):
        name = "project-" + str(i)
        result = template.replace("{{name}}", name)
        target = open("./apps/argocd/" + name + ".yml", "w+")
        target.write(result)
        target.close()

    f.close()
    print("Done")

if __name__ == "__main__":
    main()