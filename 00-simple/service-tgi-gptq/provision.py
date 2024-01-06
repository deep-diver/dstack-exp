import sys

from dstack.api import Client, Service, GPU, Client, Resources

client = Client.from_config(
    project_name="Your dstack cloud Project name",
    server_url="https://cloud.dstack.ai",
    user_token="YOUR dstack cloud USER TOKEN"
)

task = Service(
    image="ghcr.io/huggingface/text-generation-inference:latest",
    env={"MODEL_ID": "TheBloke/Llama-2-13B-chat-GPTQ"},
    commands=[
        "text-generation-launcher --trust-remote-code --quantize gptq",
    ],
    port="80",
)

run = client.runs.submit(
    run_name="my-awesome-run",  # (Optional) If not specified,
    configuration=task,
    resources=Resources(gpu=GPU(memory="24GB")),
)

run.attach()
run.detach()