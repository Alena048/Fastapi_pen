from fastapi import FastAPI, Query, Path, Body
from fastapi.responses import HTMLResponse

from new import Book, Author


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hello, world!</h1>
        </body>
    </html>
    """

@app.post('/book')
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    return {'item': item, 'author': author, 'quantity': quantity}

@app.post('/authour')
def create_authour(authour: Author = Body(..., embed=True)):
    return {'authour': authour}


@app.get('/bookQ')
def get_book(q: str = Query(..., min_length=2, max_length=5, description="Search book")):
    return q

@app.get('/book/{pk}')
def get_single_book(pk: int = Path(..., gt=1, le=25), pages: int = Query(None, gt=10, le=500)):
    return {'pk': pk, 'pages': pages}
