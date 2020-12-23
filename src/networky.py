from datetime import datetime

import speedtest
import typer

import config
import db

app = typer.Typer()


@app.command()
def setup():
    """Creates database tables"""
    db.create()
    print("Database tables created.")


@app.command()
def delete():
    """Deletes database tables."""
    db.delete()
    print("Database tables deleted.")


@app.command()
def compute():
    """Performs the speedtest and saves the result in the DB."""
    print("Testing...")
    try:
        s = speedtest.Speedtest()
        s.get_servers(servers=config.SERVERS)
        s.download(threads=config.THREADS)
        s.upload(threads=config.THREADS)
    except Exception as e:
        session = db.Session()
        update = db.Update(
            updated=datetime.now(),
            error=True,
            message=str(e)
        )
        session.add(update)
        session.commit()
        print(f"Error {e} saved in DB.")
        return

    print("Test done. Saving...")

    session = db.Session()
    _server = s.results.server
    server = db.Server(
        id=_server["id"],
        url=_server["url"],
        lat=_server["lat"],
        lon=_server["lon"],
        name=_server["name"],
        cc=_server["cc"],
        sponsor=_server["sponsor"],
    )
    session.merge(server)  # Update server if it already exists in DB
    updated = datetime.now()
    update = db.Update(
        updated=updated,
        download=round(s.results.download),
        upload=round(s.results.upload),
        ping=round(s.results.ping, 1),
        server_id=_server["id"],
        ip=s.results.client["ip"],
    )
    session.add(update)
    session.commit()
    print(f"Saved as {updated}.")
