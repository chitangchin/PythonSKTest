import asyncio
import sys
import os

# Add the src directory to the path so we can import from it
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Import the Kernel1 function
from kernel import kernel1

async def main():
    """
    Main entry point that can call different kernels.
    In the future, you can add more kernel functions and call them from here.
    """
    # Call Kernel1 for now
    await kernel1()
    
    # Future kernels can be called like this:
    # await Kernel2()
    # await Kernel3()

if __name__ == "__main__":
    asyncio.run(main())
