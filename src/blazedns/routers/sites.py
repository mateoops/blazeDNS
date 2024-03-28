from fastapi import APIRouter, HTTPException

from blazedns.models.site import Site

router = APIRouter(
    prefix="/sites",
    tags=["sites"],
    responses={404: {"description": "Not found"}},
)

sites_db = [Site(id=1, name="wp.pl"), Site(id=2, name="google.com")]


@router.get("/")
async def read_sites():
    return sites_db


@router.get("/{id}")
async def read_site(id: int):
    for site in sites_db:
        if site.id == id:
            return site
    raise HTTPException(status_code=404, detail="Site not found")


@router.put("/{id}", tags=["custom"], responses={403: {"description": "Forbidden"}})
async def update_site(id: int):
    if id == 1:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"id": id, "name": "gogogogogogole.com"}
