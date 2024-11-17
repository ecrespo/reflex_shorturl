from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

import requests

from reflex_shorturl.api.db import get_db
from reflex_shorturl.api.models import URL


url = 'http://tinyurl.com/api-create.php?url='


def hello() -> str:
    return "Hello World!"


def shorten_url(long_url):
    response = requests.get(url + long_url)
    return response.text


def create_short_url(original_url: str, db: Session = Depends(get_db)):
    short_code = URL.shorten_url(db, original_url)
    return {"short_url": f"http://localhost:8000/{short_code}"}

def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    """Redirect the user to the original URL and track clicks."""
    url = URL.get_original_url(db, short_code)
    if url:
        url.clicks += 1  # Increment the click count
        db.commit()
        return RedirectResponse(url.original_url)
    raise HTTPException(status_code=404, detail="URL not found")

def get_stats(short_code: str, db: Session = Depends(get_db)):
    url = URL.get_url_from_short_code(db, short_code)
    if url:
        return {"original_url": url.original_url, "clicks": url.clicks}
    raise HTTPException(status_code=404, detail="URL not found")
