# TrainGoApp (trainapplication)

Casual Django practice project for browsing train ticket types and destinations,
registering accounts, and “purchasing” tickets (no real payments — purchases
create dated `UserTickets` rows).

**Current scope:** users, ticket types linked to locations, purchase/list/delete
of owned tickets, staff location management, Django admin.

---

## Architecture

```
Browser → Django templates + auth
              │
              ├─ home/        welcome (tickets + locations)
              ├─ users/       CustomUser (email login), profile, data
              ├─ tickets/     Tickets, UserTickets (purchases)
              └─ locations/   Locations (staff add)
                     │
                     └─ SQLite (app/db.sqlite3)
```

Django project lives under nested `app/` (`manage.py`, settings, apps). Root
`Dockerfile` copies `app/` into the image as `/app`.

| Path | Role |
| ---- | ---- |
| `app/manage.py` | Django entrypoint |
| `app/app/` | Settings, root URLs, password-change views |
| `app/home/` | Public welcome page |
| `app/users/` | `CustomUser`, register/profile/data |
| `app/tickets/` | Ticket types + purchases |
| `app/locations/` | Destinations |
| `app/templates/`, `app/static/` | Shared UI |
| `requirements.txt` | Docker/manual install (Django 5.0.6) |
| `app/requirements.txt` | Same stack with transitive pins |

---

## Data model

- **`Locations`** — name, text, optional city, state (default `DE`), zip.
- **`Tickets`** — name, text, `duration` days (default `1`), optional FK to
  `Locations` (`related_name='tickets'`, default pk `1`).
- **`UserTickets`** — purchase join: user + ticket + `issue_date` /
  `expiry_date`; `is_active()` when expiry is after today.
- **`CustomUser`** — email as username; required first/last name and date of
  birth; M2M to tickets through `UserTickets`.

---

## Workflows

| Who | Flow |
| --- | ---- |
| Anyone | Browse `/` (tickets + locations), `/locations/`, `/tickets/tickets` |
| Visitor | Register at `/users/register/` → login at `/accounts/login/` |
| User | Profile → buy at `/tickets/buy_tickets/` → view `/users/data/` → delete purchase |
| Staff | Add locations at `/locations/add`; full CRUD via `/admin/` |

Purchase creates a `UserTickets` row with expiry = issue + ticket duration.
Duplicate **active** purchase of the same ticket type is rejected.

**Constraints / pitfalls**

- `/tickets/new` creates ticket types with only `name`/`text` (no login check);
  `duration`/`location` use model defaults — fresh DBs need a `Locations` row
  with pk `1` before that path works cleanly.
- Prefer Django admin for real ticket-type setup (duration + location).
- Purchase delete removes a `UserTickets` row, not the catalog `Tickets` type.
- Not production-ready: hardcoded `SECRET_KEY`, `DEBUG=True`, empty
  `ALLOWED_HOSTS`, SQLite, `runserver` in Docker.

---

## Local setup

Requires Python 3.12+ (use `python3` if `python` is missing).

```sh
git clone https://github.com/basit3000/trainapplication.git
cd trainapplication

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python app/manage.py migrate
python app/manage.py createsuperuser --date_of_birth YYYY-MM-DD
python app/manage.py runserver
```

Open http://127.0.0.1:8000/ — admin at `/admin/`.

`createsuperuser` is customized: email, first name, last name, and
`--date_of_birth` are required.

---

## Docker

No Compose file. Image runs `python manage.py runserver 0.0.0.0:8000` and does
**not** migrate on start.

```sh
docker build -t trainapplication .
docker run --rm -p 8000:8000 trainapplication
```

Persist SQLite and apply migrations (Linux/macOS):

```sh
docker run --rm -v "$PWD/app:/app" -p 8000:8000 trainapplication \
  sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
```

Windows bind-mount: `-v "%cd%/app:/app"`.

---

## Troubleshooting

| Symptom | Likely cause |
| ------- | ------------ |
| Table missing / OperationalError | Run `python app/manage.py migrate` |
| `manage.py` not found | Use nested path: `python app/manage.py …` |
| Superuser prompts fail | Pass `--date_of_birth` and email-based fields |
| Ticket create FK error | Create a location (admin or `/locations/add`) first |
| Auth redirects oddly | `LOGIN_REDIRECT_URL` is set twice in settings; last value (`home`) wins |

---

## License

MIT. Contributions welcome — open an issue or PR on the GitHub repository.
