import warnings
warnings.simplefilter('ignore', FutureWarning)

from datetime import datetime
from diffusers  import StableDiffusionPipeline, DDIMScheduler, DPMSolverMultistepScheduler, EulerDiscreteScheduler
from accelerate import Accelerator
from config import height, width, scale, steps, repo

device       = Accelerator().device
scheduler    = DDIMScheduler.from_pretrained(repo, subfolder="scheduler")
diffusion    = StableDiffusionPipeline.from_pretrained(repo, scheduler=scheduler).to(device)

diffusion.safety_checker            = None
diffusion.requires_safety_checker   = False

prompt          = ""
negative_prompt = ""
with open("./prompt.txt") as f: prompt = f.read()
with open("./prompt.ng.txt") as f: negative_prompt = f.read()

image       = diffusion(prompt=prompt, negative_prompt=negative_prompt, height=height, width=width, guidance_scale=scale, num_inference_steps=steps).images[0]

date = datetime.now().strftime("%Y%m%d_%H%M%S")
path = date + ".png"
image.save("./images/" + path)
