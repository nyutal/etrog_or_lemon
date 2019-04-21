from starlette.applications import Starlette
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastai.vision import load_learner, open_image, BytesIO
import torch
from pathlib import Path
#from io import BytesIO
import sys
import uvicorn
import aiohttp
import asyncio


app = Starlette()

#classes = ['etrog', 'lemon']
#data = ImageDataBunch.single_from_classes(Path('dummy'), classes).normalize(imagenet_stats)
#model = cnn_learner(data, models.resnet34)
model = load_learner('./output_models', 'resnet_34_bs_32_size_224_with_flip_tfs.pkl')


async def get_bytes(url):
    print('get_bytes()')
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()



def predict_image_from_bytes(bytes):
    print('predict_image_from_bytes()')
    img = open_image(BytesIO(bytes))
    print(type(img))
    res, class_, losses = model.predict(img)
    print(f'res, class, loss: {type(res)}, {res}, {class_}, {losses}')
    return JSONResponse({
        "prediction": str(res),
        "probability": float(losses[class_]),
    })


@app.route("/")
def form(request):
    print('main route invoked.')
    return HTMLResponse("""
        <h3>This app will classify Etrogs (Citron) vs Lemons<h3>
        <form action="/upload" method="post" enctype="multipart/form-data">
            Select image to upload:
            <input type="file" name="file">
            <input type="submit" value="Upload Image">
        </form>
        Or submit a URL:
        <form action="/classify-url" method="get">
            <input type="url" name="url">
            <input type="submit" value="Fetch and analyze image">
        </form>
    """)


@app.route("/upload", methods=["POST"])
async def upload(request):
    data = await request.form()
    bytes = await (data["file"].read())
    return predict_image_from_bytes(bytes)


@app.route("/classify-url", methods=["GET"])
async def classify_url(request):
    bytes = await get_bytes(request.query_params["url"])
    return predict_image_from_bytes(bytes)


if __name__ == "__main__":
    if "serve" in sys.argv:
        uvicorn.run(app, host="0.0.0.0", port=80)
    if "heroku" in sys.argv:
        import os
        port = int(os.environ['PORT'])
        print(f'serve on port {port}')
        uvicorn.run(app, host="0.0.0.0", port=port)

