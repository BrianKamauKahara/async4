from asyncflows import AsyncFlows
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

# Load the YAML file
flow = AsyncFlows.from_file("hello_world.yaml")

# Run the flow
async def run_flow(name:str):
    result = await flow.set_vars(name=name).run()
    print(result)

# Run the async function
asyncio.run(run_flow('Brian'))