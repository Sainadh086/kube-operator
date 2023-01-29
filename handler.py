import kopf
import yaml


@kopf.on.create('MongoDB')
def create_fn(spec, name, meta, status, **kwargs):
    sts = yaml.load(open("pod.yaml"), yaml.Loader)
    sts["metadata"]["name"] = name
    sts["spec"]["containers"][0]["image"] = spec["image"]
    print(f"And here we are! Created {name} with spec: {spec}")
    kwargs["api"].create(sts)



#create code for statefulset based on kopf



