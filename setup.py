from setuptools import setup, find_packages
setup(name="reagent",version="0.1.0",packages=find_packages(),install_requires=["fastapi>=0.104.0","uvicorn>=0.24.0","sqlalchemy>=2.0.0","redis>=5.0.0","httpx>=0.25.0","pydantic>=2.0.0","python-dotenv>=1.0.0"],python_requires=">=3.10")
