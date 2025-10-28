import os

os.environ['DEBUG'] = 'True'
os.environ['SECRET_KEY'] = 'django-insecure-r!&r16tg7@y6o2@(3fd-i*(!efze3+iw14o1#15g*zpvs(q)gg'
#os.environ['DATABASE_URL'] = 'postgresql://neondb_owner:npg_9nQvo6eFVhcr@ep-billowing-river-agiv28yp-pooler.c-2.eu-central-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

os.environ['POSTGRES_DB'] = 'personal_website'
os.environ['POSTGRES_USER'] = 'postgres'
os.environ['POSTGRES_PASSWORD'] = 'joeMburuPost'
os.environ['POSTGRES_HOST'] = '127.0.0.1'
os.environ['POSTGRES_PORT'] = '5432'