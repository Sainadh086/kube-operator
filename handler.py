import kopf
import yaml
import kubernetes as k
from kubernetes.client.rest import ApiException
from kubernetes.client.api import core_v1_api

@kopf.on.create('sampledb.beta','v1','MongoDB')
def create_fn(spec, **kwargs):
    sts = yaml.load(open("pod.yaml"), yaml.Loader)
    name = kwargs["body"]["metadata"]["name"]
    sts["metadata"]["name"] = kwargs["body"]["metadata"]["name"]
    sts["metadata"]["namespace"] = kwargs["body"]["metadata"]["namespace"]
    sts["spec"]["containers"][0]["image"] = kwargs["body"]["spec"]["image"]
    print(f"And here we are! Created {name} with spec: {spec}")
    #kwargs["api"].create(sts)
    api = core_v1_api.CoreV1Api()
    try:
        depl = api.create_namespaced_pod(namespace=sts['metadata']['namespace'], body=sts)
        # Update the parent's status.
        return {'children': [depl.metadata.uid]}
    except ApiException as e:
        print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)

#create code for statefulset based on kopf



