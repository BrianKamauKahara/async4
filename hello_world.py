from asyncflows import AsyncFlows
import os
from dotenv import load_dotenv
load_dotenv()


""" async def main():
    # Load the flow from the file
    flow = AsyncFlows.from_file("hello_world.yaml")
    # Run the flow
    result = await flow.run()
   
    print(result)


import asyncio
asyncio.run(main()) """
import asyncio
from asyncflows import AsyncFlows
os.environ["OPENAI_API_KEY"]="sk"+"-XVnIAfl2Ftj0wW"+"TCqFGoT3BlbkFJNuvvPr1GRelPThlD4j4M"

# Load the YAML file
flow = AsyncFlows.from_file("hello_world.yaml")

# Run the flow
async def run_flow(name:str):
    result = await flow.set_vars(name=name).run()
    print(result)

# Run the async function
asyncio.run(run_flow('Brian'))