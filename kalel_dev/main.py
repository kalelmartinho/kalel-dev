from fastapi import FastAPI


def create_app():
    """Factory function for creating the FastAPI app"""
    app = FastAPI()

    return app
